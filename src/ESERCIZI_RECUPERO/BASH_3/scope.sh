#PRIMA PARTE
function g(){
echo $x; x=2;
}
function f(){
x=3; g;  # 3) viene assegnato un nuovo valore alla variabile e viene chiamata g, che stampa il valore appena assegnato e ne assegna un altro ancora
}
x=1 # 1) viene assegnato il valore alla variabile
f   # 2) viene chiamata f
echo $x # 4) viene stampato il valore assegnato da g



#SECONDA PARTE
function g(){
echo $x; x=2;
}
function f(){
local x=3; g;  # 3) viene assegnato un nuovo valore alla variabile e viene chiamata g, che stampa il valore appena assegnato e ne assegna un altro ancora, ma essendoci il "local" queste assegnazioni hanno valore solo all'interno di f
}
x=1 # 1) viene assegnato il valore alla variabile
f   # 2) viene chiamata f
echo $x # 4) viene stampato il valore assegnato inizialmente