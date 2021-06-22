from DeezyMatch import inference as dm_inference

# model inference using a model stored at pretrained_model_path and pretrained_vocab_path
# dm_inference(input_file_path="./inputs/input_dfm.yaml",
#              dataset_path="dataset/dataset-string-similarity_test.txt",
#              pretrained_model_path="./models/finetuned_test001/finetuned_test001.model",
#              pretrained_vocab_path="./models/finetuned_test001/finetuned_test001.vocab")

dm_inference(input_file_path="./inputs/input_dfm.yaml",
             dataset_path="dataset/test.txt",
             pretrained_model_path="./models/finetuned_test003/finetuned_test003.model",
             pretrained_vocab_path="./models/finetuned_test003/finetuned_test003.vocab")