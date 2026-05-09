package main;

// Import semua class dari package model
import model.*;

public class Main {

    public static void main(String[] args) {

        // Membuat object admin
        Admin admin = new Admin("A01", "Mulia", "08123456789");

        // Menjalankan method login
        admin.login();

        // Menampilkan nama admin
        System.out.println("Nama Admin : " + admin.getNama());

        // Membuat object servis ringan
        Servis servis1 = new ServisRingan("S01", "Proses");

        // Membuat object turun mesin
        Servis servis2 = new TurunMesin("S02", "Selesai");

        // Polymorphism
        System.out.println("Biaya Servis Ringan : " + servis1.hitungBiayaJasa());

        // Polymorphism
        System.out.println("Biaya Turun Mesin : " + servis2.hitungBiayaJasa());
    }
}