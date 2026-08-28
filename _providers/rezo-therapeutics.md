---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.2
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rezo-therapeutics-domain-security.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/rezo-therapeutics-content-signals.yml
- group: company
  title: ''
  type: Website
  url: https://rezotx.com/
- group: company
  title: ''
  type: Blog
  url: https://rezotx.com/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rezotx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rezotx.com/terms-of-use/
- group: company
  title: ''
  type: About
  url: https://rezotx.com/technology/
- group: company
  title: ''
  type: Careers
  url: https://rezotx.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rezotx
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/rezo-therapeutics
coverage:
  checked: '2026-08-26'
  detail: Rezo Therapeutics is a clinical-stage biopharmaceutical company whose entire public web presence is nine WordPress pages (home, technology, team, careers, news, investors, privacy, terms, one stub) with no developer, docs, or API section anywhere in its sitemap; the only machine-readable surface on rezotx.com is the generic WordPress core and Jetpack /wp-json route index that every WordPress.com-hosted site serves, which is site infrastructure and not a product API.
  evidence:
  - status: 200
    url: https://rezotx.com/wp-sitemap-posts-page-1.xml
  - status: 404
    url: https://rezotx.com/openapi.json
  - status: 404
    url: https://rezotx.com/graphql
  - status: 404
    url: https://rezotx.com/llms.txt
  - status: 404
    url: https://rezotx.com/.well-known/agent-card.json
  - status: 404
    url: https://rezotx.com/.well-known/agent.json
  - status: 404
    url: https://rezotx.com/.well-known/security.txt
  - status: 404
    url: https://rezotx.com/.well-known/api-catalog
  - status: 200
    url: https://rezotx.com/robots.txt
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Rezo Therapeutics is a San Francisco (Mission Bay) biopharmaceutical company spun out of the Quantitative Biosciences Institute (QBI) at UCSF, co-founded by Nevan Krogan, that is building a disease-agnostic network-biology drug discovery platform. Its "sequence to systems to drugs" approach integrates proteomics, human genetics, structural biology, medicinal chemistry, bioinformatics and machine learning to construct comprehensive maps of molecular disease networks and identify novel, druggable targets for precision therapeutics, with an initial focus on oncology. The company launched in November 2022 with a $78M Series A led by SR One, a16z Bio + Health and Norwest Venture Partners, and appointed Derek Hicks as chief executive officer in August 2025. Rezo is a therapeutics developer rather than a software vendor: its computational platform is internal R&D tooling, and the company publishes no public API, SDK, developer portal or machine-readable contract of any kind.'
image: https://i0.wp.com/rezotx.com/wp-content/uploads/2026/03/cropped-Rezo-Icon-Favicon-1.png?fit=512%2C512&ssl=1
layout: provider
modified: '2026-08-26'
name: Rezo Therapeutics
nav: Providers
network: true
overview: 'Rezo Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Oncology.


  Rezo Therapeutics'' developer surface includes engineering blog and 9 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.5
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Rezo Therapeutics Domain Security
  slug: rezo-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rezo-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Oncology
- Proteomics
- Life Sciences
- Precision Medicine
- Artificial Intelligence
- Health
website: https://rezotx.com/
---
