from DeezyMatch import train as dm_train

# train a new model
# dm_train(input_file_path="../inputs/input_dfm.yaml",
#          dataset_path="../dataset/dataset-string-similarity_test.txt",
#          model_name="test001")

dm_train(input_file_path="inputs/input_dfm.yaml",
         dataset_path="dataset/train.txt",
         model_name="test003")