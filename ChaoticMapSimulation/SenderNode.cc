#include <omnetpp.h>
#include "LorenzEncrypt.h"
#include "message_m_m.h"

using namespace omnetpp;

class SenderNode : public cSimpleModule {
  protected:
    virtual void initialize() override {
        const std::string inputImage = "input_image.jpeg";
        const std::string encryptedImage = "encrypted_image.jpeg";

        // Lorenz attractor ile şifreleme
        lorenzEncrypt(inputImage, encryptedImage);

        // Mesaj oluştur
        Message *msg = new Message("encryptedImage");
        msg->setFileName(encryptedImage.c_str());

        // Mesajı belirli bir gecikmeyle gönder
        scheduleAt(simTime() + 2.0, msg); // 1 saniyelik gecikme
    }

    virtual void handleMessage(cMessage *msg) override {
        send(msg, "out");
        EV << "Şifreli mesaj başarıyla gönderildi.\n";
    }
};

Define_Module(SenderNode);
