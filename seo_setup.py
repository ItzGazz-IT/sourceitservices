#!/usr/bin/env python3
"""Comprehensive SEO, icon-fix, and cookie-consent setup for Source IT Services."""
import os, re, json

BASE   = r"c:\Users\gareth.vandenaardweg\Downloads\itfirm-it-solutions-and-services-2023-11-27-05-02-13-utc\IT-Firm Package\IT-firm"
DOMAIN = "https://www.sourceitservices.co.za"
OG_IMG = f"{DOMAIN}/images/resource/about-1.jpg"
BIZ_ID = f"{DOMAIN}/#business"
SITE_ID= f"{DOMAIN}/#website"

LOCAL_BIZ = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "@id": BIZ_ID,
    "name": "Source IT Services",
    "url": DOMAIN,
    "logo": f"{DOMAIN}/images/favicon.png",
    "image": OG_IMG,
    "description": "Source IT Services delivers managed IT support, cloud, connectivity, cyber security, Microsoft 365, and communications for businesses across South Africa.",
    "telephone": "+27100065557",
    "email": "support@itserv.co.za",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "20 Pyramid Road",
        "addressLocality": "Isandovale",
        "addressRegion": "Gauteng",
        "addressCountry": "ZA"
    },
    "areaServed": {"@type": "Country", "name": "South Africa"},
    "sameAs": [
        "https://www.facebook.com/people/Source-It-Services/61587054354144/",
        "https://www.instagram.com/source.itservices/"
    ]
}

def breadcrumb(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i+1, "name": n, "item": u}
            for i, (n, u) in enumerate(items)
        ]
    }

HOME = ("Home", f"{DOMAIN}/")
SVCS = ("Services", f"{DOMAIN}/services.html")

def svc_schema(name, desc, url):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "@id": url,
        "name": name,
        "description": desc,
        "provider": {"@id": BIZ_ID},
        "areaServed": {"@type": "Country", "name": "South Africa"},
        "url": url
    }

PAGES = {
    "index.html": {
        "title": "Source IT Services | Managed IT Support for South African Businesses",
        "desc":  "Source IT Services delivers managed IT support, cloud solutions, connectivity, cyber security, Microsoft 365, and communications for businesses across South Africa.",
        "kw":    "managed IT support South Africa, IT services Gauteng, cloud solutions, cyber security, Microsoft 365, business IT support",
        "og_title": "Source IT Services | Managed IT and Business Technology Support",
        "og_desc":  "Practical IT support, connectivity, cloud, and security solutions designed to keep your business productive and protected.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/",
        "schema": [
            LOCAL_BIZ,
            {"@context":"https://schema.org","@type":"WebSite","@id":SITE_ID,
             "url":DOMAIN,"name":"Source IT Services",
             "description":"Managed IT support, cloud, connectivity, cyber security, and Microsoft 365 for South African businesses",
             "publisher":{"@id":BIZ_ID}}
        ]
    },
    "about.html": {
        "title": "About Source IT Services | IT Support Specialists in Gauteng",
        "desc":  "Learn about Source IT Services — our approach to managed IT, proactive support, and accountable project delivery for South African businesses in Gauteng.",
        "kw":    "about Source IT Services, IT company South Africa, IT support Gauteng, managed IT provider, IT specialists",
        "og_title": "About Source IT Services | IT Support Specialists in Gauteng",
        "og_desc":  "Discover how Source IT Services delivers dependable IT outcomes for modern South African businesses.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/about.html",
        "schema": [
            {"@context":"https://schema.org","@type":"AboutPage","@id":f"{DOMAIN}/about.html",
             "name":"About Source IT Services","url":f"{DOMAIN}/about.html",
             "isPartOf":{"@id":SITE_ID},"about":{"@id":BIZ_ID}},
            breadcrumb([HOME, ("About Us", f"{DOMAIN}/about.html")])
        ]
    },
    "services.html": {
        "title": "IT Services for South African Businesses | Source IT Services",
        "desc":  "Explore Source IT Services: cloud, connectivity, cyber security, Microsoft 365, network, communication, security systems, and web development for South African businesses.",
        "kw":    "IT services South Africa, business technology Gauteng, managed services, cloud connectivity security, IT solutions",
        "og_title": "IT Services for South African Businesses | Source IT Services",
        "og_desc":  "Compare our IT service offerings and choose the support tailored to your business environment.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/services.html",
        "schema": [
            {"@context":"https://schema.org","@type":"CollectionPage","@id":f"{DOMAIN}/services.html",
             "name":"IT Services – Source IT Services","url":f"{DOMAIN}/services.html",
             "isPartOf":{"@id":SITE_ID},"provider":{"@id":BIZ_ID}},
            breadcrumb([HOME, ("Services", f"{DOMAIN}/services.html")])
        ]
    },
    "contact.html": {
        "title": "Contact Source IT Services | IT Support in Gauteng, South Africa",
        "desc":  "Contact Source IT Services for managed IT support, cloud, cyber security, and Microsoft 365. Call (010)\u00a0006-5557 or visit us in Isandovale, Gauteng.",
        "kw":    "contact IT support South Africa, IT services Gauteng contact, Source IT Services phone number",
        "og_title": "Contact Source IT Services | IT Support in Gauteng",
        "og_desc":  "Speak with our team for a tailored IT plan and responsive support. Call, email, or visit us in Isandovale, Gauteng.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/contact.html",
        "schema": [
            LOCAL_BIZ,
            {"@context":"https://schema.org","@type":"ContactPage","@id":f"{DOMAIN}/contact.html",
             "name":"Contact Source IT Services","url":f"{DOMAIN}/contact.html",
             "isPartOf":{"@id":SITE_ID},"about":{"@id":BIZ_ID}},
            breadcrumb([HOME, ("Contact Us", f"{DOMAIN}/contact.html")])
        ]
    },
    "service-cloud.html": {
        "title": "Cloud Solutions for South African Businesses | Source IT Services",
        "desc":  "Cloud migration, infrastructure hosting, and cloud management for South African businesses. Source IT Services delivers scalable cloud solutions with expert local support.",
        "kw":    "cloud solutions South Africa, cloud migration Gauteng, hosted infrastructure, managed cloud, cloud services business",
        "og_title": "Cloud Solutions for South African Businesses | Source IT Services",
        "og_desc":  "Scalable cloud migration and management with local support. Source IT Services keeps your cloud environment running and your business productive.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/service-cloud.html",
        "schema": [
            svc_schema("Cloud Solutions",
                "Cloud migration, infrastructure hosting, and cloud management for South African businesses.",
                f"{DOMAIN}/service-cloud.html"),
            breadcrumb([HOME, SVCS, ("Cloud Solutions", f"{DOMAIN}/service-cloud.html")])
        ]
    },
    "service-communication.html": {
        "title": "Business Communication Solutions | VoIP and Unified Comms | Source IT Services",
        "desc":  "VoIP, hosted PBX, and unified communications for South African businesses. Source IT Services modernises your telephony and collaboration tools with reliable local support.",
        "kw":    "VoIP South Africa, hosted PBX Gauteng, unified communications, business phone system, communication solutions",
        "og_title": "Business Communication Solutions | Source IT Services",
        "og_desc":  "VoIP, hosted PBX, and unified communications tailored for South African businesses.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/service-communication.html",
        "schema": [
            svc_schema("Business Communication Solutions",
                "VoIP, hosted PBX, and unified communications for South African businesses.",
                f"{DOMAIN}/service-communication.html"),
            breadcrumb([HOME, SVCS, ("Communication Solutions", f"{DOMAIN}/service-communication.html")])
        ]
    },
    "service-connectivity.html": {
        "title": "Business Connectivity Solutions | Fibre and Internet | Source IT Services",
        "desc":  "Reliable fibre, LTE, and business broadband connectivity for South African businesses. Source IT Services manages your connection with SLAs and failover support.",
        "kw":    "business connectivity South Africa, fibre internet Gauteng, business broadband, internet solutions, LTE failover",
        "og_title": "Business Connectivity Solutions | Source IT Services",
        "og_desc":  "Reliable fibre, LTE, and broadband connectivity managed with SLAs and failover for South African businesses.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/service-connectivity.html",
        "schema": [
            svc_schema("Business Connectivity Solutions",
                "Reliable fibre, LTE, and business broadband connectivity for South African businesses.",
                f"{DOMAIN}/service-connectivity.html"),
            breadcrumb([HOME, SVCS, ("Connectivity Solutions", f"{DOMAIN}/service-connectivity.html")])
        ]
    },
    "service-cyber-security.html": {
        "title": "Cyber Security Solutions for South African Businesses | Source IT Services",
        "desc":  "Protect your business from cyber threats with Source IT Services. Endpoint security, threat monitoring, firewall management, and POPIA compliance support in Gauteng.",
        "kw":    "cyber security South Africa, IT security Gauteng, endpoint protection, firewall management, POPIA compliance, threat monitoring",
        "og_title": "Cyber Security Solutions for South African Businesses | Source IT Services",
        "og_desc":  "Endpoint security, threat monitoring, and firewall management to protect your South African business.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/service-cyber-security.html",
        "schema": [
            svc_schema("Cyber Security Solutions",
                "Endpoint security, threat monitoring, firewall management, and POPIA compliance support for South African businesses.",
                f"{DOMAIN}/service-cyber-security.html"),
            breadcrumb([HOME, SVCS, ("Cyber Security", f"{DOMAIN}/service-cyber-security.html")])
        ]
    },
    "service-microsoft-365.html": {
        "title": "Microsoft 365 Setup and Management in South Africa | Source IT Services",
        "desc":  "Microsoft 365 licensing, deployment, migration, and ongoing management for South African businesses. Source IT Services ensures productive, secure cloud collaboration.",
        "kw":    "Microsoft 365 South Africa, Office 365 Gauteng, M365 migration, Microsoft 365 support, Teams SharePoint",
        "og_title": "Microsoft 365 for South African Businesses | Source IT Services",
        "og_desc":  "Microsoft 365 deployment, migration, and management with expert local support from Source IT Services.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/service-microsoft-365.html",
        "schema": [
            svc_schema("Microsoft 365 Solutions",
                "Microsoft 365 licensing, deployment, migration, and management for South African businesses.",
                f"{DOMAIN}/service-microsoft-365.html"),
            breadcrumb([HOME, SVCS, ("Microsoft 365", f"{DOMAIN}/service-microsoft-365.html")])
        ]
    },
    "service-network.html": {
        "title": "Network Solutions and IT Infrastructure in Gauteng | Source IT Services",
        "desc":  "Enterprise-grade network design, installation, and management for South African businesses. Source IT Services builds reliable, secure, and scalable network infrastructure.",
        "kw":    "network solutions South Africa, IT infrastructure Gauteng, LAN WAN, network installation, business networking",
        "og_title": "Network Solutions and IT Infrastructure | Source IT Services",
        "og_desc":  "Reliable, secure, and scalable network infrastructure for South African businesses from Source IT Services.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/service-network.html",
        "schema": [
            svc_schema("Network Solutions",
                "Enterprise-grade network design, installation, and management for South African businesses.",
                f"{DOMAIN}/service-network.html"),
            breadcrumb([HOME, SVCS, ("Network Solutions", f"{DOMAIN}/service-network.html")])
        ]
    },
    "service-security-systems.html": {
        "title": "Security Systems and CCTV Solutions in Gauteng | Source IT Services",
        "desc":  "CCTV, access control, and physical security systems for South African businesses. Source IT Services designs and installs integrated security solutions across Gauteng.",
        "kw":    "CCTV South Africa, access control Gauteng, security systems, business security, surveillance solutions",
        "og_title": "Security Systems and CCTV Solutions | Source IT Services",
        "og_desc":  "CCTV, access control, and integrated physical security systems for South African businesses.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/service-security-systems.html",
        "schema": [
            svc_schema("Security Systems",
                "CCTV, access control, and physical security systems for South African businesses.",
                f"{DOMAIN}/service-security-systems.html"),
            breadcrumb([HOME, SVCS, ("Security Systems", f"{DOMAIN}/service-security-systems.html")])
        ]
    },
    "service-web-app-development.html": {
        "title": "Web and App Development for South African Businesses | Source IT Services",
        "desc":  "Custom website design and mobile app development for South African businesses. Source IT Services builds fast, secure, and scalable web solutions that drive real results.",
        "kw":    "web development South Africa, app development Gauteng, custom website design, business web solutions, mobile app development",
        "og_title": "Web and App Development for South African Businesses | Source IT Services",
        "og_desc":  "Custom websites and mobile apps built for South African businesses. Fast, secure, and aligned to your goals.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/service-web-app-development.html",
        "schema": [
            svc_schema("Web and App Development",
                "Custom website design and mobile app development for South African businesses.",
                f"{DOMAIN}/service-web-app-development.html"),
            breadcrumb([HOME, SVCS, ("Web and App Development", f"{DOMAIN}/service-web-app-development.html")])
        ]
    },
    "popia-notice.html": {
        "title": "POPIA Notice | Personal Information Protection | Source IT Services",
        "desc":  "Read the Source IT Services POPIA notice. Understand how we collect, process, and protect your personal information under South African privacy law.",
        "kw":    "POPIA notice, personal information protection, data privacy South Africa",
        "og_title": "POPIA Notice | Source IT Services",
        "og_desc":  "How Source IT Services collects, processes, and protects your personal information under POPIA.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/popia-notice.html",
        "schema": [breadcrumb([HOME, ("POPIA Notice", f"{DOMAIN}/popia-notice.html")])]
    },
    "privacy-policy.html": {
        "title": "Privacy Policy | Source IT Services",
        "desc":  "Source IT Services privacy policy. Learn how we collect, use, and protect your personal data in compliance with South African privacy laws including POPIA.",
        "kw":    "privacy policy, data protection South Africa, personal information",
        "og_title": "Privacy Policy | Source IT Services",
        "og_desc":  "How Source IT Services handles and protects your personal data in compliance with South African law.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/privacy-policy.html",
        "schema": [breadcrumb([HOME, ("Privacy Policy", f"{DOMAIN}/privacy-policy.html")])]
    },
    "cookie-policy.html": {
        "title": "Cookie Policy | Source IT Services",
        "desc":  "Source IT Services cookie policy. Find out how we use cookies on our website and how you can manage your cookie preferences.",
        "kw":    "cookie policy, website cookies, cookie consent",
        "og_title": "Cookie Policy | Source IT Services",
        "og_desc":  "How Source IT Services uses cookies and how you can manage your preferences.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/cookie-policy.html",
        "schema": [breadcrumb([HOME, ("Cookie Policy", f"{DOMAIN}/cookie-policy.html")])]
    },
    "terms-of-service.html": {
        "title": "Terms of Service | Source IT Services",
        "desc":  "Read the Source IT Services terms of service. Understand the terms governing the use of our website and services.",
        "kw":    "terms of service, terms and conditions, Source IT Services",
        "og_title": "Terms of Service | Source IT Services",
        "og_desc":  "The terms and conditions governing the use of Source IT Services website and services.",
        "robots": "index, follow",
        "url": f"{DOMAIN}/terms-of-service.html",
        "schema": [breadcrumb([HOME, ("Terms of Service", f"{DOMAIN}/terms-of-service.html")])]
    },
    "not-found.html": {
        "title": "Page Not Found | Source IT Services",
        "desc":  "The page you are looking for could not be found. Return to the Source IT Services homepage or browse our IT services.",
        "kw":    "404 page not found",
        "og_title": "Page Not Found | Source IT Services",
        "og_desc":  "This page does not exist. Return to the Source IT Services homepage.",
        "robots": "noindex, follow",
        "url": f"{DOMAIN}/not-found.html",
        "schema": []
    },
}

NOINDEX_PAGES = ["blog.html","blog-detail.html","project.html","project-detail.html","service-detail.html"]

COOKIE_SCRIPT = '<script src="js/cookie-consent.js" defer></script>'

def make_seo_block(data):
    u   = data["url"]
    d   = data["desc"]
    kw  = data["kw"]
    ot  = data["og_title"]
    od  = data["og_desc"]
    rob = data["robots"]
    return (
        f'<meta name="description" content="{d}">\n'
        f'<meta name="keywords" content="{kw}">\n'
        f'<meta name="robots" content="{rob}">\n'
        f'<meta name="author" content="Source IT Services">\n'
        f'<meta name="geo.region" content="ZA-GP">\n'
        f'<meta name="geo.placename" content="Isandovale, Gauteng, South Africa">\n'
        f'<link rel="canonical" href="{u}">\n'
        f'<meta property="og:title" content="{ot}">\n'
        f'<meta property="og:description" content="{od}">\n'
        f'<meta property="og:type" content="website">\n'
        f'<meta property="og:url" content="{u}">\n'
        f'<meta property="og:image" content="{OG_IMG}">\n'
        f'<meta property="og:site_name" content="Source IT Services">\n'
        f'<meta property="og:locale" content="en_ZA">\n'
        f'<meta name="twitter:card" content="summary_large_image">\n'
        f'<meta name="twitter:title" content="{ot}">\n'
        f'<meta name="twitter:description" content="{od}">\n'
        f'<meta name="twitter:image" content="{OG_IMG}">'
    )

def make_schema_block(schemas):
    if not schemas:
        return ""
    parts = []
    for s in schemas:
        parts.append('<script type="application/ld+json">\n' +
                     json.dumps(s, indent=2, ensure_ascii=False) +
                     '\n</script>')
    return "\n".join(parts)

def fix_icons(content):
    # Fix fa-solid / fa-brands → FA5 equivalents
    content = content.replace('fa-solid', 'fas')
    content = content.replace('fa-brands', 'fab')
    # Fix double-base class "fa fas" produced by above (was "fa fa-solid")
    content = content.replace('"fa fas ', '"fas ')
    content = content.replace(' fa fas ', ' fas ')
    # Fix FA6 icon name → FA5 equivalent
    content = content.replace('fa-triangle-exclamation', 'fa-exclamation-triangle')
    return content

def remove_existing_seo(content):
    """Remove any existing SEO tags so we can replace with canonical versions."""
    patterns = [
        r'[ \t]*<meta[^>]*\bname="description"[^>]*>\r?\n?',
        r'[ \t]*<meta[^>]*\bname="keywords"[^>]*>\r?\n?',
        r'[ \t]*<meta[^>]*\bname="robots"[^>]*>\r?\n?',
        r'[ \t]*<meta[^>]*\bname="author"[^>]*>\r?\n?',
        r'[ \t]*<meta[^>]*\bname="geo\.[^"]*"[^>]*>\r?\n?',
        r'[ \t]*<link[^>]*\brel="canonical"[^>]*>\r?\n?',
        r'[ \t]*<meta[^>]*\bproperty="og:[^"]*"[^>]*>\r?\n?',
        r'[ \t]*<meta[^>]*\bname="twitter:[^"]*"[^>]*>\r?\n?',
        r'[ \t]*<script[^>]*\btype="application/ld\+json"[^>]*>[\s\S]*?</script>\r?\n?',
    ]
    for pat in patterns:
        content = re.sub(pat, '', content, flags=re.IGNORECASE)
    return content

def process_page(fname, data):
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8', newline='') as f:
        content = f.read()

    # 1. Fix html lang
    content = re.sub(r'<html(?:\s+lang="[^"]*")?>', '<html lang="en-ZA">', content)

    # 2. Fix icon classes
    content = fix_icons(content)

    # 3. Remove existing SEO tags
    content = remove_existing_seo(content)

    # 4. Update title (handles single- or multi-line titles)
    title_new = data["title"]
    content = re.sub(r'<title>[^<]*</title>', f'<title>{title_new}</title>', content)

    # 5. Insert SEO block right after </title>
    seo = make_seo_block(data)
    def insert_seo(m):
        return m.group(0) + '\n' + seo
    content = re.sub(r'</title>', insert_seo, content, count=1)

    # 6. Insert JSON-LD before </head>
    schema_html = make_schema_block(data.get("schema", []))
    if schema_html:
        content = content.replace('</head>', schema_html + '\n</head>', 1)

    # 7. Add cookie consent before </body>
    if COOKIE_SCRIPT not in content:
        content = content.replace('</body>', COOKIE_SCRIPT + '\n</body>', 1)

    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    print(f"  OK  {fname}")

def add_noindex(fname):
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f"  --  {fname} (not found, skipped)")
        return
    with open(path, 'r', encoding='utf-8', newline='') as f:
        content = f.read()
    content = re.sub(r'<html(?:\s+lang="[^"]*")?>', '<html lang="en-ZA">', content)
    content = fix_icons(content)
    if 'name="robots"' not in content:
        content = re.sub(r'(<meta\s+charset="[^"]*">)',
                         r'\1\n<meta name="robots" content="noindex, nofollow">', content)
    if COOKIE_SCRIPT not in content:
        content = content.replace('</body>', COOKIE_SCRIPT + '\n</body>', 1)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    print(f"  NO  {fname} (noindex)")

if __name__ == "__main__":
    print("Processing pages...")
    for fname, data in PAGES.items():
        process_page(fname, data)
    for fname in NOINDEX_PAGES:
        add_noindex(fname)
    print("\nDone! All pages processed.")
