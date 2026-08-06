import base64
import os

img_path = r"c:\Users\altaf\Desktop\ialtaf14\assets\altaf_khan.jpg"
with open(img_path, "rb") as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')

hero_svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 420" width="100%" height="100%">
  <defs>
    <!-- Background Gradients -->
    <radialGradient id="bgGlow1" cx="15%" cy="20%" r="65%">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.20"/>
      <stop offset="100%" stop-color="#090D16" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="bgGlow2" cx="85%" cy="80%" r="60%">
      <stop offset="0%" stop-color="#7000FF" stop-opacity="0.22"/>
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

    <linearGradient id="codeBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0D1117"/>
      <stop offset="100%" stop-color="#090D16"/>
    </linearGradient>

    <!-- Glow Filters -->
    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="softShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#000000" flood-opacity="0.6"/>
    </filter>

    <filter id="codeShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#00F0FF" flood-opacity="0.15"/>
    </filter>

    <!-- Photo Clip -->
    <clipPath id="photoClip">
      <rect x="0" y="0" width="200" height="268" rx="14"/>
    </clipPath>

    <!-- Blinking cursor animation -->
    <style>
      @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}
      .cursor-blink {{ animation: blink 1.1s step-end infinite; }}
    </style>
  </defs>

  <!-- ===== BASE DARK CANVAS ===== -->
  <rect width="1100" height="420" rx="18" fill="#090D16"/>
  <rect width="1100" height="420" rx="18" fill="url(#bgGlow1)"/>
  <rect width="1100" height="420" rx="18" fill="url(#bgGlow2)"/>

  <!-- Subtle Grid -->
  <g opacity="0.05" stroke="#FFFFFF" stroke-width="0.8">
    <path d="M0 42 H1100 M0 84 H1100 M0 126 H1100 M0 168 H1100 M0 210 H1100 M0 252 H1100 M0 294 H1100 M0 336 H1100 M0 378 H1100"/>
    <path d="M55 0 V420 M110 0 V420 M165 0 V420 M220 0 V420 M275 0 V420 M330 0 V420 M385 0 V420 M440 0 V420 M495 0 V420 M550 0 V420 M605 0 V420 M660 0 V420 M715 0 V420 M770 0 V420 M825 0 V420 M880 0 V420 M935 0 V420 M990 0 V420 M1045 0 V420"/>
  </g>

  <!-- Main Glass Panel -->
  <rect x="12" y="12" width="1076" height="396" rx="14" fill="rgba(15, 23, 42, 0.65)" stroke="url(#glassBorder)" stroke-width="1.5" filter="url(#softShadow)"/>

  <!-- ===== COLUMN 1: PHOTO (LEFT) ===== -->
  <g transform="translate(36, 36)">
    <!-- Neon border ring around photo -->
    <rect x="-3" y="-3" width="206" height="274" rx="17" fill="none" stroke="url(#glassBorder)" stroke-width="2" filter="url(#neonGlow)"/>
    <!-- Photo clipped -->
    <g clip-path="url(#photoClip)">
      <image href="data:image/jpeg;base64,{b64_data}" x="-8" y="-10" width="216" height="290" preserveAspectRatio="xMidYMid slice"/>
      <rect width="200" height="268" fill="url(#codeBarGrad)" opacity="0.12"/>
    </g>
    <!-- Name badge at bottom of photo -->
    <g transform="translate(8, 228)">
      <rect width="184" height="30" rx="7" fill="rgba(9,13,22,0.88)" stroke="rgba(0,240,255,0.4)" stroke-width="1"/>
      <circle cx="14" cy="15" r="4" fill="#10B981" filter="url(#neonGlow)"/>
      <text x="26" y="19" font-family="sans-serif" font-size="10.5" font-weight="700" fill="#F8FAFC">Altaf Khan • Data Analyst</text>
    </g>
  </g>

  <!-- ===== COLUMN 2: INFO (CENTER) ===== -->
  <g transform="translate(266, 36)">

    <!-- Status Pill -->
    <rect width="280" height="26" rx="13" fill="rgba(0,240,255,0.08)" stroke="rgba(0,240,255,0.35)" stroke-width="1"/>
    <circle cx="15" cy="13" r="3.5" fill="#00F0FF" filter="url(#neonGlow)"/>
    <text x="28" y="17" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#00F0FF" letter-spacing="1.1">AI &amp; DATA SCIENCE PORTFOLIO</text>

    <!-- Name -->
    <text x="0" y="74" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="42" font-weight="800" fill="url(#nameGradient)" letter-spacing="-0.5">Altaf Khan</text>

    <!-- Roles -->
    <text x="0" y="100" font-family="-apple-system, sans-serif" font-size="13.5" font-weight="600" fill="#38BDF8" letter-spacing="0.2">
      Data Analyst <tspan fill="#7000FF">•</tspan> ML Enthusiast <tspan fill="#7000FF">•</tspan> Aspiring Data Scientist
    </text>

    <!-- Tagline -->
    <text x="0" y="124" font-family="sans-serif" font-size="12" fill="#94A3B8">
      "Transforming complex datasets into predictive ML models &amp; executive dashboards."
    </text>

    <!-- Tech Badges -->
    <g transform="translate(0, 144)">
      <g transform="translate(0,0)"><rect width="78" height="26" rx="7" fill="rgba(30,41,59,0.75)" stroke="rgba(56,189,248,0.4)" stroke-width="1"/><text x="39" y="17" font-family="sans-serif" font-size="11" font-weight="600" fill="#38BDF8" text-anchor="middle">Python</text></g>
      <g transform="translate(88,0)"><rect width="58" height="26" rx="7" fill="rgba(30,41,59,0.75)" stroke="rgba(168,85,247,0.4)" stroke-width="1"/><text x="29" y="17" font-family="sans-serif" font-size="11" font-weight="600" fill="#C084FC" text-anchor="middle">SQL</text></g>
      <g transform="translate(156,0)"><rect width="74" height="26" rx="7" fill="rgba(30,41,59,0.75)" stroke="rgba(0,240,255,0.4)" stroke-width="1"/><text x="37" y="17" font-family="sans-serif" font-size="11" font-weight="600" fill="#00F0FF" text-anchor="middle">Pandas</text></g>
      <g transform="translate(240,0)"><rect width="84" height="26" rx="7" fill="rgba(30,41,59,0.75)" stroke="rgba(245,158,11,0.4)" stroke-width="1"/><text x="42" y="17" font-family="sans-serif" font-size="11" font-weight="600" fill="#FBBF24" text-anchor="middle">Power BI</text></g>
      <g transform="translate(334,0)"><rect width="110" height="26" rx="7" fill="rgba(30,41,59,0.75)" stroke="rgba(236,72,153,0.4)" stroke-width="1"/><text x="55" y="17" font-family="sans-serif" font-size="11" font-weight="600" fill="#F472B6" text-anchor="middle">Scikit-Learn</text></g>
    </g>

    <!-- Training Card -->
    <g transform="translate(0, 184)">
      <rect width="490" height="44" rx="9" fill="rgba(15,23,42,0.7)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
      <circle cx="18" cy="22" r="5" fill="#10B981" filter="url(#neonGlow)"/>
      <text x="32" y="18" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#F8FAFC">Software Testing &amp; Programming Trainee</text>
      <text x="32" y="33" font-family="sans-serif" font-size="10.5" fill="#94A3B8">QSpiders Gurugram  •  August 2025 – Present</text>
    </g>

    <!-- Action Buttons -->
    <g transform="translate(0, 242)">
      <a href="https://ialtaf14.vercel.app">
        <rect width="155" height="36" rx="18" fill="url(#accentGradient)" stroke="#00F0FF" stroke-width="1" filter="url(#neonGlow)"/>
        <text x="77.5" y="23" font-family="sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">🌐 Portfolio App</text>
      </a>
      <a href="https://www.linkedin.com/in/altaf-khan-7a544b256/">
        <g transform="translate(168, 0)">
          <rect width="110" height="36" rx="18" fill="rgba(10,102,194,0.2)" stroke="rgba(10,102,194,0.5)" stroke-width="1"/>
          <text x="55" y="23" font-family="sans-serif" font-size="12" font-weight="600" fill="#38BDF8" text-anchor="middle">💼 LinkedIn</text>
        </g>
      </a>
      <a href="mailto:altafkhan122105@gmail.com">
        <g transform="translate(288, 0)">
          <rect width="110" height="36" rx="18" fill="rgba(234,67,53,0.15)" stroke="rgba(234,67,53,0.4)" stroke-width="1"/>
          <text x="55" y="23" font-family="sans-serif" font-size="12" font-weight="600" fill="#F87171" text-anchor="middle">📧 Gmail</text>
        </g>
      </a>
    </g>

  </g>

  <!-- ===== COLUMN 3: CODE WINDOW (RIGHT) — FIXED POSITION ===== -->
  <g transform="translate(784, 26)">
    <!-- Outer glow border -->
    <rect width="296" height="368" rx="14" fill="none" stroke="rgba(0,240,255,0.25)" stroke-width="1" filter="url(#codeShadow)"/>
    <!-- Window background -->
    <rect width="296" height="368" rx="14" fill="url(#codeBg)" stroke="rgba(0,240,255,0.18)" stroke-width="1"/>

    <!-- Title bar -->
    <rect width="296" height="34" rx="14" fill="url(#codeBarGrad)"/>
    <rect y="14" width="296" height="20" fill="url(#codeBarGrad)"/>

    <!-- macOS dots -->
    <circle cx="16" cy="17" r="5" fill="#FF5F56"/>
    <circle cx="32" cy="17" r="5" fill="#FFBD2E"/>
    <circle cx="48" cy="17" r="5" fill="#27C93F"/>

    <!-- File name -->
    <text x="148" y="21" font-family="'Fira Code', monospace" font-size="10" fill="#94A3B8" text-anchor="middle">nova_analytics_engine.py</text>

    <!-- Divider under title bar -->
    <line x1="0" y1="34" x2="296" y2="34" stroke="rgba(0,240,255,0.15)" stroke-width="1"/>

    <!-- Line numbers + code -->
    <g transform="translate(0, 46)" font-family="'Fira Code', Consolas, monospace" font-size="11.5">

      <!-- Line 1 -->
      <text x="14" y="14" fill="#374151">1</text>
      <text x="36" y="14">
        <tspan fill="#F472B6">import</tspan>
        <tspan fill="#F8FAFC"> pandas </tspan>
        <tspan fill="#F472B6">as</tspan>
        <tspan fill="#38BDF8"> pd</tspan>
      </text>

      <!-- Line 2 -->
      <text x="14" y="32" fill="#374151">2</text>
      <text x="36" y="32">
        <tspan fill="#F472B6">import</tspan>
        <tspan fill="#F8FAFC"> numpy </tspan>
        <tspan fill="#F472B6">as</tspan>
        <tspan fill="#38BDF8"> np</tspan>
      </text>

      <!-- Line 3 blank -->
      <text x="14" y="50" fill="#374151">3</text>

      <!-- Line 4 -->
      <text x="14" y="68" fill="#374151">4</text>
      <text x="36" y="68">
        <tspan fill="#F472B6">from</tspan>
        <tspan fill="#F8FAFC"> novaflix </tspan>
        <tspan fill="#F472B6">import</tspan>
        <tspan fill="#A78BFA"> RecommendEngine</tspan>
      </text>

      <!-- Line 5 comment -->
      <text x="14" y="86" fill="#374151">5</text>
      <text x="36" y="86" fill="#4B5563"># Load &amp; pivot real datasets</text>

      <!-- Line 6 -->
      <text x="14" y="104" fill="#374151">6</text>
      <text x="36" y="104">
        <tspan fill="#F8FAFC">df </tspan>
        <tspan fill="#A3E635">= </tspan>
        <tspan fill="#38BDF8">pd</tspan>
        <tspan fill="#F8FAFC">.</tspan>
        <tspan fill="#60A5FA">read_sql</tspan>
        <tspan fill="#F8FAFC">(</tspan>
        <tspan fill="#A3E635">"SELECT *"</tspan>
        <tspan fill="#F8FAFC">)</tspan>
      </text>

      <!-- Line 7 -->
      <text x="14" y="122" fill="#374151">7</text>
      <text x="36" y="122">
        <tspan fill="#F8FAFC">pivot </tspan>
        <tspan fill="#A3E635">= </tspan>
        <tspan fill="#38BDF8">df</tspan>
        <tspan fill="#F8FAFC">.</tspan>
        <tspan fill="#60A5FA">pivot_table</tspan>
        <tspan fill="#F8FAFC">(</tspan>
      </text>

      <!-- Line 8 -->
      <text x="14" y="140" fill="#374151">8</text>
      <text x="36" y="140">
        <tspan fill="#F8FAFC">    values</tspan>
        <tspan fill="#A3E635">=</tspan>
        <tspan fill="#A3E635">"revenue"</tspan>
        <tspan fill="#F8FAFC">,</tspan>
      </text>

      <!-- Line 9 -->
      <text x="14" y="158" fill="#374151">9</text>
      <text x="36" y="158">
        <tspan fill="#F8FAFC">    index</tspan>
        <tspan fill="#A3E635">=</tspan>
        <tspan fill="#A3E635">"category"</tspan>
        <tspan fill="#F8FAFC">,</tspan>
      </text>

      <!-- Line 10 -->
      <text x="14" y="176" fill="#374151">10</text>
      <text x="36" y="176">
        <tspan fill="#F8FAFC">    aggfunc</tspan>
        <tspan fill="#A3E635">=</tspan>
        <tspan fill="#A3E635">"sum"</tspan>
        <tspan fill="#F8FAFC">)</tspan>
      </text>

      <!-- Line 11 blank -->
      <text x="14" y="194" fill="#374151">11</text>

      <!-- Line 12 -->
      <text x="14" y="212" fill="#374151">12</text>
      <text x="36" y="212">
        <tspan fill="#F8FAFC">model </tspan>
        <tspan fill="#A3E635">= </tspan>
        <tspan fill="#60A5FA">RecommendEngine</tspan>
        <tspan fill="#F8FAFC">()</tspan>
      </text>

      <!-- Line 13 -->
      <text x="14" y="230" fill="#374151">13</text>
      <text x="36" y="230">
        <tspan fill="#F8FAFC">scores </tspan>
        <tspan fill="#A3E635">= </tspan>
        <tspan fill="#F8FAFC">model.</tspan>
        <tspan fill="#60A5FA">fit</tspan>
        <tspan fill="#F8FAFC">(df)</tspan>
      </text>

      <!-- Line 14 blank -->
      <text x="14" y="248" fill="#374151">14</text>

      <!-- Line 15 print -->
      <text x="14" y="266" fill="#374151">15</text>
      <text x="36" y="266">
        <tspan fill="#38BDF8">print</tspan>
        <tspan fill="#F8FAFC">(</tspan>
        <tspan fill="#A3E635">"✅ Accuracy: 96.4%"</tspan>
        <tspan fill="#F8FAFC">)</tspan>
        <tspan fill="#00F0FF" class="cursor-blink">▌</tspan>
      </text>

    </g>

    <!-- Status bar at bottom of code window -->
    <g transform="translate(0, 334)">
      <rect width="296" height="34" rx="14" fill="rgba(30, 41, 59, 0.9)"/>
      <rect y="0" width="296" height="20" fill="rgba(30, 41, 59, 0.9)"/>
      <circle cx="16" cy="17" r="4" fill="#10B981"/>
      <text x="28" y="21" font-family="monospace" font-size="9.5" fill="#94A3B8">Python 3.11  •  pandas 2.1  •  sklearn ✓</text>
    </g>
  </g>

</svg>'''

output_path = r"c:\Users\altaf\Desktop\ialtaf14\assets\hero.svg"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(hero_svg_content)

# Also copy to ialtaf14-main
output_path2 = r"c:\Users\altaf\Desktop\ialtaf14\ialtaf14-main\assets\hero.svg"
with open(output_path2, "w", encoding="utf-8") as f:
    f.write(hero_svg_content)

print(f"Done! hero.svg size: {os.path.getsize(output_path)} bytes")
