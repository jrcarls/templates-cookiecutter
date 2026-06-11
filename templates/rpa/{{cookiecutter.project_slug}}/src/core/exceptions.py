class AutomationError(Exception):
    """Erro base para falhas de automação."""


class LoginError(AutomationError):
    """Falha na etapa de autenticação."""


class ElementNotFoundError(AutomationError):
    """Elemento de UI não encontrado dentro do timeout."""


class ProcessingError(AutomationError):
    """Erro durante o processamento de um item."""
