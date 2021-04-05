# Portfolio
Social media Mining \n
Understanding Machine vs. Human generated text in news \n
Text generation has been an ongoing research for ages now, it includes open domain text generation, domain text generation, style specific generation, news generation, etc. The models we have used in the project are from the GPT2 Huggingface library which is for open domain text generation. The text generation comes under natural language processing (NLP). NLP has three main steps: text pre-processing, text representation and analysis & modeling.
In the phase I of the project, me and my colleague created a dataset with news based on 2020 elections consisting of headlines, human generated articles, machine generated articles, news source and model for text generation. The machine generated articles were constructed by using the headline as the input and we analyzed the distinction between the human generated text and machine generated one. The model used to achieve this is the GPT-2 model(​Generative Pretrained Transformer 2).

Deliverables:

There are 2 code files and a csv dataset file in our submission.
1. Smm_main_step1.py:​ The first code file is a python script that extracts human generated news articles from ​https://www.nytimes.com/​ for the search topic election 2020. It iteratively loads the website (by clicking the load more button 10 times), to show a total of around 100 articles and then scrapes the links for these articles. The links are then stored in a list, this list is then used to extract the headline and body of each article and the results are input into a csv (comma separated values) file.
2. Smm_main_step2.py:​ The second code file is a python script that gives the machine generated article for each article extracted in File 1, Smm_main_step1.py​ (that was stored in csv and is read by this file), by taking the headline of every article as its input. We use the HuggingFace Python Library and beam search decoding method to generate the machine article for every headline and the results are then stored in a csv file.
3. Smm_dataset.csv:​ We combined the results from both these scripts to create our dataset in the format as shown by Table 1. The dataset was cleaned manually to remove articles that were extracting incomprehensible language/symbols or not generating machine articles and our final dataset consists of 81 row entries and 5 columns, stored in a csv file Smm_dataset.csv (format as in Table 1). The delimiter is comma.

References:

[1] ​https://github.com/AmritaBh/CSE472_Fall20_Files/blob/master/scrape_news.py 
[2] ​https://huggingface.co/blog/how-to-generate
[3] ​https://testguild.com/selenium-webdriver/#:~:text=Selenium%20WebDriver%20is%
​20an%20op​en,where%20you%20need%20browser%20automation.
[4] ​https://stackoverflow.com/questions/52800174/clicking-more-button-via-selenium/
​52804725#52804725
[5] ​https://nytimes.com/2020/09/22/climate/biden-climate-change.html?searchResultPosition=10
