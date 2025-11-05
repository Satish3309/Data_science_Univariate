class Univariate():
    def quan_qual(dataset):
        quan=[]
        qual=[]
        for column_names in dataset.columns:
            if dataset[column_names].dtypes=="object":
                qual.append(column_names)

            else:
                quan.append(column_names)

        return quan,qual