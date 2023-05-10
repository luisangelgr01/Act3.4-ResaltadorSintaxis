from flask import Flask, render_template_string, send_file
import re

app = Flask(__name__)

@app.route('/generate_html_css')
def generate_html_css():
    regex_patterns = {
        'PALABRA_RESERVADA': r"\b(?:and|break|class|def|elif|else|False|for|if|import|not|or|return|True|while)\b",
        'REAL': r"[+-]?[0-9]+(?:\.[0-9]*)?(?:[eE][+-]?[0-9]+)",
        'FLOTANTE': r'\d*\.\d+(?:[eE][-+]?\d+)?',
        'ENTERO': r'\d+',
        'SUMA': r'\+',
        'RESTA': r'-',
        'MULTIPLICACION': r'\*',
        'DIVISION': r'/',
        'PARENTESIS_ABIERTO': r'\(',
        'PARENTESIS_CERRADO': r'\)',
        'VAR': r'[a-zA-Z_][a-zA-Z0-9_]*',
        'ASIGNACION': r'=',
        'ESPACIO': r'\s',
        'COMENTARIO': r"#.*",
        'POTENCIA': r'\^'  
    }

    regex_patterns = {token_type: re.compile(pattern) for token_type, pattern in regex_patterns.items()}

    def tokenize(expression):
        tokens = []
        pos = 0
        
        while pos < len(expression):
            match = None
            
            for token_type, pattern in regex_patterns.items():
                match = pattern.match(expression[pos:])
                if match:
                    if token_type in ('FLOTANTE', 'ENTERO') and 'e' in match.group(0):
                        if 'e+' in match.group(0) or 'e-' in match.group(0):
                            try:
                                int(match.group(0).split('e')[-1])
                            except ValueError:
                                raise ValueError(f"Invalid scientific notation at position {pos}: {match.group(0)}")
                        else:
                            try:
                                int(match.group(0).split('e')[-1])
                            except ValueError:
                                raise ValueError(f"Invalid scientific notation at position {pos}: {match.group(0)}")
                    
                    if token_type != 'ESPACIO':
                        tokens.append((token_type, match.group(0)))
                        pos += match.end()
                        break
                    else:
                        pos += match.end() 
                        break
            
            if not match:
                raise ValueError(f"Invalid token at position {pos}: {expression[pos:]}")
        
        return tokens

    regex_types = ['PALABRA_RESERVADA', 'REAL', 'FLOTANTE', 'ENTERO', 'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION', 'PARENTESIS_ABIERTO', 'PARENTESIS_CERRADO', 'VAR', 'ASIGNACION', 'COMENTARIO', 'POTENCIA']
    regex_types_tuples = list(zip(regex_types, regex_types))

    with open('output.html', 'w') as f:
        f.write('<html><head><style>.PALABRA_RESERVADA {color: Plum;} .REAL {color: LightSeaGreen;} .FLOTANTE {color: PaleGreen;} .ENTERO {color: GreenYellow;} .SUMA {color: LightSteelBlue;} .RESTA {color: Gainsboro;} .MULTIPLICACION {color: LightGray;} .DIVISION {color: Silver;} .PARENTESIS_ABIERTO {color: Magenta;} .PARENTESIS_CERRADO {color: Magenta;} .VAR {color: LightSkyBlue;} .ASIGNACION {color: Lavender;} .ESPACIO {color: black;} .COMENTARIO {color: OliveDrab;} .POTENCIA {color: WhiteSmoke;} </style></head><body style="background-color:black;"><font face="Courier New"><h1 style="color: white">RESALTADOR DE SINTAXIS</h1><br><h2 style="color: white">Para poder resaltar distintos textos, modifique y guarde el archivo "sample.txt"</h2><br><h3>')
        for token_type, word in regex_types_tuples:
            f.write(f'<span class="{token_type}">{word} </span> ')
            f.write('<br>')
        f.write('<br><p style="color: white">--------------------------</p><br>')

    txt = open('sample.txt', 'r')
    Lines = txt.readlines()

    for line in Lines:
        tokens = tokenize(line)
        with open('output.html', 'a') as f:
            for token_type, word in tokens:
                f.write(f'<span class="{token_type}">{word} </span> ')
            f.write('<br>')

    txt.close()

    with open('output.html', 'a') as f:
        f.write('</h3></font></body></html>')
    return 'HTML-CSS file generated!'

@app.route('/view_html_css')
def view_html_css():
    return send_file('output.html')

if __name__ == '__main__':
    app.run(debug=True)
