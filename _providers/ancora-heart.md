---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ancora-heart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ancoraheart.com/
- group: company
  title: ''
  type: About
  url: https://www.ancoraheart.com/about-us/
- group: operate
  title: ''
  type: Support
  url: https://www.ancoraheart.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.ancoraheart.com/in-the-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ancoraheart.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ancoraheart.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ancoraheart.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/24214239/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/AncoraHeart
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCufcpLIcuygJzvUs1tlHwUA
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/AncoraHeart
coverage:
  checked: '2026-08-06'
  detail: Ancora Heart manufactures an implantable cardiac device (the AccuCinch Ventricular Restoration System) and runs ancoraheart.com purely as a WordPress marketing and clinical-trial information site; the only machine-readable endpoint on the domain is the WordPress core REST API that ships with the CMS, and every contract-discovery path returns the site's soft-404 HTML shell with a 200.
  evidence:
  - status: 200
    url: https://www.ancoraheart.com/openapi.json
  - status: 200
    url: https://www.ancoraheart.com/this-path-definitely-does-not-exist-9x8z7
  - status: 200
    url: https://www.ancoraheart.com/.well-known/agent-card.json
  - status: 404
    url: https://www.ancoraheart.com/.well-known/security.txt
  - status: 404
    url: https://www.ancoraheart.com/llms.txt
  - status: 200
    url: https://www.ancoraheart.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Ancora Heart, Inc. is a privately held medical device company headquartered at 4001 Burton Drive, Santa Clara, California, developing transcatheter therapies for people living with heart failure. Its lead product is the AccuCinch Ventricular Restoration System, a completely transcatheter implant designed to reduce the size of an enlarged left ventricle and restore cardiac structure and function in patients with heart failure with reduced ejection fraction (HFrEF) who remain symptomatic on guideline-directed medical therapy. The device is investigational and is being evaluated in the CORCINCH-HF study (NCT04331769), a prospective randomized international trial enrolling up to 400 patients across as many as 80 centers, alongside the CORCINCH-EU program in Europe. Ancora Heart is a medical device manufacturer rather than a software company: it publishes a marketing and clinical-information website for patients and physicians, and operates no public developer program, API, or SDK.'
image: https://www.ancoraheart.com/wp-content/themes/ancora/public/images/NEW_AncoraLogo_Color.svg
layout: provider
modified: '2026-08-06'
name: Ancora Heart
nav: Providers
network: true
overview: 'Ancora Heart is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Health Care, Cardiology, and Heart Failure.


  Ancora Heart''s developer surface includes support, engineering blog, YouTube channel, and 9 more developer resources.'
random_paper: 75
score:
  band: minimal
  composite: 10.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: domain-security
  name: Ancora Heart Domain Security
  slug: ancora-heart-domain-security
  summary_line: TLSv1.3
slug: ancora-heart
tags:
- Company
- Medical Devices
- Health Care
- Cardiology
- Heart Failure
- Clinical Trials
- Transcatheter Therapy
- Medical Technology
website: https://www.ancoraheart.com/
---
