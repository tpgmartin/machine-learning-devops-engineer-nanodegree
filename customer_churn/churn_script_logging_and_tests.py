import os
import logging
import churn_library as cls

logging.basicConfig(
    filename='./logs/churn_library.log',
    level = logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

def test_import(import_data):
    '''
    test data import - this example is completed for you to assist with the other test functions
    '''
    try:
        df = import_data('./data/bank_data.csv')
        logging.info('Testing import_data: SUCCESS')
    except FileNotFoundError as err:
        logging.error('Testing import_eda: The file wasn\'t found')
        raise err

    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0
    except AssertionError as err:
        logging.error('Testing import_data: The file doesn\'t appear to have rows and columns')
        raise err

    return df

def test_eda(perform_eda, df):
    '''
    test perform eda function
    '''

    perform_eda(df)

    try:
        dir_val = os.listdir('./images/eda')
        assert len(dir_val) == 5
        logging.info('Testing perform_eda: SUCCESS')
    except AssertionError as err:
        logging.error(
            'Testing perform_eda: report images not being saved as expected')
        raise err


def test_encoder_helper(encoder_helper, df):
    '''
    test encoder helper
    '''
    cat_columns = [
        'Gender',
        'Education_Level',
        'Marital_Status',
        'Income_Category',
        'Card_Category'
    ]
    response = 'Churn'

    df = encoder_helper(df, cat_columns, response)

    try:
        for col in cat_columns:
            assert f'{col}_{response}' in df.columns
        logging.info('Testing encoder_helper: SUCCESS')
    except AssertionError as err:
        logging.error(
            'Testing encoder_helper: categorical columns not being'
            'encoded as expected.'
        )
        return err
    return df


def test_perform_feature_engineering(perform_feature_engineering, df):
    '''
    test perform_feature_engineering
    '''
    X_train, X_test, y_train, y_test  = perform_feature_engineering(df, 'Churn')

    try:
        assert X_train.shape[0] > 0
        assert X_test.shape[0] > 0
        assert len(y_train) > 0
        assert len(y_test) > 0
        logging.info('Testing perform_feature_engineering: SUCCESS')
    except AssertionError as err:
        logging.error(
            'Testing perform_feature_engineering: at least one of the four '
            'returned objects are empty.'
        )
        return err

    return X_train, X_test, y_train, y_test

def test_train_models(train_models, X_train, X_test, y_train, y_test):
    '''
    test train_models
    '''
    train_models(X_train, X_test, y_train, y_test)

    try:
        dir_val = os.listdir('./images/results/')
        assert len(dir_val) == 4
        logging.info('Testing train_models, saving results images: SUCCESS')
    except AssertionError as err:
        logging.error(
            'Testing train_models: results images not being saved as expected')
        raise err

    try:
        dir_val = os.listdir('./models/')
        assert len(dir_val) == 2
        logging.info('Testing train_models, saving models: SUCCESS')
    except AssertionError as err:
        logging.error(
            'Testing perform_eda: model files not being saved as expected')
        raise err


if __name__ == '__main__':

    df = test_import(cls.import_data)

    test_eda(cls.perform_eda, df)

    df = test_encoder_helper(cls.encoder_helper, df)

    X_train, X_test, y_train, y_test = test_perform_feature_engineering(
        cls.perform_feature_engineering, df)

    test_train_models(cls.train_models, X_train, X_test, y_train, y_test)