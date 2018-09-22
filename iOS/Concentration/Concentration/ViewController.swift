//
//  ViewController.swift
//  Concentration
//
//  Created by phd on 2018/9/22.
//  Copyright © 2018年 phd. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    var flipCount = 0 {
        didSet{
            flipCountLabel.text = "Flips: \(flipCount)"
        }
    }
    @IBOutlet weak var flipCountLabel: UILabel!
    
    var emojichoices = ["👻", "🎃", "👻", "🎃"]
    
    // action creates a method
    // outlet creates an instance variable(propety)
    @IBOutlet var cardButtons: [UIButton]!
    
    @IBAction func touchCard(_ sender: UIButton) {
        //print("agh! a ghost")
        flipCount += 1
        if let cardNumber = cardButtons.index(of: sender)
        {
            print("cardNumber: \(cardNumber)")
            flipCard(withEmoji: emojichoices[cardNumber], on: sender)
        }
        else {
            print("chosen card was not in cardButtons")
        }
    }
    
    // withEmoji & on are actual parameters  It's for caller
    // Emoji & button are virtual parameters  It's for internal name(in func)
    func flipCard(withEmoji Emoji: String, on button: UIButton) {
        print("filpCard(withEmoji: \(Emoji))")
        if button.currentTitle == Emoji {
            button.setTitle("", for: UIControlState.normal)
            button.backgroundColor = #colorLiteral(red: 1, green: 0.5763723254, blue: 0, alpha: 1)
        }
        else {
            button.setTitle(Emoji, for: UIControlState.normal)
            button.backgroundColor = #colorLiteral(red: 1.0, green: 1.0, blue: 1.0, alpha: 1.0)
        }
    }
}
