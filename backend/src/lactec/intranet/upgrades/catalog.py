from lactec.intranet import logger
from lactec.intranet.content.pessoa import Pessoa
from plone import api
from Products.GenericSetup.tool import SetupTool
from Products.ZCatalog.CatalogBrains import AbstractCatalogBrain


def reindexa_pessoa(portal_setup: SetupTool):
    """Reindexa todos os objetos do tipo Pessoa."""
    brains: list[AbstractCatalogBrain] = api.content.find(portal_type="Pessoa")
    for brain in brains:
        pessoa: Pessoa = brain.getObject()
        # Reindexa os campos area e cargo do objeto pessoa
        pessoa.reindexObject(idxs=["area", "cargo"])
        logger.info(
            f"- Reindexa os campos area e cargo do objeto {pessoa.absolute_url()}"
        )
    logger.info("Reindexação completa")
