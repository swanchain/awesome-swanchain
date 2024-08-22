import axios from 'axios'

export const getRequest = async (apilink) => {
  try {
    const response = await axios.get(apilink)
    return response.data
  } catch (err) {
      console.error(err, err.response)
      return err.response.data
  }
}

export const postRequest = async (apilink, jsonObject, headers) => {
  try {
      const response = await axios.post(apilink, jsonObject, headers)
      return response.data
  } catch (err) {
    console.error(err, err.response)
      return err.response.data
  }
}