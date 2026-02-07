document.addEventListener("DOMContentLoaded", () => {
  const video = /** @type {HTMLVideoElement | null} */ (
    document.getElementById("lecturePlayer")
  );
  const playlist = document.getElementById("playlistList");
  const titleEl = document.getElementById("lectureTitle");
  const summaryEl = document.getElementById("lectureSummary");
  const indexEl = document.getElementById("lectureIndex");
  const durationEl = document.getElementById("lectureDuration");
  const progressEl = document.getElementById("courseProgress");
  const autoplayToggle = document.getElementById("autoplayToggle");
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");

  if (
    !video ||
    !playlist ||
    !titleEl ||
    !summaryEl ||
    !indexEl ||
    !durationEl ||
    !progressEl
  ) {
    return;
  }

  const items = Array.from(playlist.querySelectorAll(".playlist-item"));
  const total = parseInt(playlist.dataset.total || `${items.length}`, 10);

  let currentIndex = 0;

  function setActiveIndex(newIndex, autoplay = false) {
    if (newIndex < 0 || newIndex >= items.length) return;

    currentIndex = newIndex;

    items.forEach((el, i) => {
      el.classList.toggle("active", i === currentIndex);
    });

    const activeItem = items[currentIndex];
    const videoUrl = activeItem.getAttribute("data-video-url");
    const title = activeItem.getAttribute("data-title");
    const summary = activeItem.getAttribute("data-summary");
    const duration = activeItem.getAttribute("data-duration");

    if (videoUrl) {
      const source = video.querySelector("source");
      if (source) {
        source.src = videoUrl;
        video.load();
        if (autoplay) {
          const playPromise = video.play();
          if (playPromise && typeof playPromise.catch === "function") {
            playPromise.catch(() => {});
          }
        }
      }
    }

    titleEl.textContent = title || "";
    summaryEl.textContent = summary || "";
    indexEl.textContent = `Lecture ${currentIndex + 1} of ${total}`;
    durationEl.innerHTML = `<i class="fa-regular fa-clock"></i> ${duration || ""}`;

    const ratio = ((currentIndex + 1) / total) * 100;
    progressEl.style.width = `${ratio}%`;
  }

  function goNext(autoplay = false) {
    if (currentIndex < items.length - 1) {
      setActiveIndex(currentIndex + 1, autoplay);
      ensureVisible();
    }
  }

  function goPrev(autoplay = false) {
    if (currentIndex > 0) {
      setActiveIndex(currentIndex - 1, autoplay);
      ensureVisible();
    }
  }

  function ensureVisible() {
    const active = items[currentIndex];
    if (!active) return;
    active.scrollIntoView({ block: "nearest", behavior: "smooth" });
  }

  items.forEach((item, index) => {
    item.addEventListener("click", () => {
      setActiveIndex(index, true);
    });
  });

  if (nextBtn) {
    nextBtn.addEventListener("click", () => goNext(true));
  }

  if (prevBtn) {
    prevBtn.addEventListener("click", () => goPrev(true));
  }

  // Autoplay on video end
  video.addEventListener("ended", () => {
    const shouldAutoplay =
      autoplayToggle instanceof HTMLInputElement
        ? autoplayToggle.checked
        : false;
    if (shouldAutoplay && currentIndex < items.length - 1) {
      goNext(true);
    }
  });

  // Initialize state (ensure progress bar correct)
  setActiveIndex(currentIndex, false);
});


