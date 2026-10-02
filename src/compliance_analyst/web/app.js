const submitBtn = document.getElementById("submit-btn");
const statusEl = document.getElementById("status");
const resultsEl = document.getElementById("results");

function fillList(id, items) {
  const el = document.getElementById(id);
  el.innerHTML = "";
  for (const item of items) {
    const li = document.createElement("li");
    li.textContent = item;
    el.appendChild(li);
  }
}

submitBtn.addEventListener("click", async () => {
  const useCase = document.getElementById("use-case").value;
  statusEl.textContent = "Assessing...";
  resultsEl.hidden = true;

  try {
    const res = await fetch("/assess", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ use_case: useCase }),
    });

    if (!res.ok) {
      const err = await res.json();
      statusEl.textContent = `Error: ${err.detail}`;
      return;
    }

    const report = await res.json();
    statusEl.textContent = "";

    const tbody = document.querySelector("#verdicts-table tbody");
    tbody.innerHTML = "";
    for (const v of report.requirement_verdicts) {
      const row = document.createElement("tr");
      row.innerHTML = `<td>${v.requirement_id}</td><td>${v.verdict}</td><td>${v.evidence}</td><td>${v.recommended_action}</td>`;
      tbody.appendChild(row);
    }

    document.getElementById("overall-status").textContent = report.overall_status;
    fillList("gaps-list", report.gaps);
    fillList("risks-list", report.risks);
    fillList("next-steps-list", report.next_steps);

    resultsEl.hidden = false;
  } catch (e) {
    statusEl.textContent = `Error: ${e.message}`;
  }
});
