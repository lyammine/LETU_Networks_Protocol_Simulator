# Session.py
# Classes for handling individual connection sessions

class session:

    def __init__(self, sessionName):
        self.name = sessionName

    def HandleMessage(sessionName, sourceAddress, message):

        # -- Determine if the message belongs to me. --

        # If sessionName is non-empty and different from my own, reply that I can't take it
        if sessionName and (sessionName != self.name):
            return false

        # If sessionName is mine, reply that I can take it

        # If sourceAddress belongs to either my client or server, reply that I can take it


        # -- Determine what kind of message this is: registration or data --

        # registration from the first host gets recorded, check for parameter errors, registration timeout begins

        # registration from the second host gets recorded, check for parameter errors, confirmation gets sent out
            # registration timeout ends, data timeout begins

        # data from an unconfirmed host gets an error message sent back

        # data from a confirmed host gets passed on to the other host
