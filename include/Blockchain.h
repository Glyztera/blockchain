//
//  Blockchain.h
//  Glyztera Blockchain
//
//  Created by ExoHayvan on 8/3/2023
//  Copyright © 2023 Glyztera Coin. All rights reserved.
//

#ifndef Blockchain_h
#define Blockchain_h

#include <vector>

// Blockchain Class
class Blockchain
{
private:
    Block createGenesisBlock();
    std::vector<Block> chain;

public:
    // Constuctor
    Blockchain();
    
    // Public Functions
    std::vector<Block> getChain();
    Block *getLatestBlock();
    bool isChainValid();
    void addBlock(TransactionData data);
    void printChain();
};

#endif /* Blockchain_h */
