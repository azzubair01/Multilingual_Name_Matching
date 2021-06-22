from DeezyMatch import finetune as dm_finetune

# fine-tune a pretrained model stored at pretrained_model_path and pretrained_vocab_path
# dm_finetune(input_file_path="./inputs/input_dfm.yaml",
#             dataset_path="dataset/dataset-string-similarity_test.txt",
#             model_name="finetuned_test001",
#             pretrained_model_path="./models/test001/test001.model",
#             pretrained_vocab_path="./models/test001/test001.vocab")

dm_finetune(input_file_path="./inputs/input_dfm.yaml",
            dataset_path="dataset/finetune.txt",
            model_name="finetuned_test003",
            pretrained_model_path="./models/test003/test003.model",
            pretrained_vocab_path="./models/test003/test003.vocab")