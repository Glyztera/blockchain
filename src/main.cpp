//
//  Block.cpp
//  Glyztera Blockchain
//
//  Created by ExoHayvan on 8/3/2023
//  Copyright © 2023 Glyztera Coin. All rights reserved.
//

#include <iostream>
#include <ctime>
#include <vector>

#include "TransactionData.h"
#include "Block.h"
#include "Blockchain.h"

int main()
{
    // Start Blockchain
    Blockchain glyztera;

    // Data for first block
    time_t data1Time;
    TransactionData data1(1.5, "Joe", "Sally", time(&data1Time));
    glyztera.addBlock(data1);

    // Data for second block
    time_t data2Time;
    TransactionData data2(0.2233, "Martha", "Fred", time(&data2Time));
    glyztera.addBlock(data2);

    // Let's see what's in the Glyztera blockchain!
    glyztera.printChain();

    // Is it valid?
    std::cout << "\nIs chain still valid? " << glyztera.isChainValid() << std::endl;

    // Someone's getting sneaky
    Block *hackBlock = glyztera.getLatestBlock();
    hackBlock->data.amount = 10000; // Oh yeah!
    hackBlock->data.receiverKey = "Jon"; // mwahahahaha!

    // Let's look at data
    glyztera.printChain();

    // Awww! Why is it not valid?
    std::cout << "\nIs chain still valid? " << glyztera.isChainValid() << std::endl;

    return 0;
}
