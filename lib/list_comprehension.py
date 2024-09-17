#!/usr/bin/env python3

def return_evens(num_list):
    evenNumbers = [(n) for n in (num_list) if n % 2==0]
    return evenNumbers

def make_exclamation(sentence_list):
    return [n + "!"for n in (sentence_list)]