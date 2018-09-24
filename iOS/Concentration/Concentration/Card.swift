//
//  Card.swift
//  Concentration
//
//  Created by phd on 2018/9/24.
//  Copyright © 2018年 phd. All rights reserved.
//

import Foundation

struct Card {
    var isFaceUp = false
    var isMached = false
    var indentifier: Int
    
    static var indentifierFactory = 0
    
    static func getUniqueIndentifier() -> Int {
        indentifierFactory += 1
        return indentifierFactory
    }
    
    init() {
        self.indentifier = Card.getUniqueIndentifier()
    }
}
