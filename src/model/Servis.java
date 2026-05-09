package model;

// Abstract class
public abstract class Servis {

    // Attribute servis
    protected String idServis;
    protected String status;

    // Constructor
    public Servis(String idServis, String status) {
        this.idServis = idServis;
        this.status = status;
    }

    // Abstract method
    // Wajib dioverride oleh subclass
    public abstract double hitungBiayaJasa();
}