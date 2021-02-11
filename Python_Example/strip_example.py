#strip methodu istenmeyen karakteri kırpma işleminde kullanılır

a = "        ablan star bebeğim                  "
a.strip()

b = "222222ablan star bebeğim22222"
b.strip("2")

c = "****222***222ablan star bebeğim22***222****"
c.strip("2""*")

d = "**/**2///2*/*222ablan star bebeğim22*/**/222**/**"
d.strip("2""*""/")
