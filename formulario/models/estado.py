from django.db import models

class Estados(models.Model):
    class Estado:
        acre = 'Acre'
        alagoas = 'Alagoas'
        amapa = 'Amapá'
        amazonas = 'Amazonas'
        bahia = 'Bahia'
        ceara = 'Ceará'
        distrito_federal = 'Distrito Federal'
        espirito_santo = 'Espírito Santo'
        goias = 'Goiás'
        maranhao = 'Maranhão'
        mato_grosso = 'Mato Grosso'
        mato_grosso_do_sul = 'Mato Grosso do Sul'
        minas_gerais = 'Minas Gerais'
        para = 'Pará'
        paraiba = 'Paraíba'
        parana = 'Paraná'
        pernambuco = 'Pernambuco'
        piaui = 'Piauí'
        rio_de_janeiro = 'Rio de Janeiro'
        rio_grande_do_norte = 'Rio Grande do Norte'
        rio_grande_do_sul = 'Rio Grande do Sul'
        rondonia = 'Rondônia'
        roraima = 'Roraima'
        santa_catarina = 'Santa Catarina'
        sao_paulo = 'São Paulo'
        sergipe = 'Sergipe'
        tocantins = 'Tocantins'

    estado = models.CharField(max_length=30, choices=[
    (Estado.acre, "AC"),
    (Estado.alagoas, "AL"),
    (Estado.amapa, "AP"),
    (Estado.amazonas, "AM"),
    (Estado.bahia, "BA"),
    (Estado.ceara, "CE"),
    (Estado.distrito_federal, "DF"),
    (Estado.espirito_santo, "ES"),
    (Estado.goias, "GO"),
    (Estado.maranhao, "MA"),
    (Estado.mato_grosso, "MT"),
    (Estado.mato_grosso_do_sul, "MS"),
    (Estado.minas_gerais, "MG"),
    (Estado.para, "PA"),
    (Estado.paraiba, "PB"),
    (Estado.parana, "PR"),
    (Estado.pernambuco, "PE"),
    (Estado.piaui, "PI"),
    (Estado.rio_de_janeiro, "RJ"),
    (Estado.rio_grande_do_norte, "RN"),
    (Estado.rio_grande_do_sul, "RS"),
    (Estado.rondonia, "RO"),
    (Estado.roraima, "RR"),
    (Estado.santa_catarina, "SC"),
    (Estado.sao_paulo, "SP"),
    (Estado.sergipe, "SE"),
    (Estado.tocantins, "TO"),
])
    
    def __str__(self):
        return self.estado

