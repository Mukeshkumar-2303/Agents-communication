function MessageBubble({ sender, text }) {

  return (
    <div className={`message ${sender}`}>
      <strong>{sender}:</strong>
      <p>{text}</p>
    </div>
  )
}

export default MessageBubble