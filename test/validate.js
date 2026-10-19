import fs from 'fs';
import path from 'path';

const projectDir = path.resolve('C:/Users/Amruthreddy/.gemini/antigravity/scratch/cocrew-workspace');
console.log('🔍 Running automated validation suite on CO CREW WORKSPACE...');

let errors = 0;
let passes = 0;

function assert(condition, message) {
  if (condition) {
    console.log(`  ✅ PASS: ${message}`);
    passes++;
  } else {
    console.error(`  ❌ FAIL: ${message}`);
    errors++;
  }
}

// 1. Check required files
console.log('\n--- Checking Project Assets & Files ---');
const requiredFiles = [
  'index.html',
  'styles.css',
  'cocrew-workspace-logo.jpg',
  'package.json',
  'vercel.json'
];

requiredFiles.forEach(file => {
  const filePath = path.join(projectDir, file);
  assert(fs.existsSync(filePath), `Required file exists: ${file}`);
});

// 2. Inspect index.html contents
console.log('\n--- Inspecting index.html Semantics & Sections ---');
const html = fs.readFileSync(path.join(projectDir, 'index.html'), 'utf8');

// Section 1: Hero
assert(html.includes('FOR CREATORS · BY CREATORS'), 'Hero contains approved eyebrow');
assert(html.includes('CREATE.') && html.includes('GROW.') && html.includes('BUILD MORE.'), 'Hero contains exact 3-line headline with punctuation');
assert(html.includes('CO CREW WORKSPACE helps creators build their brand'), 'Hero contains exact approved supporting copy');
assert(html.includes('Request a Service') && html.includes('Explore Digital Store'), 'Hero contains both primary and secondary CTAs');
assert(html.includes('hero-visual-frame'), 'Hero contains CSS-powered geometric visual frame (no AI/stock images)');

// Section 2: Six-service strip
console.log('\n--- Inspecting Six-Service Strip Order & Truthful Availability ---');
const service01 = html.indexOf('Content & Creator Solutions');
const service02 = html.indexOf('Creator Growth & Mentorship');
const service03 = html.indexOf('Creator–Editor Connect');
const service04 = html.indexOf('Portfolio & Website Development');
const service05 = html.indexOf('Digital Products');
const service06 = html.indexOf('AI Agents & Workflow Automation');

assert(service01 !== -1 && service02 > service01 && service03 > service02 && service04 > service03 && service05 > service04 && service06 > service05, 'Six services are displayed in exact required order (01 to 06)');
assert(html.includes('badge-available') && html.includes('badge-catalogue') && html.includes('badge-coming-soon'), 'Availability badges correctly distinguish Available, Catalogue, and Coming Soon');
assert(html.includes('Not Orderable — Under Development'), 'Coming Soon service is truthfully marked non-orderable');

// Section 3: Services overview
console.log('\n--- Inspecting Services Overview Content ---');
assert(html.includes('tailored to the creator\'s niche, platform, and language'), 'Service 01 copy verified');
assert(html.includes('Practical growth guidance, content reviews, and workshops'), 'Service 02 copy verified');
assert(html.includes('A human-led process in which the team reviews requirements'), 'Service 03 copy verified');
assert(html.includes('Creator portfolios, personal websites, and landing pages'), 'Service 04 copy verified');

// Section 4: Digital Store honest state
console.log('\n--- Inspecting Digital Store Honesty ---');
assert(!html.includes('discount') && !html.includes('checkout') && !html.includes('stripe'), 'No fake discounts, checkouts, or payment simulations');
assert(html.includes('In Curation') || html.includes('Catalogue In Curation'), 'Honest curation status presented');

// Section 5: How It Works
console.log('\n--- Inspecting 4-Step How It Works Workflow ---');
assert(html.includes('DISCOVER') && html.includes('SUBMIT') && html.includes('REVIEW') && html.includes('FOLLOW UP'), 'All 4 launch workflow steps present (Discover, Submit, Review, Follow up)');

// Section 6: Final Call to Action
console.log('\n--- Inspecting Final CTA ---');
assert(html.includes('YOUR NEXT CREATIVE MOVE STARTS HERE.'), 'Final CTA headline verified');
assert(html.includes('Tell us what you\'re building. Let\'s explore how CO CREW WORKSPACE can help.'), 'Final CTA supporting copy verified');

// Section 7: Footer
console.log('\n--- Inspecting Footer ---');
assert(html.includes('&copy; 2026 CO CREW WORKSPACE') || html.includes('© 2026 CO CREW WORKSPACE'), 'Footer copyright notice present');
assert(html.includes('Privacy Policy') && html.includes('Terms of Service') && html.includes('Refund Policy'), 'Policy links present in footer');

// Navigation & Modals
console.log('\n--- Inspecting Header & Request Modal Flow ---');
assert(html.includes('cc-nav-item-link') && html.includes('cc-btn-outlined-red'), 'Header has desktop row and outlined red CTA');
assert(html.includes('id="mobile-drawer"'), 'Mobile drawer component present');
assert(html.includes('id="service-request-form"') && html.includes('localStorage.setItem'), 'Request modal with local persistence logic present');

// Stylesheet check
console.log('\n--- Inspecting styles.css ---');
const css = fs.readFileSync(path.join(projectDir, 'styles.css'), 'utf8');
assert(css.includes('--cc-red: #FF1E27'), 'Brand red #FF1E27 present');
assert(css.includes('--cc-canvas: #070708'), 'Near-black canvas #070708 present');
assert(css.includes('backdrop-filter: blur'), 'Glassmorphism backdrop blur present');
assert(css.includes('prefers-reduced-motion'), 'Reduced motion accessibility query present');

console.log(`\n========================================`);
console.log(`Suite Results: ${passes} Passed, ${errors} Failed`);
console.log(`========================================`);

if (errors > 0) {
  process.exit(1);
} else {
  console.log('🎉 ALL VALIDATION TESTS PASSED!');
  process.exit(0);
}
