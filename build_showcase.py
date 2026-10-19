import os
import base64

# Read logo base64
logo_path = r'C:\Users\Amruthreddy\.gemini\antigravity\scratch\cocrew-workspace\cocrew-workspace-logo.jpg'
with open(logo_path, 'rb') as f:
    b64_logo = base64.b64encode(f.read()).decode('utf-8')
data_uri = f'data:image/jpeg;base64,{b64_logo}'

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CO CREW WORKSPACE - Header & Navigation Showcase</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    :root {{
      --cc-canvas: #070708;
      --cc-surface-glass: rgba(10, 10, 12, 0.76);
      --cc-surface-glass-scrolled: rgba(7, 7, 9, 0.92);
      --cc-red: #FF1E27;
      --cc-red-glow: rgba(255, 30, 39, 0.22);
      --cc-red-glow-strong: rgba(255, 30, 39, 0.5);
      --cc-text-primary: #FFFFFF;
      --cc-text-muted: #9CA3AF;
      --cc-divider: rgba(255, 255, 255, 0.08);
    }}

    /* Ambient dark backdrop inside card */
    .showcase-stage {{
      background-color: var(--cc-canvas);
      background-image: 
        radial-gradient(circle at 50% 30px, rgba(255, 30, 39, 0.12) 0%, transparent 65%),
        radial-gradient(circle at 90% 80px, rgba(255, 30, 39, 0.05) 0%, transparent 45%),
        linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
      background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
    }}

    /* Header Bar Simulation */
    .preview-navbar {{
      background: var(--cc-surface-glass);
      backdrop-filter: blur(18px) saturate(180%);
      -webkit-backdrop-filter: blur(18px) saturate(180%);
      border-bottom: 1px solid var(--cc-divider);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }}

    .preview-navbar.scrolled {{
      background: var(--cc-surface-glass-scrolled);
      backdrop-filter: blur(24px) saturate(200%);
      box-shadow: 0 16px 36px -10px rgba(0, 0, 0, 0.8),
                  0 0 1px 1px rgba(255, 255, 255, 0.04);
    }}

    /* Refined top hairline reflection */
    .preview-navbar::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 1px;
      background: linear-gradient(90deg, 
        rgba(255, 255, 255, 0) 0%, 
        rgba(255, 255, 255, 0.12) 20%, 
        rgba(255, 30, 39, 0.35) 50%, 
        rgba(255, 255, 255, 0.12) 80%, 
        rgba(255, 255, 255, 0) 100%
      );
      pointer-events: none;
    }}

    /* Outlined Red CTA Button */
    .preview-btn-service {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 7px;
      padding: 9px 20px;
      font-size: 12.5px;
      font-weight: 600;
      letter-spacing: 0.045em;
      text-transform: uppercase;
      color: #FFFFFF;
      background: rgba(255, 30, 39, 0.06);
      border: 1.5px solid var(--cc-red);
      border-radius: 9999px;
      cursor: pointer;
      box-shadow: 0 0 16px var(--cc-red-glow);
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      user-select: none;
    }}

    .preview-btn-service:hover {{
      background: var(--cc-red);
      color: #FFFFFF;
      box-shadow: 0 0 24px var(--cc-red-glow-strong);
      transform: translateY(-1px);
    }}

    .preview-btn-service:active {{
      transform: translateY(0) scale(0.97);
    }}

    /* Active Nav Link with glowing ruby dot */
    .preview-nav-link {{
      position: relative;
      font-size: 13.5px;
      font-weight: 500;
      letter-spacing: 0.035em;
      color: var(--cc-text-muted);
      cursor: pointer;
      padding: 6px 4px;
      transition: color 0.2s ease;
      user-select: none;
    }}

    .preview-nav-link:hover {{
      color: #FFFFFF;
    }}

    .preview-nav-link.active {{
      color: #FFFFFF;
      font-weight: 600;
    }}

    .preview-nav-link.active::after {{
      content: "";
      position: absolute;
      bottom: -3px;
      left: 50%;
      transform: translateX(-50%);
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background-color: var(--cc-red);
      box-shadow: 0 0 8px 1.5px var(--cc-red);
      animation: pulse-ruby 2.5s infinite ease-in-out;
    }}

    @keyframes pulse-ruby {{
      0%, 100% {{ opacity: 0.85; transform: translateX(-50%) scale(1); }}
      50% {{ opacity: 1; transform: translateX(-50%) scale(1.2); box-shadow: 0 0 12px 2.5px var(--cc-red); }}
    }}

    /* Logo link */
    .preview-logo-img {{
      height: 38px;
      width: auto;
      object-fit: contain;
      filter: drop-shadow(0 0 8px rgba(0, 0, 0, 0.7));
      transition: filter 0.25s ease, transform 0.25s ease;
    }}

    .preview-logo-img:hover {{
      filter: drop-shadow(0 0 14px rgba(255, 30, 39, 0.35));
      transform: translateY(-0.5px);
    }}
  </style>
</head>
<body class="bg-transparent text-[var(--foreground)] antialiased p-3 sm:p-5 font-sans">

  <!-- Main Card Shell -->
  <div class="bg-[var(--card)] text-[var(--foreground)] border border-[var(--border)] rounded-2xl p-4 sm:p-6 shadow-2xl overflow-hidden max-w-5xl mx-auto space-y-6">
    
    <!-- Top Bar: Header & Controls -->
    <div class="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-[var(--border)]">
      <div>
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-[#FF1E27] animate-ping"></span>
          <h2 class="text-[var(--foreground)] font-bold text-base sm:text-lg tracking-tight">
            CO CREW WORKSPACE
          </h2>
          <span class="text-xs font-semibold px-2 py-0.5 rounded-full bg-[#FF1E27]/10 text-[#FF1E27] border border-[#FF1E27]/30 uppercase tracking-wider">
            Header & Navigation
          </span>
        </div>
        <p class="text-[var(--muted-foreground)] text-xs mt-0.5">
          Refined fusion: Minimalism (Usability) · Maximalism (Contrast) · Glassmorphism (Depth)
        </p>
      </div>

      <!-- Interactive Controls -->
      <div class="flex items-center gap-2 flex-wrap">
        <!-- Viewport Mode -->
        <div class="bg-black/20 p-0.5 rounded-lg border border-[var(--border)] flex items-center text-xs">
          <button id="btn-mode-desktop" class="px-2.5 py-1 rounded-md font-medium text-white bg-[#FF1E27]/80 shadow-sm transition-all" onclick="setMode('desktop')">
            Desktop (1280px)
          </button>
          <button id="btn-mode-mobile" class="px-2.5 py-1 rounded-md font-medium text-[var(--muted-foreground)] hover:text-white transition-all" onclick="setMode('mobile')">
            Mobile (390px)
          </button>
        </div>

        <!-- Glass Tint Toggle -->
        <button id="btn-toggle-scroll" class="px-2.5 py-1 rounded-lg border border-[var(--border)] text-xs font-medium hover:bg-white/5 transition-all flex items-center gap-1.5" onclick="toggleGlassScroll()">
          <span id="scroll-status-dot" class="w-1.5 h-1.5 rounded-full bg-zinc-400"></span>
          <span id="scroll-status-text">Simulate Scroll</span>
        </button>

        <!-- Inspector Toggle -->
        <button id="btn-toggle-spec" class="px-2.5 py-1 rounded-lg border border-[var(--border)] text-xs font-medium text-[var(--muted-foreground)] hover:text-white hover:bg-white/5 transition-all" onclick="toggleInspector()">
          Design Specs
        </button>
      </div>
    </div>

    <!-- PREVIEW STAGE CONTAINER -->
    <div id="preview-stage-wrapper" class="relative transition-all duration-300 w-full flex justify-center">
      
      <div id="preview-container" class="w-full rounded-xl overflow-hidden border border-white/10 shadow-2xl showcase-stage transition-all duration-300 relative min-h-[340px] flex flex-col justify-between">
        
        <!-- ================================================================
             DESKTOP / MOBILE RESPONSIVE NAVBAR
             ================================================================ -->
        <div id="navbar-root" class="preview-navbar w-full">
          <div class="max-w-7xl mx-auto h-[74px] px-4 sm:px-8 flex items-center justify-between">
            
            <!-- LEFT: ORIGINAL CO CREW WORKSPACE LOGO -->
            <div class="flex-shrink-0 flex items-center">
              <a href="#home" class="inline-flex items-center group" title="CO CREW WORKSPACE">
                <img src="{data_uri}" alt="CO CREW WORKSPACE" class="preview-logo-img">
              </a>
            </div>

            <!-- CENTRE: NAVIGATION (DESKTOP) -->
            <div id="nav-links-desktop" class="hidden lg:flex items-center gap-7">
              <span class="preview-nav-link active" onclick="selectNav('home', this)">Home</span>
              <span class="preview-nav-link" onclick="selectNav('services', this)">Services</span>
              <span class="preview-nav-link" onclick="selectNav('store', this)">Digital Store</span>
              <span class="preview-nav-link" onclick="selectNav('about', this)">About</span>
              <span class="preview-nav-link" onclick="selectNav('contact', this)">Contact</span>
            </div>

            <!-- RIGHT: OUTLINED RED \"REQUEST A SERVICE\" BUTTON -->
            <div class="flex items-center gap-3">
              <button class="preview-btn-service" onclick="triggerCtaToast()">
                <span>Request a Service</span>
                <svg class="w-3 h-3" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M3.33334 8H12.6667M12.6667 8L8.66667 4M12.6667 8L8.66667 12" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>

              <!-- Mobile Hamburger Trigger -->
              <button id="mobile-trigger-btn" class="lg:hidden w-9 h-9 rounded-lg bg-white/5 border border-white/10 flex items-center justify-center text-white hover:bg-white/10 transition-all" onclick="toggleMobileDrawer()">
                <svg id="mobile-ham-svg" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7h16M4 17h16"/>
                </svg>
              </button>
            </div>

          </div>

          <!-- Mobile Drawer Container -->
          <div id="preview-mobile-drawer" class="hidden flex-col bg-[#08080A]/95 backdrop-blur-2xl border-b border-white/10 px-5 py-4 space-y-3">
            <div class="flex flex-col gap-1.5">
              <div class="px-3 py-2 rounded-lg bg-white/5 text-white font-semibold text-sm flex items-center justify-between border-l-2 border-[#FF1E27]" onclick="selectMobileNav('home')">
                <span>Home</span>
                <span class="w-1.5 h-1.5 rounded-full bg-[#FF1E27] shadow-[0_0_8px_#FF1E27]"></span>
              </div>
              <div class="px-3 py-2 rounded-lg hover:bg-white/5 text-zinc-400 hover:text-white font-medium text-sm flex items-center justify-between transition-all" onclick="selectMobileNav('services')">
                <span>Services</span>
                <span class="text-[11px] text-zinc-600">01-06</span>
              </div>
              <div class="px-3 py-2 rounded-lg hover:bg-white/5 text-zinc-400 hover:text-white font-medium text-sm flex items-center justify-between transition-all" onclick="selectMobileNav('store')">
                <span>Digital Store</span>
                <span class="text-[11px] text-zinc-600">Catalog</span>
              </div>
              <div class="px-3 py-2 rounded-lg hover:bg-white/5 text-zinc-400 hover:text-white font-medium text-sm transition-all" onclick="selectMobileNav('about')">
                <span>About</span>
              </div>
              <div class="px-3 py-2 rounded-lg hover:bg-white/5 text-zinc-400 hover:text-white font-medium text-sm transition-all" onclick="selectMobileNav('contact')">
                <span>Contact</span>
              </div>
            </div>
            <div class="pt-2 border-t border-white/10">
              <button class="preview-btn-service w-full justify-center py-2.5 text-xs" onclick="triggerCtaToast()">
                <span>Request a Service</span>
                <svg class="w-3.5 h-3.5" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M3.33334 8H12.6667M12.6667 8L8.66667 4M12.6667 8L8.66667 12" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Ambient Dark Canvas Showcase (Strictly No Hero/Cards/Dashboard) -->
        <div class="p-6 text-center space-y-2 relative z-10 flex flex-col items-center justify-center my-auto">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-white/10 bg-white/5 backdrop-blur-md text-xs text-zinc-400">
            <span class="w-1.5 h-1.5 rounded-full bg-[#FF1E27]"></span>
            <span id="active-nav-label">Active View: Home</span>
          </div>
          <p class="text-xs text-zinc-500 max-w-sm">
            Header floats over deep obsidian canvas with translucent dark glass, 18px backdrop blur, delicate specular top hairline, and sharp contrast.
          </p>
        </div>

        <!-- Notification Toast -->
        <div id="cta-toast" class="absolute bottom-4 left-1/2 transform -translate-x-1/2 bg-black/90 border border-[#FF1E27]/50 text-white text-xs px-4 py-2 rounded-full shadow-[0_0_20px_rgba(255,30,39,0.35)] opacity-0 pointer-events-none transition-all duration-300 z-50 flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-[#FF1E27]"></span>
          <span>"Request a Service" action triggered successfully.</span>
        </div>

      </div>
    </div>

    <!-- DESIGN SPECIFICATIONS & ARCHITECTURE ACCORDION -->
    <div id="inspector-panel" class="hidden pt-4 border-t border-[var(--border)] space-y-4 text-xs">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
        
        <!-- 1. MINIMALISM -->
        <div class="p-3.5 rounded-xl bg-black/30 border border-white/5 space-y-1.5">
          <div class="flex items-center gap-2 font-semibold text-white">
            <span class="w-2 h-2 rounded-full bg-white"></span>
            <span>Minimalism (Clarity)</span>
          </div>
          <p class="text-[var(--muted-foreground)] leading-relaxed">
            • Compact 74px height with zero visual clutter.<br>
            • Centred 5-item navigation hierarchy.<br>
            • Clear, unambiguous labelling.<br>
            • Ample breathing room and strict horizontal alignment.
          </p>
        </div>

        <!-- 2. MAXIMALISM -->
        <div class="p-3.5 rounded-xl bg-black/30 border border-white/5 space-y-1.5">
          <div class="flex items-center gap-2 font-semibold text-[#FF1E27]">
            <span class="w-2 h-2 rounded-full bg-[#FF1E27]"></span>
            <span>Maximalism (Expression)</span>
          </div>
          <p class="text-[var(--muted-foreground)] leading-relaxed">
            • Preserves authentic raw brushwork logo.<br>
            • Piercing contrast: #070708 canvas vs #FFFFFF text.<br>
            • Confident #FF1E27 outlined CTA button with hover fill.<br>
            • Luminous ruby pulse on active navigation states.
          </p>
        </div>

        <!-- 3. GLASSMORPHISM -->
        <div class="p-3.5 rounded-xl bg-black/30 border border-white/5 space-y-1.5">
          <div class="flex items-center gap-2 font-semibold text-zinc-300">
            <span class="w-2 h-2 rounded-full bg-zinc-400"></span>
            <span>Glassmorphism (Depth)</span>
          </div>
          <p class="text-[var(--muted-foreground)] leading-relaxed">
            • Surface: rgba(10,10,12, 0.76) dark obsidian tint.<br>
            • 18px backdrop-filter blur + 180% saturation.<br>
            • Subtle top specular hairline with gradient red bleed.<br>
            • Razor-thin 1px bottom divider line (rgba(255,255,255,0.08)).
          </p>
        </div>

      </div>

      <!-- Token Quick Reference -->
      <div class="p-3 rounded-xl bg-black/20 border border-white/5 flex flex-wrap items-center justify-between gap-2 text-[11px] text-[var(--muted-foreground)]">
        <div><strong>Canvas:</strong> #070708</div>
        <div><strong>Brand Red:</strong> #FF1E27</div>
        <div><strong>Text High-Contrast:</strong> #FFFFFF</div>
        <div><strong>Text Inactive:</strong> #9CA3AF</div>
        <div><strong>Divider:</strong> 1px solid rgba(255,255,255,0.08)</div>
        <div><strong>Height:</strong> 74px Desktop / 68px Mobile</div>
      </div>
    </div>

  </div>

  <!-- Interactive Script -->
  <script>
    let currentMode = 'desktop';
    let isScrolled = false;
    let isDrawerOpen = false;
    let isInspectorOpen = false;

    function setMode(mode) {{
      currentMode = mode;
      const container = document.getElementById('preview-container');
      const btnDesk = document.getElementById('btn-mode-desktop');
      const btnMob = document.getElementById('btn-mode-mobile');
      const desktopNav = document.getElementById('nav-links-desktop');
      const mobileTrigger = document.getElementById('mobile-trigger-btn');
      const mobileDrawer = document.getElementById('preview-mobile-drawer');

      if (mode === 'mobile') {{
        container.style.maxWidth = '390px';
        btnMob.className = 'px-2.5 py-1 rounded-md font-medium text-white bg-[#FF1E27]/80 shadow-sm transition-all';
        btnDesk.className = 'px-2.5 py-1 rounded-md font-medium text-[var(--muted-foreground)] hover:text-white transition-all';
        desktopNav.classList.add('hidden');
        desktopNav.classList.remove('lg:flex');
        mobileTrigger.classList.remove('lg:hidden');
      }} else {{
        container.style.maxWidth = '100%';
        btnDesk.className = 'px-2.5 py-1 rounded-md font-medium text-white bg-[#FF1E27]/80 shadow-sm transition-all';
        btnMob.className = 'px-2.5 py-1 rounded-md font-medium text-[var(--muted-foreground)] hover:text-white transition-all';
        desktopNav.classList.remove('hidden');
        desktopNav.classList.add('lg:flex');
        mobileTrigger.classList.add('lg:hidden');
        mobileDrawer.classList.add('hidden');
        mobileDrawer.classList.remove('flex');
        isDrawerOpen = false;
      }}
    }}

    function toggleGlassScroll() {{
      isScrolled = !isScrolled;
      const nav = document.getElementById('navbar-root');
      const dot = document.getElementById('scroll-status-dot');
      const text = document.getElementById('scroll-status-text');

      if (isScrolled) {{
        nav.classList.add('scrolled');
        dot.className = 'w-1.5 h-1.5 rounded-full bg-[#FF1E27] shadow-[0_0_6px_#FF1E27]';
        text.innerText = 'Scrolled Glass (Dense)';
      }} else {{
        nav.classList.remove('scrolled');
        dot.className = 'w-1.5 h-1.5 rounded-full bg-zinc-400';
        text.innerText = 'Simulate Scroll';
      }}
    }}

    function toggleInspector() {{
      isInspectorOpen = !isInspectorOpen;
      const panel = document.getElementById('inspector-panel');
      const btn = document.getElementById('btn-toggle-spec');
      if (isInspectorOpen) {{
        panel.classList.remove('hidden');
        btn.classList.add('text-white', 'bg-white/10');
      }} else {{
        panel.classList.add('hidden');
        btn.classList.remove('text-white', 'bg-white/10');
      }}
    }}

    function selectNav(item, element) {{
      document.querySelectorAll('.preview-nav-link').forEach(el => el.classList.remove('active'));
      element.classList.add('active');
      document.getElementById('active-nav-label').innerText = 'Active View: ' + element.innerText;
    }}

    function selectMobileNav(item) {{
      const labels = {{
        'home': 'Home',
        'services': 'Services',
        'store': 'Digital Store',
        'about': 'About',
        'contact': 'Contact'
      }};
      document.getElementById('active-nav-label').innerText = 'Active View: ' + (labels[item] || item);
      toggleMobileDrawer();
    }}

    function toggleMobileDrawer() {{
      const drawer = document.getElementById('preview-mobile-drawer');
      const svg = document.getElementById('mobile-ham-svg');
      isDrawerOpen = !isDrawerOpen;

      if (isDrawerOpen) {{
        drawer.classList.remove('hidden');
        drawer.classList.add('flex');
        svg.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>';
      }} else {{
        drawer.classList.add('hidden');
        drawer.classList.remove('flex');
        svg.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7h16M4 17h16"/>';
      }}
    }}

    function triggerCtaToast() {{
      const toast = document.getElementById('cta-toast');
      toast.classList.remove('opacity-0', 'pointer-events-none');
      toast.classList.add('opacity-100');
      setTimeout(() => {{
        toast.classList.remove('opacity-100');
        toast.classList.add('opacity-0', 'pointer-events-none');
      }}, 2500);
    }}
  </script>
</body>
</html>
"""

target_file = r'C:\Users\Amruthreddy\.gemini\antigravity\brain\e685e2a3-f5ae-4d21-9ab3-8c988c8a310a\header_navigation_showcase.html'
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Saved showcase artifact HTML successfully to:', target_file)
