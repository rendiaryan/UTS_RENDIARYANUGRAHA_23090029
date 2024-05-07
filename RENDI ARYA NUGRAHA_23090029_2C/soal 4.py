def hitung_bmi(berat_badan, tinggi_badan):
    bmi = berat_badan / ((tinggi_badan/100) ** 2)
    return bmi

def beri_rekomendasi(bmi):
    if bmi < 18.5:
        return "Kamu berada di bawah berat badan normal. Disarankan untuk meningkatkan asupan makanan."
    elif bmi >= 18.5 and bmi < 24.9:
        return "Kamu memiliki berat badan normal. Pertahankan gaya hidup sehatmu!"
    elif bmi >= 24.9 and bmi < 29.9:
        return "Kamu mengalami overweight. Disarankan untuk menurunkan berat badan dengan diet seimbang dan olahraga teratur."
    else:
        return "Kamu mengalami obesitas. Konsultasikan dengan dokter atau ahli gizi untuk rencana penurunan berat badan yang tepat."

berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (cm): "))

bmi = hitung_bmi(berat, tinggi)
print("BMI kamu adalah:", bmi)
print(beri_rekomendasi(bmi))
