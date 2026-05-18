import axios from 'axios'

const API = axios.create({
  baseURL: 'http://localhost:8000'
})

export const sendMessage = async (
  sessionId,
  message
) => {

  const response = await API.post('/chat', {
    session_id: sessionId,
    message
  })

  return response.data
}