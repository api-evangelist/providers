---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-12'
  detail: 'Aerwave sells managed Wi-Fi as an operated service, not as a developer product: aerwave.com is a Wix marketing site with no developer, API or documentation link anywhere in its navigation or sitemap, the only two application hosts are Blazor WebAssembly apps for resident registration and the resident portal, and api/docs/developer/portal subdomains on aerwave.com all return NXDOMAIN.'
  evidence:
  - status: 400
    url: https://www.aerwave.com/openapi.json
  - status: 404
    url: https://portal.getaerwave.com/openapi.json
  - status: 400
    url: https://www.aerwave.com/.well-known/api-catalog
  - status: 200
    url: https://www.aerwave.com/pages-sitemap.xml
  - status: 200
    url: https://www.aerwave.com/llms.txt
  - status: 200
    url: https://www.aerwave.com/_api/mcp
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: Aerwave is a Dallas, Texas managed Wi-Fi provider founded in 2019 that builds and operates fiber-backed, property-wide wireless networks for multifamily apartment communities and student housing. Its HomeWiFi platform gives each resident a private, VLAN-isolated network with individual encryption and instant-on gigabit service without a rented router, while property owners and managers get a SaaS portal for network management, resident onboarding and support. Aerwave publishes no public developer program or API documentation; the machine-readable surface it does serve is an llms.txt and a live, anonymous Model Context Protocol endpoint on its marketing site, both provided by its Wix hosting platform.
image: https://register.getaerwave.com/images/aerwave_website_logo.png
layout: provider
modified: '2026-09-12'
name: Aerwave
nav: Providers
network: true
random_paper: 12
slug: aerwave
tags:
- Company
- Managed WiFi
- Multifamily
- Real Estate
- Telecommunications
- Internet Service Provider
- Connectivity
- Smart Buildings
- PropTech
---
