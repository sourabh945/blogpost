// Navigate to Home Page
document.getElementById("homeBtn").addEventListener("click", () => {
  alert("Redirecting to Home page...");
  window.location.href = "/home"; // Update with the actual home page URL
});

// Simulate Upload Button
document.getElementById("uploadBtn").addEventListener("click", () => {
  alert("You are already on the Upload page.");
});

// Logout Button Logic
document.getElementById("logoutBtn").addEventListener("click", () => {
  alert("Logging out...");
  window.location.href = "/logout/for/you"; // Update with the actual logout URL
});

// Submit New Post
document.getElementById("submitPostBtn").addEventListener("click", () => {
  const title = document.getElementById("titleInput").value;
  const content = document.getElementById("contentInput").value;

  if (!title || !content) {
    alert("Both title and content are required!");
    return;
  }

  alert(`Post Submitted!\nTitle: ${title}\n`);
  // Example POST request to backend
  fetch("/newBlog/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      title: title,
      content: content,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      alert("Post created successfully!");
      console.log(data);
    })
    .catch((error) => {
      alert("Error in creating post.");
      console.error("Error:", error);
    });
  window.location.href = "/home/";
});
