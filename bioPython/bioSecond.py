from Bio import SeqIO

# Загрузка файла с последовательностями
record = SeqIO.read("sequence.fasta", "fasta")

# Получение информации о последовательности
print(f"Организм: {record.description}")
print(f"Длина: {len(record.seq)}")

# Перевод в аминокислотную последовательность
protein_seq = record.seq.translate()
print(f"Аминокислотная последовательность: {protein_seq}")
