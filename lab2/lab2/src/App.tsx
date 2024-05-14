import React, { useState, useEffect } from 'react';
import './main.global.css';
import { Header } from './components/Header';
import { PageMain } from './components/PageMain';
import { PageDoctors } from './components/PageDoctors';
import { BrowserRouter, Route, Routes } from "react-router-dom";

function AppComponent() {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  return (
    <>
      {mounted &&
        <BrowserRouter>
          <Header />
          <Routes>
            <Route path='/' element={<PageMain />} />
            <Route path='/doctors' element={<PageDoctors />} />
          </Routes>
        </BrowserRouter>
      }
    </>
  );
}

export const App = () =>
  <AppComponent />
;
