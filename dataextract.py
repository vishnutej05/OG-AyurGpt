import difflib
from database import csv_thing,meds,content,dose,precaution,reference
from prompt_processing import tokenizer

def textGen(user_input):
    dis=csv_thing()
    user_words = tokenizer(user_input)

    corrections = []
    dis_indices = []
    corrected_input = []

    def find_correction(word):
        closest_match = []
        dis_index = []

        for category_index, category in enumerate(dis):
            matches = difflib.get_close_matches(word, category, cutoff=0.9)

            if matches:
                closest_match.append(matches[0])
                dis_index.append(category_index)

        return closest_match, dis_index

    for i, word in enumerate(user_words):
        correction, dis_index = find_correction(word)
        for c in correction:
            corrections.append(c if c is not None else word)
        for d in dis_index:
            if d is not None:
                dis_indices.append(d)
    for j in corrections:
        corrected_input.append(j)

    medicines=meds()
    contents=content()
    dosage=dose()
    precautions=precaution()
    references=reference()
    #print(dis_indices)
    if dis_indices != []:
        med=str(medicines[dis_indices[0]][0]).capitalize()
        con=str(contents[dis_indices[0]])
        dos=str(dosage[dis_indices[0]][0])
        pre=str(precautions[dis_indices[0]][0]).upper()
        ref=str(references[dis_indices[0]][0]).upper()
        symp=str(corrected_input[0]).capitalize()
        text = f"Identified Symptom: {symp} <br />Ayurvedic Formulation Matched: {med} <br />Contents: {con} <br />Dosage: {dos} <br />Precautions: {pre} <br />Reference: {ref}"

        
        return(text)
    
    return 'No Data Found'

# print(textGen('sdkjfghgjks'))




