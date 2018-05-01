from utils import load_dataset, train_classifier, evaluate_model, create_nominal_dataset
from sklearn.model_selection import train_test_split


def main():
   data_dict = load_dataset()
   nominal_data = create_nominal_dataset(data_dict)
   data_dict['nominal'] = nominal_data
   data_train, data_test, label_train, label_test = train_test_split(data_dict['nominal'], data_dict['labels'], test_size = 0.20, random_state=True)
   model = train_classifier(data_train, label_train)
   evaluate_model(model, data_test, label_test)


if __name__ == "__main__":
    main()
