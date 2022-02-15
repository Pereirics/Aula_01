# def fact(n):
# 	if n == 0:
# 		return 1
# 	else:
# 		return n * fact(n - 1)
#
#
# def fact1(n):
# 	r = 1
# 	for n in range(1, n + 1):
# 		r *= n
# 	return r
#
#
# def soma_dois_a_dois(n):
# 	soma = 0
# 	for r in range(1, n + 1, 2):
# 		soma += r
# 	return soma
#
#
# print(fact(3), fact1(3))
# print(soma_dois_a_dois(3))
#
# s = 'Ola mundo'
# s = s + ' ' + s
# print(s)
#
# l = list(range(5))
# l.append(5)
# l.extend(range(7, 10))
# l.insert(6, 6)
#
# print(l)
#
# l.pop()  # apaga e devolve
# l.pop(2)
#
# print(l)
#
# l.reverse()
# print(l)
# l.sort()
# print(l)
#
#
# def maior(s):
# 	return max(s.split(), key=len)
#
#
# la2 = [
# 	('Pedro', [2, 4, 3, 1, 4]),
# 	('Maria', [3, 5, 5, 2, 1]),
# 	('Carla', [5, 5, 5, 5, 3]),
# 	('Jose', [2, 3, 4, 2, 4])
# ]
#
#
# # notas decrescentes, nome crescente
# def ordena(pauta):
# 	final = [(nome, 20 * sum(notas) / 25) for (nome, notas) in pauta]
# 	final.sort(key=lambda t: t[0])  # ordena por nomes
# 	final.sort(key=lambda t: t[1], reverse=True)  # ordena por notas e reverte pois quero ordem decrescente
# 	return final
#
#
# print(ordena(la2))


def frequencia(text):
	l = text.split()
	dic = {}
	for word in l:
		if word in dic:
			dic[word] += 1
		else:
			dic[word] = 1

	tup = []
	for key in dic:
		tup.append((key, dic[key]))

	tup.sort(key=lambda ord_alf: t[0])
	tup.sort(key=lambda ord_num: t[1], reverse=True)
	result = []
	for t in tup:
		result.append(t[0])
	return result


def frequencia1(text): # SÓ ORDENA POR NUMEROS NÃO PELAS CHAVES
	l = text.split()
	dic = {}
	for word in l:
		if word in dic:
			dic[word] += 1
		else:
			dic[word] = 1
	return sorted(sorted(dic), key=dic.get, reverse=True)


texto = "o tempo perguntou ao tempo quanto tempo o tempo tem"
print(frequencia1(texto))

