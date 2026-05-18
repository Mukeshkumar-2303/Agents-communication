import { useState } from 'react'

import ChatWindow from './components/ChatWindow'
import InputBox from './components/InputBox'
import Loader from './components/Loader'

import { sendMessage } from './services/api'

function App() {

  const [messages, setMessages] = useState([])
  const [loading, setLoading] = useState(false)

  const sessionId = 'session-123'

  const handleSend = async (message) => {

    const userMessage = {
      sender: 'User',
      text: message
    }

    const frontendMessage = {
      sender: 'frontend-agent',
      text: 'Sending request to Backend Agent...'
    }

    setMessages((prev) => [
      ...prev,
      userMessage,
      frontendMessage
    ])

    try {

      setLoading(true)

      const response = await sendMessage(
        sessionId,
        message
      )

      setLoading(false)

      const backendMessage = {
        sender: 'backend-agent',
        text: response.message
      }

      setMessages((prev) => [
        ...prev,
        backendMessage
      ])

    } catch (error) {

      setLoading(false)

      setMessages((prev) => [
        ...prev,
        {
          sender: 'System',
          text: 'Error communicating with backend'
        }
      ])
    }
  }

  return (
    <div className="app-container">

      <h1>AI Agent Communication System</h1>

      <ChatWindow messages={messages} />

      {loading && <Loader />}

      <InputBox onSend={handleSend} />

    </div>
  )
}

export default App