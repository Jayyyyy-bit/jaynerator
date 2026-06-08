import React from 'react';

interface UserProps {
  // define your props here
}

const User: React.FC<UserProps> = () => {
  return (
    <div className="flex flex-col items-center justify-center p-4">
      <h1 className="text-2xl font-bold text-gray-800">User</h1>
    </div>
  );
};

export default User;