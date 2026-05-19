import re, os

BASE = r'C:\Users\gareth.vandenaardweg\Downloads\itfirm-it-solutions-and-services-2023-11-27-05-02-13-utc\IT-Firm Package\IT-firm'

pages = ['index.html', 'service-cloud.html', 'about.html', 'service-cyber-security.html']
for p in pages:
    with open(os.path.join(BASE, p), encoding='utf-8') as f:
        c = f.read()
    title = re.search(r'<title>([^<]+)</title>', c)
    theme = 'theme-color' in c
    sitemap_link = 'rel="sitemap"' in c
    breadcrumb = 'BreadcrumbList' in c
    print(p + ':')
    print('  title       : ' + (title.group(1) if title else 'MISSING'))
    print('  theme-color : ' + ('YES' if theme else 'MISSING'))
    print('  sitemap link: ' + ('YES' if sitemap_link else 'MISSING'))
    print('  BreadcrumbList: ' + ('YES' if breadcrumb else 'N/A'))
    print()
