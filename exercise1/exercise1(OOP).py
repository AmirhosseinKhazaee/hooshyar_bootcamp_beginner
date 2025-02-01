class Dna:
    def __init__(self,dna_seq,recognition_seq):
        self.dna_seq = dna_seq
        self.recognition_seq = recognition_seq
    def fragments(self):
        detected_fragments = [fragment for fragment in self.dna_seq.split(self.recognition_seq) if fragment]
        return detected_fragments    
    def recognition_site(self):
        recognition_site = []
        index = 0
        while True:
            detected = dna_seq.find(recognition_seq,index)
            if detected ==-1:
                break
            if detected not in recognition_site:
                final_detect = detected
                if index > 0:
                    final_detect -= 1 
                recognition_site.append(final_detect)
            index += detected   
        return recognition_site
dna_seq = "AAGAATTCGGAATTCCGGAATTC"
recognition_seq = "GAATTC"
sample1 = Dna(dna_seq,recognition_seq)
# print(sample1.fragments())
# print(sample1.recognition_site())
dna_samples = {
    "DNA Sample 1": {
        "dna_seq": "ATCGGAATTCAGCTGA",
        "recognition_seq": "GAATTC"
    },
    "DNA Sample 2": {
        "dna_seq": "AGTCGGAATTCAGCGAAGGAATTC",
        "recognition_seq": "GAATTC"
    },
    "DNA Sample 3": {
        "dna_seq": "AAGGATCCGGAATTCGGGGAATTCG",
        "recognition_seq": "GAATTC"
    },
    "DNA Sample 4": {
        "dna_seq": "GTAGCGAATTCGATCGAAGGGAATTCGAGCTTGAATTC",
        "recognition_seq": "GAATTC"
    },
    "DNA Sample 5": {
        "dna_seq": "ATCGAATTCGTAGGAATTCAGTAAAGGAATTCAGCGAT",
        "recognition_seq": "GAATTC"
    }
}
for dna_sample in dna_samples:
    dna_seq = dna_samples[dna_sample]["dna_seq"]
    recognition_seq = dna_samples[dna_sample]["recognition_seq"]
    sample = Dna(dna_seq,recognition_seq)
    fragments = sample.fragments()
    recognition_site = sample.recognition_site()
    print(
        f"""
    {dna_sample} :
    Fragments : {fragments}
    Recognition Site : {recognition_site}
"""
    )
