import multiprocessing as mp

from rec_sizing.optimization.module.CollectiveMILPPool import CollectiveMILPPool
from rec_sizing.custom_types.collective_milp_pool_types import (
	BackpackCollectivePoolDict,
	OutputsCollectivePoolDict
)
from joblib import Parallel, delayed
from loguru import logger


def run_pre_collective_pool_milp(backpack: BackpackCollectivePoolDict) \
		-> OutputsCollectivePoolDict:
	"""
	Use this function to compute a standalone collective MILP for a given renewable energy community (REC) or citizens
	energy community (CEC) under a pool market structure.
	This function is specific for a pre-delivery timeframe, providing the schedules for controllable assets,
	such as battery energy storage systems (BESS, presently the only modelled controllable assets) for days- to
	years-ahead, optimal transactions between REC members and optimal investments in new storage and/or RES capacities.
	The function requires the provision of several forecasts, parameters and other data which thoroughly described
	below, under the parameter "backpack". Arrays with time-varying data such as consumption/generation forecasts and
	opportunity costs must comply with the expected length defined by the MILP's horizon and step
	(e.g., for a 24h horizon, and a step of 15 minutes or 0.25 hours, the length of the arrays must be 96).
	:param backpack: {
		'nr_days' a float with the number of days to consider in the optimization
		'l_grid': an array with the applicable tariffs for self-consumed energy, in €/kWh
		'delta_t': a float or int with the optimization time step to be considered, in hours
		'storage_ratio': a float or int indicating a reference ratio between maximum admissible input and output storage
		power and storage nominal capacity, in kW/kWh; this fundamental ratio will be considered for any storage asset
		installation suggestion by the MILP
		'strict_pos_coeffs': boolean indicating if the (dynamic) allocation coefficients that are generated by the
			internal REC transactions need to be strictly positive (as the Portuguese legislation currently demands)
			or not
		'total_share_coeffs': boolean indicating that meters with surplus must share all that surplus with meters that
			are consuming in the REC if the REC has a deficit (i.e., total consumption > total generation); on the
			other hand, if the REC has a surplus (i.e., total generation > total consumption), meters with surplus must
			share their surplus with consumming members up to their consumption, and the remaning surplus can be sold
			to the retailer; this implementation follows out interpretation of the curent Portuguese law.
		'meters' : structure with information relative to each meter
		{
			#meter_id: {
				'l_buy': an array with the opportunity costs for buying energy from the retailer
				'l_sell': an array with the opportunity costs for selling energy to the retailer
				'l_cont': a float representing the the contracted power tariff of the meter, adjusted to one day
				'l_gic': a float representing the investment cost for additional RES installation in the meter,
				adjusted to one day
				'l_bic': a float representing the investment cost for additional storage installation in the meter,
				adjusted to one day
				'e_c': an array with the forecasted energy consumption behind the meter, in kWh
				'p_meter_max': a float with the maximum capacity the meter can safely handle, in kW
				'p_gn_init': a float with te initial installed RES generation capacity at the meter, in kW
				'e_g_factor': an array with the RES generation profile factor for the meter's location
				'p_gn_min': a float representing the minimum RES capacity to be installed at the meter
				'p_gn_max': a float representing the maximum RES capacity to be installed at the meter
				'e_bn_init': a float with te initial installed storage capacity at the meter, in kW
				'e_bn_min': a float representing the minimum storage to be installed at the meter
				'e_bn_max': a float representing the maximum storage to be installed at the meter
				'soc_min': a percentage, applicable to "e_bn", identifying a minimum limit to the energy content
				'eff_bc': a fixed value, between 0 and 1, that expresses the charging efficiency of the BESS
				'eff_bd': a fixed value, between 0 and 1, that expresses the discharging efficiency of the BESS
				'soc_max': a percentage, applicable to "e_bn", identifying a maximum limit to the energy content
			}
		}
	}
	:return: {
		'c_ind2pool': dict of floats with the individual costs with energy for the optimization horizon, in €;
			positive values are costs, negative values are profits
		'c_ind2pool_without_deg': same as "c_ind2pool" without the degradation costs, in €
		'c_ind2pool_without_deg_and_p_extra':  same as "c_ind2pool" without the degradation costs and
			power limit violation costs, in €
		'c_ind2pool_without_p_extra': same as "c_ind2pool" without the power limit violation costs, in €
		'deg_cost2pool': dict of floats with the batteries' total degradation cost, in €
		'delta_alc': dict of arrays with auxiliary binary values
		'delta_bc': dict of arrays with auxiliary binary values
		'delta_cmet': dict of arrays with auxiliary binary values
		'delta_coeff': dict of arrays with auxiliary binary values
		'delta_slc': dict of arrays with auxiliary binary values
		'delta_sup': dict of arrays with auxiliary binary values
		'dual_prices: array with the market equilibrium shadow prices to be used as LEM prices, in €/kWh
		'e_alc': dict of arrays with the allocated energies to each Meter / member, in kWh
		'e_bat': dict of dict of arrays with the evolution of the energy content of each storage asset, in kWh
		'e_bc': dict of dict of arrays with the charging energy setpoints for each storage asset, in kWh
		'e_bd': dict of dict of arrays with the discharging energy setpoints for each storage asset, in kWh
		'e_cmet': dict of arrays with the net load consumptions forecasted after using the BESS, in kWh
		'e_consumed': dict of arrays with the forecasted energy consumptions from the retailer, in kWh
		'e_pur_pool': dict of arrays with the scheduled total energies bought on the LEM, in kWh
		'e_sale_pool': dict of arrays with the scheduled total energies sold on the LEM, in kWh
		'e_slc_pool': dict of arrays with the self-consumed energies from the REC, in kWh
		'e_sup_market': array with energy bought at market-indexed buying tariff, in kWh
		'e_sup_retail': array with energy bought at the retailer opportunity costs, in kWh
		'e_sur_market': array with energy sold at market-indexed selling tariff, in kW,
		'e_sur_retail': array with energy sold at the retailer opportunity costs, in kWh
		'milp_status': string with the status of the optimization problem; only non-error value is "Optimal"
		'obj_value': value obtained for the objective function under an optimal solution of the MILP
		'p_extra': dict of arrays with the extra power consumed (positive) or injected (negative) beyond the maximum
			admissible power limit at the connection points with the grid, in kW
		'p_extra_cost2pool': dict of floats with the total power limit violation costs, in €
		'soc_bat': dict of arrays with the evolution of the SoC of each storage asset, in %
	}
	"""
	logger.info('Running a pre-delivery standalone/second stage collective (pool) MILP...')

	milp = CollectiveMILPPool(backpack)
	milp.solve_milp()
	results = milp.generate_outputs()

	logger.info('Running a pre-delivery standalone/second stage collective (pool) MILP... DONE!')

	return results


if __name__ == '__main__':
	from rec_sizing.optimization.structures.I_O_collective_pool_milp import (
		INPUTS_NO_INSTALL_POOL,
		INPUTS_INSTALL_POOL
	)
	outputs = run_pre_collective_pool_milp(INPUTS_INSTALL_POOL)
	pass
