def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):  # Eğer eleman bir listeyse, içeriğini düzleştir
            result.extend(flatten(item))  # Rekürsif olarak çağır
        else:
            result.append(item)  # Liste değilse sonucu ekle
    return result

# Örnek kullanım:
input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output_list = flatten(input_list)

print(output_list)
# Çıktı: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
