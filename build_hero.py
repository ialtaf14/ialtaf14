import os

svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 400" width="100%" height="100%">
  <defs>
    <radialGradient id="bg1" cx="20%" cy="25%" r="60%">
      <stop offset="0%" stop-color="#0ea5e9" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#0a0f1e" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="bg2" cx="80%" cy="75%" r="55%">
      <stop offset="0%" stop-color="#6366f1" stop-opacity="0.20"/>
      <stop offset="100%" stop-color="#0a0f1e" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.65"/>
      <stop offset="50%" stop-color="#818cf8" stop-opacity="0.40"/>
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.55"/>
    </linearGradient>
    <linearGradient id="nameg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="55%" stop-color="#e0f2fe"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
    <linearGradient id="btngrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0ea5e9"/>
      <stop offset="100%" stop-color="#6366f1"/>
    </linearGradient>
    <linearGradient id="codebg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0d1117"/>
      <stop offset="100%" stop-color="#0a0f1e"/>
    </linearGradient>
    <linearGradient id="titlebar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#161b22"/>
      <stop offset="100%" stop-color="#0d1117"/>
    </linearGradient>
    <!-- Bar chart bar gradients -->
    <linearGradient id="barA" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0369a1" stop-opacity="0.6"/>
    </linearGradient>
    <linearGradient id="barB" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#3730a3" stop-opacity="0.6"/>
    </linearGradient>
    <linearGradient id="barC" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#4ade80"/>
      <stop offset="100%" stop-color="#15803d" stop-opacity="0.6"/>
    </linearGradient>
    <linearGradient id="barD" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#92400e" stop-opacity="0.6"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="shadow">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#000" flood-opacity="0.55"/>
    </filter>
    <filter id="codeGlow">
      <feDropShadow dx="0" dy="4" stdDeviation="14" flood-color="#0ea5e9" flood-opacity="0.18"/>
    </filter>
    <style>
      @keyframes blink {{ 0%,100%{{opacity:1}} 50%{{opacity:0}} }}
      .cur {{ animation: blink 1.1s step-end infinite; }}
    </style>
  </defs>

  <!-- Canvas -->
  <rect width="1100" height="400" rx="16" fill="#0a0f1e"/>
  <rect width="1100" height="400" rx="16" fill="url(#bg1)"/>
  <rect width="1100" height="400" rx="16" fill="url(#bg2)"/>

  <!-- Subtle grid -->
  <g opacity="0.04" stroke="#fff" stroke-width="0.7">
    <path d="M0 50H1100 M0 100H1100 M0 150H1100 M0 200H1100 M0 250H1100 M0 300H1100 M0 350H1100"/>
    <path d="M100 0V400 M200 0V400 M300 0V400 M400 0V400 M500 0V400 M600 0V400 M700 0V400 M800 0V400 M900 0V400 M1000 0V400"/>
  </g>

  <!-- Main glass panel -->
  <rect x="12" y="12" width="1076" height="376" rx="13" fill="rgba(13,20,40,0.70)" stroke="url(#border)" stroke-width="1.5" filter="url(#shadow)"/>

  <!-- ── COL 1: DATA CHART VISUAL ── -->
  <g transform="translate(30,28)">
    <!-- Chart card -->
    <rect width="220" height="344" rx="12" fill="rgba(13,20,40,0.80)" stroke="rgba(56,189,248,0.25)" stroke-width="1.2"/>

    <!-- Chart title -->
    <text x="110" y="26" font-family="system-ui,sans-serif" font-size="10" font-weight="700" fill="#38bdf8" text-anchor="middle" letter-spacing="0.8">ANALYTICS DASHBOARD</text>
    <line x1="16" y1="34" x2="204" y2="34" stroke="rgba(56,189,248,0.18)" stroke-width="0.8"/>

    <!-- KPI cards row -->
    <g transform="translate(12, 44)">
      <!-- KPI 1 -->
      <rect width="90" height="44" rx="6" fill="rgba(14,165,233,0.12)" stroke="rgba(14,165,233,0.30)" stroke-width="1"/>
      <text x="45" y="18" font-family="system-ui,sans-serif" font-size="16" font-weight="800" fill="#38bdf8" text-anchor="middle">96.4%</text>
      <text x="45" y="32" font-family="system-ui,sans-serif" font-size="8.5" fill="#94a3b8" text-anchor="middle">EDA Precision</text>
      <text x="45" y="42" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80" text-anchor="middle">▲ +3.8%</text>

      <!-- KPI 2 -->
      <rect x="100" width="90" height="44" rx="6" fill="rgba(99,102,241,0.12)" stroke="rgba(99,102,241,0.30)" stroke-width="1"/>
      <text x="145" y="18" font-family="system-ui,sans-serif" font-size="16" font-weight="800" fill="#a5b4fc" text-anchor="middle">4.2x</text>
      <text x="145" y="32" font-family="system-ui,sans-serif" font-size="8.5" fill="#94a3b8" text-anchor="middle">SQL Speed</text>
      <text x="145" y="42" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80" text-anchor="middle">▲ -76% latency</text>
    </g>

    <!-- Bar chart label -->
    <text x="110" y="108" font-family="system-ui,sans-serif" font-size="8.5" fill="#64748b" text-anchor="middle">Revenue by Region (Pivot Table)</text>

    <!-- Bar chart -->
    <g transform="translate(18, 115)">
      <!-- Gridlines -->
      <line x1="0" y1="0" x2="184" y2="0" stroke="rgba(255,255,255,0.06)" stroke-width="0.8"/>
      <line x1="0" y1="35" x2="184" y2="35" stroke="rgba(255,255,255,0.06)" stroke-width="0.8"/>
      <line x1="0" y1="70" x2="184" y2="70" stroke="rgba(255,255,255,0.06)" stroke-width="0.8"/>
      <line x1="0" y1="105" x2="184" y2="105" stroke="rgba(255,255,255,0.06)" stroke-width="0.8"/>

      <!-- Bars -->
      <rect x="6"  y="22" width="28" height="83" rx="4" fill="url(#barA)"/>
      <rect x="52" y="8"  width="28" height="97" rx="4" fill="url(#barB)"/>
      <rect x="98" y="35" width="28" height="70" rx="4" fill="url(#barC)"/>
      <rect x="144" y="15" width="28" height="90" rx="4" fill="url(#barD)"/>

      <!-- Bar value labels -->
      <text x="20"  y="18" font-family="system-ui,sans-serif" font-size="8" fill="#38bdf8" text-anchor="middle">68K</text>
      <text x="66"  y="4"  font-family="system-ui,sans-serif" font-size="8" fill="#a5b4fc" text-anchor="middle">81K</text>
      <text x="112" y="31" font-family="system-ui,sans-serif" font-size="8" fill="#4ade80" text-anchor="middle">53K</text>
      <text x="158" y="11" font-family="system-ui,sans-serif" font-size="8" fill="#fbbf24" text-anchor="middle">74K</text>

      <!-- X-axis labels -->
      <text x="20"  y="118" font-family="system-ui,sans-serif" font-size="7.5" fill="#64748b" text-anchor="middle">North</text>
      <text x="66"  y="118" font-family="system-ui,sans-serif" font-size="7.5" fill="#64748b" text-anchor="middle">South</text>
      <text x="112" y="118" font-family="system-ui,sans-serif" font-size="7.5" fill="#64748b" text-anchor="middle">East</text>
      <text x="158" y="118" font-family="system-ui,sans-serif" font-size="7.5" fill="#64748b" text-anchor="middle">West</text>

      <!-- Baseline -->
      <line x1="0" y1="105" x2="184" y2="105" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
    </g>

    <!-- Divider -->
    <line x1="16" y1="248" x2="204" y2="248" stroke="rgba(56,189,248,0.12)" stroke-width="0.8"/>

    <!-- SQL mini snippet -->
    <text x="18" y="264" font-family="system-ui,sans-serif" font-size="8" fill="#64748b">SQL Query</text>
    <rect x="12" y="270" width="196" height="60" rx="6" fill="rgba(9,13,22,0.70)" stroke="rgba(99,102,241,0.20)" stroke-width="1"/>
    <text x="18" y="286" font-family="'Fira Code',monospace" font-size="9">
      <tspan fill="#818cf8">SELECT</tspan>
      <tspan fill="#e2e8f0"> region,</tspan>
    </text>
    <text x="18" y="300" font-family="'Fira Code',monospace" font-size="9">
      <tspan fill="#818cf8">  SUM</tspan>
      <tspan fill="#e2e8f0">(revenue)</tspan>
      <tspan fill="#818cf8"> AS</tspan>
      <tspan fill="#4ade80"> total</tspan>
    </text>
    <text x="18" y="314" font-family="'Fira Code',monospace" font-size="9">
      <tspan fill="#818cf8">FROM</tspan>
      <tspan fill="#fbbf24"> sales</tspan>
      <tspan fill="#818cf8"> GROUP BY</tspan>
      <tspan fill="#e2e8f0"> region</tspan>
    </text>

    <!-- Data points processed -->
    <g transform="translate(12, 340)">
      <circle cx="6" cy="6" r="4" fill="#22c55e" filter="url(#glow)"/>
      <text x="16" y="10" font-family="system-ui,sans-serif" font-size="8.5" fill="#94a3b8">1.52M+ data points processed</text>
    </g>
  </g>

  <!-- ── COL 2: INFO (CENTER) ── -->
  <g transform="translate(272,32)">

    <!-- Badge -->
    <rect width="268" height="24" rx="12" fill="rgba(14,165,233,0.10)" stroke="rgba(14,165,233,0.40)" stroke-width="1"/>
    <circle cx="14" cy="12" r="3.5" fill="#38bdf8" filter="url(#glow)"/>
    <text x="26" y="16.5" font-family="system-ui,sans-serif" font-size="10" font-weight="700" fill="#38bdf8" letter-spacing="1">DATA ANALYST • OPEN TO WORK</text>

    <!-- Name -->
    <text x="0" y="70" font-family="system-ui,-apple-system,sans-serif" font-size="42" font-weight="800" fill="url(#nameg)" letter-spacing="-0.5">Altaf Khan</text>

    <!-- Title -->
    <text x="0" y="95" font-family="system-ui,sans-serif" font-size="13.5" font-weight="600" fill="#7dd3fc" letter-spacing="0.3">Data Analyst  ·  Python  ·  SQL  ·  Power BI  ·  Excel</text>

    <!-- Summary line -->
    <text x="0" y="118" font-family="system-ui,sans-serif" font-size="11.5" fill="#94a3b8">B.Tech CSE Graduate, 2026 — Pandas · NumPy · Matplotlib · Jupyter · EDA · BI Dashboards</text>

    <!-- Skill badges row 1 -->
    <g transform="translate(0,136)">
      <g><rect width="68" height="24" rx="6" fill="rgba(14,165,233,0.15)" stroke="rgba(14,165,233,0.45)" stroke-width="1"/><text x="34" y="16" font-family="system-ui,sans-serif" font-size="10.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Python</text></g>
      <g transform="translate(76,0)"><rect width="50" height="24" rx="6" fill="rgba(99,102,241,0.15)" stroke="rgba(99,102,241,0.45)" stroke-width="1"/><text x="25" y="16" font-family="system-ui,sans-serif" font-size="10.5" font-weight="700" fill="#a5b4fc" text-anchor="middle">SQL</text></g>
      <g transform="translate(134,0)"><rect width="80" height="24" rx="6" fill="rgba(245,158,11,0.15)" stroke="rgba(245,158,11,0.40)" stroke-width="1"/><text x="40" y="16" font-family="system-ui,sans-serif" font-size="10.5" font-weight="700" fill="#fbbf24" text-anchor="middle">Power BI</text></g>
      <g transform="translate(222,0)"><rect width="58" height="24" rx="6" fill="rgba(34,197,94,0.15)" stroke="rgba(34,197,94,0.40)" stroke-width="1"/><text x="29" y="16" font-family="system-ui,sans-serif" font-size="10.5" font-weight="700" fill="#4ade80" text-anchor="middle">Excel</text></g>
      <g transform="translate(288,0)"><rect width="66" height="24" rx="6" fill="rgba(14,165,233,0.10)" stroke="rgba(14,165,233,0.35)" stroke-width="1"/><text x="33" y="16" font-family="system-ui,sans-serif" font-size="10.5" font-weight="600" fill="#7dd3fc" text-anchor="middle">Pandas</text></g>
      <g transform="translate(362,0)"><rect width="74" height="24" rx="6" fill="rgba(99,102,241,0.10)" stroke="rgba(99,102,241,0.35)" stroke-width="1"/><text x="37" y="16" font-family="system-ui,sans-serif" font-size="10.5" font-weight="600" fill="#c7d2fe" text-anchor="middle">Matplotlib</text></g>
    </g>

    <!-- Skill badges row 2 -->
    <g transform="translate(0,168)">
      <g><rect width="66" height="24" rx="6" fill="rgba(14,165,233,0.10)" stroke="rgba(14,165,233,0.30)" stroke-width="1"/><text x="33" y="16" font-family="system-ui,sans-serif" font-size="10.5" font-weight="600" fill="#7dd3fc" text-anchor="middle">NumPy</text></g>
      <g transform="translate(74,0)"><rect width="92" height="24" rx="6" fill="rgba(34,197,94,0.10)" stroke="rgba(34,197,94,0.30)" stroke-width="1"/><text x="46" y="16" font-family="system-ui,sans-serif" font-size="10.5" font-weight="600" fill="#86efac" text-anchor="middle">Jupyter NB</text></g>
      <g transform="translate(174,0)"><rect width="50" height="24" rx="6" fill="rgba(249,115,22,0.10)" stroke="rgba(249,115,22,0.35)" stroke-width="1"/><text x="25" y="16" font-family="system-ui,sans-serif" font-size="10.5" font-weight="600" fill="#fdba74" text-anchor="middle">EDA</text></g>
      <g transform="translate(232,0)"><rect width="94" height="24" rx="6" fill="rgba(245,158,11,0.10)" stroke="rgba(245,158,11,0.30)" stroke-width="1"/><text x="47" y="16" font-family="system-ui,sans-serif" font-size="10.5" font-weight="600" fill="#fcd34d" text-anchor="middle">Scikit-learn</text></g>
    </g>

    <!-- Training info box -->
    <g transform="translate(0,206)">
      <rect width="468" height="38" rx="8" fill="rgba(13,20,40,0.65)" stroke="rgba(255,255,255,0.07)" stroke-width="1"/>
      <circle cx="16" cy="19" r="4" fill="#22c55e" filter="url(#glow)"/>
      <text x="30" y="14.5" font-family="system-ui,sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Data Analytics Training — QSpiders Gurugram</text>
      <text x="30" y="29" font-family="system-ui,sans-serif" font-size="10" fill="#94a3b8">Aug 2025 – Aug 2026  ·  Python · SQL · Power BI · Excel · Pandas · EDA</text>
    </g>

    <!-- Action buttons -->
    <g transform="translate(0,258)">
      <a href="https://ialtaf14.vercel.app">
        <rect width="148" height="34" rx="17" fill="url(#btngrad)" stroke="rgba(56,189,248,0.5)" stroke-width="1" filter="url(#glow)"/>
        <text x="74" y="22" font-family="system-ui,sans-serif" font-size="12" font-weight="700" fill="#fff" text-anchor="middle">🌐 Portfolio</text>
      </a>
      <a href="https://www.linkedin.com/in/altaf-khan-7a544b256/">
        <g transform="translate(160,0)">
          <rect width="110" height="34" rx="17" fill="rgba(10,102,194,0.20)" stroke="rgba(10,102,194,0.55)" stroke-width="1"/>
          <text x="55" y="22" font-family="system-ui,sans-serif" font-size="12" font-weight="600" fill="#60a5fa" text-anchor="middle">💼 LinkedIn</text>
        </g>
      </a>
      <a href="mailto:altafkhan122105@gmail.com">
        <g transform="translate(280,0)">
          <rect width="98" height="34" rx="17" fill="rgba(234,67,53,0.15)" stroke="rgba(234,67,53,0.45)" stroke-width="1"/>
          <text x="49" y="22" font-family="system-ui,sans-serif" font-size="12" font-weight="600" fill="#f87171" text-anchor="middle">📧 Email</text>
        </g>
      </a>
      <a href="https://github.com/ialtaf14">
        <g transform="translate(388,0)">
          <rect width="98" height="34" rx="17" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.18)" stroke-width="1"/>
          <text x="49" y="22" font-family="system-ui,sans-serif" font-size="12" font-weight="600" fill="#e2e8f0" text-anchor="middle">🐙 GitHub</text>
        </g>
      </a>
    </g>

    <!-- Certifications strip -->
    <g transform="translate(0,306)">
      <text x="0" y="12" font-family="system-ui,sans-serif" font-size="9" fill="#64748b" letter-spacing="0.5">CERTIFICATIONS</text>
      <g transform="translate(0,18)">
        <rect width="130" height="22" rx="5" fill="rgba(14,165,233,0.08)" stroke="rgba(14,165,233,0.25)" stroke-width="1"/>
        <text x="65" y="15" font-family="system-ui,sans-serif" font-size="8.5" fill="#7dd3fc" text-anchor="middle">Cisco Data Analytics</text>
      </g>
      <g transform="translate(138,18)">
        <rect width="130" height="22" rx="5" fill="rgba(14,165,233,0.08)" stroke="rgba(14,165,233,0.25)" stroke-width="1"/>
        <text x="65" y="15" font-family="system-ui,sans-serif" font-size="8.5" fill="#7dd3fc" text-anchor="middle">Cisco Data Science</text>
      </g>
      <g transform="translate(276,18)">
        <rect width="100" height="22" rx="5" fill="rgba(99,102,241,0.08)" stroke="rgba(99,102,241,0.25)" stroke-width="1"/>
        <text x="50" y="15" font-family="system-ui,sans-serif" font-size="8.5" fill="#a5b4fc" text-anchor="middle">NPTEL AI (IIT)</text>
      </g>
      <g transform="translate(384,18)">
        <rect width="84" height="22" rx="5" fill="rgba(99,102,241,0.08)" stroke="rgba(99,102,241,0.25)" stroke-width="1"/>
        <text x="42" y="15" font-family="system-ui,sans-serif" font-size="8.5" fill="#a5b4fc" text-anchor="middle">NPTEL IoT</text>
      </g>
    </g>

  </g>

  <!-- ── COL 3: CODE WINDOW (RIGHT) ── -->
  <g transform="translate(798,22)">
    <rect width="278" height="354" rx="12" fill="url(#codebg)" stroke="rgba(56,189,248,0.22)" stroke-width="1.2" filter="url(#codeGlow)"/>

    <!-- Title bar -->
    <rect width="278" height="32" rx="12" fill="url(#titlebar)"/>
    <rect y="16" width="278" height="16" fill="url(#titlebar)"/>
    <circle cx="15" cy="16" r="4.5" fill="#ff5f56"/>
    <circle cx="29" cy="16" r="4.5" fill="#ffbd2e"/>
    <circle cx="43" cy="16" r="4.5" fill="#27c93f"/>
    <text x="139" y="20" font-family="'Fira Code',monospace" font-size="9.5" fill="#6b7280" text-anchor="middle">data_analysis.py</text>
    <line x1="0" y1="32" x2="278" y2="32" stroke="rgba(56,189,248,0.12)" stroke-width="1"/>

    <!-- Code -->
    <g transform="translate(0,44)" font-family="'Fira Code',Consolas,monospace" font-size="10.8">
      <text x="12" y="14" fill="#374151">1</text>
      <text x="28" y="14"><tspan fill="#f472b6">import</tspan><tspan fill="#e2e8f0"> pandas </tspan><tspan fill="#f472b6">as</tspan><tspan fill="#38bdf8"> pd</tspan></text>

      <text x="12" y="30" fill="#374151">2</text>
      <text x="28" y="30"><tspan fill="#f472b6">import</tspan><tspan fill="#e2e8f0"> numpy </tspan><tspan fill="#f472b6">as</tspan><tspan fill="#38bdf8"> np</tspan></text>

      <text x="12" y="46" fill="#374151">3</text>
      <text x="28" y="46"><tspan fill="#f472b6">import</tspan><tspan fill="#e2e8f0"> matplotlib.pyplot </tspan><tspan fill="#f472b6">as</tspan><tspan fill="#38bdf8"> plt</tspan></text>

      <text x="12" y="62" fill="#374151">4</text>

      <text x="12" y="78" fill="#374151">5</text>
      <text x="28" y="78" fill="#4b5563"># Load &amp; clean dataset</text>

      <text x="12" y="94" fill="#374151">6</text>
      <text x="28" y="94"><tspan fill="#e2e8f0">df </tspan><tspan fill="#86efac">= </tspan><tspan fill="#38bdf8">pd</tspan><tspan fill="#e2e8f0">.</tspan><tspan fill="#60a5fa">read_csv</tspan><tspan fill="#e2e8f0">(</tspan><tspan fill="#a3e635">"sales_data.csv"</tspan><tspan fill="#e2e8f0">)</tspan></text>

      <text x="12" y="110" fill="#374151">7</text>
      <text x="28" y="110"><tspan fill="#e2e8f0">df.</tspan><tspan fill="#60a5fa">dropna</tspan><tspan fill="#e2e8f0">(inplace=</tspan><tspan fill="#f472b6">True</tspan><tspan fill="#e2e8f0">)</tspan></text>

      <text x="12" y="126" fill="#374151">8</text>

      <text x="12" y="142" fill="#374151">9</text>
      <text x="28" y="142" fill="#4b5563"># Pivot table by region</text>

      <text x="12" y="158" fill="#374151">10</text>
      <text x="28" y="158"><tspan fill="#e2e8f0">pivot </tspan><tspan fill="#86efac">= </tspan><tspan fill="#38bdf8">df</tspan><tspan fill="#e2e8f0">.</tspan><tspan fill="#60a5fa">pivot_table</tspan><tspan fill="#e2e8f0">(</tspan></text>

      <text x="12" y="174" fill="#374151">11</text>
      <text x="28" y="174"><tspan fill="#e2e8f0">    values</tspan><tspan fill="#86efac">=</tspan><tspan fill="#a3e635">"revenue"</tspan><tspan fill="#e2e8f0">,</tspan></text>

      <text x="12" y="190" fill="#374151">12</text>
      <text x="28" y="190"><tspan fill="#e2e8f0">    index</tspan><tspan fill="#86efac">=</tspan><tspan fill="#a3e635">"region"</tspan><tspan fill="#e2e8f0">,</tspan></text>

      <text x="12" y="206" fill="#374151">13</text>
      <text x="28" y="206"><tspan fill="#e2e8f0">    aggfunc</tspan><tspan fill="#86efac">=</tspan><tspan fill="#a3e635">"sum"</tspan><tspan fill="#e2e8f0">)</tspan></text>

      <text x="12" y="222" fill="#374151">14</text>

      <text x="12" y="238" fill="#374151">15</text>
      <text x="28" y="238" fill="#4b5563"># Visualize with Matplotlib</text>

      <text x="12" y="254" fill="#374151">16</text>
      <text x="28" y="254"><tspan fill="#38bdf8">df</tspan><tspan fill="#e2e8f0">[</tspan><tspan fill="#a3e635">"revenue"</tspan><tspan fill="#e2e8f0">].</tspan><tspan fill="#60a5fa">plot</tspan><tspan fill="#e2e8f0">(kind=</tspan><tspan fill="#a3e635">"bar"</tspan><tspan fill="#e2e8f0">)</tspan></text>

      <text x="12" y="270" fill="#374151">17</text>
      <text x="28" y="270"><tspan fill="#38bdf8">plt</tspan><tspan fill="#e2e8f0">.</tspan><tspan fill="#60a5fa">title</tspan><tspan fill="#e2e8f0">(</tspan><tspan fill="#a3e635">"Revenue by Region"</tspan><tspan fill="#e2e8f0">)</tspan></text>

      <text x="12" y="286" fill="#374151">18</text>
      <text x="28" y="286"><tspan fill="#38bdf8">plt</tspan><tspan fill="#e2e8f0">.</tspan><tspan fill="#60a5fa">show</tspan><tspan fill="#e2e8f0">()</tspan><tspan fill="#38bdf8" class="cur"> ▌</tspan></text>
    </g>

    <!-- Status bar -->
    <g transform="translate(0,322)">
      <rect width="278" height="32" rx="12" fill="#161b22"/>
      <rect y="0" width="278" height="16" fill="#161b22"/>
      <circle cx="14" cy="16" r="3.5" fill="#22c55e"/>
      <text x="26" y="20" font-family="'Fira Code',monospace" font-size="9" fill="#6b7280">Python 3.11  ·  pandas 2.1  ·  numpy 1.26</text>
    </g>
  </g>

</svg>'''

for path in [
    r"c:\Users\altaf\Desktop\ialtaf14\assets\hero.svg",
    r"c:\Users\altaf\Desktop\ialtaf14\ialtaf14-main\assets\hero.svg",
]:
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Written {path} — {os.path.getsize(path):,} bytes")
