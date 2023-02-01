class ChatBox {
    constructor() {
        this.ags = {
            chatBox: document.querySelector('.chat-window'),
            sendBtn: document.querySelector('#send-button')
        }

        this.messages = [];
    }


    display() {
        const {chatBox, sendBtn} = this.args;
        sendBtn.addEventListener('click', () => this.onSendBtn(chatBox))
        const node = chatBox.querySelector('#input');
        node.addEventListener('keyup', ({key}) => {
            if (key === "Enter") {
                this.onSendBtn(chatBox);
            }
        })
    }

    onSendBtn(chatBox) {
        var textField = chatBox.querySelector('#message');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

        fetch($SCRIPT_ROOT + '/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then(r => r.json())
        .then(r => {
            let msg2 = { name: "RhyBot", message: r.answer };
            this.messages.push(msg2);
            this.updateChatText(chatBox)
            textField.value = ''
        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatBox);
            textField.value = ''
        });
    }

    updateChatText(chatBox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item,) {
            if (item.name === "RhyBot") {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
            }
            else {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
        });

        const chatmessage = chatBox.querySelector('.chat-window');
        chatmessage.innerHTML = html;
    }

}

const chatBox = new ChatBox();
chatBox.display();

