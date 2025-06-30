
import React from 'react';

const VideoDetail = ({ video }) => {
    return (
        <div>
            <h2>{video.title}</h2>
            <video controls>
                <source src={video.url} type="video/mp4" />
                Your browser does not support HTML video.
            </video>
            <p>{video.description}</p>
        </div>
    );
};

export default VideoDetail;
