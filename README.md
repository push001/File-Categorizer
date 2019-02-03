# File-Categorizer
A simple program written in **python** which uses the concept of **regular expression** to automate the manual task of selecting and moving the files from one type of category to another type of category.
# Description
As an engineering student , in each semester I need to download the question papers of each subject from the FTP server of my college for exam preparation.
Question Papers of all subject are stored in **year-wise category**, but during preparation I tackle subjects individually. So manually every time I have to go to each folder in year-wise category, choose 1 paper and then move it to **subject-wise category**. So I have created this program which can do such mundane task for me.

Filename is made up of two parts and the glitch is that it is not in ideal form(like - subject_name.pdf) , it may be in multiple forms(with some redundant text at the end of filename or multiple spaces in between the parts of filename) but common thing is that in most of the cases core name (subject_name) is present, so to resolve this issue **regular expression** is used.
