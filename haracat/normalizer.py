from mikatools import *
from natas.normalize import call_onmt


def _chunks(l, n):
	n = max(1, n)
	return [l[i:i+n] for i in range(0, len(l), n)]

def _dechunk(l):
	c = [x[0] for x in l]
	c = " _ ".join(c)
	c = c.replace(" ", "")
	c = c.replace("_"," ")
	return c

def diacritics_sentences(tokenized_sentences):
	chunks = []
	sentence_map = []
	for i, tokenized_sentence in enumerate(tokenized_sentences):
		chunks_l = _chunks([" ".join(x) for x in tokenized_sentence],5)
		sent_chunks = [" _ ".join(x) for x in chunks_l]
		for c in sent_chunks:
			chunks.append(c)
			sentence_map.append(i)
	res = _normalize_chunks(chunks)
	normalized_sentences = []
	cur =0
	norm = []
	for i,s in enumerate(res):
		sent_i = sentence_map[i]
		if sent_i != cur:
			cur = sent_i
			normalized_sentences.append(norm)
			norm = []
		if sent_i == cur:
			norm.append(s)
	normalized_sentences.append(norm)
	r = [_dechunk(x) for x in normalized_sentences]
	return r




def diacritics_sentence(tokens):
	chunks_l = _chunks([" ".join(x) for x in tokens],5)
	chunks = [" _ ".join(x) for x in chunks_l]
	res = _normalize_chunks(chunks)
	return _dechunk(res)

def _normalize_chunks(chunks):
	model_name = "haracat_historical.pt"
	model_name = script_path("models/" + model_name)

	res = call_onmt(chunks, model_name, n_best=1)
	return res