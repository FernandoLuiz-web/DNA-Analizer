from manager import Dna_Analizer_Manager, View_Manager

cont = Dna_Analizer_Manager
view = View_Manager


bacteria = cont.rna_Bacteria
human = cont.rna_human

view.HtmlGenerator("bacteria", bacteria)
view.HtmlGenerator("human", human)
