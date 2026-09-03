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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evergreen-theragnostics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.evergreentgn.com/
- group: company
  title: ''
  type: About
  url: https://www.evergreentgn.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.evergreentgn.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.evergreentgn.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evergreentgn.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.evergreentgn.com/terms-of-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/evergreentgn
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/evergreen-theragnostics_stock/
coverage:
  checked: '2026-08-12'
  detail: Evergreen Theragnostics is a cGMP radiopharmaceutical CDMO and drug developer whose product is manufactured radioligand doses, not software — its six-page WordPress marketing site has no developer, docs, or api subdomain (all three fail to resolve in DNS), no GitHub organization, and every /.well-known/ path returns the theme 404 page.
  evidence:
  - status: 404
    url: https://www.evergreentgn.com/.well-known/agent-card.json
  - status: 404
    url: https://www.evergreentgn.com/openapi.json
  - status: 404
    url: https://www.evergreentgn.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/evergreentgn
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: 'Evergreen Theragnostics is a Springfield, New Jersey radiopharmaceutical company founded in 2019 that operates a cGMP contract development and manufacturing organization (CDMO) for therapeutic and diagnostic radiopharmaceuticals, alongside its own clinical pipeline of theragnostic pairs including the OCTEVY PET diagnostic imaging agent for neuroendocrine tumors. Its 14,000 square foot Springfield facility carries seven commercial-scale production suites, sterility lines, quality control and packaging space serving radioligand therapy developers. Lantheus Holdings completed its acquisition of the company on April 1, 2025, and Evergreen now operates as part of Lantheus. The company sells manufacturing services and drug products, not software: it publishes no developer program, no public API, and no machine-readable specifications.'
image: https://www.evergreentgn.com/wp-content/uploads/evergreen-theragnostics-og-img.jpg
layout: provider
modified: '2026-08-12'
name: Evergreen Theragnostics
nav: Providers
network: true
overview: 'Evergreen Theragnostics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Pharmaceuticals, Life Sciences, and Manufacturing.


  Evergreen Theragnostics'' developer surface includes engineering blog and 8 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evergreen-theragnostics/refs/heads/main/screenshots/evergreen-theragnostics-2026-09-02T145444.png
security:
- kind: domain-security
  name: Evergreen Theragnostics Domain Security
  slug: evergreen-theragnostics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: evergreen-theragnostics
tags:
- Company
- Healthcare
- Pharmaceuticals
- Life Sciences
- Manufacturing
- Radiopharmaceuticals
- Oncology
- Contract Manufacturing
- Medical Imaging
website: https://www.evergreentgn.com/
---
