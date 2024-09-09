"use client";
import React, { createContext, useState, useContext } from "react";
import { useRouter } from 'next/router';
import themes from "./themes";
import toast from "react-hot-toast";
import api from "../api";

export const GlobalContext = createContext();
export const GlobalUpdateContext = createContext();

export const GlobalProvider = ({ children }) => {
  const [selectedTheme, setSelectedTheme] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  const [modal, setModal] = useState(false);
  const [collapsed, setCollapsed] = useState(false);

  const [tasks, setTasks] = useState([]);

  const theme = themes[selectedTheme];

  const openModal = () => {
    setModal(true);
  };

  const closeModal = () => {
    setModal(false);
  };

  const collapseMenu = () => {
    setCollapsed(!collapsed);
  };

  const allTasks = async () => {
    setIsLoading(true);

    try {
      const response = await api.get(`/tasks/`);

      const sorted = response.data.sort((a, b) => {
        return (
          new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime()
        );
      });  

      setTasks(sorted);

    } catch (error) {
      console.log("Failed to fetch tasks", error);
      toast.error("Something went wrong");
    }
  };

  const deleteTask = async (id) => {
    try {
      const response = await api.delete(`/tasks/${id}`);

      toast.success("Task deleted");

      allTasks();

    } catch (error) {
      console.log("Failed to delete task", error);
      toast.error("Something went wrong");
    }
  };

  const updateTask = async (task) => {
    try {
      const response = await api.put(`/tasks/`, task);

      toast.success("Task updated");

      allTasks();
    } catch (error) {
      console.log(error);
      toast.error("Something went wrong");
    }
  };

  const completedTasks = tasks.filter((task) => task.isCompleted === true);
  const importantTasks = tasks.filter((task) => task.isImportant === true);
  const incompleteTasks = tasks.filter((task) => task.isCompleted === false);

  React.useEffect(() => {
    const fetchUser = async () => {
      const username = 'test';
      const password = 'test';

      try {
        const formData = new URLSearchParams();
        formData.append("username", username);
        formData.append("password", password);

        const response = await api.post('/login/', formData,
          {
            headers: { 
              'Access-Control-Allow-Origin': '*',
              "Content-Type": "application/x-www-form-urlencoded"
            },
          }
        );

        localStorage.setItem('token', response.data.access_token);

        allTasks();

      } catch (error) {
        console.error('Failed to fetch user:', error);
      }
    };

    fetchUser();
  }, []);

  return (
    <GlobalContext.Provider
      value={{
        theme,
        tasks,
        deleteTask,
        isLoading,
        completedTasks,
        importantTasks,
        incompleteTasks,
        updateTask,
        modal,
        openModal,
        closeModal,
        allTasks,
        collapsed,
        collapseMenu,
      }}
    >
      <GlobalUpdateContext.Provider value={{}}>
        {children}
      </GlobalUpdateContext.Provider>
    </GlobalContext.Provider>
  );
};

export const useGlobalState = () => useContext(GlobalContext);
export const useGlobalUpdate = () => useContext(GlobalUpdateContext);
