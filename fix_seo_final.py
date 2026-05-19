import os
import re
import json

BASE = r'C:\Users\gareth.vandenaardweg\Downloads\itfirm-it-solutions-and-services-2023-11-27-05-02-13-utc\IT-Firm Package\IT-firm'
BASE_URL = 'https://www.itserv.co.za'

BREADCRUMBS = {
    'about.html': [
        ('Home', BASE_URL + '/'),
        ('About Us', BASE_URL + '/about.html'),
    ],
    'services.html': [
        ('Home', BASE_URL + '/'),
        ('Services', BASE_URL + '/services.html'),
    ],
    'contact.html': [
        ('Home', BASE_URL + '/'),
        ('Contact', BASE_URL + '/contact.html'),
    ],
    'service-cloud.html': [
        ('Home', BASE_URL + '/'),
        ('Services', BASE_URL + '/services.html'),
        ('Cloud Solutions', BASE_URL + '/service-cloud.html'),
    ],
    'service-cyber-security.html': [
        ('Home', BASE_URL + '/'),
        ('Services', BASE_URL + '/services.html'),
        ('Cyber Security', BASE_URL + '/service-cyber-security.html'),
    ],
    'service-network.html': [
        ('Home', BASE_URL + '/'),
        ('Services', BASE_URL + '/services.html'),
        ('Network Solutions', BASE_URL + '/service-network.html'),
    ],
    'service-connectivity.html': [
        ('Home', BASE_URL + '/'),
        ('Services', BASE_URL + '/services.html'),
        ('Connectivity Solutions', BASE_URL + '/service-connectivity.html'),
    ],
    'service-microsoft-365.html': [
        ('Home', BASE_URL + '/'),
        ('Services', BASE_URL + '/services.html'),
        ('Microsoft 365', BASE_URL + '/service-microsoft-365.html'),
    ],
    'service-communication.html': [
        ('Home', BASE_URL + '/'),
        ('Services', BASE_URL + '/services.html'),
        ('Communication Solutions', BASE_URL + '/service-communication.html'),
    ],
    'service-web-app-development.html': [
        ('Home', BASE_URL + '/'),
        ('Services', BASE_URL + '/services.html'),
        ('Web & App Development', BASE_URL + '/service-web-app-development.html'),
    ],
    'service-security-systems.html': [
        ('Home', BASE_URL + '/'),
        ('Services', BASE_URL + '/services.html'),
        ('Security Systems', BASE_URL + '/service-security-systems.html'),
    ],
    'terms-of-service.html': [
        ('Home', BASE_URL + '/'),
        ('Terms of Service', BASE_URL + '/terms-of-service.html'),
    ],
    'privacy-policy.html': [
        ('Home', BASE_URL + '/'),
        ('Privacy Policy', BASE_URL + '/privacy-policy.html'),
    ],
    'cookie-policy.html': [
        ('Home', BASE_URL + '/'),
        ('Cookie Policy', BASE_URL + '/cookie-policy.html'),
    ],
    'popia-notice.html': [
        ('Home', BASE_URL + '/'),
        ('POPIA Notice', BASE_URL + '/popia-notice.html'),
    ],
}


def make_breadcrumb_json(items):
    list_items = []
    for i, (name, url) in enumerate(items):
        list_items.append({
            '@type': 'ListItem',
            'position': i + 1,
            'name': name,
            'item': url,
        })
    schema = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': list_items,
    }
    return json.dumps(schema, ensure_ascii=False)


changed = []

for filename in os.listdir(BASE):
    if not filename.endswith('.html'):
        continue
    path = os.path.join(BASE, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # 1. Add theme-color if missing
    if 'theme-color' not in content:
        content = re.sub(
            r'(<meta\s+charset=[^>]+>)',
            r'\1\n<meta name="theme-color" content="#042D80">',
            content, count=1, flags=re.IGNORECASE,
        )

    # 2. Add sitemap link in head if missing
    if 'rel="sitemap"' not in content and "rel='sitemap'" not in content:
        content = re.sub(
            r'(<meta\s+charset=[^>]+>)',
            r'\1\n<link rel="sitemap" type="application/xml" href="/sitemap.xml">',
            content, count=1, flags=re.IGNORECASE,
        )

    # 3. Add BreadcrumbList JSON-LD if defined for this page and not already present
    if filename in BREADCRUMBS and 'BreadcrumbList' not in content:
        schema_tag = '<script type="application/ld+json">' + make_breadcrumb_json(BREADCRUMBS[filename]) + '</script>'
        content = re.sub(r'(</head>)', schema_tag + '\n' + r'\1', content, count=1, flags=re.IGNORECASE)

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        changed.append(filename)

print(f'Updated {len(changed)} files:')
for f in sorted(changed):
    print(f'  {f}')
