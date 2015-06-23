from random import choice

noun_list = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]

verb_list = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]

adjective_list = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]

preposition_list = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]

adverb_list = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

used_words = []


def random_unused_word(word_list, used_word_list):
    chosen_word = choice(word_list)
    if chosen_word not in used_word_list:
        used_word_list.append(chosen_word)
        return chosen_word
    else:
        return random_unused_word(word_list, used_word_list)

adj1, adj2, adj3 = random_unused_word(adjective_list, used_words), random_unused_word(adjective_list, used_words), random_unused_word(adjective_list, used_words)

n1, n2, n3 = random_unused_word(noun_list, used_words), random_unused_word(noun_list, used_words), random_unused_word(noun_list, used_words)

v1, v2, v3 = random_unused_word(verb_list, used_words), random_unused_word(verb_list, used_words), random_unused_word(verb_list, used_words)

p1, p2 = random_unused_word(preposition_list, used_words), random_unused_word(preposition_list, used_words)

adv1 = random_unused_word(adverb_list, used_words)


def make_poem():
    poem = """{} {} {} {} the {} {}\n{}, the {} {}\nthe {} {} {} a {} {}""".format(adj1, n1, v1, p1, adj2, n2, adv1, n1, v2, n2, v3, p2, adj3, n3)
    if adj1[0] in ['a', 'e', 'i', 'o', 'u']:
        poem = "An " + poem
        title = "An {} {}\n\n".format(adj1, n1)
        poem = title + poem
        return poem
    else:
        poem = "A " + poem
        title = "A {} {}\n\n".format(adj1, n1)
        poem = title + poem
        return poem
print make_poem()
