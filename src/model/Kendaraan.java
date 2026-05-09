package model;

// Class kendaraan
public class Kendaraan {

    // Attribute kendaraan
    private String idKendaraan;
    private String jenis;
    private String nomorPolisi;

    // Constructor
    public Kendaraan(String idKendaraan, String jenis, String nomorPolisi) {
        this.idKendaraan = idKendaraan;
        this.jenis = jenis;
        this.nomorPolisi = nomorPolisi;
    }

    // Method menampilkan info kendaraan
    public void getInfo() {
        System.out.println("ID Kendaraan : " + idKendaraan);
        System.out.println("Jenis        : " + jenis);
        System.out.println("Nomor Polisi : " + nomorPolisi);
    }
}