//
//  TransactionData.h
//  Glyztera Blockchain
//
//  Created by ExoHayvan on 8/3/2023
//  Copyright © 2023 Glyztera Coin. All rights reserved.
//

#ifndef TransactionData_h
#define TransactionData_h

struct TransactionData
{
    double amount;
    std::string senderKey;
    std::string receiverKey;
    time_t timestamp;
    
    TransactionData(){};
    
    TransactionData(double amt, std::string sender, std::string receiver, time_t time)
    {
        amount = amt;
        senderKey = sender;
        receiverKey = receiver;
        timestamp = time;
    };
};

#endif /* TransactionData_h */
