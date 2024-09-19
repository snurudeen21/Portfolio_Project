let rainVideo = document.getElementById("rain-video");
let sunVideo = document.getElementById("sun-video");
let currentWeather = "rain"; // Start with rain

function toggleWeatherVideo() {
  if (currentWeather === "rain") {
    // Hide rain, show sun, pause rain, and play sun
    rainVideo.style.opacity = "0"; // Fade out rain
    rainVideo.style.visibility = "hidden";
    rainVideo.pause(); // Pause rain video

    sunVideo.style.opacity = "1"; // Fade in sun
    sunVideo.style.visibility = "visible";
    sunVideo.play(); // Play sun video

    currentWeather = "sun";
  } else {
    // Hide sun, show rain, pause sun, and play rain
    sunVideo.style.opacity = "0"; // Fade out sun
    sunVideo.style.visibility = "hidden";
    sunVideo.pause(); // Pause sun video

    rainVideo.style.opacity = "1"; // Fade in rain
    rainVideo.style.visibility = "visible";
    rainVideo.play(); // Play rain video

    currentWeather = "rain";
  }
}

// Change weather video every 14 seconds
setInterval(toggleWeatherVideo, 14000);
