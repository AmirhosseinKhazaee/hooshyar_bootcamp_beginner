dna_seq = "AAGAATTCGGAATTCCGGAATTC"
recognition_seq = "GAATTC"
fragments = [fragment for fragment in dna_seq.split(recognition_seq) if fragment]
recognition_site = []
index = 0
while True:
    detected = dna_seq.find(recognition_seq,index)
    if detected ==-1:
        break
    if detected not in recognition_site:
        if index > 0:
            recognition_site.append(detected -1)
        else : 
            recognition_site.append(detected)
    index += detected   
print(fragments)