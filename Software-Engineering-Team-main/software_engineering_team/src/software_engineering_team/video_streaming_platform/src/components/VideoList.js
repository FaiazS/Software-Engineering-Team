
import React from 'react';

const VideoList = ({ videos, onSelect }) => {
   return (
      <div>
         {videos.map(video => (
            <div key={video.id} onClick={() => onSelect(video)}>
               <h2>{video.title}</h2>
            </div>
         ))}
      </div>
   );
};

export default VideoList;
