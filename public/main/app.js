function initializeVideoPlayer({ title, jsonFilePath, storageKey }) {
  document.getElementById('page-title').innerText = title;
  document.getElementById('video-title').innerText = title;

  let currentVideoIndex = 0;
  let videos = [];

  function loadSavedState() {
    const savedState = JSON.parse(localStorage.getItem(storageKey) || '{}');
    if (savedState.currentVideoIndex !== undefined) {
      currentVideoIndex = savedState.currentVideoIndex;
    }
    return savedState.currentVideoTime || 0;
  }

  function saveState() {
    const videoPlayer = document.getElementById('video-player');
    const state = {
      currentVideoIndex,
      currentVideoTime: videoPlayer.currentTime,
    };
    localStorage.setItem(storageKey, JSON.stringify(state));
  }

  function loadVideo(index, startTime = 0) {
    const videoData = videos[index];
    const videoPlayer = document.getElementById('video-player');
    const videoSource = document.getElementById('video-source');

    document.getElementById('video-title').innerText = videoData.title;
    videoSource.src = videoData.videoUrl;

    videoPlayer.load();
    videoPlayer.currentTime = startTime;
    videoPlayer.play();
  }

  function renderEpisodeList() {
    const episodeList = document.getElementById('episode-list');
    episodeList.innerHTML = '';
    videos.forEach((video, index) => {
      const listItem = document.createElement('li');
      listItem.classList.add('episode-item');
      listItem.textContent = video.title;
      listItem.onclick = function () {
        currentVideoIndex = index;
        loadVideo(currentVideoIndex);
        saveState();
      };
      episodeList.appendChild(listItem);
    });
  }

  fetch(jsonFilePath)
    .then(response => response.json())
    .then(data => {
      videos = data;
      const savedTime = loadSavedState();
      loadVideo(currentVideoIndex, savedTime);
      renderEpisodeList();
    })
    .catch(error => console.error('Error loading the JSON file:', error));

  document.getElementById('next-btn').addEventListener('click', function () {
    if (currentVideoIndex < videos.length - 1) {
      currentVideoIndex++;
      loadVideo(currentVideoIndex);
      saveState();
    }
  });

  document.getElementById('prev-btn').addEventListener('click', function () {
    if (currentVideoIndex > 0) {
      currentVideoIndex--;
      loadVideo(currentVideoIndex);
      saveState();
    }
  });

  const videoPlayer = document.getElementById('video-player');
  videoPlayer.addEventListener('pause', saveState);
  window.addEventListener('beforeunload', saveState);

  document.getElementById('skip-btn').addEventListener('click', function () {
    videoPlayer.currentTime = 120;
    saveState();
  });
}
