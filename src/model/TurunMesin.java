package model;

// Inheritance dari class Servis
public class TurunMesin extends Servis {

    // Constructor
    public TurunMesin(String idServis, String status) {
        super(idServis, status);
    }

    // Override method abstract
    @Override
    public double hitungBiayaJasa() {

        // Biaya jasa turun mesin
        return 1000000;
    }
}