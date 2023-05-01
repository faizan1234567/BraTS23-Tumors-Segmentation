'''set up the config for brats dataset, train and test folders names and
some parameters'''
import os

class Config:
    root_dir = "/gdrive/MyDrive/THESIS BraTs NUST"
    train_root_dir = "/gdrive/MyDrive/THESIS BraTs NUST/MICCAI_BraTS2020_TrainingData/MICCAI_BraTS2020_TrainingData"
    test_root_dir  = "/gdrive/MyDrive/THESIS BraTs NUST/MICCAI_BraTS2020_ValidationData/MICCAI_BraTS2020_ValidationData"
    path_to_train_csv = "/gdrive/MyDrive/THESIS BraTs NUST/train_data.csv"
    seed = 50
    survival_info_csv_train = "/gdrive/MyDrive/THESIS BraTs NUST/MICCAI_BraTS2020_TrainingData/MICCAI_BraTS2020_TrainingData/survival_info.csv"
    name_mapping_csv_train = "/gdrive/MyDrive/THESIS BraTs NUST/MICCAI_BraTS2020_TrainingData/MICCAI_BraTS2020_TrainingData/name_mapping.csv"
    survival_info_csv_test = "/gdrive/MyDrive/THESIS BraTs NUST/MICCAI_BraTS2020_ValidationData/MICCAI_BraTS2020_ValidationData/survival_evaluation.csv"
    name_mapping_csv_test = "/gdrive/MyDrive/THESIS BraTs NUST/MICCAI_BraTS2020_ValidationData/MICCAI_BraTS2020_ValidationData/name_mapping_validation_data.csv"
    validation_csv = "/gdrive/MyDrive/THESIS BraTs NUST/MICCAI_BraTSXX_TestData/Testset/test_set.csv"
    a_test_patient = "/gdrive/MyDrive/THESIS BraTs NUST/MICCAI_BraTSXX_TestData/Testset/BraTS19_TCIA08_167_1"
    LGG18 = "/gdrive/MyDrive/Brats18/LGG"
    HGG18 = "/gdrive/MyDrive/Brats18/HGG"
    data_dir = "/gdrive/MyDrive/THESIS BraTs NUST"
    brats18_val_data = "/gdrive/MyDrive/THESIS BraTs NUST/MICCAI_BraTSXX_TestData/Testset"
    brats19_test_data = "/gdrive/MyDrive/THESIS BraTs NUST/MICCAI_BraTS19_Test/MICCAI_BraTS19_Test"
    brats19_test_survival_csv = "/gdrive/MyDrive/THESIS BraTs NUST/MICCAI_BraTS19_Test/MICCAI_BraTS19_Test/test_set.csv"
    
    class Testset:
        Brat19_HGG_path = "/gdrive/MyDrive/Medical Dataset/MICCAI_BraTS_2019_Data_Training/HGG"
        Brats19_LGG_path = "/gdrive/MyDrive/Medical Dataset/MICCAI_BraTS_2019_Data_Training/LGG"
        Brats19_TestData = "/gdrive/MyDrive/Medical Dataset/MICCAI_BraTS_2019_Data_Training/Testset"
        size = 41
        HGG_files = 21
        LGG_files = 20
        val_dir_path = "/gdrive/MyDrive/THESIS BraTs NUST/MICCAI_BraTSXX_TestData/Testset"
        # '/gdrive/MyDrive/THESIS BraTs NUST/MICCAI_BraTSXX_TestData/Testset'
    class newGlobalConfigs:
        root_dir = "E:/Brats21 Data/training"
        train_root_dir = root_dir + "/RSNA_ASNR_MICCAI_BraTS2021_TrainingData_16July2021"+ "/RSNA_ASNR_MICCAI_BraTS2021_TrainingData_16July2021"
        test_root_dir = "E:/Brats21 Data/validation/RSNA_ASNR_MICCAI_BraTS2021_ValidationData/RSNA_ASNR_MICCAI_BraTS2021_ValidationData"
        path_to_csv = root_dir + "/BraTS21-17_Mapping.csv"
        pretrained_model = ""
        survival_info_df = ""
        name_mapping_df = path_to_csv
        seed = 50
        class swinUNetCongis:
            roi = (128, 128, 128)
            batch_size = 2
            fold = 1
            max_epochs = 100
            infer_overlap = 0.5
            val_every = 10

