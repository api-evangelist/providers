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
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pattern-bioscience-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pattern-bioscience-llms.txt
- group: company
  title: ''
  type: Website
  url: https://pattern.bio/
- group: company
  title: ''
  type: About
  url: https://pattern.bio/about-us/
- group: other
  title: ''
  type: Technology
  url: https://pattern.bio/our-tech/
- group: other
  title: ''
  type: Science
  url: https://pattern.bio/our-science/
- group: company
  title: ''
  type: Blog
  url: https://pattern.bio/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://pattern.bio/feed/
- group: company
  title: ''
  type: News
  url: https://pattern.bio/news/
- group: operate
  title: ''
  type: Support
  url: https://pattern.bio/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://pattern.bio/join-us/
- group: other
  title: ''
  type: Glossary
  url: https://pattern.bio/glossary/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pattern.bio/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pattern.bio/privacy-policy/
- group: company
  title: ''
  type: Newsletter
  url: https://pattern.bio/sign-up/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/patternbio
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/pattern-bioscience
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/pattern-bioscience_stock/
coverage:
  checked: '2026-08-04'
  detail: Pattern Bioscience is a pre-commercial in vitro diagnostics manufacturer whose product is a physical Single-Cell Microbiology instrument and test panel awaiting FDA clearance; pattern.bio is a twelve-page WordPress marketing site where /api, /docs, /developers, /openapi.json and every /.well-known/ path return 404 and no api., app., docs. or developer. subdomain resolves in DNS.
  evidence:
  - status: 404
    url: https://pattern.bio/developers
  - status: 404
    url: https://pattern.bio/openapi.json
  - status: 404
    url: https://pattern.bio/.well-known/agent-card.json
  - status: 404
    url: https://pattern.bio/.well-known/security.txt
  - status: 404
    url: https://pattern.bio/llms.txt
  - status: 200
    url: https://pattern.bio/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-04'
description: 'Pattern Bioscience is a privately held in vitro diagnostics company founded in 2016 and headquartered in Austin, Texas, developing a culture-free Single-Cell Microbiology system for rapid bacterial identification and antibiotic susceptibility testing (ID/AST). The platform isolates individual bacterial cells in picoliter-scale droplets and reads the metabolic patterns those cells produce over time, using machine learning to identify the pathogen and determine phenotypic susceptibility in hours instead of the days a culture workflow requires. The company holds FDA Breakthrough Device Designation for its Pneumonia Action Panel, raised $43M in Series D financing in November 2025 to pursue FDA clearance, and is backed by Illumina Ventures, Omnimed Capital, CARB-X, the AMR Action Fund and a $22.5M BARDA contract. Pattern is pre-commercial: it publishes a marketing and news site at pattern.bio and no public API, developer portal, SDK or machine-readable specification.'
image: https://pattern.bio/wp-content/uploads/2019/10/PatternLogo_black.svg
layout: provider
modified: '2026-08-04'
name: Pattern Bioscience
nav: Providers
network: true
overview: 'Pattern Bioscience is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Diagnostics, Healthcare, Medical Devices, and In Vitro Diagnostics.


  Pattern Bioscience''s developer surface includes engineering blog, product news, support, and 15 more developer resources.'
random_paper: 115
score:
  band: minimal
  composite: 12.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pattern-bioscience/refs/heads/main/screenshots/pattern-bioscience-2026-08-07T191603.png
security:
- kind: domain-security
  name: Pattern Bioscience Domain Security
  slug: pattern-bioscience-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pattern-bioscience
tags:
- Company
- Diagnostics
- Healthcare
- Medical Devices
- In Vitro Diagnostics
- Microbiology
- Antimicrobial Resistance
- Life Sciences
- Machine Learning
- Austin
website: https://pattern.bio/
---
