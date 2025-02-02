from collections import Counter

cipher_text = """
LOJUM YLJME PDYVJ QXTDV SVJNL DMTJZ WMJGG YSNDL UYLEO SKDVC
GEPJS MDIPD NEJSK DNJTJ LSKDL OSVDV DNGYN VSGLL OSCIO LGOYG
ESNEP CGYSN GUJMJ DGYNK DPPYX PJDGG SVDNT WMSWS GYLYS NGSKJ
CEPYQ GSGLD MLPYN IUSCP QOYGM JGCPL GDWWJ DMLSL OJCNY NYLYD
LJQLO DLCNL YPLOJ TPJDM NJQLO JWMSE JGGJG XTUOY EOOJO DQDMM
YBJQD LLOJV LOJTV YIOLU JPPES NGYQJ MOYVD GDNJE MSVDN EJM
"""

substitution_map = {
    'A': 'J', 'B': 'I', 'C': 'B', 'D': 'R', 'E': 'K', 'F': 'T',
    'G': 'C', 'H': 'N', 'I': 'O', 'J': 'F', 'K': 'Q', 'L': 'Y',
    'M': 'G', 'N': 'A', 'O': 'U', 'P': 'Z', 'Q': 'H', 'R': 'S',
    'S': 'V', 'T': 'W', 'U': 'M', 'V': 'X', 'W': 'L', 'X': 'D',
    'Y': 'E', 'Z': 'P'
}

def decrypt_text(cipher_text, substitution_map):
    decrypted_text = []
    for char in cipher_text:
        if char in substitution_map:
            decrypted_text.append(substitution_map[char])
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def count_letters(text):
    cleaned_text = text.replace(" ", "").replace("\n", "")
    return Counter(cleaned_text)

letter_count = count_letters(cipher_text)

print("Conteo de letras en el texto cifrado:", letter_count)

decrypted_text = decrypt_text(cipher_text, substitution_map)
print(decrypted_text)
