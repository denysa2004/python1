#exercitii partial
#2 semminar 1
'''
nume=input("nume")
prenume=input("prenume")
print(f' Hallo {nume} , {prenume}')

d={}
for ch in nume:
    if ch in d:
        d[ch] += 1
    else:
        d[ch]=1
print(d)
'''
#ex 2
'''
n=(int)(input('n='))
s=0
while n!=0:
    s+=n
    n=(int)(input('n='))
print(s)
'''
#4
'''
s='^&%^##%%^'
new=''
for i in s:
    if i not in new:
        new+=i
print(new)

#5
def prim(n):
    if n==1 or n==0:
        return 0
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1

def main():
    N=(int)(input('N='))
    for i in range(N+1):
        if prim(i)==1:
            print(i)
main()
'''
#seminar 2
#ex 1
'''
def func(word):
    d={}
    for ch in word:
        if ch not in d:
            d[ch]=1
        else:
            d[ch]+=1
    return d
word='school'
print(func(word))

#ex 2
def add_tags(ch,word):
    print(f' < {ch} > {word} </{ch}>')
add_tags('i','python')

#ex 3
def pali(string):
    if string==string[::-1]:
        return 1
    else:
        return 0
print(pali('mama'))
'''
#ex 4
'''
def facult(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
print(facult(4))

#ex 5
def func(word):
    d={}
    for ch in word:
        if ch  not in d:
            d[ch]=1
        else:
            d[ch]+=1
    for ch in word:
        if d[ch]==1:
            print(ch)
func('schooll')

#ex 6
d = {}
d1={}
def func(word,word1):
    for ch in word:
         if ch in d:
             d[ch] += 1
         else:
             d[ch] = 1

    for ch in word1:
         if ch in d1:
             d1[ch] += 1
         else:
             d1[ch] = 1

    if d==d1:
        return True
    else:
        return False

word='ana'
word1='naa'
print(func(word,word1))
'''
#ex 8
def func(word,sub):
    i=0
    j=0
    nr=0
    while i< len(word):
        if word[i] == sub[j]:
            i+=1
            j+=1
            nr+=1

        else:
            i+=1
            nr=0
    if nr==len(sub):
        print('yes')
    else:
        print('no')
word='svingk'
sub='ing'
func(word,sub)