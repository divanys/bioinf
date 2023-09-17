
from Bio import Entrez, SeqIO
import TOKEN
# Устанавливаем email для запроса к NCBI
# Entrez.email = TOKEN.EMAIL

# Запрос к NCBI для получения белковой последовательности по идентификатору
handle = Entrez.efetch(db="protein", id="NP_001191026", rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()

# print(record)
full_protein_sequence = record.seq

# Преобразуем последовательность в строку
full_protein_sequence_string = str(full_protein_sequence)

# Теперь full_protein_sequence_string содержит полную белковую последовательность в виде строки
print(full_protein_sequence_string)