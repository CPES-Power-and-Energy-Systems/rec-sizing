# not used on tests (pkl used instead), just for example
CLUSTERING_INPUTS = {
	'nr_days': 2,
	'delta_t': 1,
	'nr_representative_days': 1,
	'l_grid': [0.01, 0.02, 0.03, 0.04, 0.01, 0.02, 0.03, 0.04, 0.01, 0.02, 0.03, 0.04,
			   0.01, 0.02, 0.03, 0.04, 0.01, 0.02, 0.03, 0.04, 0.01, 0.02, 0.03, 0.04,
			   0.02, 0.03, 0.04, 0.05, 0.02, 0.03, 0.04, 0.05, 0.02, 0.03, 0.04, 0.05,
			   0.02, 0.03, 0.04, 0.05, 0.02, 0.03, 0.04, 0.05, 0.02, 0.03, 0.04, 0.05],
	'timeseries_data': {
		'CPE#1': {
			'e_g_factor': [0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7,
						   0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0,
						   0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,
						   0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.0, 0.0, 0.0, 0.0],
			'e_c': [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2,
					1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2,
					2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3,
					2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3],
			'l_buy': [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					  0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					  0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					  0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06],
			'l_sell': [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					   0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					   0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					   0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06]
		},
		'CPE#2': {
			'e_g_factor': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
						   0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
						   0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
						   0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			'e_c': [0.1, 0.2, 0.3, 0.4, 0.3, 0.2, 0.1, 0.2, 0.3, 0.4, 0.3, 0.2,
					0.1, 0.2, 0.3, 0.4, 0.3, 0.2, 0.1, 0.2, 0.3, 0.4, 0.3, 0.2,
					0.2, 0.3, 0.4, 0.5, 0.4, 0.3, 0.2, 0.3, 0.4, 0.5, 0.4, 0.3,
					0.2, 0.3, 0.4, 0.5, 0.4, 0.3, 0.2, 0.3, 0.4, 0.5, 0.4, 0.3],
			'l_buy': [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					  0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					  0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
					  0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05],
			'l_sell': [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					   0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					   0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
					   0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
		},
		'CPE#3': {
			'e_g_factor': [0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7,
						   0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0,
						   0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,
						   0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.0, 0.0, 0.0, 0.0],
			'e_c': [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2,
					1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2,
					2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3,
					2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3],
			'l_buy': [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					  0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					  0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					  0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06],
			'l_sell': [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					   0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					   0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
					   0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06]
		},
	}
}

CLUSTERING_OUTPUTS = {
	'inertia': 7.198,
	'cluster_labels': ['0', '0'],
	'representative_e_g_factor': {
		'CPE#1': {
			'0': [0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7,
				  0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0]
		},
		'CPE#2': {
			'0': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
				  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
		},
		'CPE#3': {
			'0': [0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7,
				  0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0]
		}
	},
	'representative_e_c': {
		'CPE#1': {
			'0': [1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0, 2.0, 3.0, 4.0, 3.0, 2.0,
				  1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0, 2.0, 3.0, 4.0, 3.0, 2.0]
		},
		'CPE#2': {
			'0': [0.1, 0.2, 0.3, 0.4, 0.3, 0.2, 0.1, 0.2, 0.3, 0.4, 0.3, 0.2,
				  0.1, 0.2, 0.3, 0.4, 0.3, 0.2, 0.1, 0.2, 0.3, 0.4, 0.3, 0.2]
		},
		'CPE#3': {
			'0': [1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0, 2.0, 3.0, 4.0, 3.0, 2.0,
				  1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0, 2.0, 3.0, 4.0, 3.0, 2.0]
		}
	},
	'representative_l_buy': {
		'CPE#1': {
			'0': [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
				  0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06]
		},
		'CPE#2': {
			'0': [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
				  0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06]
		},
		'CPE#3': {
			'0': [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
				  0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06]
		}
	},
	'representative_l_sell': {
		'CPE#1': {
			'0': [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
				  0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06]
		},
		'CPE#2': {
			'0': [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
				  0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06]
		},
		'CPE#3': {
			'0': [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06,
				  0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06]
		}
	},
	'representative_l_grid': {
		'0': [0.01, 0.02, 0.03, 0.04, 0.01, 0.02, 0.03, 0.04, 0.01, 0.02, 0.03, 0.04,
			  0.01, 0.02, 0.03, 0.04, 0.01, 0.02, 0.03, 0.04, 0.01, 0.02, 0.03, 0.04]
	},
	'cluster_nr_days': {
		'0': 2
	}
}
