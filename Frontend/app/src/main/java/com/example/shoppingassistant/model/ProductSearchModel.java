package com.example.shoppingassistant.model;

import java.util.ArrayList;

public class ProductSearchModel {
    public QueryReceived query_received;
    public ArrayList<Result> results;
    public class QueryReceived{
        public String query;
        public int max_price;
        public String size;
    }

    public class Result{
        public String name;
        public int price;
        public String size;
        public boolean available;
        public String color;
    }
}
