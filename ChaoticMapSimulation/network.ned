

network ChaoticNetwork
{
    @display("bgb=722,561");
    submodules:
        sender: SenderNode { // Verici düğüm
            @display("p=129,282");
        }
        receiver: ReceiverNode { // Alıcı düğüm
            @display("p=580,282");
        }
    connections:
        sender.out --> receiver.in; // Verici -> Alıcı bağlantısı
        receiver.out --> sender.in; // Alıcı -> Verici (isteğe bağlı geri bildirim için)
}
