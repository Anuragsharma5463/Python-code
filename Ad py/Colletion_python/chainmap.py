

from collections import ChainMap

dictionary_1={
    "like":"grapes",
    "Dislike":"Apple",

}
dictionary_2={
    "like":"grapes",
    "Dislike":"Apple",
    
}
list_using_chainmap=ChainMap(dictionary_1,dictionary_2)
print(list_using_chainmap)