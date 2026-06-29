from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":

    # Data Ingestion
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    print("Data Ingestion Completed")

    # Data Transformation
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
        train_data,
        test_data
    )

    print("Data Transformation Completed")

    # Model Training
    model_trainer = ModelTrainer()
    score = model_trainer.initiate_model_trainer(train_arr, test_arr)

    print(f"Model Training Completed")
    print(f"R2 Score: {score}")