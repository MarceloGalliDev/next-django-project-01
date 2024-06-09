import json
from typing import Any, Optional, Union
from django.utils.translation import gettext_lazy as _
from rest_framework.renderers import JSONRenderer


class GenericJSONRenderer(JSONRenderer):
    # usamos utf-8 para renderizar os caracteres corretamente
    charset = 'utf-8'

    # aqui definimos um rótulo padrão para os objetos que serão renderizado no json
    object_label = 'object'

    # o método render converte os dados em uma representação Json
    # data é os dados, accepted_media_types são tipo de midias aceitos, renderer_context é o contexto adicional para o renderer
    def render(
        self,
        data: Any,
        accepted_media_type: Optional[str] = None,
        renderer_context: Optional[dict] = None
    ) -> Union[bytes, str]:
        if renderer_context is None:
            renderer_context = {}

        # aqui buscamos dentro do context o view se tem o valor object_label se tiver ele retorna se não ele retorna o definido padrão
        view = renderer_context.get('view')
        if hasattr(view, 'object_label'):
            object_label = view.object_label
        else:
            object_label = self.object_label

        response = renderer_context.get('response')

        if not response:
            raise ValueError(_('Response not found in renderer context'))

        status_code = response.status_code
        errors = data.get('errors', None)

        # depois da verificação do object_label se obtivermos erro ele retorna a renderização padrão da classe JsonRenderer
        if errors is not None:
            return super(GenericJSONRenderer, self).render(data)

        # se não houver erros ele retorna um dicionario com o rótulo do object_label com o status_code e os dados
        # esse dicionario é convertido para UTF-8 antes de ser renderizado para correção de caracteres inválidos no JSON
        return json.dumps({"status_code": status_code, object_label: data}).encode(self.charset)
