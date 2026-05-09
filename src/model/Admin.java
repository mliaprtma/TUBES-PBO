package model;

// Inheritance dari class Pengguna
public class Admin extends Pengguna {

    // Constructor subclass
    public Admin(String id, String nama, String noTelepon) {
        // Memanggil constructor parent class
        super(id, nama, noTelepon);
    }

    // Method tambah data
    public void tambahData() {
        System.out.println("Data ditambahkan");
    }

    // Method hapus data
    public void hapusData() {
        System.out.println("Data dihapus");
    }

    // Method update data
    public void updateData() {
        System.out.println("Data diperbarui");
    }
}