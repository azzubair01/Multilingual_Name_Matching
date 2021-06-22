from DeezyMatch import combine_vecs

# combine vectors stored in queries/test and save them in combined/queries_test
combine_vecs(rnn_passes=['fwd', 'bwd'],
             input_scenario='queries/test',
             output_scenario='combined/queries_test',
             print_every=10)