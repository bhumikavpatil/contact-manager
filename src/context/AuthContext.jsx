"use client"

import { createContext, useContext, useState, useEffect } from "react"
import API_ENDPOINTS from "../config/api"

const AuthContext = createContext()

export const useAuth = () => {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider")
  }
  return context
}

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  // Load user from localStorage on app start
  useEffect(() => {
    const savedUser = localStorage.getItem("contactManager_user")
    if (savedUser) {
      setUser(JSON.parse(savedUser))
    }
    setLoading(false)
  }, [])

  // Save user to localStorage whenever user changes
  useEffect(() => {
    if (user) {
      localStorage.setItem("contactManager_user", JSON.stringify(user))
    } else {
      localStorage.removeItem("contactManager_user")
    }
  }, [user])

  const login = async (email, password) => {
    try {
      const response = await fetch(API_ENDPOINTS.AUTH.LOGIN, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      })

      const data = await response.json()

      if (response.ok) {
        const { user, token } = data
        setUser(user)
        localStorage.setItem('contactManager_token', token)
        return { success: true, message: "Successfully logged in!" }
      } else {
        return { success: false, message: data.message || "Login failed" }
      }
    } catch (error) {
      return { success: false, message: "Network error. Please check if the backend is running." }
    }
  }

  const register = async (name, email, password) => {
    try {
      const response = await fetch(API_ENDPOINTS.AUTH.REGISTER, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email, password }),
      })

      const data = await response.json()

      if (response.ok) {
        const { user, token } = data
        setUser(user)
        localStorage.setItem('contactManager_token', token)
        return { success: true, message: "Account created successfully! Welcome to Contact Manager." }
      } else {
        return { success: false, message: data.message || "Registration failed" }
      }
    } catch (error) {
      return { success: false, message: "Network error. Please check if the backend is running." }
    }
  }

  const logout = () => {
    setUser(null)
    localStorage.removeItem('contactManager_token')
  }

  const value = {
    user,
    login,
    register,
    logout,
    loading,
  }

  return <AuthContext.Provider value={value}>{!loading && children}</AuthContext.Provider>
}
