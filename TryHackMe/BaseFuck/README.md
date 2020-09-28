# BaseFuck

This is a challenge that consist in a extract the flag from the contenof the file.

BaseFuck challenge [Here](https://tryhackme.com/jr/basefuck)

## Step 1

![Base64](https://raw.githubusercontent.com/n0obit4/CTF/master/TryHackMe/BaseFuck/Pictures/Base64.png)

If we look the text it can be appreciated a text similar to Base64 cipher.


## Step 2

![Brain Fuck](https://raw.githubusercontent.com/n0obit4/CTF/master/TryHackMe/BaseFuck/Pictures/Chars.jpg)

But if we look at the text and do a deep analysis we can visualize characters that do not belong to base64 characters.


## Step 3

We identify the characters to continue. These are the characters **<>-[].+** and look like the same characters from the brain fuck cipher.

#### BrainFuck

Brainfuck is an esoteric programming language created in 1993 by Urban Müller.

Example of a **Hello, World!** in Brain Fuck

>++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<+
+.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-
]<+.

OK!, Already known this it is necessary to extract the characters from the text.

## Step 4

We create a script and there automatized it.

The script is [here](https://github.com/n0obit4/CTF/blob/master/TryHackMe/BaseFuck/Base_Fuck_Solver.py) in the repository.

We Execute the script and obtain result in a basefuck code.

```
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++++++++++++++++.------------.+++++.++++++++++++++.<+++++++++++++++.>---------.<+++++++++++++.-.>----.<--.------------------.>+++++++.---------..-------.+++++++++++++.<++++++++++++++++++.<+++++++++++++++++++.++++++++..------.>>+++++++++++.
```

After we decode it and obtain the flag


thm{U****************}

