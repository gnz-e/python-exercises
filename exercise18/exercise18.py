"""
Problema: Median of Two Sorted Arrays

Dados dos arreglos ordenados, nums1 y nums2, de tamaño 
m y n respectivamente, devuelve la mediana de ambos arreglos.

La complejidad temporal total debe ser O(log (m+n)).

Ejemplo 1:

Entrada: nums1 = [1,3], nums2 = [2]
Salida: 2.00000
Explicación: el arreglo resultante es [1,2,3] y la mediana es 2.

Ejemplo 2:

Entrada: nums1 = [1,2], nums2 = [3,4]
Salida: 2.50000
Explicación: el arreglo resultante es [1,2,3,4] y la mediana es (2 + 3) / 2 = 2.5.
"""

def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    array = nums1 + nums2
    array.sort()

    length_array = len(array)

    if length_array % 2 != 0:
        return float(array[length_array // 2])
    else:
        valor1 = array[length_array // 2 - 1]
        valor2 = array[length_array // 2]

        return float(valor1 + valor2) / 2

print(find_median_sorted_arrays([1, 3], [2]))
print(find_median_sorted_arrays([1, 2], [3, 4]))