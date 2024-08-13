# Gerekli Kütüphanelerin Yüklenmesi
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns

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

# Keşifsel Veri Analizi (EDA)
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

# Korelasyon matrisini ısı haritası ile gösterme
print("\nKorelasyon matrisinin ısı haritası:")
plt.figure(figsize=(10, 7))
# 'class' sütununu çıkararak sadece sayısal sütunlarla korelasyon matrisini hesaplayın
numeric_columns = iris.drop(columns=['class'])
sns.heatmap(numeric_columns.corr(), annot=True, cmap='coolwarm')
plt.show()

# Raporlama
# Bulgu ve içgörülerinizi özetleyen bir rapor oluşturma
print("\nRaporlama:")
print("""
- Veri kümesinin genel özellikleri: Iris veri kümesi, iris çiçeklerinin sepal uzunluğu, sepal genişliği, petal uzunluğu ve petal genişliği gibi özelliklerini içerir. 
- Sınıf dağılımları: Üç farklı sınıf (setosa, versicolor, virginica) vardır ve her bir sınıf eşit sayıda gözlem içermektedir.
- Önemli korelasyonlar: Sepal genişliği ve uzunluğu ile petal genişliği ve uzunluğu arasında belirgin bir korelasyon gözlemlenmiştir.
- Dikkat çekici özellikler: Setosa sınıfı, diğer sınıflardan belirgin bir şekilde ayrılmaktadır ve özellikle petal uzunluğu ve genişliği açısından farklılık göstermektedir.
""")
