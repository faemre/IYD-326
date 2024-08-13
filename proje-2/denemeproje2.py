# Gerekli Kütüphanelerin Yüklenmesi
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report

# Veri Kümesini Yükleme
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris = pd.read_csv(url, header=None, names=column_names)

# İlk birkaç satırı gösterme
print("İlk birkaç satır:")
print(iris.head())

# Veri Temizleme
# Eksik değerleri kontrol etme
print("\nEksik değerlerin kontrolü:")
print(iris.isnull().sum())

# Veri türlerini kontrol etme
print("\nVeri türlerinin kontrolü:")
print(iris.dtypes)

# Temel istatistikleri hesaplama
print("\nTemel istatistikler:")
print(iris.describe())

# Sınıf dağılımını gösterme
print("\nSınıf dağılımı:")
print(iris['class'].value_counts())

# Veri Görselleştirme
# Çiftler arası ilişkileri gösteren bir pairplot oluşturma
print("\nPairplot oluşturuluyor...")
sns.pairplot(iris, hue='class')
plt.show()

# Korelasyon matrisinin ısı haritası ile gösterme
print("\nKorelasyon matrisinin ısı haritası:")
plt.figure(figsize=(10, 7))
# Sadece sayısal sütunları kullanarak korelasyon matrisini hesapla
numeric_columns = iris.drop(columns=['class'])
sns.heatmap(numeric_columns.corr(), annot=True, cmap='coolwarm')
plt.show()

# Veri Ön İşleme
# Kategorik veriyi sayısal değere dönüştürme
iris['class'] = iris['class'].map({'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2})

# Özellikleri (X) ve hedef değişkeni (Y) belirleme
X = iris.drop('class', axis=1) #özellikler(taç,çanak,yaprak...)
y = iris['class'] # Bitki Türleri 

# Eğitim ve test setlerine ayırma
#Rastgele seçim işlemlerinin tekrarlabilmesi
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Eğitimi
# Modeli oluşturma
# istatiksel model
model = LogisticRegression(max_iter=200)

# Modeli eğitme
model.fit(X_train, y_train) #logistic regresyon modelini eğitim verisi kullanarak eğitme

# Model Değerlendirme
# Tahmin yapma
# logistic regresyon modelini kullanma
y_pred = model.predict(X_test)

# Performans metrikleri
#bir makine öğrenme modelinin performansını değerlendirmek için çeşitli metrikleri hesaplıyoruz. 
accuracy = accuracy_score(y_test, y_pred) #Doğruluk
precision = precision_score(y_test, y_pred, average='macro') #Kesinlik
recall = recall_score(y_test, y_pred, average='macro') #Duyarlılık modelin pozitif sınıfları ne kadar iyi yakaladığı 
conf_matrix = confusion_matrix(y_test, y_pred) #modelin tahmin ettiği sınıflar ile gerçek sınıflar arasındaki ilişkiyi gösteren bir matris oluşturur.(performans görsel olarak özetler)
class_report = classification_report(y_test, y_pred) #Sınıflandırma raporu(performans) Bu fonksiyon, modelin performansını detaylı bir şekilde özetleyen bir rapor oluşturur.

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"\nConfusion Matrix:\n{conf_matrix}")
print(f"\nClassification Report:\n{class_report}")

# Raporlama
# Bulgu ve içgörülerinizi özetleyen bir rapor oluşturma
print("\nRaporlama:")
print(f"""
- Veri kümesinin genel özellikleri: Iris veri kümesi, iris çiçeklerinin sepal uzunluğu, sepal genişliği, petal uzunluğu ve petal genişliği gibi özelliklerini içerir.
- Sınıf dağılımları: Üç farklı sınıf (setosa, versicolor, virginica) vardır.
- Model Performansı:
  - Accuracy: {accuracy}
  - Precision: {precision}
  - Recall: {recall}
  - Confusion Matrix:
{conf_matrix}
  - Classification Report:
{class_report}
""")
