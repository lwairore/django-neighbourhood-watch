Regular Expression
-Made available through the re module.
-You specify the rules for the set of possible strings that you want to match. You can also use Res to modify a string or to split it apart in various ways.
-For advanced use, it may be necessary to pay careful attention to how the engine will execute a given RE, and write the RE in a certain way in order to produce bytecode that runs faster.

Matching Characters
-The regular expression test will match the string test exactly. 
-There are exceptions to this rule; some characters are special metacharacters, and dont match themselves. Instead, they signal that some out of the ordinary thing should be matched, or they affect other positions of the RE by repeating them or changing their meaning.:
. ^ $ * + ? { } [ ]  \  | ( )

[ and ]
-[ and ] are used for specifying a character class, which is a set of characters that you wish to match. 
-Characters can be listed individually, or a range of characters can be indicated by giving two characters and separating them by ‘-’.
-eg, [abc] will match any of the characters a, b or c; this is the same as [a-c], which uses a range to express the same set of charaters.
-Metacharcters are not active inside classes. Eg, [akm$] will match any of the characters ‘a’, ‘k’, ‘m’ or ‘$’; $ is stripped of it’s special nature inside the character class.
-You can match the characters not listed within the class by complementing the set by incluiding ‘^’ as the first character of the class. Eg, [^5] will match any character except ‘5’. If the caret appears elsewhere in a character class, it does not have special meaning. Eg, [5^] will match either a ‘5’ or a ‘^’.

\
-The backslash can be followed by various characters to signal various special sequences.
-Also used to escape all the metacharacters so you can still match them in patterns; for eg, if you want to match a [ or \, you can precede them with a backslash to remove their special meaning: \[ or \\.
-Some of the special sequences beginning with ‘\’ represent predefined sets of characters that are often useful, such as digits, the set of letters, or the set of anything that isnt a whitespace.
-Eg: \w matches any alphanumeric character. If the regex pattern is expressed in terms of bytes, \w is equivalent of [a-zA-Z0-9_]. You can use the more restricted definition of \w in a string pattern by supplying the re.ASCII flag when compling the regular expression.
\d- Matches any decimal digit; equivalent to the class [0-9].
\D-Matches any non-digit character; equivalent to the class [^0-9].
\s-Matches any white space character; this equivalent to the class [ \t\n\r\f\v].
\S-Matches any non-whitespace character; equivalent to the class [^ \t\n\r\f\v].
-These sequences can be included inside a character class. Eg, [\s,.] is a character class that will match any whitespace character or ‘,’ or ‘.’

.(dot)
-It matches anything except a newline character, and there’s an alternate mode (re.DOTALL) where it will match even newline.
-. is often used where you want to match “any charcter”.

Repeating Things
-You can specify portions of the RE that must be repeated a certain number of times.

*
-* doesnt match the literal character ‘*’; instead, it specifies that the previous charcter can be matched zero or more times, instead of exactly once.
-Eg, ca*t will match ‘ct’ (0 ‘o’ characters), ‘cat’ (1 ‘a’).
-Repetitions such as * are greedy; when repeating a RE, the matching engine will try to repeat it as many times as possible. If later portions of the pattern dont match, the matching engine will then back up and try again with fewer repetitions.
-Eg, a[bcd]*b. This matches ‘a’, zero or ,more letters from the class [bcd], and finally ends with a ‘b’. Now imagine matching this RE against the string ‘abcd’.
1.  a – The a in the RE matches.
2. abcd – The engine matches [bcd]*, going as far as it can, which is to the end of the string.
3. Failure – The engine tries to match b, but the curremt position is at the end of the string, so it fails.
4. abcb- Back up, so that [bcd]*  matches one less charcter.
5. Failure – Try b again, but the current position is at the last character, which is a ‘d’.
6. abc – Back up again, so that [bcd]* is only matching bc.
6.abcb – Try b again. This time the charcter at the current position is ‘b’, so it succeeds.
-This demonstrates how the mathing engine goes as far as it can at first, and if no match is found it will then progressively back up and retry the rest of the RE again and again. It will back up until it has tried zero matches for [bcd]* , and if that subsequently fails, the engine will conclude that the string doesnt match the RE at all.

+ 
-Another repeating metacharacter, which matches one or more times.
-Remember * matches zero or more times so whatever’s being repeated may not be present at all, while + matches one or more times.
-Eg, ca+t will match ‘cat’ (1 ‘a’) but wont match ‘ct’.

-There are two more repeating qualifiers. The question mark character, ?, matches either once or zero times; Eg. home-?brew matches either ‘homebrew’  or ‘home-brew’.

-{m,n} where m  and n are decimal integers. This qualifier means there must be atleast m repetitions and at most n. For eg, a/{1,3}b will match ‘a/b’, ‘a//b’ and ‘a///b’. It wont match ‘ab’, which has no slashes or ‘a////b’ which has four slashes.
-You can omit either m or n ; Omitting m is interpreted as a lower limit of 0, while omitting n results in an upper bound of infinity.
-NB;
 {0,} is the same as *, 
 {1,} equivalent to +,
 {0,1} same as ?
It’s better to use *, +, or ? When you can because they’re shorter and easier to read.


Using Regular Expressions
-The re module providesan interface to the regular expression engine allowing you to compile Res into objects and then perform matches with them.

Compiling Regular Expressions
-Regular expressions are compiled into pattern objects, which have methods for various operations such as searching for pattern matches or performing string substituions.
 import re
 p = re.compile(‘ab*’)
 p  #re,compile(‘ab*’)
-re.compile() also accepts an optional flags argument, used to enable various special features and syntax variations.
 p = re.compile(‘ab*’, re.IGNORECASE)
-Res are passed/handled as strings because regular expressions arent part of the core Python language, and no special syntax was created for expressing them.
-Putting Res in strings keep the Python language simpler, but has one disadvantage which is the next topic.

The Backslah Plague
-Regular expressions use the backslash character(‘\’) to indicate special forms or allow special characters to be used without invoking their special meaining. This conflicts with Python’s usage of the same character for the same purpose in string literals.
-Let’s say you want to write a RE that matches the string \section, which might be found in a LaTeX file. Start with the desired string to be matched, section. Next, you must escape any backslashes and other metacharacters by preeceeding them with a backslash, \\section. The resulting string must be passed to re.compile() must be \\section. However, to express this as a Python string literal, both backslashes must be escaped again hence, \\\\section.
-To match a literal backslash , one has to write ‘\\\\’ as the RE string, because the regular expression must be \\, and each backslash must be expressed as \\ inside a regular Python string literal. 
The solution is to use Python’s raw string notation for regular expressions; backslashes are not handled in any special way in a string literal prefixed with ‘r’, so r“\n” is a two character string containing ‘\’ and ‘n’, while “\n” is a  one-character string containing a newline. Regular expressions will often be written in Python code using this raw string notation.

-In addition, special escape sequences that are valid in regular expresiions, but not valid as Python string literals, now result in a DeprecationWarning and will eventually become a SyntaxError, which means the sequence will be invalid if raw string notation or escaping the backslashes isnt used.
ab*(Regular String) r“ab*”(Raw string)
\\\\section(Regular String)  r“\\section”(Raw string)
\\w+\\s+\\l(Regular string) r“\w+\s+\l” (Raw string)

Performing Matches
-match() - Determine if the RE matches at the beginning of the string.
-search() - Scan through a string, looking for any location where this RE matches.
-findall() - Find all sunstrings where the RE matches, and returns them as a list.
-finditer() - Find all substrings where the RE matches, and returns them as an iterator.

-match() and search() return None if no match can be found. If they’re successful, a match object instance is returned, containing information about the match: where it starts and ends, the substring it matched, and more.

 import re
 p = re.compile(‘[a-z]+’)
 p #re.compile(‘[a-z]’)
-Now you can try matching various strings against RE [a-z]+.An empty string should match ar all, since +means ‘one or more repetions’. Match() should return None in this case. You can explicitly print the result of match() to make this clear.
 p.match(“”)
 print(p.match(“”)) #None

Next, let’s try it on a string tempo that should match. In this case match() will return a  match object, so you should store the result in a  variable for future use.
m = p.match(‘tempo’)
 m # <re.Match object; span=(0, 5), match = ‘tempo’>
Match object instances also have several methods and attributes; the most important are:
1. group() - Return the string matched by the RE
2. start() - Return the starting position of the match
3. end() - Return the ending position of the match
4. span() - Return a tuple containing the (start, end) positions of the match.
 m.group() # ‘tempo’
 m.start(), m.end() #(0,5)
 m.span() # (0, 5)
-Since the match() method only checks if the RE matches at the start of a string, start() will always be zero. However, the search() method of patterns scans through the string, so the match may not start at zero in that case.
print(p.match(‘::: mesage’ )) #None
m = p.search(“::: message”); print(m) # <re.Match object; span=(4, 11) , match= “message”
m.group() # ‘message’
m.span() #(4, 11)
- In actual programs, the most  common style is to store the match object in a variable, and then check if it was None.
 p = re.compile( … ) 
m = p.match( ‘string goes here’ )
if m:
	print(‘Match found: ’, m.group())
else: 
	print(‘No match’)
- findall() returns a list of mactching strings:
 p = re.comple(r‘\d+’)
 p.findall(‘12 drummers drumming, 11 pipers piping, 10 lords a leaping ’) 
# [‘12’, ‘11’, ‘10’]
- The r prefix, making the literal a raw string literal, is needed in this eg. because escape sequences in a normal “cooked” string literal are not recognized by Python.
-findall() has to create the entire list before it can be returned as the result. The finditer() method returns a sequence of match object instances as an iterator:
p = re.compile(r‘\d+’)
iterator = p.finditer(‘12 drummers drumming, 11 … 10 ...’)
iterator #<callable_iterator object at 0x...>
for match in iterator:
	print(match.span())
#(0, 2)
#(22, 24)
#(29, 31)