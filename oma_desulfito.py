__author__ = 'admin'
#cepas=['2Ddes', '3PCE1s', '2Dmes', '2DP7s', '2Dres', '2LMGs', '2PCESs', '2PCP1s' , '2TCPAs', '2Y51s', '3LBEs', 'DCB2s', 'DhaTCE1_proteomes.txt' ]
names=['Desulfitobacterium dehalogenans ATCC 51507', 'Desulfitobacterium sp. PCE1','Desulfitobacterium metallireducens DSM 15288', 'Desulfitobacterium hafniense DP-7',   'Dehalobacter restrictus PER-K23', 'Desulfitobacterium dichloroeliminans LMG P-21439', 'Desulfitobacterium hafniense PCE-S', 'Desulfitobacterium hafniense PCP-1', 'Desulfitobacterium hafniense TCP-A', 'Desulfitobacterium hafniense Y51', 'Desulfitobacterium sp. LBE', 'Desulfitobacterium hafniense DCB-2', 'Desulfitobacterium hafniense TCE1']
index= open('index_desulfito.txt', 'r').readlines()
comunes = open('Core.txt','w')
orto = open('OrthologousGroups.txt','r').readlines()
single = open('Singletons.txt','w')
#fasta = open('Fasta.fasta','w')
over = open('Overview.txt','w')
inparoutput = open('Inparalogs.txt','w')
pairsoutput = open('Pairs.txt','w')
ortho= open('Orthologous_Desulfito.xls', 'w')
pairwise=[]
####### quitar # cuando termines orto
#for c in range(0, len(cepas)-1):
 #   for x in range(1, 12):
  #      pairwise.append(str(cepas[c])+'-'+str(cepas[x]+'.txt'))

#for i in range(0,len(pairwise)):
#    try:
#info=[]
#for g in range(0, len(cepas)):
#    proteome=open(cepas[g]+'.fa', 'r').read()
#    proteome.split('>')
#    for p in proteome:
#        info.append(p[:p.index('\n')])
#print info[0:15]
### OrthologousGroups
lineas = []
fila = []
lineabuena=[]
todosorto=[]
orto=orto[4:]
listaidusados=[]
#for i in index: #por cada gen del indice completo de todos los genes de todas las bacterias
for o in orto:  #por cada linea de ortologos, sacar el id nada mas
    writelinea=[]
    fila=o.split('\t')
    fila=fila[1:]
    for j in fila:
        test=0
        if ':' in j:
            colon=j.index(':')
            if j.count(':') > 1:
                colon2=j[colon+3:].index(':')+1
                colon=colon+colon2+2
                id=j[j.index(':')+1:colon]
                for i in index: #por cada linea de headers
                    if id in i: #por cada hit en la fila
                        test=i.count(id)
                        listaidusados.append(id)
                        ortho.write(str(id+'\t'+i[i.find(' ')+1:-1]+'\t'))
                    if test>1:
                        print id
    #for w in writelinea
    #ortho.write(str(writelinea))
    ortho.write('\n')

print 'fini'