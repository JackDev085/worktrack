from datetime import datetime
import json
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
import os

from workouts.models import Exercicio, Equipamento, Musculo

class Command(BaseCommand):
    help = 'Importa dados de exercícios a partir de um arquivo JSON'

    def handle(self, *args, **kwargs):
        # Caminho para o arquivo JSON
        datafile = 'data/data.json'
        
        # Verifica se o arquivo existe
        if not os.path.exists(datafile):
            self.stdout.write(self.style.ERROR(f'Arquivo não encontrado: {datafile}'))
            return

        # Carrega o arquivo JSON
        with open(datafile, 'r') as f:
            data = json.load(f)
        
        # Mapeia IDs de categorias e equipamentos para objetos
        equipamento_map = {equipamento.id: equipamento for equipamento in Equipamento.objects.all()}
        musculo_map = {musculo.id: musculo for musculo in Musculo.objects.all()}

        # Lista de objetos de Exercicio para bulk_create
        exercicios = []
        
        # Processa os dados e cria instâncias de Exercicio
        for item in data:
            equipamento = equipamento_map.get(item['equipment'])
            muscles = [musculo_map.get(musculo_id) for musculo_id in item['muscles']]

            exercicio = Exercicio(
                name=item['name'],
                description=item['description'],
                gif_url=item['gif_url'],
                equipment=equipamento
            )
            exercicios.append(exercicio)

        # Cria os objetos de Exercicio no banco de dados
        Exercicio.objects.bulk_create(exercicios)
        
        # Associa músculos a cada exercício
        for exercicio in Exercicio.objects.all():
            for musculo in muscles:
                exercicio.musculos.add(musculo)

        self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))
