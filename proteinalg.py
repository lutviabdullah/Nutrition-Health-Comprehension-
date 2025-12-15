class AnalisisKonsumsiProtein:
    def __init__(self):
        """Inisialisasi data konsumsi protein per provinsi di Indonesia"""
        self.data_provinsi = [
            {"provinsi": "DKI Jakarta", "protein": 75.2, "kategori": ""},
            {"provinsi": "Jawa Barat", "protein": 62.8, "kategori": ""},
            {"provinsi": "Jawa Timur", "protein": 65.4, "kategori": ""},
            {"provinsi": "Jawa Tengah", "protein": 61.9, "kategori": ""},
            {"provinsi": "Bali", "protein": 68.7, "kategori": ""},
            {"provinsi": "Sumatera Utara", "protein": 59.3, "kategori": ""},
            {"provinsi": "Sulawesi Selatan", "protein": 63.5, "kategori": ""},
            {"provinsi": "Kalimantan Timur", "protein": 70.1, "kategori": ""},
            {"provinsi": "Papua", "protein": 52.4, "kategori": ""},
            {"provinsi": "Nusa Tenggara Timur", "protein": 55.6, "kategori": ""},
            {"provinsi": "Riau", "protein": 66.3, "kategori": ""},
            {"provinsi": "Banten", "protein": 64.2, "kategori": ""},
            {"provinsi": "DI Yogyakarta", "protein": 67.8, "kategori": ""},
            {"provinsi": "Kalimantan Selatan", "protein": 60.5, "kategori": ""},
            {"provinsi": "Aceh", "protein": 58.9, "kategori": ""}
        ]
        
        # Standar kecukupan protein (IDN, 2019)
        self.standar_protein = {
            "Sangat Baik": 70.0,    # ≥ 70 g/kapita/hari
            "Baik": 60.0,          # 60-69.9 g/kapita/hari
            "Cukup": 50.0,         # 50-59.9 g/kapita/hari
            "Kurang": 0.0          # < 50 g/kapita/hari
        }
    
    def kategorikan_protein(self):
        """Mengategorikan provinsi berdasarkan tingkat konsumsi protein"""
        for prov in self.data_provinsi:
            protein = prov["protein"]
            
            if protein >= self.standar_protein["Sangat Baik"]:
                prov["kategori"] = "Sangat Baik"
            elif protein >= self.standar_protein["Baik"]:
                prov["kategori"] = "Baik"
            elif protein >= self.standar_protein["Cukup"]:
                prov["kategori"] = "Cukup"
            else:
                prov["kategori"] = "Kurang"
    
    def selection_sort_protein_descending(self):
        """Mengurutkan data provinsi berdasarkan konsumsi protein (descending)"""
        data = self.data_provinsi.copy()
        n = len(data)
        
        print("\n=== PROSES SELECTION SORT ===")
        
        for i in range(n):
            # Temukan provinsi dengan protein tertinggi
            max_index = i
            
            for j in range(i + 1, n):
                if data[j]["protein"] > data[max_index]["protein"]:
                    max_index = j
            
            # Tampilkan proses pertukaran
            if max_index != i:
                print(f"Iterasi {i+1}: Tukar {data[i]['provinsi']} ({data[i]['protein']}) "
                      f"dengan {data[max_index]['provinsi']} ({data[max_index]['protein']})")
                
                # Tukar posisi
                data[i], data[max_index] = data[max_index], data[i]
            else:
                print(f"Iterasi {i+1}: {data[i]['provinsi']} sudah pada posisi benar")
        
        return data
    
    def selection_sort_protein_ascending(self):
        """Mengurutkan data provinsi berdasarkan konsumsi protein (ascending)"""
        data = self.data_provinsi.copy()
        n = len(data)
        
        for i in range(n):
            # Temukan provinsi dengan protein terendah
            min_index = i
            
            for j in range(i + 1, n):
                if data[j]["protein"] < data[min_index]["protein"]:
                    min_index = j
            
            # Tukar posisi
            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]
        
        return data
    
    def cari_provinsi_tertinggi_terendah(self):
        """Mencari provinsi dengan konsumsi protein tertinggi dan terendah"""
        tertinggi = self.data_provinsi[0]
        terendah = self.data_provinsi[0]
        
        for prov in self.data_provinsi[1:]:
            if prov["protein"] > tertinggi["protein"]:
                tertinggi = prov
            if prov["protein"] < terendah["protein"]:
                terendah = prov
        
        return tertinggi, terendah
    
    def hitung_rata_rata(self):
        """Menghitung rata-rata konsumsi protein nasional"""
        total = sum(prov["protein"] for prov in self.data_provinsi)
        return total / len(self.data_provinsi)
    
    def analisis_kategori(self):
        """Menganalisis distribusi provinsi per kategori"""
        kategori_count = {"Sangat Baik": 0, "Baik": 0, "Cukup": 0, "Kurang": 0}
        
        for prov in self.data_provinsi:
            kategori_count[prov["kategori"]] += 1
        
        return kategori_count
    
    def tampilkan_hasil_analisis(self):
        """Menampilkan hasil analisis lengkap"""
        # Kategorikan data
        self.kategorikan_protein()
        
        print("=" * 70)
        print("ANALISIS KONSUMSI PROTEIN DI INDONESIA")
        print("Berdasarkan Data Simulasi Susenas 2022")
        print("=" * 70)
        
        # Tampilkan data awal
        print("\n1. DATA AWAL KONSUMSI PROTEIN PER PROVINSI:")
        print("-" * 50)
        print(f"{'No.':<3} {'Provinsi':<25} {'Protein (g/hari)':<15} {'Kategori':<10}")
        print("-" * 50)
        for i, prov in enumerate(self.data_provinsi, 1):
            print(f"{i:<3} {prov['provinsi']:<25} {prov['protein']:<15.1f} {prov['kategori']:<10}")
        
        # Sorting menggunakan selection sort
        data_terurut = self.selection_sort_protein_descending()
        
        # Tampilkan hasil sorting
        print("\n" + "=" * 70)
        print("2. RANKING PROVINSI BERDASARKAN KONSUMSI PROTEIN")
        print("(Menggunakan Algoritma Selection Sort)")
        print("-" * 70)
        print(f"{'Rank':<5} {'Provinsi':<25} {'Protein (g/hari)':<15} {'Kategori':<10}")
        print("-" * 70)
        
        for i, prov in enumerate(data_terurut, 1):
            print(f"{i:<5} {prov['provinsi']:<25} {prov['protein']:<15.1f} {prov['kategori']:<10}")
        
        # Analisis statistik
        print("\n" + "=" * 70)
        print("3. ANALISIS STATISTIK")
        print("-" * 70)
        
        # Rata-rata nasional
        rata_rata = self.hitung_rata_rata()
        print(f"Rata-rata Konsumsi Protein Nasional: {rata_rata:.1f} g/kapita/hari")
        
        # Provinsi tertinggi dan terendah
        tertinggi, terendah = self.cari_provinsi_tertinggi_terendah()
        print(f"Provinsi dengan Konsumsi Tertinggi: {tertinggi['provinsi']} ({tertinggi['protein']} g/hari)")
        print(f"Provinsi dengan Konsumsi Terendah: {terendah['provinsi']} ({terendah['protein']} g/hari)")
        
        # Distribusi kategori
        kategori_dist = self.analisis_kategori()
        print("\nDistribusi Provinsi Berdasarkan Kategori:")
        for kategori, jumlah in kategori_dist.items():
            persentase = (jumlah / len(self.data_provinsi)) * 100
            print(f"  {kategori}: {jumlah} provinsi ({persentase:.1f}%)")
        
        # Rekomendasi
        print("\n" + "=" * 70)
        print("4. REKOMENDASI KEBIJAKAN")
        print("-" * 70)
        
        if terendah["protein"] < 50:
            print(f"⚠️  PERHATIAN: {terendah['provinsi']} memiliki konsumsi protein sangat rendah")
            print("   Rekomendasi:")
            print("   - Program suplementasi protein untuk kelompok rentan")
            print("   - Edukasi gizi seimbang")
            print("   - Pengembangan sumber protein lokal")
        
        if rata_rata < 60:
            print(f"\n📊 Konsumsi protein nasional ({rata_rata:.1f} g/hari) masih di bawah target (60 g/hari)")
            print("   Strategi yang dapat dilakukan:")
            print("   - Peningkatan produksi protein hewani dan nabati")
            print("   - Program fortifikasi pangan")
            print("   - Penyuluhan pola makan beragam")
        
        print("\n" + "=" * 70)
        print("Sumber: Data simulasi untuk keperluan akademis")
        print("Standar: Angka Kecukupan Protein Indonesia (2019)")
        print("=" * 70)

# Fungsi utama untuk menjalankan program
def main():
    # Inisialisasi analisis
    analisis = AnalisisKonsumsiProtein()
    
    # Jalankan analisis lengkap
    analisis.tampilkan_hasil_analisis()
    
    # Demonstrasi tambahan: Sorting ascending
    print("\n" + "=" * 70)
    print("5. DEMONSTRASI TAMBAHAN: ASCENDING SORT")
    print("-" * 70)
    
    data_ascending = analisis.selection_sort_protein_ascending()
    print("Urutan dari Konsumsi Protein Terendah ke Tertinggi:")
    print(f"{'No.':<3} {'Provinsi':<25} {'Protein (g/hari)':<15}")
    print("-" * 45)
    for i, prov in enumerate(data_ascending, 1):
        print(f"{i:<3} {prov['provinsi']:<25} {prov['protein']:<15.1f}")

if __name__ == "__main__":
    main()