const header = document.getElementById("header");
const menuBtn = document.getElementById("menuBtn");
const nav = document.getElementById("nav");
const year = document.getElementById("year");
const orderForm = document.getElementById("orderForm");
const formSuccess = document.getElementById("formSuccess");

const MSG_PHONE = "79272102531";
const MSG_PHONE_PLUS = "+79272102531";

if (year) {
  year.textContent = String(new Date().getFullYear());
}

window.addEventListener(
  "scroll",
  () => {
    header?.classList.toggle("scrolled", window.scrollY > 24);
  },
  { passive: true }
);

menuBtn?.addEventListener("click", () => {
  const open = nav?.classList.toggle("open");
  menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
});

nav?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    nav.classList.remove("open");
    menuBtn?.setAttribute("aria-expanded", "false");
  });
});

const revealTargets = document.querySelectorAll(
  ".section-head, .cat, .why-visual, .why-content, .benefit-row article, .order-panel, .delivery-grid > div, .contacts-inner, .strip-item"
);

revealTargets.forEach((el) => el.classList.add("reveal"));

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.16, rootMargin: "0px 0px -40px 0px" }
);

revealTargets.forEach((el) => observer.observe(el));

orderForm?.addEventListener("submit", (event) => {
  event.preventDefault();
  const data = new FormData(orderForm);
  const name = String(data.get("name") || "").trim();
  const phone = String(data.get("phone") || "").trim();
  const message = String(data.get("message") || "").trim();

  const text = [
    "Здравствуйте! Заявка с сайта Czech Biser.",
    name ? `Имя: ${name}` : "",
    phone ? `Контакт: ${phone}` : "",
    message ? `Интересует: ${message}` : "",
  ]
    .filter(Boolean)
    .join("\n");

  if (formSuccess) {
    formSuccess.hidden = false;
  }

  const url = `https://wa.me/${MSG_PHONE}?text=${encodeURIComponent(text)}`;
  window.open(url, "_blank", "noopener");
  orderForm.reset();
});

// Max не умеет ссылку «написать по номеру» как WhatsApp.
// Открываем веб-версию и копируем номер, чтобы быстро найти контакт.
document.querySelectorAll(".js-msg-max, a[href*='web.max.ru']").forEach((el) => {
  el.addEventListener("click", async (event) => {
    event.preventDefault();
    const phone = el.getAttribute("data-phone") || MSG_PHONE;
    const plus = phone.startsWith("+") ? phone : `+${phone}`;
    try {
      await navigator.clipboard.writeText(plus);
    } catch (_) {
      /* ignore */
    }
    window.open("https://web.max.ru/", "_blank", "noopener");
  });
});
