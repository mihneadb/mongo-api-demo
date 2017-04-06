from mongoengine import connect, register_connection, Document, StringField

import constants


class Comment(Document):
    text = StringField(required=True)
    type = StringField(required=True, choices=[constants.PRO,
                                               constants.CON,
                                               constants.OTHER])
    sentiment = StringField(choices=[constants.POSITIVE,
                                     constants.NEGATIVE,
                                     constants.NEUTRAL])


connect(host='db')

