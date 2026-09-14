---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/saphlux-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.saphlux.com/
- group: company
  title: ''
  type: Blog
  url: https://www.saphlux.com/blog-3
- group: company
  title: ''
  type: BlogRSS
  url: https://www.saphlux.com/blog-3?format=rss
- group: operate
  title: ''
  type: Support
  url: https://www.saphlux.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.saphlux.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.saphlux.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/saphlux-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/saphlux-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/saphlux-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: Saphlux is a semiconductor materials and display-module manufacturer — it sells semi-polar (20-21) GaN-on-sapphire epitaxial wafers and NPQD quantum-dot Micro-LED panels to display OEMs — and its entire public surface is a four-item Squarespace marketing site (Home / Products / Newsroom / Contact) whose 150-URL sitemap contains no developer, docs, or API reference page at all.
  evidence:
  - status: 200
    url: https://www.saphlux.com/sitemap.xml
  - status: 404
    url: https://www.saphlux.com/developers
  - status: 404
    url: https://www.saphlux.com/openapi.json
  - status: 404
    url: https://www.saphlux.com/llms.txt
  - status: 404
    url: https://www.saphlux.com/.well-known/agent-card.json
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Saphlux is a quantum dot Micro-LED (QD-MLED) display technology company founded in 2014 out of Yale University and headquartered in San Diego, California, with additional operations in China and Japan. It commercialized semi-polar (20-21) GaN-on-sapphire epitaxial wafers to address efficiency droop and the green gap in nitride emitters, and now mass-produces NPQD quantum-dot Micro-LED devices. Its product lineup spans QD-COB and QD-COB Pro Series panels for large-format commercial and home-theater displays and the T-Series monolithic full-color micro-displays for all-day wearable AR eyewear and AI smart glasses. Saphlux is a semiconductor materials and display-module manufacturer that sells hardware to OEMs and display integrators; it publishes no public developer program, API, or SDK.
image: https://static1.squarespace.com/static/60f70a871d58107fff2b086c/t/6511e9a071a8b360ae17c10e/1695672736192/logo.png?format=1500w
layout: provider
modified: '2026-08-26'
name: Saphlux
nav: Providers
network: true
overview: 'Saphlux is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Displays, Micro-LED, and Quantum Dots.


  Saphlux''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Saphlux Plans Pricing
  plan_count: 0
  slug: saphlux-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Saphlux Rate Limits
  slug: saphlux-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/saphlux/refs/heads/main/screenshots/saphlux-2026-09-02T154408.png
security:
- kind: domain-security
  name: Saphlux Domain Security
  slug: saphlux-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: saphlux
tags:
- Company
- Semiconductors
- Displays
- Micro-LED
- Quantum Dots
- Hardware
- Augmented Reality
- Optoelectronics
- Manufacturing
website: https://www.saphlux.com/
---
