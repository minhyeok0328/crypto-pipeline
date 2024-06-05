package org.crypto;

import org.crypto.processing.ByBit;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");

        ByBit byBit = new ByBit();
        byBit.start();
    }
}