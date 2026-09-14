---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agrist-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agrist.com/
- group: company
  title: ''
  type: About
  url: https://agrist.com/about-agrist-english
- group: other
  title: ''
  type: Summary
  url: https://agrist.com/corporate/company
- group: company
  title: ''
  type: Newsroom
  url: https://agrist.com/news
- group: company
  title: ''
  type: Blog
  url: https://agrist.com/archives/category/column
- group: company
  title: ''
  type: BlogRSS
  url: https://agrist.com/feed
- group: operate
  title: ''
  type: PressReleases
  url: https://agrist.com/archives/category/pressrelease
- group: operate
  title: ''
  type: FAQ
  url: https://agrist.com/faq
- group: operate
  title: ''
  type: ContactUs
  url: https://agrist.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agrist.com/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://agrist.com/recruit
- group: other
  title: ''
  type: Sustainability
  url: https://agrist.com/sustainability
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agrist/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/agrist_inc
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/AGRIST_INC
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/agrist_inc/
coverage:
  checked: '2026-09-13'
  detail: AGRIST sells harvesting robots and the bundled AGRIST Ai cultivation-support system directly to greenhouse farmers as a turnkey package, and its 48-page WordPress site has no developer, documentation, API or integration section at all — contract discovery against agrist.com and www.agrist.com returned a hard 404 for /openapi.json, /llms.txt, /apis.json and every named /.well-known/ path, the only certificate-issued subdomain (farmpr.agrist.com) no longer resolves in DNS, and the single machine-readable surface on the domain is the stock WordPress core REST API at /wp-json whose 231 routes are entirely CMS and plugin namespaces (wp/v2, oembed, Wordfence, Site Kit, SiteOrigin), not an AGRIST product.
  evidence:
  - status: 404
    url: https://agrist.com/openapi.json
  - status: 404
    url: https://agrist.com/llms.txt
  - status: 404
    url: https://agrist.com/.well-known/agent-card.json
  - status: 200
    url: https://agrist.com/wp-sitemap-posts-page-1.xml
  - status: 200
    url: https://agrist.com/wp-json/
  reason: no-developer-program
  state: none
created: '2026-09-13'
description: 'AGRIST Inc. (AGRIST株式会社) is a Japanese deep-tech agricultural robotics company founded in October 2019 and headquartered in Shintomi-cho, Koyu-gun, Miyazaki Prefecture, with an AI robot farm in Higashikushira (Kagoshima), an AI robot test facility in Shintomi-cho and the AGRIST Joso Farm in Joso City, Ibaraki. Its flagship product is "L", an automatic bell-pepper harvesting robot that travels along overhead wires strung between greenhouse rows rather than on ground rails, using multiple cameras and a proprietary computer-vision model to find and cut harvest-ready fruit through layered foliage; a cucumber harvesting robot followed. Around the hardware the company sells AGRIST Ai, a greenhouse cultivation-support and yield-forecasting system fed by robot patrol data and environmental sensors, and it operates its own farms plus Smart Agri University (SAU), a nine-month smart-agriculture training program. AGRIST is venture-backed through a Series B that includes Mizuho Capital,
  Global Infrastructure Management, Nippon Steel Kowa Real Estate, Nippon Express Holdings, Takamiya and Sparx, and has taken more than 27 domestic and international awards including a CES 2023 Innovation Award and a Japanese Minister of Agriculture, Forestry and Fisheries Award. It is a robotics and farm-operations business, not a software vendor: as of 2026-09-13 it publishes no developer program, no public API, no SDK and no machine-readable API contract of any kind.'
image: https://agrist.com/wp-content/uploads/2020/12/logo.png
layout: provider
modified: '2026-09-13'
name: Agrist
nav: Providers
network: true
overview: 'Agrist is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Robotics, and Artificial Intelligence.


  Agrist''s developer surface includes engineering blog, FAQ, YouTube channel, and 14 more developer resources.'
random_paper: 20
security:
- kind: domain-security
  name: Agrist Domain Security
  slug: agrist-domain-security
  summary_line: TLSv1.3
slug: agrist
tags:
- Company
- Agriculture
- AgTech
- Robotics
- Artificial Intelligence
- Computer Vision
- Smart Farming
- Greenhouse
- Automation
- Food Tech
- Deep Tech
- Japan
website: https://agrist.com/
---
