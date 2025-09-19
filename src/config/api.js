// API Configuration
const API_BASE_URL = process.env.REACT_APP_API_URL || window.location.origin;

export const API_ENDPOINTS = {
  AUTH: {
    LOGIN: `${API_BASE_URL}/api/auth/login`,
    REGISTER: `${API_BASE_URL}/api/auth/register`,
  },
  CONTACTS: {
    LIST: `${API_BASE_URL}/api/contacts`,
    CREATE: `${API_BASE_URL}/api/contacts`,
    UPDATE: (id) => `${API_BASE_URL}/api/contacts/${id}`,
    DELETE: (id) => `${API_BASE_URL}/api/contacts/${id}`,
    TOGGLE_FAVORITE: (id) => `${API_BASE_URL}/api/contacts/${id}/toggle-favorite`,
  },
  HEALTH: `${API_BASE_URL}/api/health`,
};

export default API_ENDPOINTS;
