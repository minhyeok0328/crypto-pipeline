package com.crypto.streaming.abstracts;

public interface Exchange {
    public abstract void start() throws InterruptedException;

    void onMessage();
}
