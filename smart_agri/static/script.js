const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

// <!-- ========== DASHBOARD SCRIPT ========== -->
// Toggle on/off devices like water pump and LED
function toggleDevice(device) {
    fetch(`/toggle/${device}/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": "{{ csrf_token }}",
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        const label = document.getElementById(device + "Label");
        const toggleInput = document.getElementById(device + "Toggle");
        label.textContent = data.status ? "ON" : "OFF";
        toggleInput.checked = data.status;
    });
}

// Sidebar toggle for mobile
function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    sidebar.style.display = sidebar.style.display === "block" ? "none" : "block";
}