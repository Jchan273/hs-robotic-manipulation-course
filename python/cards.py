cards = {
    "Pikachu": "Common",
    "Charizard": "Rare",
    "Blastoise": "Rare",
    "Mewtwo": "Legendary",
    "Jigglypuff": "Uncommon",
    "Snorlax": "Common",
    "Dragonite": "Rare"
}

def count_rarity_levels(cards):
  """
  >>> count_rarity_levels(cards)
  {'Common': 2, 'Rare': 3, 'Legendary': 1, 'Uncommon': 1}
  """
  
  result = {}
  for card in cards:
    rarity = card[key]
    if rarity in result:
        result[rarity]= result[rarity]+1
    else:
        result[rarity] = 1

  return result
  
def filter_by_rarity(cards, rarity):
  """
  Filter cards based on the specified rarity level.

  Examples:
  >>> filter_by_rarity(cards, "Rare")
  {'Charizard': 'Rare', 'Blastoise': 'Rare', 'Dragonite': 'Rare'}
    
  >>> filter_by_rarity(cards, "Common")
  {'Pikachu': 'Common', 'Snorlax': 'Common'}
  
  >>> filter_by_rarity(cards, "Legendary")
  {'Mewtwo': 'Legendary'}
    
  >>> filter_by_rarity(cards, "Uncommon")
  {'Jigglypuff': 'Uncommon'}
    
  >>> filter_by_rarity(cards, "Mythical")  # Returns an empty dictionary for non-existent rarity
  {}
  """
  di = {}
  for r in cards:
    pok = cards[r]
    if pok == rarity:
        di.update({r:pok})

  return di
    

def sort_cards_by_rank(cards):
    """
    Sort the cards based on rarity using the rank dictionary provied. 
    The output should be a a lists of lists where each sublist is [key, value]
    pair.
    
    HINT: We can sort sequences by a key using the sorted function.
        - https://www.w3schools.com/python/ref_func_sorted.asp
    
    Examples:
    >>> sort_cards_by_rank(cards)
    [['Mewtwo', 'Legendary'], ['Charizard', 'Rare'], ['Blastoise', 'Rare'], ['Dragonite', 'Rare'], ['Jigglypuff', 'Uncommon'], ['Pikachu', 'Common'], ['Snorlax', 'Common']]

    """
    rank = {
        'Common': 1, 'Uncommon': 2, 
        'Rare': 3, 'Legendary': 4
    }
    res = []
    for key, value in cards.items():
        pair = [key,value]
        res.append(pair)


    return sorted(res, key = lambda item: rank[item[1]])