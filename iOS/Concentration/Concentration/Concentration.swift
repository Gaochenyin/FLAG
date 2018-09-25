//
//  Concentration.swift
//  Concentration
//
//  Created by phd on 2018/9/24.
//  Copyright © 2018年 phd. All rights reserved.
//

import Foundation

class Concentration {
    var cards = [Card]()
    
    init(numberOfPairsOfCards: Int) {
        for _ in 0...numberOfPairsOfCards {
            let card = Card()
            cards += [card, card]
        }
    }
    
    var indexOfOneAndOnlyFaceUpCard: Int?
    
    func chooseCard(at index: Int) {
        
    }
    
    // TODO: Shuffle the cards
    
}
