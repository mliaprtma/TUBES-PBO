package model;

// Subclass dari Pengguna
public class Pelanggan extends Pengguna {

    // Constructor
    public Pelanggan(String id, String nama, String noTelepon) {
        super(id, nama, noTelepon);
    }

    // Method melihat status servis
    public void lihatStatus() {
        System.out.println("Melihat status servis");
    }

    // Method melihat riwayat servis
    public void lihatRiwayat() {
        System.out.println("Melihat riwayat servis");
    }
}