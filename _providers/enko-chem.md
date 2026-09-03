---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
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
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enko-chem-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enko-chem-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.enko.ag/
- group: company
  title: ''
  type: About
  url: https://www.enko.ag/about-enko
- group: other
  title: ''
  type: Platform
  url: https://www.enko.ag/our-platform
- group: company
  title: ''
  type: Blog
  url: https://www.enko.ag/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/enko-chem
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enko.ag/privacy-policy
- group: commercial
  title: ''
  type: Legal
  url: https://www.enko.ag/legal
- group: operate
  title: ''
  type: Contact
  url: https://www.enko.ag/contact
- group: company
  title: ''
  type: Careers
  url: https://www.enko.ag/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/enko-ag
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/enko-chem_stock/
coverage:
  checked: '2026-08-12'
  detail: Enko is a crop-protection chemistry R&D company whose ENKOMPASS platform is internal discovery tooling, not a product — the Webflow marketing site 404s on every spec, docs and .well-known path, no api/docs/developer subdomain resolves, and the github.com/enko-chem org holds only seven forks of third-party scientific tools with no first-party code.
  evidence:
  - status: 404
    url: https://www.enko.ag/openapi.json
  - status: 404
    url: https://www.enko.ag/.well-known/agent-card.json
  - status: 404
    url: https://www.enko.ag/developers
  - status: 404
    url: https://www.enko.ag/llms.txt
  - status: 200
    url: https://api.github.com/orgs/enko-chem/repos
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: Enko Chem, Inc. (Enko) is an agricultural life sciences company founded in 2017 and headquartered in Mystic, Connecticut, where it operates an 89,000 sq ft research lab and greenhouse campus. Enko discovers and develops next-generation crop protection chemistry — weed, disease, insect and soil-pest control — using its proprietary ENKOMPASS platform, which combines DNA-encoded library screening, structure-based design, artificial intelligence and machine learning to identify new modes of action and lead molecules faster and at lower cost than conventional agrochemical R&D. Enko works through partnerships with Syngenta, Bayer, Nufarm and the Gates Foundation Strategic Investment Fund rather than selling software, and publishes no public API, developer portal, SDK or machine-readable specification.
image: https://cdn.prod.website-files.com/62956a153328518931d92e9b/629ec5af86f484f75e7538b7_Enko%20Logo%20Dark.svg
layout: provider
modified: '2026-08-12'
name: Enko Chem
nav: Providers
network: true
overview: 'Enko Chem is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Crop Protection, and Agrochemicals.


  Enko Chem''s developer surface includes engineering blog, legal docs, and 11 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enko-chem/refs/heads/main/screenshots/enko-chem-2026-09-02T145403.png
security:
- kind: domain-security
  name: Enko Chem Domain Security
  slug: enko-chem-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: enko-chem
tags:
- Company
- Agriculture
- AgTech
- Crop Protection
- Agrochemicals
- Life Sciences
- Chemistry
- Artificial Intelligence
- Machine-Learning
- Drug Discovery
- Research and Development
website: https://www.enko.ag/
---
