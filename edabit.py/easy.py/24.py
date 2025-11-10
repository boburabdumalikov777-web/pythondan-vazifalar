'''Create a function that takes a single word string and does the following:

Concatenates inator to the end if the word ends with a consonant, otherwise, concatenate -inator instead.

Adds the word length of the original word to the end, supplied with "000".

The examples should make this clear.

Examples
inator_inator("Shrink") ➞ "Shrinkinator 6000"

inator_inator("Doom") ➞ "Doominator 4000"

inator_inator("EvilClone") ➞ "EvilClone-inator 9000"'''
def inator_inator(inv):
	x="aueioAUEIO"
	if inv[-1] in x:
		y=f"{inv}-inator {len(inv)}000"
	else:
		y=f"{inv}inator {len(inv)}000"
	return y


print(inator_inator("Shrink")) # ➞ "Shrinkinator 6000"

print(inator_inator("Doom")) #➞ "Doominator 4000"

print(inator_inator("EvilClone")) #➞ "EvilClone-inator 9000"