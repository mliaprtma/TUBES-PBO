package model;

// Subclass dari Pengguna
public class Mekanik extends Pengguna {

    // Constructor
    public Mekanik(String id, String nama, String noTelepon) {
        super(id, nama, noTelepon);
    }

    // Method update status servis
    public void updateStatusServis() {
        System.out.println("Status servis diperbarui");
    }
}