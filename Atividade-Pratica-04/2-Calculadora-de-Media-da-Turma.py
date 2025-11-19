#2 - Criar um código que registre as notas de alunos e calcular a média da turma.

def registrar_notas(numero_alunos):
    registro = {}
    print("\n .... Registro de Notas  ....")
    
    for i in range(numero_alunos):
        print(f"\nAluno {i+1}/{numero_alunos}:")
        
        while True:
            nome = input("Digite o nome do aluno: ").strip()
            if nome:
                break
            print("O nome não pode ser vazio. Tente novamente.")

        notas_aluno = []
        numero_provas = 3
        
        for j in range(numero_provas):
            while True:
                try:
                    nota = float(input(f"Digite a nota da Prova {j+1} (0 a 10): "))
                    if 0 <= nota <= 10:
                        notas_aluno.append(nota)
                        break
                    else:
                        print("Nota inválida. Digite um valor entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida. Digite um número para a nota.")
        
        registro[nome] = notas_aluno
        
    return registro

def calcular_media_aluno(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

def calcular_media_turma(registro):
    medias_alunos = {}
    soma_medias_turma = 0
    
    for nome, notas in registro.items():
        media_aluno = calcular_media_aluno(notas)
        medias_alunos[nome] = media_aluno
        soma_medias_turma += media_aluno
        
    numero_alunos = len(registro)
    media_geral = soma_medias_turma / numero_alunos if numero_alunos > 0 else 0
    
    return medias_alunos, media_geral

def exibir_resultados(medias_alunos, media_geral):
    print("\n" + "="*40)
    print("           RESULTADOS DA TURMA           ")
    print("="*40)
    
    for nome, media in medias_alunos.items():
        print(f"| Aluno: {nome:<20} | Média: {media:>5.2f} |")
    
    print("-" * 40)
    print(f"| MÉDIA GERAL DA TURMA:       | {media_geral:>5.2f} |")
    print("="*40)

def main():
    while True:
        try:
            num_alunos = int(input("Quantos alunos há na turma? "))
            if num_alunos > 0:
                break
            else:
                print("O número de alunos deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            
    registro_notas = registrar_notas(num_alunos)
    
    if not registro_notas:
        print("\nNenhuma nota foi registrada. Encerrando.")
        return

    medias_alunos, media_geral = calcular_media_turma(registro_notas)
    
    exibir_resultados(medias_alunos, media_geral)

if __name__ == "__main__":
    main()