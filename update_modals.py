import re

file_path = r"c:\Users\fumil\Desktop\html_practice\Portfolio\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

css_to_add = """
/* ===== CERTIFICATE MODAL ===== */
.cert-modal {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  z-index: 2000;
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  animation: fadeIn 0.3s ease;
}

.cert-modal.active {
  display: flex;
}

.cert-modal-content {
  position: relative;
  width: 90%;
  max-width: 900px;
  height: 85vh;
  display: flex;
  justify-content: center;
  align-items: center;
  animation: scaleIn 0.3s ease;
}

@media (max-width: 768px) {
  .cert-modal-content {
    width: 95%;
    height: 80vh;
  }
}

@media (max-width: 480px) {
  .cert-modal-content {
    width: 98%;
    height: 75vh;
  }
}

.cert-modal-content img,
.cert-modal-content iframe {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  border-radius: 12px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
  background: white; /* In case PDF has transparent background */
}

.cert-modal-close {
  position: absolute;
  top: -40px;
  right: 0;
  width: 36px;
  height: 36px;
  background: rgba(26, 26, 46, 0.9);
  border: 1px solid var(--border);
  border-radius: 50%;
  color: var(--accent);
  font-size: 18px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition);
  z-index: 10;
}

.cert-modal-close:hover {
  background: var(--accent);
  color: #fff;
  transform: scale(1.1);
}

@media (max-width: 768px) {
  .cert-modal-close {
    top: -40px;
    right: 0;
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* Make certificate cards clickable */
.cert-card {
  cursor: pointer;
}

.cert-card:not(.coming-soon) {
  transition: var(--transition);
}

.cert-card:not(.coming-soon):hover {
  border-color: var(--accent);
  transform: translateY(-4px);
  box-shadow: 0 0 40px rgba(108, 99, 255, 0.3);
}
"""

content = content.replace("</style>", css_to_add + "\n          </style>", 1)

# Replace NOUN wrapper
content = content.replace(
    '<div class="reveal" style="background: var(--bg-card); border: 1px solid var(--border); border-radius: 20px; padding: 32px; transition: var(--transition); cursor: default;">',
    '<div class="reveal" style="background: var(--bg-card); border: 1px solid var(--border); border-radius: 20px; padding: 32px; transition: var(--transition); cursor: pointer;" onclick="openCertModal(\'nounModal\')">',
    1
)

# Replace NOUN inner card
old_noun_card = """          <div class="cert-card">
            <div class="cert-icon">🎓</div>
            <div class="cert-title">B.A. (Hons.) Second Class (Upper Division)</div>
            <div class="cert-issuer">National Open University of Nigeria (NOUN)</div>
            <div class="cert-date">March 2026 • English Major</div>
            <div class="cert-description">
              Bachelor of Arts degree with focus on English language studies. Completed all coursework and examinations successfully.
            </div>
            <span class="cert-badge">Verified</span>
          </div>"""

new_noun_card = """          <div class="cert-card">
            <div class="cert-icon">🎓</div>
            <div class="cert-title">B.A. (Hons.) Second Class (Upper Division)</div>
            <div class="cert-issuer">National Open University of Nigeria (NOUN)</div>
            <div class="cert-date">March 2026 • English Major</div>
            <div class="cert-description">
              Bachelor of Arts degree with focus on English language studies. Completed all coursework and examinations successfully.
            </div>
            <span class="cert-badge">Verified</span>
            <div style="margin-top: 16px; font-size: 12px; color: var(--accent); font-weight: 600;">
              Click to view certificate →
            </div>
          </div>"""

content = content.replace(old_noun_card, new_noun_card)

# Replace CFG card
old_cfg = """        <!-- Certification 2: Code First Girls Python -->
        <div class="reveal" style="background: var(--bg-card); border: 1px solid var(--border); border-radius: 20px; padding: 32px; transition: var(--transition); cursor: default;">
          <div class="cert-card">
            <div class="cert-icon">🐍</div>
            <div class="cert-title">Python Kickstarter Course</div>
            <div class="cert-issuer">Code First Girls</div>
            <div class="cert-date">June 2026 • Introduction to Python</div>
            <div class="cert-description">
              Completed introductory Python programming course covering fundamentals, data structures, and practical coding skills. Hands-on learning experience.
            </div>
            <span class="cert-badge">Certified</span>
          </div>
        </div>"""

new_cfg = """        <!-- Certification 2: Code First Girls Python -->
        <div class="reveal" style="background: var(--bg-card); border: 1px solid var(--border); border-radius: 20px; padding: 32px; transition: var(--transition); cursor: pointer;" onclick="openCertModal('cfgModal')">
          <div class="cert-card">
            <div class="cert-icon">🐍</div>
            <div class="cert-title">Python Kickstarter Course</div>
            <div class="cert-issuer">Code First Girls</div>
            <div class="cert-date">June 2026 • Introduction to Python</div>
            <div class="cert-description">
              Completed introductory Python programming course covering fundamentals, data structures, and practical coding skills. Hands-on learning experience.
            </div>
            <span class="cert-badge">Certified</span>
            <div style="margin-top: 16px; font-size: 12px; color: var(--accent); font-weight: 600;">
              Click to view certificate →
            </div>
          </div>
        </div>"""

content = content.replace(old_cfg, new_cfg)

modal_html = """
<!-- ===== CERTIFICATE MODALS ===== -->

<!-- NOUN Degree Certificate Modal -->
<div class="cert-modal" id="nounModal">
  <div class="cert-modal-content">
    <button class="cert-modal-close" onclick="closeCertModal('nounModal')">
      <i class="fa-solid fa-xmark"></i>
    </button>
    <img src="Bachelor_of_Arts_Degree_Certificate_-_Kadri_Kehinde_Karimat__Jpeg_.jpg" 
         alt="NOUN Bachelor of Arts Degree Certificate"
         loading="lazy">
  </div>
</div>

<!-- Code First Girls Python Certificate Modal -->
<div class="cert-modal" id="cfgModal">
  <div class="cert-modal-content">
    <button class="cert-modal-close" onclick="closeCertModal('cfgModal')">
      <i class="fa-solid fa-xmark"></i>
    </button>
    <iframe src="Certificate_-_Kehinde_Kadri.pdf" 
            alt="Code First Girls Python Certificate"
            style="width: 100%; height: 100%; border: none; border-radius: 12px;">
    </iframe>
  </div>
</div>

<script>
// --- Certificate Modal Functions ---

function openCertModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.add('active');
    document.body.style.overflow = 'hidden'; // Prevent scrolling
  }
}

function closeCertModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = 'auto'; // Re-enable scrolling
  }
}

// Close modal when clicking outside the image
document.querySelectorAll('.cert-modal').forEach(modal => {
  modal.addEventListener('click', function(e) {
    if (e.target === this) {
      closeCertModal(this.id);
    }
  });
});

// Close modal on Escape key
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    document.querySelectorAll('.cert-modal.active').forEach(modal => {
      closeCertModal(modal.id);
    });
  }
});
</script>
"""

content = content.replace("</body>", modal_html + "\n</body>")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
