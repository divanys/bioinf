from Bio.Seq import Seq

# Создаем объект с последовательностью ДНК
dna_sequence = Seq("AGTACACTGGT")

# Выводим последовательность
print(dna_sequence)

# Получаем комплементарную последовательность ДНК
complementary_seq = dna_sequence.complement()
print(complementary_seq)

# Транскрибируем ДНК в РНК
rna_sequence = dna_sequence.transcribe()
print(rna_sequence)