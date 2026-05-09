package model;

// Class sparepart
public class SukuCadang {

    // Encapsulation menggunakan private
    private String namaPart;
    private int stock;
    private double harga;

    // Constructor
    public SukuCadang(String namaPart, int stock, double harga) {
        this.namaPart = namaPart;
        this.stock = stock;
        this.harga = harga;
    }

    // Method mengurangi stok
    public void kurangiStock(int jumlah) {
        stock -= jumlah;
    }

    // Method menambah stok
    public void tambahStock(int jumlah) {
        stock += jumlah;
    }

    // Getter stock
    public int getStock() {
        return stock;
    }
}