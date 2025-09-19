"use client"

import React, { createContext, useContext, useState, useEffect } from "react"
import { useAuth } from "./AuthContext"
import API_ENDPOINTS from "../config/api"

const ContactContext = createContext()

export const useContacts = () => {
  const context = useContext(ContactContext)
  if (!context) {
    throw new Error("useContacts must be used within a ContactProvider")
  }
  return context
}

export const ContactProvider = ({ children }) => {
  const { user } = useAuth()
  const [contacts, setContacts] = useState([])
  const [searchTerm, setSearchTerm] = useState("")
  const [sortBy, setSortBy] = useState("name") // 'name', 'favorites'

  // Load contacts from API when user changes
  useEffect(() => {
    if (user) {
      loadContacts()
    } else {
      setContacts([])
    }
  }, [user])

  const loadContacts = async () => {
    try {
      const token = localStorage.getItem('contactManager_token')
      const response = await fetch(API_ENDPOINTS.CONTACTS.LIST, {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })

      if (response.ok) {
        const data = await response.json()
        setContacts(data.contacts || [])
      } else {
        console.error('Failed to load contacts')
        setContacts([])
      }
    } catch (error) {
      console.error('Error loading contacts:', error)
      setContacts([])
    }
  }

  const addContact = async (contactData) => {
    try {
      const token = localStorage.getItem('contactManager_token')
      if (!token) {
        throw new Error('No authentication token found. Please log in again.')
      }

      console.log('Creating contact:', contactData)
      console.log('Using token:', token.substring(0, 20) + '...')

      const response = await fetch(API_ENDPOINTS.CONTACTS.CREATE, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify(contactData),
      })

      console.log('Response status:', response.status)

      if (response.ok) {
        const newContact = await response.json()
        console.log('Contact created successfully:', newContact)
        setContacts((prev) => [...prev, newContact])
        return newContact
      } else {
        const error = await response.json()
        console.error('Server error:', error)
        throw new Error(error.message || 'Failed to create contact')
      }
    } catch (error) {
      console.error('Error creating contact:', error)
      alert(`Error creating contact: ${error.message}`)
      throw error
    }
  }

  const updateContact = async (id, contactData) => {
    try {
      const token = localStorage.getItem('contactManager_token')
      const response = await fetch(API_ENDPOINTS.CONTACTS.UPDATE(id), {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify(contactData),
      })

      if (response.ok) {
        const updatedContact = await response.json()
        setContacts((prev) => prev.map((contact) => (contact.id === id ? updatedContact : contact)))
        return updatedContact
      } else {
        const error = await response.json()
        throw new Error(error.message || 'Failed to update contact')
      }
    } catch (error) {
      console.error('Error updating contact:', error)
      throw error
    }
  }

  const deleteContact = async (id) => {
    try {
      const token = localStorage.getItem('contactManager_token')
      const response = await fetch(API_ENDPOINTS.CONTACTS.DELETE(id), {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })

      if (response.ok) {
        setContacts((prev) => prev.filter((contact) => contact.id !== id))
      } else {
        const error = await response.json()
        throw new Error(error.message || 'Failed to delete contact')
      }
    } catch (error) {
      console.error('Error deleting contact:', error)
      throw error
    }
  }

  const toggleFavorite = async (id) => {
    try {
      const token = localStorage.getItem('contactManager_token')
      const response = await fetch(API_ENDPOINTS.CONTACTS.TOGGLE_FAVORITE(id), {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })

      if (response.ok) {
        const updatedContact = await response.json()
        setContacts((prev) =>
          prev.map((contact) => (contact.id === id ? updatedContact : contact)),
        )
      } else {
        const error = await response.json()
        throw new Error(error.message || 'Failed to toggle favorite')
      }
    } catch (error) {
      console.error('Error toggling favorite:', error)
      throw error
    }
  }

  // Filter and sort contacts
  const filteredAndSortedContacts = React.useMemo(() => {
    const filtered = contacts.filter(
      (contact) =>
        contact.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        contact.email.toLowerCase().includes(searchTerm.toLowerCase()) ||
        (contact.phone && contact.phone.includes(searchTerm)),
    )

    // Sort contacts
    filtered.sort((a, b) => {
      if (sortBy === "favorites") {
        if (a.isFavorite && !b.isFavorite) return -1
        if (!a.isFavorite && b.isFavorite) return 1
        return a.name.localeCompare(b.name)
      } else {
        return a.name.localeCompare(b.name)
      }
    })

    return filtered
  }, [contacts, searchTerm, sortBy])

  const value = {
    contacts: filteredAndSortedContacts,
    allContacts: contacts,
    searchTerm,
    setSearchTerm,
    sortBy,
    setSortBy,
    addContact,
    updateContact,
    deleteContact,
    toggleFavorite,
  }

  return <ContactContext.Provider value={value}>{children}</ContactContext.Provider>
}
