from flask import Flask, request, jsonify, render_template, Response     #pip install Flask
import mysql.connector                                                   #pip install mysql-connector-python
                                              


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']
    response = {
        'message': process_chat(message)
    }

    return jsonify(response)

user_state = "start"    # Para rastrear o estado atual do usuário


# conexao com bd
conn =  mysql.connector.connect(host='localhost',
                database='bdCIC',
                user='root',
                password='')

cursor = conn.cursor()
# fim da conexao com bd



def process_chat(message):
    global user_state
    global rm 

    if message == 'menu':
            user_state = "start"
            


    elif user_state == "start":
        if message == '1':
            user_state = "aluno_menu"
            return 'Bem-vindo, aluno! </br><br>Escolha uma opção:<br/><b>1. </b> Desejo uma declaração escolar;<br/><b>2. </b> Desejo ver o calendário escolar;<br/><b>3. </b> Desejo solicitar o boletim;<br/><b>4. </b> Desejo saber meu RM;<br/><br/><br/>Digite <b>menu</b> sempre que quiser voltar ao menu.'
        elif message == '2':
            user_state = "vestibulando_menu"
            return 'Bem-vindo, candidato! </br><br>Escolha uma opção:<br/><b>1. </b> Desejo saber mais  sobre os cursos oferecidos;<br/><b>2. </b> Desejo saber o endereço da unidade;<br/><b>3. </b> Contatos;<br/><b>4. </b> Como ingressar no MTEC;<br/><b>5. </b> Como ingressar no modular;<br/><b>6. </b> O que é a modalidade MTEC;</br><b>7. </b>Há cotas no processo seletivo?;'
        else:
            return 'Desculpe, não entendi a sua escolha. Por favor, escolha "aluno" ou "vestibulando" para começar.'

    
    elif user_state == "vestibulando_menu":
        if message == '1':
            user_state = "saber_mais"
            return 'Claro, digite:</br><b>1. </b> Para saber mais sobre os cursos integrados ao ensino médio;<br/><b>2. </b> Para os cursos modulares.'

        elif message == '2':
            return 'Endereço:Rua Cristobal Claudio Elillo, 088 – Parque CECAP'
        
        elif message == '3':
            return '<b>Email:</b></br>etecguarulhos@gmail.com </br> <b>Telefone:</b></br>(11) 2087-2544'
        
        elif message == '4':
            return '<b>Ensino MTEC:</b></br>Para concorrer uma vaga em nossa instituição nesse módulo basta estar/ter concluindo/concluído o ensino fundamental II, ou seja, o 9º ano, e se inscrever para participar da prova de conhecimentos gerais, composta de 50 questões de múltiplas escolhas! Caso queira conhecer melhor este modulo escolha a opção 6 do menu principal.'
        
        elif message == '5':
            return '<b>Ensino Modular:</b></br>Nessa modalidade, tanto quem já concluiu o ensino médio quanto para quem ainda está cursando, o curso técnico é totalmente separado do ensino regular, funcionando de fato como um curso profissionalizante. Para concorrer uma à vaga basta participar da prova de conhecimentos gerais, composta de 50 questões de múltiplas escolhas! Caso queira conhecer melhor este modulo escolha a opção 7 do menu principal.'
        
        elif message == '6':
            return 'MTEC é uma modalidade de ensino, o estudante cursará o Ensino Médio estruturado em conjunto com a formação do técnico optado por ele, numa jornada de até 30 aulas semanais (até 6 aulas diárias), em cada uma das 3 séries. Cada curso tem a sua grade modificada de acordo com as disciplinas necessárias. No final da jornada o estudante receberá tanto o diploma de conclusão do ensino médio quanto do técnico.'

        elif message == '7':
            return 'SIM! No momento da inscrição aqueles aptos às cotas podem selecionar a/as que melhor se identificam.'

        else:
            return 'Desculpe, não entendi a sua escolha. Por favor, escolha uma das opções disponíveis.'

    elif user_state == "saber_mais" and message == '1':
        return 'Desenvolvimento de Sistemas, Logística e Administração.'
    elif user_state == "saber_mais" and message == '2':
        return 'Técnico em Adiministração (com 20% online) ---Noite</br>Técnico em Desenvolvimento de Sistemas (com 20% online) ---Noite'
    

    elif user_state == "aluno_menu":        
        if message == '1':
            user_state = "aluno_declaracao"
            return 'Por favor, digite o seu RM.'
        elif message == '2':
            return 'Essa função está em desenvolvimento.'
        elif message == '3':
            user_state = "aluno_boletim"
            return 'Por favor, digite o seu RM para que eu possa fazer a solicitação do boletim.'
        elif message == '4':
            user_state = "procura_rm"
            return 'Por favor, digite o seu nome completo.'
        else:
            return 'Desculpe, não entendi a sua escolha. Por favor, escolha uma das opções disponíveis.'
    #fim aluno menu
    

    
    #inicio para solicitar Declaração
    elif user_state == "aluno_declaracao":
        rm = message
        sql = "SELECT * FROM tbAluno WHERE rm_aluno = %s"
        rm_procurado = rm
        cursor.execute(sql, (rm_procurado,))
        resultados = cursor.fetchall()

        if resultados:
            for resultado in resultados:
                user_state = "aluno_declaracao_confirma"
                rm_aluno, nome_aluno, tel_aluno = resultado
                return f'Nome: {nome_aluno} <br/> RM: {rm_aluno} <br/> Telefone: {tel_aluno} <br/> Esses dados são realmente seus? Digite "sim" caso positivo'
        else:
                return 'Nenhum resultado encontrado. Tente novamente'

    elif user_state == "aluno_declaracao_confirma" and message.lower() == 'sim':
            user_state = "start"
            sql = "INSERT INTO tbAtendimento (tipo_ate, data_ate) VALUES ('online', '2023-11-17')"
            sql2 = "INSERT INTO atendi_solicita_servico (cod_servico, num_atendi) VALUES (1, %s)"
            sql3 = "insert into aluno_retira_data (rm_aluno, num_atendi) values (%s, %s)"
            # Executa a primeira consulta para inserir na tabela tbAtendimento
            cursor.execute(sql)
            # Obtém o valor da última chave primária inserida
            pk_tbatend = cursor.lastrowid
            # Executa a segunda consulta usando o valor da chave primária
            cursor.execute(sql2, (pk_tbatend,))
            cursor.execute(sql3, (rm, pk_tbatend,))
            # Confirma as alterações no banco de dados
            conn.commit()
            # Fecha a conexão com o banco de dados
            conn.close()

            return 'Sua solicitação foi enviada com sucesso!!'
    #fim para solicitar Declaração

    

        
    
    elif user_state == "aluno_boletim":
        rm = message
        sql = "SELECT * FROM tbAluno WHERE rm_aluno = %s"
        rm_procurado = rm
        cursor.execute(sql, (rm_procurado,))
        resultados = cursor.fetchall()

        if resultados:
            for resultado in resultados:
                user_state = "aluno_boletim_confirma"
                rm_aluno, nome_aluno, tel_aluno = resultado
                return f'Nome: {nome_aluno} <br/> RM: {rm_aluno} <br/> Telefone: {tel_aluno} <br/> Esses dados são realmente seus? Digite "sim" caso positivo'
        else:
                return 'Nenhum resultado encontrado. Tente novamente'


    elif user_state == "aluno_boletim_confirma" and message.lower() == 'sim':
            user_state = "start"
            sql = "INSERT INTO tbAtendimento (tipo_ate, data_ate) VALUES ('online', '2023-11-17')"
            sql2 = "INSERT INTO atendi_solicita_servico (cod_servico, num_atendi) VALUES (2, %s)"
            sql3 = "insert into aluno_retira_data (rm_aluno, num_atendi) values (%s, %s)"
            # Executa a primeira consulta para inserir na tabela tbAtendimento
            cursor.execute(sql)
            # Obtém o valor da última chave primária inserida
            pk_tbatend = cursor.lastrowid
            # Executa a segunda consulta usando o valor da chave primária
            cursor.execute(sql2, (pk_tbatend,))
            cursor.execute(sql3, (rm, pk_tbatend,))
            # Confirma as alterações no banco de dados
            conn.commit()
            # Fecha a conexão com o banco de dados
            conn.close()

            return 'Sua solicitação foi enviada com sucesso!!'




    #inicio para pesquisar RM
    elif user_state == "procura_rm":
        
            nomeAluno = message
            sql = "SELECT * FROM tbAluno WHERE nome_aluno = %s"
            cursor.execute(sql, (nomeAluno,))
            resultados = cursor.fetchall()

            if resultados:
                for resultado in resultados:
                    rm_aluno, nome_aluno, tel_aluno = resultado
                    return f'{nome_aluno} o seu RM é {rm_aluno}'
            else:
                    cursor.close()
                    conn.close()
                    return 'Nenhum resultado encontrado  :('
    #fim para pesquisar RM


if __name__ == '__main__':
    app.run()
