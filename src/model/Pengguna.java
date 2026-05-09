package model;

// Class induk (parent class)
public class Pengguna {

    // Attribute protected agar bisa diwariskan ke subclass
    protected String id;
    protected String nama;
    protected String noTelepon;

    // Constructor
    public Pengguna(String id, String nama, String noTelepon) {
        this.id = id;
        this.nama = nama;
        this.noTelepon = noTelepon;
    }

    // Method login
    public void login() {
        System.out.println("Login berhasil");
    }

    // Method logout
    public void logout() {
        System.out.println("Logout berhasil");
    }

    // Getter nama
    public String getNama() {
        return nama;
    }
}