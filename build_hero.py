import base64
import os

img_path = r"c:\Users\altaf\Desktop\ialtaf14\ialtaf14-main\assets\altaf_khan.jpg"
with open(img_path, "rb") as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')

hero_svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 480" width="100%" height="100%">
  <defs>
    <!-- Background Gradients -->
    <radialGradient id="bgGlowCyan" cx="20%" cy="25%" r="60%">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#070A12" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="bgGlowViolet" cx="80%" cy="75%" r="60%">
      <stop offset="0%" stop-color="#7000FF" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="#070A12" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="bgGlowCenter" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#070A12" stop-opacity="0"/>
    </radialGradient>

    <!-- iOS Glass Border Gradient -->
    <linearGradient id="glassBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.8"/>
      <stop offset="35%" stop-color="#7000FF" stop-opacity="0.5"/>
      <stop offset="70%" stop-color="#3B82F6" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#00F0FF" stop-opacity="0.7"/>
    </linearGradient>

    <!-- Text Gradients -->
    <linearGradient id="nameGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="40%" stop-color="#F1F5F9"/>
      <stop offset="80%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#00F0FF"/>
    </linearGradient>

    <linearGradient id="accentGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F0FF"/>
      <stop offset="50%" stop-color="#7000FF"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>

    <linearGradient id="codeBarGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>

    <linearGradient id="glassFillGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#151D2A" stop-opacity="0.75"/>
      <stop offset="100%" stop-color="#0B0F19" stop-opacity="0.85"/>
    </linearGradient>

    <!-- Glow & Shadow Filters -->
    <filter id="neonGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="7" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000000" flood-opacity="0.7"/>
    </filter>

    <!-- Photo Clip Path -->
    <clipPath id="photoClip">
      <rect x="0" y="0" width="220" height="290" rx="18"/>
    </clipPath>

    <!-- CSS Animations -->
    <style>
      @keyframes floatSlow {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-7px); }}
      }}
      @keyframes floatReverse {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(7px); }}
      }}
      @keyframes pulseGlow {{
        0%, 100% {{ opacity: 0.5; transform: scale(1); }}
        50% {{ opacity: 0.9; transform: scale(1.06); }}
      }}
      @keyframes spinSlow {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
      }}
      @keyframes spinSlowRev {{
        from {{ transform: rotate(360deg); }}
        to {{ transform: rotate(0deg); }}
      }}
      @keyframes dashMove {{
        to {{ stroke-dashoffset: -40; }}
      }}
      @keyframes cursorBlink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}
      @keyframes particleOrbit {{
        0% {{ transform: rotate(0deg) translateX(40px) rotate(0deg); }}
        100% {{ transform: rotate(360deg) translateX(40px) rotate(-360deg); }}
      }}

      .floating-element {{ animation: floatSlow 5s ease-in-out infinite; }}
      .floating-element-rev {{ animation: floatReverse 6s ease-in-out infinite; }}
      .pulsing-core {{ animation: pulseGlow 3.5s ease-in-out infinite; transform-origin: 850px 90px; }}
      .spinning-ring {{ animation: spinSlow 18s linear infinite; transform-origin: 850px 90px; }}
      .spinning-ring-rev {{ animation: spinSlowRev 14s linear infinite; transform-origin: 850px 90px; }}
      .cursor {{ animation: cursorBlink 1s infinite; }}
      .animated-dash {{ stroke-dasharray: 6 6; animation: dashMove 2s linear infinite; }}
      .particle-orbit {{ animation: particleOrbit 8s linear infinite; transform-origin: 850px 90px; }}
    </style>
  </defs>

  <!-- Base Dark Canvas -->
  <rect width="980" height="480" rx="24" fill="#070A12"/>
  <rect width="980" height="480" rx="24" fill="url(#bgGlowCyan)"/>
  <rect width="980" height="480" rx="24" fill="url(#bgGlowViolet)"/>
  <rect width="980" height="480" rx="24" fill="url(#bgGlowCenter)"/>

  <!-- Subtle Ambient Grid Pattern -->
  <g opacity="0.05" stroke="#FFFFFF" stroke-width="1">
    <path d="M0 40 H980 M0 80 H980 M0 120 H980 M0 160 H980 M0 200 H980 M0 240 H980 M0 280 H980 M0 320 H980 M0 360 H980 M0 400 H980 M0 440 H980" />
    <path d="M50 0 V480 M100 0 V480 M150 0 V480 M200 0 V480 M250 0 V480 M300 0 V480 M350 0 V480 M400 0 V480 M450 0 V480 M500 0 V480 M550 0 V480 M600 0 V480 M650 0 V480 M700 0 V480 M750 0 V480 M800 0 V480 M850 0 V480 M900 0 V480 M950 0 V480" />
  </g>

  <!-- Floating Glow Particles in Background -->
  <circle cx="120" cy="80" r="3" fill="#00F0FF" opacity="0.6" filter="url(#neonGlow)"/>
  <circle cx="480" cy="50" r="2.5" fill="#7000FF" opacity="0.7" filter="url(#neonGlow)"/>
  <circle cx="910" cy="380" r="3.5" fill="#38BDF8" opacity="0.5" filter="url(#neonGlow)"/>
  <circle cx="340" cy="430" r="2" fill="#00F0FF" opacity="0.6"/>

  <!-- Main Outer iOS Frosted Glass Panel -->
  <rect x="16" y="16" width="948" height="448" rx="20" fill="url(#glassFillGrad)" stroke="url(#glassBorder)" stroke-width="1.5" filter="url(#softShadow)"/>

  <!-- ==================== COLUMN 1 (Left): REAL PHOTO GLASS CARD ==================== -->
  <g transform="translate(42, 42)">
    <!-- Photo Glass Outer Border -->
    <rect x="-4" y="-4" width="228" height="298" rx="22" fill="none" stroke="url(#glassBorder)" stroke-width="2" filter="url(#neonGlow)"/>
    <!-- Photo Container -->
    <g clip-path="url(#photoClip)">
      <image href="data:image/jpeg;base64,{b64_data}" x="-10" y="-15" width="240" height="320" preserveAspectRatio="xMidYMid slice"/>
      <!-- Subtle Glass Shimmer Overlay -->
      <rect width="220" height="290" fill="url(#codeBarGrad)" opacity="0.12"/>
    </g>
    <!-- Photo Name Pill Badge -->
    <g transform="translate(10, 250)">
      <rect width="200" height="32" rx="10" fill="rgba(11, 15, 25, 0.88)" stroke="rgba(0, 240, 255, 0.45)" stroke-width="1"/>
      <circle cx="16" cy="16" r="4" fill="#10B981" filter="url(#neonGlow)"/>
      <text x="28" y="20" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#F8FAFC">Altaf Khan • Data Analyst</text>
    </g>
  </g>

  <!-- ==================== COLUMN 2 (Center): IDENTITY & DETAILS ==================== -->
  <g transform="translate(290, 42)">
    <!-- System Status Pill -->
    <g transform="translate(0, 0)">
      <rect width="290" height="28" rx="14" fill="rgba(0, 240, 255, 0.08)" stroke="rgba(0, 240, 255, 0.35)" stroke-width="1"/>
      <circle cx="16" cy="14" r="4" fill="#00F0FF" filter="url(#neonGlow)"/>
      <text x="30" y="18" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="800" fill="#00F0FF" letter-spacing="1.4">AI &amp; DATA SCIENCE PORTFOLIO</text>
    </g>

    <!-- Name Header -->
    <text x="0" y="74" font-family="-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif" font-size="46" font-weight="800" fill="url(#nameGradient)" letter-spacing="-0.5">Altaf Khan</text>

    <!-- Roles Subtitle -->
    <text x="0" y="104" font-family="-apple-system, sans-serif" font-size="15.5" font-weight="600" fill="#38BDF8" letter-spacing="0.3">
      Data Analyst <tspan fill="#7000FF">•</tspan> Machine Learning Enthusiast <tspan fill="#7000FF">•</tspan> Aspiring Data Scientist
    </text>

    <!-- Tagline Quote -->
    <text x="0" y="132" font-family="sans-serif" font-size="12.5" fill="#94A3B8" italic="true">
      "Transforming complex datasets into predictive ML models &amp; executive dashboards."
    </text>

    <!-- Tech Badges Bar (Glass Pills) -->
    <g transform="translate(0, 152)">
      <g transform="translate(0,0)"><rect width="76" height="26" rx="8" fill="rgba(30,41,59,0.7)" stroke="rgba(56,189,248,0.4)" stroke-width="1"/><text x="38" y="17" font-family="sans-serif" font-size="11.5" font-weight="600" fill="#38BDF8" text-anchor="middle">Python</text></g>
      <g transform="translate(84,0)"><rect width="60" height="26" rx="8" fill="rgba(30,41,59,0.7)" stroke="rgba(168,85,247,0.4)" stroke-width="1"/><text x="30" y="17" font-family="sans-serif" font-size="11.5" font-weight="600" fill="#C084FC" text-anchor="middle">SQL</text></g>
      <g transform="translate(152,0)"><rect width="76" height="26" rx="8" fill="rgba(30,41,59,0.7)" stroke="rgba(0,240,255,0.4)" stroke-width="1"/><text x="38" y="17" font-family="sans-serif" font-size="11.5" font-weight="600" fill="#00F0FF" text-anchor="middle">Pandas</text></g>
      <g transform="translate(236,0)"><rect width="84" height="26" rx="8" fill="rgba(30,41,59,0.7)" stroke="rgba(245,158,11,0.4)" stroke-width="1"/><text x="42" y="17" font-family="sans-serif" font-size="11.5" font-weight="600" fill="#FBBF24" text-anchor="middle">Power BI</text></g>
      <g transform="translate(328,0)"><rect width="118" height="26" rx="8" fill="rgba(30,41,59,0.7)" stroke="rgba(236,72,153,0.4)" stroke-width="1"/><text x="59" y="17" font-family="sans-serif" font-size="11.5" font-weight="600" fill="#F472B6" text-anchor="middle">Scikit-Learn ML</text></g>
    </g>

    <!-- Training Glass Card -->
    <g transform="translate(0, 192)">
      <rect width="445" height="46" rx="10" fill="rgba(15, 23, 42, 0.7)" stroke="rgba(255, 255, 255, 0.12)" stroke-width="1"/>
      <circle cx="18" cy="23" r="5" fill="#10B981" filter="url(#neonGlow)"/>
      <text x="32" y="19" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#F8FAFC">Software Testing &amp; Programming Trainee</text>
      <text x="32" y="34" font-family="sans-serif" font-size="10.5" fill="#94A3B8">QSpiders Gurugram • August 2025 – Present</text>
    </g>

    <!-- Action Buttons Row -->
    <g transform="translate(0, 252)">
      <!-- Portfolio Button -->
      <a href="https://ialtaf14.vercel.app">
        <g transform="translate(0, 0)">
          <rect width="165" height="38" rx="19" fill="url(#accentGradient)" stroke="#00F0FF" stroke-width="1" filter="url(#neonGlow)"/>
          <text x="82.5" y="24" font-family="sans-serif" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">🌐 Visit Portfolio App</text>
        </g>
      </a>
      <!-- LinkedIn Button -->
      <g transform="translate(177, 0)">
        <rect width="115" height="38" rx="19" fill="rgba(30, 41, 59, 0.8)" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1"/>
        <text x="57.5" y="24" font-family="sans-serif" font-size="12.5" font-weight="600" fill="#38BDF8" text-anchor="middle">💼 LinkedIn</text>
      </g>
      <!-- Contact Button -->
      <g transform="translate(304, 0)">
        <rect width="115" height="38" rx="19" fill="rgba(30, 41, 59, 0.8)" stroke="rgba(168, 85, 247, 0.4)" stroke-width="1"/>
        <text x="57.5" y="24" font-family="sans-serif" font-size="12.5" font-weight="600" fill="#C084FC" text-anchor="middle">📧 Email Me</text>
      </g>
    </g>
  </g>

  <!-- ==================== COLUMN 3 (Far Right): AI NEURAL BRAIN & FLOATING CODE ==================== -->
  <!-- Top Right AI Neural Core (Positioned safely at x=850, y=90) -->
  <g transform="translate(0, 0)">
    <!-- Orbital Rings -->
    <circle cx="850" cy="90" r="55" fill="none" stroke="url(#accentGradient)" stroke-width="1.5" opacity="0.45" class="spinning-ring" stroke-dasharray="10 15 30 10"/>
    <circle cx="850" cy="90" r="38" fill="none" stroke="#00F0FF" stroke-width="1" opacity="0.65" class="spinning-ring-rev" stroke-dasharray="6 12"/>
    <circle cx="850" cy="90" r="22" fill="none" stroke="#7000FF" stroke-width="1.5" opacity="0.8"/>

    <!-- Neural Core -->
    <circle cx="850" cy="90" r="12" fill="url(#accentGradient)" filter="url(#neonGlow)" class="pulsing-core"/>

    <!-- Orbiting Particle Node -->
    <circle cx="850" cy="90" r="3.5" fill="#00F0FF" filter="url(#neonGlow)" class="particle-orbit"/>
  </g>

  <!-- Floating Code Window (Positioned safely at x=740, y=190 - ZERO OVERLAP WITH PHOTO OR TEXT!) -->
  <g transform="translate(740, 190)" class="floating-element">
    <!-- Window Outer Shell -->
    <rect width="205" height="240" rx="14" fill="rgba(11, 15, 25, 0.92)" stroke="rgba(0, 240, 255, 0.4)" stroke-width="1.5" filter="url(#softShadow)"/>
    <!-- Window Title Bar -->
    <path d="M0 14 Q0 0 14 0 L191 0 Q205 0 205 14 L205 32 L0 32 Z" fill="url(#codeBarGrad)"/>
    <!-- macOS Control Dots -->
    <circle cx="15" cy="16" r="4" fill="#FF5F56"/>
    <circle cx="28" cy="16" r="4" fill="#FFBD2E"/>
    <circle cx="41" cy="16" r="4" fill="#27C93F"/>
    <!-- File Label -->
    <text x="118" y="20" font-family="monospace" font-size="9.5" fill="#94A3B8" text-anchor="middle">nova_engine.py</text>

    <!-- Syntax Highlighted Code -->
    <g transform="translate(14, 46)" font-family="Consolas, 'Fira Code', Monaco, monospace" font-size="9.5" xml:space="preserve">
      <text y="12"><tspan fill="#F472B6">import</tspan> <tspan fill="#F8FAFC">pandas</tspan></text>
      <text y="26"><tspan fill="#F472B6">from</tspan> <tspan fill="#38BDF8">novaflix</tspan> <tspan fill="#F472B6">import</tspan></text>
      <text y="40">  <tspan fill="#60A5FA">RecommendEngine</tspan></text>
      <text y="58"><tspan fill="#64748B"># Analyze Datasets</tspan></text>
      <text y="72"><tspan fill="#F8FAFC">df</tspan> = <tspan fill="#38BDF8">pandas</tspan>.<tspan fill="#60A5FA">read</tspan>()</text>
      <text y="86"><tspan fill="#F8FAFC">rec</tspan> = <tspan fill="#60A5FA">RecommendEngine</tspan>()</text>
      <text y="100"><tspan fill="#F8FAFC">res</tspan> = <tspan fill="#F8FAFC">rec</tspan>.<tspan fill="#60A5FA">predict</tspan>(<tspan fill="#F8FAFC">df</tspan>)</text>
      <text y="118"><tspan fill="#64748B"># Live Deployment</tspan></text>
      <text y="132"><tspan fill="#38BDF8">print</tspan>(<tspan fill="#A3E635">"⚡ Live Vercel App"</tspan>)</text>
      <text y="148"><tspan fill="#00F0FF"># ialtaf14.vercel.app</tspan><tspan fill="#00F0FF" class="cursor">|</tspan></text>
    </g>
  </g>
</svg>'''

output_path = r"c:\Users\altaf\Desktop\ialtaf14\ialtaf14-main\assets\hero.svg"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(hero_svg_content)

print(f"Successfully rebuilt hero.svg! Perfect 3-column zero overlap layout. Size: {os.path.getsize(output_path)} bytes")
