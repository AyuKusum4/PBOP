import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns

# preprocessing data
def preprocessing_data(data):
    print("========== Preprocessing Data ==========")
    
    for col in data.select_dtypes(include='object').columns:
        data[col] = data[col].fillna(data[col].mode()[0])  
    for col in data.select_dtypes(include='number').columns:
        data[col] = data[col].fillna(data[col].median())  
    
    le = LabelEncoder()
    for col in data.select_dtypes(include='object').columns:
        data[col] = le.fit_transform(data[col])
    
    print("Selesai Preprocessing!\n")
    return data

# menampilkan histogram
def plot_histogram(data, features):
    for feature in features:
        if feature in data.columns:
            plt.figure(figsize=(8, 6))
            data[feature].hist(bins=20)
            plt.title(f'Histogram of {feature}')
            plt.xlabel(feature)
            plt.ylabel('Frequency')
            plt.show()

# memvalidasi kolom input
def validate_columns(data, features, label):
    for col in features:
        if col not in data.columns:
            print(f"Kolom {col} tidak ditemukan di dataset!")
            return False
    if label not in data.columns:
        print(f"Kolom {label} tidak ditemukan di dataset!")
        return False
    return True

# menampilkan confusion matrix
def plot_confusion_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Class 0', 'Class 1'], yticklabels=['Class 0', 'Class 1'])
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()

def main():
    data = None
    X_train, X_test, y_train, y_test = None, None, None, None

    while True:
        print("\n========== Analisis Air Quality ==========")
        print("1. Masukkan File")
        print("2. Analisis dengan Algoritma")
        print("3. Keluar")
        
        pilihan = input("Pilih Menu (1/2/3): ")
        
        if pilihan == '1':
            file_name = input("Masukkan Nama File: ")
            try:
                data = pd.read_excel(file_name)
                print("File Berhasil Dibaca!\n")
                print(data.head())
                
                data = preprocessing_data(data)
                
                print("Pilih kolom untuk fitur (dipisahkan koma):")
                features = [f.strip() for f in input().split(',')] 
                label = input("Pilih kolom untuk label: ")
                
                # Validasi kolom
                if not validate_columns(data, features, label):
                    continue
            
                X = data[features]
                y = data[label]
            
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                print("Data Berhasil Diproses!\n")
                
                # Menampilkan histogram untuk fitur yang dipilih
                plot_histogram(data, features)
                
            except Exception as e:
                print(f"Error: {e}")
        
        elif pilihan == '2':
            if data is None:
                print("Data belum dimasukkan! Pilih menu 1 terlebih dahulu untuk memuat data.\n")
                continue
            
            print("\n========== Pilih Algoritma ==========")
            print("1. Naive Bayes")
            print("2. Random Forest")
            algo = input("Masukkan Pilihan Algoritma (1/2): ")
            
            if algo == '1':
                model = GaussianNB()
            elif algo == '2':
                model = RandomForestClassifier()
            else:
                print("Algoritma tidak valid!")
                continue
            
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            
            print("\n========== Hasil Evaluasi ==========")
            print("Accuracy:", accuracy_score(y_test, y_pred))
            print(classification_report(y_test, y_pred))
            
            # Menampilkan confusion matrix
            plot_confusion_matrix(y_test, y_pred)
            
        elif pilihan == '3':
            print("Program Selesai. Terima Kasih!")
            break
        else:
            print("Pilihan tidak valid! Coba lagi.")

if __name__ == "__main__":
    main()
