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
        if !cards[index].isMached {
            // 1. card is not matched
            if let matchIndex = indexOfOneAndOnlyFaceUpCard, matchIndex != index {
                // 2. the choosen card is not we have choosen before
                if cards[matchIndex].indentifier == cards[index].indentifier {
                    cards[matchIndex].isMached = true
                    cards[index].isMached = true
                }
                
                cards[index].isFaceUp = true
                indexOfOneAndOnlyFaceUpCard = nil
            }
            // 2. if the card was choosen before or no choosen card
            else {
                for flipDownIndex in cards.indices {
                    cards[flipDownIndex].isFaceUp = false
                }
                
                cards[index].isFaceUp = true
                indexOfOneAndOnlyFaceUpCard = index
            }
        }
        // 1. if the card was matched before, do nothing
    }
    
    // TODO: Shuffle the cards
    
}
