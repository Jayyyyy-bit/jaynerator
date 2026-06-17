import React from 'react';

interface ProdProps {
  children: React.ReactNode;
}

const Prod: React.FC<ProdProps> = ({ children }) => {
  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      <header className="bg-white shadow px-6 py-4">
        {/* header content */}
      </header>

      <main className="flex-1 p-6">
        {children}
      </main>

      <footer className="bg-white border-t px-6 py-4 text-sm text-gray-400">
        {/* footer content */}
      </footer>
    </div>
  );
};

export default Prod;