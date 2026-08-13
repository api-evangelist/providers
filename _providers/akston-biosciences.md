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
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.akstonbio.com/
- group: company
  title: ''
  type: About
  url: https://www.akstonbio.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.akstonbio.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.akstonbio.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://www.akstonbio.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.akstonbio.com/careers/
- group: other
  title: ''
  type: Team
  url: https://www.akstonbio.com/team/
- group: company
  title: ''
  type: Partners
  url: https://www.akstonbio.com/partners/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/akston-biosciences-corporation/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/akston-biosciences-domain-security.yml
coverage:
  checked: '2026-08-06'
  detail: Akston Biosciences is a veterinary protein-therapeutics developer and manufacturer whose entire web presence is a nine-page WordPress marketing site (about/process/pipeline/news/careers/contact) with no developer section; api., developer., docs. and portal.akstonbio.com are all NXDOMAIN and every spec and .well-known probe returned 404.
  evidence:
  - status: 404
    url: https://www.akstonbio.com/openapi.json
  - status: 404
    url: https://www.akstonbio.com/llms.txt
  - status: 404
    url: https://www.akstonbio.com/.well-known/agent-card.json
  - status: 404
    url: https://www.akstonbio.com/.well-known/security.txt
  - status: 200
    url: https://www.akstonbio.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Akston Biosciences Corporation is a privately held biotechnology company headquartered in Beverly, Massachusetts, founded in 2011 by the team from SmartCells, Inc. and led by CEO Todd Zion, Ph.D. Akston designs, develops and manufactures protein therapeutics built on its proprietary Ambifect Fc-fusion protein platform, with a pipeline focused on companion-animal (veterinary) medicine: PD-L1 monoclonal antibody oncology candidates (AKS-701d, AKS-619d), a long-acting GLP-1 for feline weight management (AKS-562c), an IL-31 targeting therapy for canine pruritus (AKS-699), and NGF-targeting candidates for osteoarthritis pain. Its veterinary insulin program was sold to Dechra in 2024, and human programs continue through the Vakston and Diamune Therapeutics subsidiaries. The company announced a manufacturing expansion in Shreveport, Louisiana. Akston is a therapeutics developer and manufacturer, not a software vendor: it publishes a corporate marketing site and no public API, SDK,
  developer portal or machine-readable specification.'
image: https://www.akstonbio.com/wp-content/themes/ssw-akston/assets/images/header/akston-logo.svg
layout: provider
modified: '2026-08-06'
name: Akston Biosciences
nav: Providers
network: true
overview: 'Akston Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Pharmaceuticals, and Animal Health.


  Akston Biosciences'' developer surface includes engineering blog and 9 more developer resources.'
random_paper: 60
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/akston-biosciences/refs/heads/main/screenshots/akston-biosciences-2026-08-07T161135.png
security:
- kind: domain-security
  name: Akston Biosciences Domain Security
  slug: akston-biosciences-domain-security
  summary_line: TLSv1.3
slug: akston-biosciences
tags:
- Company
- Biotechnology
- Life Sciences
- Pharmaceuticals
- Animal Health
- Veterinary Medicine
- Protein Therapeutics
- Biomanufacturing
website: https://www.akstonbio.com/
---
