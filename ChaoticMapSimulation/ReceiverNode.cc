#include <omnetpp.h>
#include "LorenzEncrypt.h"
#include "message_m_m.h"

using namespace omnetpp;

class ReceiverNode : public cSimpleModule {
  protected:
    virtual void handleMessage(cMessage *msg) override {
        Message *receivedMsg = check_and_cast<Message *>(msg);
        const std::string encryptedImage = receivedMsg->getFileName();
        const std::string decryptedImage = "decrypted_image.jpeg";

        // Lorenz attractor ile şifre çözme
        lorenzDecrypt(encryptedImage, decryptedImage);

        EV << "Dosya basarıyla çözüldü ve kaydedildi: " << decryptedImage << "\n";

        delete msg;
    }
};

Define_Module(ReceiverNode);
