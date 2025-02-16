package com.example.shoppingassistant.model;

public class Product {
    private String name;
    private int price;
    private String size;
    private boolean available;

    public String getName() {
        return name;
    }

    public int getPrice() {
        return price;
    }

    public String getSize() {
        return size;
    }

    public boolean isStock() {
        return available;
    }
}

