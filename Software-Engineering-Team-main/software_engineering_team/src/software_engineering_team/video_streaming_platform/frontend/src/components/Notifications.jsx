import React, { useEffect } from 'react';
import axios from 'axios';

const Notifications = () => {
  useEffect(() => {
    const fetchNotifications = async () => {
      try {
        const response = await axios.post('/api/notifications', { user_id: 'user-1', message: 'New video uploaded!' });
        console.log(response.data);
      } catch (error) {
        console.error('Error fetching notifications.');
      }
    };
    fetchNotifications();
  }, []);

  return <div>Check console for notifications.</div>;
};

export default Notifications;