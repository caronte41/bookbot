def count_words(str):
    num = str.split()
    return len(num)

def count_chars(str):
    char_arr = [char.lower() for word in str for char in word]  
    new_dict = {}
    for sc in char_arr:
        new_dict[sc] = new_dict.get(sc, 0) + 1
    return new_dict    

def char_stats_sorted(char_dict):    
    return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
            
