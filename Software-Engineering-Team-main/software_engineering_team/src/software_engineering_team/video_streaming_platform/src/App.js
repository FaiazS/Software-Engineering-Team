
import React, { useEffect, useState } from 'react';
import VideoList from './components/VideoList';
import VideoDetail from './components/VideoDetail';

const App = () => {
    const [videos, setVideos] = useState([]);
    const [selectedVideo, setSelectedVideo] = useState(null);

    useEffect(() => {
        const fetchVideos = async () => {
            const response = await fetch('/api/videos');
            const data = await response.json();
            setVideos(data);
        };
        fetchVideos();
    }, []);

    return (
        <div>
            <h1>Video Streaming Platform</h1>
            <VideoList videos={videos} onSelect={setSelectedVideo} />
            {selectedVideo && <VideoDetail video={selectedVideo} />}
        </div>
    );
};

export default App;
