package model;

// Class transaksi
public class Transaksi {

    // Attribute transaksi
    private String idTransaksi;
    private double totalBiaya;

    // Constructor
    public Transaksi(String idTransaksi) {
        this.idTransaksi = idTransaksi;
    }

    // Method menghitung total biaya
    public void hitungTotal(double biayaServis, double hargaSparepart) {
        totalBiaya = biayaServis + hargaSparepart;
    }

    // Method cetak nota
    public void cetakNota() {
        System.out.println("ID Transaksi : " + idTransaksi);
        System.out.println("Total Biaya  : " + totalBiaya);
    }
}