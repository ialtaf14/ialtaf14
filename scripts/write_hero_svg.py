from pathlib import Path

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 480" width="100%" height="100%">
  <defs>
    <radialGradient id="bg1" cx="20%" cy="20%" r="50%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#060B17" stop-opacity="1"/>
    </radialGradient>
    <radialGradient id="bg2" cx="80%" cy="25%" r="42%">
      <stop offset="0%" stop-color="#A855F7" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#060B17" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="glassBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#60A5FA" stop-opacity="0.95"/>
      <stop offset="45%" stop-color="#8B5CF6" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="glassFill" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0D1421" stop-opacity="0.72"/>
      <stop offset="100%" stop-color="#090E18" stop-opacity="0.48"/>
    </linearGradient>
    <filter id="shadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="16" stdDeviation="20" flood-color="#0D172A" flood-opacity="0.34"/>
    </filter>
    <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <style>
      @keyframes driftUp { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-12px); } }
      @keyframes driftDown { 0%,100% { transform: translateY(0); } 50% { transform: translateY(12px); } }
      @keyframes shine { 0% { opacity: 0; transform: translateX(-100px); } 50% { opacity: 0.32; } 100% { opacity: 0; transform: translateX(980px); } }
      @keyframes pulse { 0%,100% { transform: scale(1); opacity: 0.7; } 50% { transform: scale(1.08); opacity: 1; } }
      @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
      .drift { animation: driftUp 8s ease-in-out infinite; }
      .drift-slow { animation: driftDown 11s ease-in-out infinite; }
      .pulse { animation: pulse 4.8s ease-in-out infinite; transform-origin: center; }
      .spin { animation: rotate 24s linear infinite; transform-origin: center; }
      .shine { animation: shine 18s linear infinite; }
      .codeCursor { animation: pulse 1.2s steps(2, end) infinite; }
    </style>
  </defs>
  <rect width="980" height="480" rx="24" fill="#060B17"/>
  <rect width="980" height="480" rx="24" fill="url(#bg1)"/>
  <rect width="980" height="480" rx="24" fill="url(#bg2)"/>
  <rect x="46" y="40" width="888" height="400" rx="30" fill="rgba(255,255,255,0.04)"/>
  <rect x="56" y="50" width="868" height="380" rx="26" fill="url(#glassFill)" stroke="url(#glassBorder)" stroke-width="1.4" filter="url(#shadow)"/>
  <rect x="62" y="56" width="140" height="18" rx="9" fill="rgba(255,255,255,0.08)"/>
  <rect x="62" y="84" width="240" height="2" fill="rgba(255,255,255,0.1)"/>
  <rect x="62" y="96" width="300" height="2" fill="rgba(255,255,255,0.08)"/>
  <text x="70" y="90" font-family="Inter, Arial, sans-serif" font-size="13" fill="#A5B4FC">Data profile • analytics dashboard • modern glass effect</text>
  <text x="70" y="138" font-family="Inter, Arial, sans-serif" font-size="44" font-weight="800" fill="#FFFFFF">Altaf Khan</text>
  <text x="70" y="178" font-family="Inter, Arial, sans-serif" font-size="18" fill="#94A3B8">Data Analyst • B.Tech CSE • Machine Learning Enthusiast</text>
  <g transform="translate(70, 198)">
    <rect x="0" y="42" width="760" height="130" rx="24" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.1)"/>
    <rect x="0" y="42" width="760" height="130" rx="24" fill="rgba(255,255,255,0.12)" opacity="0.17"/>
    <path d="M0 80 H760" stroke="rgba(255,255,255,0.16)" stroke-width="1"/>
    <path d="M0 112 H760" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
    <text x="28" y="70" font-family="Inter, sans-serif" font-size="12" fill="#E2E8F0" font-weight="700">Projects & insights</text>
    <text x="28" y="96" font-family="Inter, sans-serif" font-size="11" fill="#94A3B8">RealityML • NovaFlix • Nova AI • NovaRecon</text>
    <text x="28" y="118" font-family="Inter, sans-serif" font-size="11" fill="#94A3B8">Advanced SQL, Power BI, EDA, model evaluation, dashboard creation.</text>
    <rect x="530" y="56" width="190" height="74" rx="16" fill="rgba(56,189,248,0.12)" stroke="rgba(56,189,248,0.28)" stroke-width="1"/>
    <text x="545" y="84" font-family="Inter, sans-serif" font-size="12" fill="#60A5FA" font-weight="700">Open to Work</text>
    <text x="545" y="104" font-family="Inter, sans-serif" font-size="11" fill="#CBD5E1">Entry-level Data Analyst, ML, Data Science</text>
    <circle cx="620" cy="130" r="6" fill="#38BDF8" opacity="0.9"/>
    <circle cx="642" cy="130" r="5" fill="#A855F7" opacity="0.9"/>
    <circle cx="664" cy="130" r="4" fill="#22D3EE" opacity="0.9"/>
  </g>
  <g transform="translate(560, 110)" class="drift">
    <rect x="0" y="0" width="310" height="220" rx="28" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.1)"/>
    <rect x="0" y="0" width="310" height="220" rx="28" fill="url(#glassFill)" stroke="url(#glassBorder)" stroke-width="1.2"/>
    <circle cx="66" cy="66" r="44" fill="rgba(56,189,248,0.18)" class="pulse"/>
    <circle cx="66" cy="66" r="26" fill="#38BDF8" opacity="0.9"/>
    <text x="48" y="72" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">96.4%</text>
    <text x="48" y="92" font-family="Inter, sans-serif" font-size="10.5" fill="#94A3B8">Model precision</text>
    <rect x="20" y="134" width="270" height="12" rx="6" fill="rgba(255,255,255,0.08)"/>
    <rect x="20" y="154" width="232" height="10" rx="5" fill="#60A5FA"/>
    <text x="20" y="178" font-family="Inter, sans-serif" font-size="11" fill="#E2E8F0">Data cleaning • EDA • dashboard delivery</text>
    <path d="M20 190 L80 160 L116 194 L168 150 L220 186 L272 172" fill="none" stroke="#22D3EE" stroke-width="2.5" opacity="0.95"/>
  </g>
  <g transform="translate(130, 298)" class="drift-slow">
    <rect x="0" y="0" width="260" height="142" rx="24" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)"/>
    <rect x="16" y="16" width="228" height="24" rx="12" fill="rgba(56,189,248,0.14)"/>
    <text x="24" y="34" font-family="Inter, sans-serif" font-size="11" fill="#A5B4FC">Skill progress</text>
    <g transform="translate(24, 56)">
      <rect x="0" y="0" width="220" height="12" rx="6" fill="rgba(255,255,255,0.08)"/>
      <rect x="0" y="0" width="170" height="12" rx="6" fill="#8B5CF6"/>
      <text x="0" y="-6" font-family="Inter, sans-serif" font-size="9.5" fill="#E2E8F0">Python & analytics</text>
    </g>
    <g transform="translate(24, 86)">
      <rect x="0" y="0" width="220" height="12" rx="6" fill="rgba(255,255,255,0.08)"/>
      <rect x="0" y="0" width="155" height="12" rx="6" fill="#60A5FA"/>
      <text x="0" y="-6" font-family="Inter, sans-serif" font-size="9.5" fill="#E2E8F0">Power BI & visualization</text>
    </g>
    <g transform="translate(24, 116)">
      <rect x="0" y="0" width="220" height="12" rx="6" fill="rgba(255,255,255,0.08)"/>
      <rect x="0" y="0" width="130" height="12" rx="6" fill="#22D3EE"/>
      <text x="0" y="-6" font-family="Inter, sans-serif" font-size="9.5" fill="#E2E8F0">ML & scikit-learn</text>
    </g>
  </g>
  <rect x="68" y="110" width="160" height="18" rx="9" fill="rgba(255,255,255,0.08)"/>
  <rect x="70" y="148" width="9" height="9" rx="2" fill="#38BDF8"/>
  <rect x="86" y="148" width="9" height="9" rx="2" fill="#8B5CF6"/>
  <rect x="102" y="148" width="9" height="9" rx="2" fill="#22D3EE"/>
  <g transform="translate(72, 254)" fill="none" stroke="#60A5FA" stroke-width="1.1" opacity="0.3">
    <path d="M0 24 C40 8 120 8 180 22" class="spin"/>
    <path d="M0 42 C48 56 136 56 180 42" class="spin"/>
    <path d="M0 60 C32 76 128 76 180 60" class="spin"/>
  </g>
  <rect x="340" y="310" width="230" height="110" rx="20" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.12)"/>
  <rect x="348" y="318" width="214" height="94" rx="16" fill="rgba(255,255,255,0.08)"/>
  <text x="362" y="338" font-family="Inter, Arial, sans-serif" font-size="10.5" fill="#C7D2FE" letter-spacing="0.12em">LIVE DATA SIGNAL</text>
  <text x="362" y="362" font-family="Inter, Arial, sans-serif" font-size="25" font-weight="800" fill="#FFFFFF">21.4k</text>
  <text x="362" y="384" font-family="Inter, Arial, sans-serif" font-size="11.5" fill="#94A3B8">queries / day</text>
  <path d="M362 394 L398 366 L428 392 L462 352 L498 382" fill="none" stroke="#22D3EE" stroke-width="3" stroke-linecap="round"/>
  <circle cx="570" cy="366" r="8" fill="#60A5FA" opacity="0.9"/>
  <circle cx="590" cy="388" r="6" fill="#8B5CF6" opacity="0.9"/>
  <rect x="782" y="50" width="130" height="72" rx="18" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.12)"/>
  <rect x="792" y="62" width="110" height="38" rx="10" fill="rgba(56,189,248,0.16)"/>
  <text x="802" y="84" font-family="Inter, Arial, sans-serif" font-size="11" fill="#38BDF8">Live stats</text>
  <text x="802" y="100" font-family="Inter, Arial, sans-serif" font-size="12.5" font-weight="800" fill="#FFFFFF">76%</text>
  <rect x="720" y="150" width="180" height="140" rx="24" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.12)"/>
  <rect x="734" y="202" width="38" height="62" rx="12" fill="#38BDF8"/>
  <rect x="780" y="188" width="38" height="76" rx="12" fill="#8B5CF6"/>
  <rect x="826" y="158" width="38" height="106" rx="12" fill="#22D3EE"/>
  <g class="shine" fill="rgba(255,255,255,0.16)">
    <rect x="64" y="58" width="140" height="16" rx="8"/>
  </g>
  <g transform="translate(64, 266)" fill="#60A5FA" opacity="0.4">
    <circle cx="0" cy="0" r="4"/>
    <circle cx="18" cy="-6" r="2.4"/>
    <circle cx="42" cy="4" r="2.8"/>
    <circle cx="88" cy="-4" r="3.2"/>
    <circle cx="120" cy="6" r="2.6"/>
    <circle cx="148" cy="-8" r="2.4"/>
  </g>
  <text x="70" y="360" font-family="Inter, Arial, sans-serif" font-size="11" fill="#94A3B8">Glass visuals • motion • polished analytics</text>
  <text x="70" y="382" font-family="Inter, Arial, sans-serif" font-size="12.5" fill="#FFFFFF">Premium portfolio hero with animated data systems.</text>
  <circle cx="824" cy="390" r="32" fill="rgba(56,189,248,0.08)"/>
  <circle cx="824" cy="390" r="18" fill="#22D3EE" opacity="0.28" class="pulse"/>
  <circle cx="824" cy="390" r="10" fill="#38BDF8"/>
  <text x="100" y="420" font-family="Inter, Arial, sans-serif" font-size="10.5" fill="#94A3B8">Built for GitHub profiles — no scripts, pure SVG motion.</text>
</svg>"""
Path("assets/hero.svg").write_text(svg_content, encoding="utf-8")
