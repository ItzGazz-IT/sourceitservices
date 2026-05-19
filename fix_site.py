import os, re

BASE = r'C:\Users\gareth.vandenaardweg\Downloads\itfirm-it-solutions-and-services-2023-11-27-05-02-13-utc\IT-Firm Package\IT-firm'
BASE_URL = 'https://www.itserv.co.za'
OG_IMAGE = f'{BASE_URL}/images/main-slider/1.jpg'
SITE_NAME = 'Source IT Services'

# ── Per-page SEO data ──────────────────────────────────────────────────────────
SEO = {
    'index.html': {
        'title': 'Source IT Services | Managed IT Support South Africa',
        'description': 'Source IT Services delivers managed IT support, cloud, connectivity, cyber security, Microsoft 365, and communications for South African businesses. Fast response, trusted results.',
        'keywords': 'managed IT support South Africa, IT services South Africa, cloud solutions, cyber security, Microsoft 365, connectivity, network support, IT company South Africa',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/', 'og_url': f'{BASE_URL}/', 'schema': 'home',
    },
    'about.html': {
        'title': 'About Source IT Services | IT Partner South Africa',
        'description': 'Learn about Source IT Services — a South African IT company providing practical managed support, cloud, connectivity, and cyber security for growing businesses.',
        'keywords': 'Source IT Services about, IT company South Africa, managed IT partner, business technology support South Africa',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/about.html', 'og_url': f'{BASE_URL}/about.html', 'schema': 'about',
    },
    'services.html': {
        'title': 'IT Services South Africa | Cloud, Security & More | Source IT Services',
        'description': 'Explore our full range of IT services: cloud solutions, connectivity, cyber security, Microsoft 365, network support, communications, security systems, and web development.',
        'keywords': 'IT services South Africa, cloud, connectivity, cyber security, Microsoft 365, network solutions, security systems, web development, managed IT services',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/services.html', 'og_url': f'{BASE_URL}/services.html', 'schema': 'services',
    },
    'contact.html': {
        'title': 'Contact Source IT Services | IT Support South Africa',
        'description': 'Contact Source IT Services for IT support, connectivity, cloud, and cyber security in South Africa. Call, email, or chat on WhatsApp for a fast response.',
        'keywords': 'contact IT support South Africa, IT helpdesk, Source IT Services contact, IT quote South Africa',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/contact.html', 'og_url': f'{BASE_URL}/contact.html', 'schema': 'contact',
    },
    'service-cloud.html': {
        'title': 'Cloud Solutions South Africa | Source IT Services',
        'description': 'Scalable cloud solutions for South African businesses. Source IT Services designs, migrates, and manages cloud infrastructure to improve performance, flexibility, and security.',
        'keywords': 'cloud solutions South Africa, cloud migration, managed cloud services, cloud infrastructure, business cloud support',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/service-cloud.html', 'og_url': f'{BASE_URL}/service-cloud.html', 'schema': 'service', 'service_name': 'Cloud Solutions',
    },
    'service-cyber-security.html': {
        'title': 'Cyber Security Solutions South Africa | Source IT Services',
        'description': 'Protect your business with enterprise cyber security from Source IT Services. Threat detection, endpoint protection, firewalls, and POPIA-aligned security for South African businesses.',
        'keywords': 'cyber security South Africa, endpoint protection, firewall, threat detection, IT security services, POPIA compliance, ransomware protection',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/service-cyber-security.html', 'og_url': f'{BASE_URL}/service-cyber-security.html', 'schema': 'service', 'service_name': 'Cyber Security Solutions',
    },
    'service-network.html': {
        'title': 'Network Solutions South Africa | Source IT Services',
        'description': 'Reliable business network design, installation, and support. Source IT Services delivers LAN, WAN, and wireless managed network monitoring for South African companies.',
        'keywords': 'network solutions South Africa, business networking, LAN WAN setup, managed network support, wireless network installation',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/service-network.html', 'og_url': f'{BASE_URL}/service-network.html', 'schema': 'service', 'service_name': 'Network Solutions',
    },
    'service-connectivity.html': {
        'title': 'Connectivity Solutions South Africa | Source IT Services',
        'description': 'Business fibre, LTE backup, and dedicated internet for South African businesses. Fast, reliable connectivity with 24/7 monitoring and support from Source IT Services.',
        'keywords': 'business fibre South Africa, connectivity solutions, internet for business, LTE backup, dedicated internet access, fibre connectivity',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/service-connectivity.html', 'og_url': f'{BASE_URL}/service-connectivity.html', 'schema': 'service', 'service_name': 'Connectivity Solutions',
    },
    'service-microsoft-365.html': {
        'title': 'Microsoft 365 Solutions South Africa | Source IT Services',
        'description': 'Microsoft 365 licensing, deployment, migration, and ongoing support for South African businesses. Email, Teams, SharePoint, and OneDrive managed by Source IT Services.',
        'keywords': 'Microsoft 365 South Africa, Office 365, Microsoft Teams, SharePoint, OneDrive, email migration, M365 support, Microsoft 365 licensing',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/service-microsoft-365.html', 'og_url': f'{BASE_URL}/service-microsoft-365.html', 'schema': 'service', 'service_name': 'Microsoft 365 Solutions',
    },
    'service-communication.html': {
        'title': 'Communication Solutions South Africa | Source IT Services',
        'description': 'VoIP, PBX, and unified communications for South African businesses. Source IT Services delivers reliable, scalable communication systems to keep your team connected.',
        'keywords': 'VoIP South Africa, business PBX, unified communications, business phone system, communication IT solutions, hosted VoIP',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/service-communication.html', 'og_url': f'{BASE_URL}/service-communication.html', 'schema': 'service', 'service_name': 'Communication Solutions',
    },
    'service-web-app-development.html': {
        'title': 'Web & App Development South Africa | Source IT Services',
        'description': 'Professional web and application development for South African businesses. Source IT Services builds responsive websites, business portals, and custom digital solutions.',
        'keywords': 'web development South Africa, app development, business website, custom software development, digital solutions South Africa, website design',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/service-web-app-development.html', 'og_url': f'{BASE_URL}/service-web-app-development.html', 'schema': 'service', 'service_name': 'Web & App Development',
    },
    'service-security-systems.html': {
        'title': 'Security Systems South Africa | Source IT Services',
        'description': 'CCTV, access control, and physical security systems for South African businesses. Source IT Services installs and monitors integrated security solutions.',
        'keywords': 'security systems South Africa, CCTV installation, access control, business security, surveillance systems, physical security',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/service-security-systems.html', 'og_url': f'{BASE_URL}/service-security-systems.html', 'schema': 'service', 'service_name': 'Security Systems',
    },
    'terms-of-service.html': {
        'title': 'Terms of Service | Source IT Services',
        'description': 'Read the terms and conditions governing use of Source IT Services. Understand your rights and responsibilities when working with us.',
        'keywords': 'terms of service, terms and conditions, Source IT Services legal',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/terms-of-service.html', 'og_url': f'{BASE_URL}/terms-of-service.html',
    },
    'privacy-policy.html': {
        'title': 'Privacy Policy | Source IT Services',
        'description': 'Source IT Services privacy policy. Learn how we collect, use, and protect your personal information in compliance with POPIA and South African law.',
        'keywords': 'privacy policy, data protection, POPIA, personal information, Source IT Services privacy',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/privacy-policy.html', 'og_url': f'{BASE_URL}/privacy-policy.html',
    },
    'cookie-policy.html': {
        'title': 'Cookie Policy | Source IT Services',
        'description': 'Source IT Services cookie policy. Find out which cookies we use on this website and how to manage or disable them.',
        'keywords': 'cookie policy, cookies, website cookies, Source IT Services',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/cookie-policy.html', 'og_url': f'{BASE_URL}/cookie-policy.html',
    },
    'popia-notice.html': {
        'title': 'POPIA Notice | Source IT Services',
        'description': 'Source IT Services POPIA (Protection of Personal Information Act) notice. Understand how we collect, process, and protect your personal data under South African law.',
        'keywords': 'POPIA notice, personal information, data privacy South Africa, Source IT Services POPIA, Protection of Personal Information Act',
        'robots': 'index, follow', 'canonical': f'{BASE_URL}/popia-notice.html', 'og_url': f'{BASE_URL}/popia-notice.html',
    },
    'not-found.html': {
        'title': '404 Page Not Found | Source IT Services',
        'description': 'The page you requested could not be found. Return to Source IT Services for managed IT, cloud, connectivity, and cyber security support in South Africa.',
        'keywords': 'page not found, 404, Source IT Services',
        'robots': 'noindex, follow', 'canonical': f'{BASE_URL}/', 'og_url': f'{BASE_URL}/',
    },
    'service-detail.html': {
        'title': 'IT Services | Source IT Services',
        'description': 'Explore IT services from Source IT Services including cloud, connectivity, cyber security, and Microsoft 365 for South African businesses.',
        'keywords': 'IT services South Africa, Source IT Services',
        'robots': 'noindex, follow', 'canonical': f'{BASE_URL}/services.html', 'og_url': f'{BASE_URL}/services.html',
    },
    'blog.html': {
        'title': 'Blog | Source IT Services',
        'description': 'IT insights and technology resources from Source IT Services.',
        'keywords': 'IT blog, Source IT Services, technology insights',
        'robots': 'noindex, follow', 'canonical': f'{BASE_URL}/services.html', 'og_url': f'{BASE_URL}/services.html',
    },
    'blog-detail.html': {
        'title': 'Blog | Source IT Services',
        'description': 'IT insights and technology resources from Source IT Services.',
        'keywords': 'IT blog, Source IT Services, technology insights',
        'robots': 'noindex, follow', 'canonical': f'{BASE_URL}/services.html', 'og_url': f'{BASE_URL}/services.html',
    },
    'project.html': {
        'title': 'Projects | Source IT Services',
        'description': 'IT project solutions from Source IT Services.',
        'keywords': 'IT projects, Source IT Services',
        'robots': 'noindex, follow', 'canonical': f'{BASE_URL}/services.html', 'og_url': f'{BASE_URL}/services.html',
    },
    'project-detail.html': {
        'title': 'Project Detail | Source IT Services',
        'description': 'IT project detail from Source IT Services.',
        'keywords': 'IT projects, Source IT Services',
        'robots': 'noindex, follow', 'canonical': f'{BASE_URL}/services.html', 'og_url': f'{BASE_URL}/services.html',
    },
}

# ── JSON-LD schema blocks ──────────────────────────────────────────────────────
LOCAL_BUSINESS_SCHEMA = """{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Source IT Services",
  "description": "Managed IT support, cloud, connectivity, cyber security, Microsoft 365, and communications for South African businesses.",
  "url": "https://www.itserv.co.za",
  "telephone": "+27837754514",
  "email": "support@itserv.co.za",
  "address": {"@type": "PostalAddress", "addressCountry": "ZA"},
  "areaServed": {"@type": "Country", "name": "South Africa"},
  "sameAs": [
    "https://www.facebook.com/people/Source-It-Services/61587054354144/",
    "https://www.instagram.com/source.itservices/"
  ]
}"""

WEBSITE_SCHEMA = """{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Source IT Services",
  "url": "https://www.itserv.co.za"
}"""

def make_service_schema(service_name):
    return f"""{{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "{service_name}",
  "provider": {{
    "@type": "LocalBusiness",
    "name": "Source IT Services",
    "url": "https://www.itserv.co.za",
    "telephone": "+27837754514",
    "areaServed": {{"@type": "Country", "name": "South Africa"}}
  }}
}}"""

def get_schema_block(seo):
    schema_type = seo.get('schema', '')
    lines = []
    if schema_type == 'home':
        lines.append(f'<script type="application/ld+json">{LOCAL_BUSINESS_SCHEMA}</script>')
        lines.append(f'<script type="application/ld+json">{WEBSITE_SCHEMA}</script>')
    elif schema_type in ('about', 'contact', 'services'):
        lines.append(f'<script type="application/ld+json">{LOCAL_BUSINESS_SCHEMA}</script>')
    elif schema_type == 'service':
        lines.append(f'<script type="application/ld+json">{make_service_schema(seo["service_name"])}</script>')
    return '\n'.join(lines)

# ── SEO meta block builder ─────────────────────────────────────────────────────
def build_seo_block(filename, seo):
    d = seo
    og_title = d['title']
    og_desc  = d['description']
    og_url   = d['og_url']
    schema   = get_schema_block(d)
    block = f"""<meta name="description" content="{d['description']}">
<meta name="keywords" content="{d['keywords']}">
<meta name="robots" content="{d['robots']}">
<meta name="author" content="Source IT Services">
<meta name="geo.region" content="ZA">
<meta name="geo.placename" content="South Africa">
<link rel="canonical" href="{d['canonical']}">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{og_url}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:site_name" content="Source IT Services">
<meta property="og:locale" content="en_ZA">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{og_desc}">
<meta name="twitter:image" content="{OG_IMAGE}">"""
    if schema:
        block += '\n' + schema
    return block

# ── Cookie banner HTML (self-contained, inline styles) ────────────────────────
COOKIE_BANNER = '''<!-- Cookie Consent (POPIA/GDPR) -->
<div id="src-cookie-banner" role="dialog" aria-label="Cookie consent" style="display:none;position:fixed;bottom:0;left:0;right:0;background:#0d1233;color:#e8eaf6;padding:14px 20px;z-index:99999;align-items:center;justify-content:space-between;gap:16px;box-shadow:0 -4px 20px rgba(0,0,0,0.45);font-size:14px;font-family:inherit;flex-wrap:wrap;">
  <p style="margin:0;flex:1;min-width:200px;">We use cookies to improve your experience. By using this site you accept our <a href="cookie-policy.html" style="color:#7eb3ff;text-decoration:underline;">Cookie Policy</a>. Personal data is handled in accordance with <a href="popia-notice.html" style="color:#7eb3ff;text-decoration:underline;">POPIA</a>.</p>
  <div style="display:flex;gap:10px;align-items:center;flex-shrink:0;">
    <button id="src-cookie-accept" style="background:linear-gradient(135deg,#042D80,#0550A8);color:#fff;border:none;padding:9px 22px;border-radius:6px;cursor:pointer;font-size:14px;font-weight:600;white-space:nowrap;" aria-label="Accept cookies">Accept</button>
    <a href="cookie-policy.html" style="color:#8fa8c8;font-size:13px;text-decoration:none;white-space:nowrap;">Learn more</a>
  </div>
</div>
<script>(function(){var b=document.getElementById('src-cookie-banner');var btn=document.getElementById('src-cookie-accept');if(b&&!localStorage.getItem('src_cc')){b.style.display='flex';}if(btn){btn.addEventListener('click',function(){localStorage.setItem('src_cc','1');document.getElementById('src-cookie-banner').style.display='none';});}})();</script>'''

# ── Patterns to strip out old SEO tags (line-by-line) ─────────────────────────
STRIP_LINE_PATTERNS = [
    re.compile(r'^\s*<meta\s[^>]*name=["\']description["\'][^>]*>\s*$', re.IGNORECASE),
    re.compile(r'^\s*<meta\s[^>]*name=["\']keywords["\'][^>]*>\s*$', re.IGNORECASE),
    re.compile(r'^\s*<meta\s[^>]*name=["\']robots["\'][^>]*>\s*$', re.IGNORECASE),
    re.compile(r'^\s*<meta\s[^>]*name=["\']author["\'][^>]*>\s*$', re.IGNORECASE),
    re.compile(r'^\s*<meta\s[^>]*name=["\']geo\.[^"\']*["\'][^>]*>\s*$', re.IGNORECASE),
    re.compile(r'^\s*<meta\s[^>]*property=["\']og:[^"\']*["\'][^>]*>\s*$', re.IGNORECASE),
    re.compile(r'^\s*<meta\s[^>]*name=["\']twitter:[^"\']*["\'][^>]*>\s*$', re.IGNORECASE),
    re.compile(r'^\s*<link\s[^>]*rel=["\']canonical["\'][^>]*>\s*$', re.IGNORECASE),
]

# ── Main processing ────────────────────────────────────────────────────────────
all_files = [f for f in os.listdir(BASE) if f.endswith('.html')]
changed = []
skipped = []

for filename in sorted(all_files):
    if filename not in SEO:
        skipped.append(filename)
        continue

    path = os.path.join(BASE, filename)
    with open(path, 'r', encoding='utf-8') as fh:
        content = fh.read()

    original = content

    # 1. Fix fa-brands → fab, fa-solid → fas (FA6 → FA5 class names)
    content = re.sub(r'\bfa-brands\b', 'fab', content)
    content = re.sub(r'\bfa-solid\b', 'fas', content)

    # 2. Fix <html> lang attribute
    content = re.sub(r'<html(\s[^>]*)?>',
                     lambda m: '<html lang="en-ZA">', content, count=1)

    # 3. Remove existing JSON-LD scripts
    content = re.sub(r'\s*<script\s+type=["\']application/ld\+json["\']>[\s\S]*?</script>', '', content)

    # 4. Strip old individual SEO meta/link tags line by line
    lines = content.split('\n')
    new_lines = [ln for ln in lines if not any(p.match(ln) for p in STRIP_LINE_PATTERNS)]
    content = '\n'.join(new_lines)

    # 5. Insert new SEO block right after <meta charset...> line
    seo_block = build_seo_block(filename, SEO[filename])
    charset_pat = re.compile(r'(<meta\s+charset=[^>]+>)', re.IGNORECASE)
    if charset_pat.search(content):
        content = charset_pat.sub(r'\1\n' + seo_block, content, count=1)
    else:
        # Fallback: insert after <head>
        content = re.sub(r'(<head[^>]*>)', r'\1\n' + seo_block, content, count=1, flags=re.IGNORECASE)

    # 6. Add cookie consent banner before </body> (only once)
    if 'src-cookie-banner' not in content:
        content = content.replace('</body>', COOKIE_BANNER + '\n</body>', 1)

    if content != original:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(content)
        changed.append(filename)
    else:
        print(f'  no change: {filename}')

print(f'\n✓ Updated {len(changed)} files:')
for f in changed:
    print(f'  {f}')
if skipped:
    print(f'\n  Skipped (not in SEO map): {skipped}')

# ── Create sitemap.xml ─────────────────────────────────────────────────────────
from datetime import date
today = date.today().isoformat()
indexable = [
    ('', '1.0', 'weekly'),
    ('about.html', '0.8', 'monthly'),
    ('services.html', '0.9', 'monthly'),
    ('contact.html', '0.8', 'monthly'),
    ('service-cloud.html', '0.7', 'monthly'),
    ('service-cyber-security.html', '0.7', 'monthly'),
    ('service-network.html', '0.7', 'monthly'),
    ('service-connectivity.html', '0.7', 'monthly'),
    ('service-microsoft-365.html', '0.7', 'monthly'),
    ('service-communication.html', '0.7', 'monthly'),
    ('service-web-app-development.html', '0.7', 'monthly'),
    ('service-security-systems.html', '0.7', 'monthly'),
    ('terms-of-service.html', '0.3', 'yearly'),
    ('privacy-policy.html', '0.3', 'yearly'),
    ('cookie-policy.html', '0.3', 'yearly'),
    ('popia-notice.html', '0.3', 'yearly'),
]
url_entries = ''
for path_suffix, priority, freq in indexable:
    url = f'{BASE_URL}/{path_suffix}'
    url_entries += f'''  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>\n'''

sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{url_entries}</urlset>'''
with open(os.path.join(BASE, 'sitemap.xml'), 'w', encoding='utf-8') as fh:
    fh.write(sitemap)
print('\n✓ Created sitemap.xml')

# ── Create robots.txt ──────────────────────────────────────────────────────────
robots = f"""User-agent: *
Allow: /
Disallow: /not-found.html
Disallow: /service-detail.html
Disallow: /blog.html
Disallow: /blog-detail.html
Disallow: /project.html
Disallow: /project-detail.html

Sitemap: {BASE_URL}/sitemap.xml
"""
with open(os.path.join(BASE, 'robots.txt'), 'w', encoding='utf-8') as fh:
    fh.write(robots)
print('✓ Created robots.txt')
print('\nAll done.')
