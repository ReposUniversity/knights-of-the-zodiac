const fs = require('fs');

let episodes = [];

for (let i = 1; i <= 12; i++) {
    const episodeNumber = i < 10 ? `0${i}` : i;
    episodes.push({
        title: `Law & Order: Trial By Jury Ep. ${i}`,
        url: "https://archive.org/details/knightsofthezodiac12",
        videoUrl: `https://ia601302.us.archive.org/35/items/law-order-trial-by-jury-s01/Law%20%26%20Order%20Trial%20By%20Jury%2FLaw%20%26%20Order%20Trial%20By%20Jury%20S01E${episodeNumber}.ia.mp4`
    });
}

const firstEpisode = episodes[0];
const fileName = firstEpisode.title.toLowerCase().replace(/ /g, '_').replace(/\d+/g, '').replace(/[^a-z_]/g, '').replace(/__+/g, '_') + '.json';
fs.writeFileSync(fileName, JSON.stringify(episodes, null, 2));
