package model;

// Inheritance dari class Servis
public class ServisRingan extends Servis {

    // Constructor
    public ServisRingan(String idServis, String status) {
        super(idServis, status);
    }

    // Override method abstract
    @Override
    public double hitungBiayaJasa() {

        // Biaya jasa servis ringan
        return 100000;
    }
}