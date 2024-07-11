from env_preferences import global_vars as global_variables
from framework.api.models.np_tracking_post import Tracking
from framework.api.models.np_tracking_post import Document
from framework.api.models.np_tracking_post import MethodProperties


MODEL_NAME: str = 'TrackingDocumentGeneral'
CALL_METHOD: str = 'getStatusDocuments'
SYSTEM: str = 'DevCentre'


class TrackingBuilder:

    @staticmethod
    def build_tracking_request(doc_number: str) -> Tracking:
        doc = Document(
            DocumentNumber=doc_number,
            Phone=str(global_variables.PHONE_NUMBER)
        )

        documents: list[Document] = [doc]

        method_properties = MethodProperties(
            Documents=documents
        )

        return Tracking(
            apiKey=global_variables.API_KEY,
            modelName=MODEL_NAME,
            calledMethod=CALL_METHOD,
            methodProperties=method_properties,
            system=SYSTEM
        )
