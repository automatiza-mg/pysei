from dataclasses import dataclass
from typing import Self

from .enums import Aplicabilidade, NivelAcesso
from .sin import decode_sin, encode_sin


class Model:
    @staticmethod
    def from_record(record: dict) -> Self: ...

    @classmethod
    def from_many_records(cls, records: list[dict]) -> list[Self]:
        return [cls.from_record(record) for record in records]


@dataclass
class Assinatura(Model):
    nome: str
    cargo_funcao: str
    data_hora: str
    id_usuario: str
    id_origem: str
    id_orgao: str
    sigla: str

    @staticmethod
    def from_record(record):
        return Assinatura(
            nome=record["Nome"],
            cargo_funcao=record["CargoFuncao"],
            data_hora=record["DataHora"],
            id_usuario=record["IdUsuario"],
            id_origem=record["IdOrigem"],
            id_orgao=record["IdOrgao"],
            sigla=record["Sigla"],
        )


@dataclass
class Campo(Model):
    nome: str
    valor: str

    @staticmethod
    def from_record(record):
        return Campo(
            nome=record["Nome"],
            valor=record["Valor"],
        )


@dataclass
class Unidade(Model):
    id_unidade: str
    sigla: str
    descricao: str
    protocolo: bool | None
    arquivamento: bool | None
    ouvidoria: bool | None

    @staticmethod
    def from_record(record):
        return Unidade(
            id_unidade=record["IdUnidade"],
            sigla=record["Sigla"],
            descricao=record["Descricao"],
            protocolo=decode_sin(record["SinProtocolo"]),
            arquivamento=decode_sin(record["SinArquivamento"]),
            ouvidoria=decode_sin(record["SinOuvidoria"]),
        )


@dataclass
class Usuario(Model):
    id_usuario: str
    sigla: str
    nome: str

    @staticmethod
    def from_record(record):
        return Usuario(
            id_usuario=record["IdUsuario"],
            sigla=record["Sigla"],
            nome=record["Nome"],
        )


@dataclass
class AtributoAndamento(Model):
    nome: str
    valor: str
    id_origem: str

    @staticmethod
    def from_record(record):
        return AtributoAndamento(
            nome=record["Nome"],
            valor=record["Valor"],
            id_origem=record["IdOrigem"],
        )


@dataclass
class Assunto(Model):
    codigo_estruturado: str | None
    descricao: str | None

    @staticmethod
    def from_record(record: dict):
        return Assunto(
            codigo_estruturado=record["CodigoEstruturado"],
            descricao=record["Descricao"],
        )


@dataclass
class ProcedimentoResumido(Model):
    id_tipo_procedimento: str
    procedimento_formatado: str
    tipo_procedimento: str

    @staticmethod
    def from_record(record):
        return ProcedimentoResumido(
            id_tipo_procedimento=record["IdTipoProcedimento"],
            procedimento_formatado=record["ProcedimentoFormatado"],
            tipo_procedimento=record["TipoProcedimento"],
        )


@dataclass
class Observacao(Model):
    descricao: str
    unidade: Unidade

    @staticmethod
    def from_record(record):
        return Observacao(
            descricao=record["Descricao"],
            unidade=Unidade.from_record(record["Unidade"]),
        )


@dataclass
class Interessado(Model):
    sigla: str
    nome: str

    @staticmethod
    def from_record(record):
        return Interessado(
            sigla=record["Sigla"],
            nome=record["Nome"],
        )


@dataclass
class Andamento(Model):
    id_andamento: str | None
    id_tarefa: str | None
    id_tarefa_modulo: str | None
    descricao: str | None
    data_hora: str | None
    unidade: Unidade | None
    usuario: Usuario | None
    atributos: list[AtributoAndamento] | None

    @staticmethod
    def from_record(record):
        andamento = Andamento(
            id_andamento=record["IdAndamento"],
            id_tarefa=record["IdTarefa"],
            id_tarefa_modulo=record["IdTarefaModulo"],
            descricao=record["Descricao"],
            data_hora=record["DataHora"],
            unidade=None,
            usuario=None,
            atributos=None,
        )

        if record["Unidade"] is not None:
            andamento.unidade = Unidade.from_record(record["Unidade"])

        if record["Usuario"] is not None:
            andamento.usuario = Usuario.from_record(record["Usuario"])

        if record["Atributos"] is not None:
            andamento.atributos = AtributoAndamento.from_many_records(
                record["Atributos"]
            )

        return andamento


@dataclass
class Marcador(Model):
    id_marcador: str
    nome: str
    icone: str
    ativo: bool

    @staticmethod
    def from_record(record):
        return Marcador(
            id_marcador=record["IdMarcador"],
            nome=record["Nome"],
            icone=record["Icone"],
            ativo=decode_sin(record["SinAtivo"]),
        )


@dataclass
class ArquivoExtensao(Model):
    id_andamento_marcador: str
    texto: str
    data_hora: str
    usuario: Usuario


@dataclass
class DefinicaoControlePrazo(Model):
    protocolo_procedimento: str
    data_prazo: str
    dias: str
    dias_uteis: bool

    def to_record(self) -> dict:
        return {
            "ProtocoloProcedimento": self.protocolo_procedimento,
            "DataPrazo": self.data_prazo,
            "Dias": self.dias,
            "SinDiasUteis": encode_sin(self.dias_uteis),
        }


@dataclass
class Serie(Model):
    id_serie: str
    nome: str
    aplicabilidade: Aplicabilidade | None

    @staticmethod
    def from_record(record):
        serie = Serie(
            id_serie=record["IdSerie"],
            nome=record["Nome"],
            aplicabilidade=None,
        )

        if record["Aplicabilidade"] is not None:
            serie.aplicabilidade = Aplicabilidade.from_str(record["Aplicabilidade"])

        return serie


@dataclass
class TipoProcedimento(Model):
    id_tipo_procedimento: str
    nome: str

    @staticmethod
    def from_record(record):
        return TipoProcedimento(
            id_tipo_procedimento=record["IdTipoProcedimento"],
            nome=record["Nome"],
        )


@dataclass
class UnidadeProcedimentoAberto(Model):
    unidade: Unidade
    usuario_atribuido: Usuario

    @staticmethod
    def from_record(record):
        return UnidadeProcedimentoAberto(
            unidade=Unidade.from_record(record["Unidade"]),
            usuario_atribuido=Usuario.from_record(record["UsuarioAtribuido"]),
        )


@dataclass
class RetornoConsultaProcedimento(Model):
    id_procedimento: str
    procedimento_formatado: str
    especificacao: str
    data_autuacao: str
    link_acesso: str
    nivel_acesso_local: NivelAcesso
    nivel_acesso_global: NivelAcesso
    tipo_procedimento: TipoProcedimento
    andamento_geracao: Andamento
    andamento_conclusao: Andamento
    ultimo_andamento: Andamento
    unidades_procedimento_aberto: list[UnidadeProcedimentoAberto]
    assuntos: list[Assunto]
    observacoes: list[Observacao]
    interessados: list[Interessado]
    procedimentos_relacionados: list[ProcedimentoResumido]
    procedimentos_anexados: list[ProcedimentoResumido]

    @staticmethod
    def from_record(record):
        return RetornoConsultaProcedimento(
            id_procedimento=record["IdProcedimento"],
            procedimento_formatado=record["ProcedimentoFormatado"],
            especificacao=record["Especificacao"],
            data_autuacao=record["DataAutuacao"],
            link_acesso=record["LinkAcesso"],
            nivel_acesso_local=NivelAcesso.from_str(record["NivelAcessoLocal"]),
            nivel_acesso_global=NivelAcesso.from_str(record["NivelAcessoGlobal"]),
            tipo_procedimento=TipoProcedimento.from_record(record["TipoProcedimento"]),
            andamento_geracao=Andamento.from_record(record["AndamentoGeracao"]),
            andamento_conclusao=Andamento.from_record(record["AndamentoConclusao"]),
            ultimo_andamento=Andamento.from_record(record["UltimoAndamento"]),
            unidades_procedimento_aberto=UnidadeProcedimentoAberto.from_many_records(
                record["UnidadesProcedimentoAberto"]
            ),
            assuntos=Assunto.from_many_records(record["Assuntos"]),
            observacoes=Observacao.from_many_records(record["Observacoes"]),
            interessados=Interessado.from_many_records(record["Interessados"]),
            procedimentos_relacionados=ProcedimentoResumido.from_many_records(
                record["ProcedimentosRelacionados"]
            ),
            procedimentos_anexados=ProcedimentoResumido.from_many_records(
                record["ProcedimentosAnexados"]
            ),
        )


@dataclass
class RetornoConsultaDocumento(Model):
    id_procedimento: str
    procedimento_formatado: str
    id_documento: str
    documento_formatado: str
    nivel_acesso_local: NivelAcesso
    nivel_acesso_global: NivelAcesso
    link_acesso: str
    serie: Serie
    numero: str | None
    nome_arvore: str
    descricao: str
    data: str
    unidade_elaboradora: Unidade
    andamento_geracao: Andamento
    assinaturas: list[Assinatura]
    campos: list[Campo]

    @staticmethod
    def from_record(record):
        return RetornoConsultaDocumento(
            id_procedimento=record["IdProcedimento"],
            procedimento_formatado=record["ProcedimentoFormatado"],
            id_documento=record["IdDocumento"],
            documento_formatado=record["DocumentoFormatado"],
            nivel_acesso_local=NivelAcesso.from_str(record["NivelAcessoLocal"]),
            nivel_acesso_global=NivelAcesso.from_str(record["NivelAcessoGlobal"]),
            link_acesso=record["NivelAcesso"],
            serie=Serie.from_record(record["Serie"]),
            numero=record["Numero"],
            nome_arvore=record["NomeArvore"],
            descricao=record["Descricao"],
            unidade_elaboradora=Unidade.from_record(record["UnidadeElaboradora"]),
            andamento_geracao=Andamento.from_record(record["AndamentoGeracao"]),
            assinaturas=Assinatura.from_many_records(record["Assinaturas"]),
            campos=Campo.from_many_records(record["Campos"]),
        )
