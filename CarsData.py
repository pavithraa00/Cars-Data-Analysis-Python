import pandas as pd
car = pd.read_csv('2. Cars Data1.csv')

car.head()
car.shape
car.columns
car.index
car.dtypes
car.count()

#### DATA ANALTYICS WITH PYTHON ON CAR DATASET

## 1.Data CLeaning (Find all the null values in the dataset. If there is any null value in a column,then fill it with either mean or median or mode of that column)
car['Make'] = car['Make'].fillna(car['Make'].mode()[0])
car['Model'] = car['Model'].fillna(car['Model'].mode()[0])
car['Type'] = car['Type'].fillna(car['Type'].mode()[0])
car['Origin'] = car['Origin'].fillna(car['Origin'].mode()[0])
car['DriveTrain'] = car['DriveTrain'].fillna(car['DriveTrain'].mode()[0])
car['MSRP'] = car['MSRP'].fillna(car['MSRP'].mode()[0])
car['Invoice'] = car['Invoice'].fillna(car['Invoice'].mode()[0])

car['EngineSize'] = car['EngineSize'].fillna(car['EngineSize'].mean())
car['Cylinders'] = car['Cylinders'].fillna(car['Cylinders'].median())  # better choice
car['Horsepower'] = car['Horsepower'].fillna(car['Horsepower'].mean())
car['MPG_City'] = car['MPG_City'].fillna(car['MPG_City'].mean())
car['MPG_Highway'] = car['MPG_Highway'].fillna(car['MPG_Highway'].mean())
car['Weight'] = car['Weight'].fillna(car['Weight'].mean())
car['Wheelbase'] = car['Wheelbase'].fillna(car['Wheelbase'].mean())
car['Length'] = car['Length'].fillna(car['Length'].mean())
car.isnull().sum()

## 2.Value_counts (Check what are the different types of 'Make' are there in our dataset and what is the count of each 'Make' in the data?)
car['Make'].value_counts()

## 3.Filtering (Show all the records where "Origin" is 'Asia' or 'Europe')
car[(car['Origin'] == 'Asia') | (car['Origin'] == 'Europe') ]

## 4.Removing unwanted records (Remove all the records(rows) where 'Weight' is above 4000)
car[~(car['Weight'] > 4000)]

## 5.Applying function on a column (Increase all the values of 'MPG_City' column by 3)
car['MPG_City']=car['MPG_City'].apply(lambda x:x+3)
car

## 6.Find correlation between numerical columns
car.corr(numeric_only=True)

## 7.Find cars where MPG is above average of their Origin
car[car['MPG_City'] > car.groupby('Origin')['MPG_City'].transform('mean')]

## 8.Which Origin has best average MPG
car.groupby('Origin')['MPG_City'].mean()

## 9.Find cars where Horsepower is greater than average horsepower
car[car['Horsepower'] > car['Horsepower'].mean()]

## 10.Find top 3 cars (per Origin) with highest MPG_City
car.groupby('Origin').apply(lambda x:x.nlargest(3,'MPG_City'))

## 11.Which car types are fuel efficient
car.groupby('Type')['MPG_City'].mean()

 ## 12.Which brands are most expensive
 car['MSRP'] = car['MSRP'].replace('[\$,]', '', regex=True)   ## removing string characters
 car['MSRP'] = pd.to_numeric(car['MSRP'])                     ## converting to numbers
 car.groupby('Make')['MSRP'].mean().sort_values(ascending=False).head(10)
