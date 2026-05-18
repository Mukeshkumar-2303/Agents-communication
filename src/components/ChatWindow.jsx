import MessageBubble from './MessageBubble'

function ChatWindow({ messages }) {

  return (
    <div className="chat-window">

      {messages.map((msg, index) => (
        <MessageBubble
          key={index}
          sender={msg.sender}
          text={msg.text}
        />
      ))}

    </div>
  )
}

export default ChatWindow