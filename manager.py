import os

file_path = "dados"
for i in os.listdir(file_path):
    name = i.split(".")[0] + "_entrada"
    rnaData = open(file_path + "\\" + i).read().replace("\n", "")
    exec(f"{name} = '{rnaData}'")


def rna_constructor(input):
    aminoacids = ['A', 'T', 'C', 'G']
    cont = {}
    for i in aminoacids:
        for j in aminoacids:
            cont[i + j] = 0
    for k in range(len(input) - 1):
        cont[input[k] + input[k + 1]] += 1
    return cont


class View_Manager:

    @staticmethod
    def HtmlGenerator(name, input):
        multiplying_operator = 1
        html = name + ".html"
        html_path = "static/"+html
        output = open(html_path, "w")
        for y in input:
            transparency = input[y] / max(input.values())
            output.write("<div style='width:100px; border:1px solid #111; height:100px;"
                         " float:left; background-color:rgba(0, 0, 0, " + str(transparency) + "')></div>")
            if multiplying_operator % 4 == 0:
                output.write("<div style='clear:both'></div>")
            multiplying_operator += 1

        output.close()


class Dna_Analizer_Manager:
    # if a new .fasta file is inserted in the database, it will be implemented only and exclusively in the
    # Dna_Analizer_Controller class!

    rna_Bacteria = rna_constructor(bacteria_entrada)
    rna_human = rna_constructor(humano_entrada)

    def __init__(self, rna_Bacteria, rna_human):
        self.rna_Bacteria = rna_Bacteria
        self.rna_human = rna_human
