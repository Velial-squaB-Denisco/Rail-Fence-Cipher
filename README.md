# Rail-Fence-Cipher

# Шифр Rail-Fence

## 📜 Описание

Шифр Rail-Fence — это метод перестановочного шифрования, который используется для защиты текстовой информации. Он представляет собой визуальное расположение символов строки в зигзагообразном порядке по "рельсам", что делает текст нечитаемым без знания ключа (количества рельсов).

## 🔑 Принцип работы

### 1. Подготовка данных

- **Символы**: Шифр Rail-Fence может работать с любыми символами, включая буквы, цифры и специальные символы.
- **Удаление пробелов**: Входной текст может быть очищен от пробелов и других нежелательных символов, если это необходимо.

### 2. Определение количества рельсов

- **Количество рельсов**: Пользователь задает количество рельсов, по которым будет распределяться текст. Это число должно быть >= 2.

### 3. Шифрование текста

Шифрование текста происходит следующим образом:

1. **Создание матрицы**: На основе количества рельсов создается матрица, где строки соответствуют рельсам, а столбцы — позициям символов.

2. **Заполнение матрицы**:
   - Символы текста заполняют матрицу в зигзагообразном порядке: сначала вниз, затем вверх, и так далее.
   - Направление меняется, когда достигается верхний или нижний рельс.

3. **Формирование закодированной строки**:
   - Закодированная строка формируется путем объединения всех символов в каждом рельсе.

### 4. Расшифрование текста

Для расшифрования используется то же количество рельсов:

1. **Создание матрицы**: Аналогично шифрованию, создается матрица с метками позиций.

2. **Заполнение матрицы символами**:
   - Закодированная строка заполняет матрицу в порядке, определенном метками.

3. **Формирование декодированной строки**:
   - Декодированная строка формируется путем чтения символов из матрицы в зигзагообразном порядке.

### 5. Пример шифрования и расшифрования

**Исходный текст**: `HELLO`
**Количество рельсов**: `3`

1. Заполнение матрицы:
   ```
   H   E
    E L O
   ```

2. Зашифрование:
   - Сначала читаем первый рельс: `HE`
   - Затем второй рельс: `ELO`

**Зашифрованный текст**: `HEELO`

3. Расшифрование выполняется аналогично с использованием 3 рельсов.

## 🔒 Заключение

Шифр Rail-Fence позволяет пользователю задавать количество рельсов, что делает его гибким инструментом для шифрования текста. Однако, как и любой другой шифр, он подвержен атакам, поэтому важно использовать достаточное количество рельсов для обеспечения безопасности.

## 🔍 Почему стоит использовать шифр Rail-Fence?

Шифр Rail-Fence — это классический метод шифрования, который до сих пор вызывает интерес благодаря своей простоте и визуальной наглядности. Он позволяет пользователю настроить количество рельсов, что делает его уникальным для каждого случая использования. Хотя современные методы шифрования могут быть более надежными, шифр Rail-Fence остается отличным учебным инструментом и может быть использован для базовой защиты данных.

---

## 📜 Документация кода

---

## Введение

Шифр Rail-Fence — это классический метод перестановочного шифрования, который использует зигзагообразное расположение символов по "рельсам" для шифрования и дешифрования текста. Этот класс реализует шифр Rail-Fence на языке Python.

## Класс `RailFenceCipher`

### Инициализация

```python
class RailFenceCipher(object):
    def __init__(self, num_rails):
        self.num_rails = num_rails
```

- **`num_rails`**: Количество рельсов, используемых для шифрования и дешифрования. Должно быть >= 2.

### Методы

#### `encode(text)`

Шифрует переданный текст с использованием заданного количества рельсов.

- **Параметры**:
  - `text`: Текст, который нужно зашифровать.

- **Возвращает**: Зашифрованный текст.

- **Описание**:
  - Метод использует количество рельсов для распределения символов текста в зигзагообразном порядке.
  - Символы затем объединяются в зашифрованную строку.

#### `decode(text)`

Дешифрует переданный текст с использованием заданного количества рельсов.

- **Параметры**:
  - `text`: Текст, который нужно расшифровать.

- **Возвращает**: Расшифрованный текст.

- **Описание**:
  - Метод использует количество рельсов для восстановления исходного порядка символов.
  - Символы затем объединяются в расшифрованную строку.

### Обработка ошибок

- Если при шифровании или дешифровании возникает ошибка (например, если текст содержит символы, не входящие в алфавит), метод возвращает исходный текст и выводит сообщение "ERROR".

### Пример использования

```python
cipher = RailFenceCipher(3)
e = cipher.encode("HELLO")
d = cipher.decode(e)
print(e, d)
```

- **Вывод**:
  ```plaintext
  HEELO HELLO
  ```

### Особенности

- **Симметричность**: Шифр Rail-Fence является симметричным, то есть для шифрования и дешифрования используется одно и то же количество рельсов.
- **Безопасность**: Шифр Rail-Fence более устойчив к криптографическим атакам по сравнению с простыми перестановочными шифрами, но все же уязвим для атак с использованием частотного анализа, особенно если количество рельсов мало.

## Зависимости

Для работы этого кода не требуется никаких дополнительных библиотек.

## Автор

Velial-squaB-Denisco
