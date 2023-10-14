# Импорт необходимых библиотек и модулей
import tensorflow.keras as k
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Flatten

# Ввод тренировочных и тестовых данных
(x_train, y_train) = mnist.load_data()

# Нормализация входных данных
x_train = x_train / 255

# Категоризация выходных данных
y_train_cat = k.utils.to_categorical(y_train, 10)

# Построение полносвязной нейросети
model = k.Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Параметры обучения нейросети
model.compile(optimizer='SGD',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Процесс обучения нейросети
model.fit(x_train, y_train_cat, batch_size=16, epochs=7)

# Сохранение модели
model.save('model2.h5')
