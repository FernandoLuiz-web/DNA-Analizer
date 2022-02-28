from controllers import Dna_Analizer_Controller


def HtmlGenerator(name, input):
    z = 1
    html = name + ".html"
    html_path = "static/"+html
    output = open(html_path, "w")
    for y in input:
        transparency = input[y] / max(input.values())
        output.write("<div style='width:100px; border:1px solid #111; height:100px;"
                     " float:left; background-color:rgba(0, 0, 0, " + str(transparency) + "')></div>")

        if z % 4 == 0:
            output.write("<div style='clear:both'></div>")
        z += 1

    output.close()


cont = Dna_Analizer_Controller

bacteria = cont.rna_Bacteria
human = cont.rna_human

HtmlGenerator("bacteria", bacteria)
HtmlGenerator("human", human)
