import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
import csv

my_list = []
#read the headlines scrapped from the website in step 1
with open('elections_final_2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:

        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        # add the EOS token as PAD token to avoid warnings
        model = TFGPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)

        # encode context the generation is conditioned on
        input_ids = tokenizer.encode(row[0], return_tensors='tf')
        # set no_repeat_ngram_size to 2
        beam_output = model.generate(
            input_ids,
            max_length=1000,
            num_beams=5,
            no_repeat_ngram_size=2,
            early_stopping=True
        )
        my_list.append([tokenizer.decode(beam_output[0], skip_special_tokens=True)])
#write machine generated text into a csv file
file = open('text_generated.csv', 'w+', newline='')
with file:
    write = csv.writer(file)
    write.writerows(my_list)