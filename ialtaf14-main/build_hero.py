import base64
import os

img_path = r"c:\Users\altaf\Desktop\ialtaf14\ialtaf14-main\assets\altaf_khan.jpg"
with open(img_path, "rb") as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')

hero_svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 460" width="100%" height="100%">
  <defs>
    <!-- Background Gradients -->
    <radialGradient id="bgGlow1" cx="15%" cy="20%" r="65%">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#090D16" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="bgGlow2" cx="85%" cy="80%" r="65%">
      <stop offset="0%" stop-color="#7000FF" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#090D16" stop-opacity="0"/>
    </radialGradient>

    <!-- Glass Border Gradient -->
    <linearGradient id="glassBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.7"/>
      <stop offset="40%" stop-color="#7000FF" stop-opacity="0.4"/>
      <stop offset="70%" stop-color="#3B82F6" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#00F0FF" stop-opacity="0.6"/>
    </linearGradient>

    <!-- Text Gradients -->
    <linearGradient id="nameGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="50%" stop-color="#F1F5F9"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>

    <linearGradient id="accentGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F0FF"/>
      <stop offset="50%" stop-color="#7000FF"/>
      <stop offset="100%" stop-color="#3B82F6"/>
    </linearGradient>

    <linearGradient id="codeBarGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>

    <!-- Glow & Shadow Filters -->
    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="softShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.6"/>
    </filter>

    <!-- Photo Clip Path -->
    <clipPath id="photoClip">
      <rect x="0" y="0" width="220" height="280" rx="16"/>
    </clipPath>

    <!-- CSS Animations -->
    <style>
      @keyframes floatSlow {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-8px); }}
      }}
      @keyframes pulseGlow {{
        0%, 100% {{ opacity: 0.4; transform: scale(1); }}
        50% {{ opacity: 0.85; transform: scale(1.04); }}
      }}
      @keyframes spinSlow {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
      }}
      @keyframes cursorBlink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}

      .floating-element {{ animation: floatSlow 6s ease-in-out infinite; }}
      .pulsing-core {{ animation: pulseGlow 4s ease-in-out infinite; transform-origin: 820px 90px; }}
      .spinning-ring {{ animation: spinSlow 20s linear infinite; transform-origin: 820px 90px; }}
      .cursor {{ animation: cursorBlink 1s infinite; }}
    </style>
  </defs>

  <!-- Base Dark Canvas -->
  <rect width="950" height="460" rx="20" fill="#090D16"/>
  <rect width="950" height="460" rx="20" fill="url(#bgGlow1)"/>
  <rect width="950" height="460" rx="20" fill="url(#bgGlow2)"/>

  <!-- Subtle Grid Pattern -->
  <g opacity="0.06" stroke="#FFFFFF" stroke-width="1">
    <path d="M0 40 H950 M0 80 H950 M0 120 H950 M0 160 H950 M0 200 H950 M0 240 H950 M0 280 H950 M0 320 H950 M0 360 H950 M0 400 H950 M0 440 H950" />
    <path d="M50 0 V460 M100 0 V460 M150 0 V460 M200 0 V460 M250 0 V460 M300 0 V460 M350 0 V460 M400 0 V460 M450 0 V460 M500 0 V460 M550 0 V460 M600 0 V460 M650 0 V460 M700 0 V460 M750 0 V460 M800 0 V460 M850 0 V460 M900 0 V460" />
  </g>

  <!-- Main Outer Glass Panel -->
  <rect x="15" y="15" width="920" height="430" rx="16" fill="rgba(15, 23, 42, 0.65)" stroke="url(#glassBorder)" stroke-width="1.5" filter="url(#softShadow)"/>

  <!-- ==================== LEFT COLUMN: REAL PHOTO ==================== -->
  <g transform="translate(45, 45)">
    <!-- Photo Glass Outer Border -->
    <rect x="-4" y="-4" width="228" height="288" rx="20" fill="none" stroke="url(#glassBorder)" stroke-width="2" filter="url(#neonGlow)"/>
    <!-- Photo Container -->
    <g clip-path="url(#photoClip)">
      <image href="data:image/jpeg;base64,{b64_data}" x="-10" y="-15" width="240" height="310" preserveAspectRatio="xMidYMid slice"/>
      <!-- Glass Overlay Gradient -->
      <rect width="220" height="280" fill="url(#codeBarGrad)" opacity="0.15"/>
    </g>
    <!-- Photo Label Badge -->
    <g transform="translate(10, 240)">
      <rect width="200" height="32" rx="8" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(0, 240, 255, 0.4)" stroke-width="1"/>
      <circle cx="16" cy="16" r="4" fill="#10B981" filter="url(#neonGlow)"/>
      <text x="28" y="20" font-family="sans-serif" font-size="11" font-weight="700" fill="#F8FAFC">Altaf Khan • Data Analyst</text>
    </g>
  </g>

  <!-- ==================== MIDDLE/RIGHT: INFORMATION ==================== -->
  <g transform="translate(295, 45)">
    <!-- Status Pill -->
    <g transform="translate(0, 0)">
      <rect width="295" height="28" rx="14" fill="rgba(0, 240, 255, 0.08)" stroke="rgba(0, 240, 255, 0.35)" stroke-width="1"/>
      <circle cx="16" cy="14" r="4" fill="#00F0FF" filter="url(#neonGlow)"/>
      <text x="30" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#00F0FF" letter-spacing="1.2">AI &amp; DATA SCIENCE PORTFOLIO</text>
    </g>

    <!-- Name Header -->
    <text x="0" y="72" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="44" font-weight="800" fill="url(#nameGradient)" letter-spacing="-0.5">Altaf Khan</text>

    <!-- Roles Subtitle -->
    <text x="0" y="102" font-family="-apple-system, sans-serif" font-size="16" font-weight="600" fill="#38BDF8" letter-spacing="0.3">
      Data Analyst <tspan fill="#7000FF">•</tspan> Machine Learning Enthusiast <tspan fill="#7000FF">•</tspan> Aspiring Data Scientist
    </text>

    <!-- Tagline -->
    <text x="0" y="130" font-family="sans-serif" font-size="13" fill="#94A3B8" italic="true">
      "Transforming complex datasets into predictive ML models &amp; executive dashboards."
    </text>

    <!-- Tech Stack Glass Badges -->
    <g transform="translate(0, 150)">
      <g transform="translate(0,0)"><rect width="80" height="28" rx="8" fill="rgba(30,41,59,0.7)" stroke="rgba(56,189,248,0.4)" stroke-width="1"/><text x="40" y="18" font-family="sans-serif" font-size="12" font-weight="600" fill="#38BDF8" text-anchor="middle">Python</text></g>
      <g transform="translate(90,0)"><rect width="65" height="28" rx="8" fill="rgba(30,41,59,0.7)" stroke="rgba(168,85,247,0.4)" stroke-width="1"/><text x="32.5" y="18" font-family="sans-serif" font-size="12" font-weight="600" fill="#C084FC" text-anchor="middle">SQL</text></g>
      <g transform="translate(165,0)"><rect width="80" height="28" rx="8" fill="rgba(30,41,59,0.7)" stroke="rgba(0,240,255,0.4)" stroke-width="1"/><text x="40" y="18" font-family="sans-serif" font-size="12" font-weight="600" fill="#00F0FF" text-anchor="middle">Pandas</text></g>
      <g transform="translate(255,0)"><rect width="90" height="28" rx="8" fill="rgba(30,41,59,0.7)" stroke="rgba(245,158,11,0.4)" stroke-width="1"/><text x="45" y="18" font-family="sans-serif" font-size="12" font-weight="600" fill="#FBBF24" text-anchor="middle">Power BI</text></g>
      <g transform="translate(355,0)"><rect width="130" height="28" rx="8" fill="rgba(30,41,59,0.7)" stroke="rgba(236,72,153,0.4)" stroke-width="1"/><text x="65" y="18" font-family="sans-serif" font-size="12" font-weight="600" fill="#F472B6" text-anchor="middle">Scikit-Learn ML</text></g>
    </g>

    <!-- Training Glass Card -->
    <g transform="translate(0, 192)">
      <rect width="600" height="48" rx="10" fill="rgba(15, 23, 42, 0.65)" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1"/>
      <circle cx="20" cy="24" r="6" fill="#10B981" filter="url(#neonGlow)"/>
      <text x="36" y="20" font-family="sans-serif" font-size="12" font-weight="700" fill="#F8FAFC">Software Testing &amp; Programming Trainee</text>
      <text x="36" y="36" font-family="sans-serif" font-size="11" fill="#94A3B8">QSpiders Gurugram • August 2025 – Present</text>
    </g>

    <!-- Action Buttons Row -->
    <g transform="translate(0, 255)">
      <!-- Portfolio Button -->
      <a href="https://ialtaf14.vercel.app">
        <rect width="165" height="38" rx="19" fill="url(#accentGradient)" stroke="#00F0FF" stroke-width="1" filter="url(#neonGlow)"/>
        <text x="82.5" y="24" font-family="sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">🌐 Visit Portfolio App</text>
      </a>
      <!-- LinkedIn Button -->
      <g transform="translate(180, 0)">
        <rect width="120" height="38" rx="19" fill="rgba(30, 41, 59, 0.8)" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1"/>
        <text x="60" y="24" font-family="sans-serif" font-size="13" font-weight="600" fill="#38BDF8" text-anchor="middle">💼 LinkedIn</text>
      </g>
      <!-- Contact Button -->
      <g transform="translate(315, 0)">
        <rect width="120" height="38" rx="19" fill="rgba(30, 41, 59, 0.8)" stroke="rgba(168, 85, 247, 0.4)" stroke-width="1"/>
        <text x="60" y="24" font-family="sans-serif" font-size="13" font-weight="600" fill="#C084FC" text-anchor="middle">📧 Email Me</text>
      </g>
    </g>
  </g>

  <!-- Floating Code Window (Realistic IDE) -->
  <g transform="translate(565, 260)" class="floating-element">
    <rect width="355" height="170" rx="12" fill="rgba(15, 23, 42, 0.9)" stroke="rgba(0, 240, 255, 0.35)" stroke-width="1.5" filter="url(#softShadow)"/>
    <path d="M0 12 Q0 0 12 0 L343 0 Q355 0 355 12 L355 30 L0 30 Z" fill="url(#codeBarGrad)"/>
    <circle cx="16" cy="15" r="4.5" fill="#FF5F56"/>
    <circle cx="30" cy="15" r="4.5" fill="#FFBD2E"/>
    <circle cx="44" cy="15" r="4.5" fill="#27C93F"/>
    <text x="177.5" y="19" font-family="monospace" font-size="10.5" fill="#94A3B8" text-anchor="middle">nova_analytics_engine.py</text>
    <g transform="translate(16, 44)" font-family="Consolas, 'Fira Code', monospace" font-size="11" xml:space="preserve">
      <text y="12"><tspan fill="#F472B6">import</tspan> <tspan fill="#F8FAFC">pandas</tspan> <tspan fill="#F472B6">as</tspan> <tspan fill="#38BDF8">pd</tspan></text>
      <text y="28"><tspan fill="#F472B6">from</tspan> <tspan fill="#F8FAFC">novaflix</tspan> <tspan fill="#F472B6">import</tspan> <tspan fill="#38BDF8">RecommendEngine</tspan></text>
      <text y="44"><tspan fill="#64748B"># Analyze &amp; Predict Real Datasets</tspan></text>
      <text y="60"><tspan fill="#F8FAFC">data</tspan> = <tspan fill="#38BDF8">pd</tspan>.<tspan fill="#60A5FA">read_sql</tspan>(<tspan fill="#A3E635">"SELECT * FROM nova_recon"</tspan>)</text>
      <text y="76"><tspan fill="#F8FAFC">scores</tspan> = <tspan fill="#60A5FA">RecommendEngine</tspan>().<tspan fill="#60A5FA">fit</tspan>(<tspan fill="#F8FAFC">data</tspan>)</text>
      <text y="92"><tspan fill="#38BDF8">print</tspan>(<tspan fill="#A3E635">"⚡ Live on https://ialtaf14.vercel.app"</tspan>)<tspan fill="#00F0FF" class="cursor">|</tspan></text>
    </g>
  </g>
</svg>'''

output_path = r"c:\Users\altaf\Desktop\ialtaf14\ialtaf14-main\assets\hero.svg"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(hero_svg_content)

print(f"Successfully generated hero.svg with embedded base64 photo! Size: {os.path.getsize(output_path)} bytes")
