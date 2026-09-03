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
- group: company
  title: ''
  type: Website
  url: https://orasis-pharma.com/
- group: company
  title: ''
  type: About
  url: https://orasis-pharma.com/about
- group: operate
  title: ''
  type: Support
  url: https://orasis-pharma.com/contact
- group: company
  title: ''
  type: Blog
  url: https://orasis-pharma.com/press-releases
- group: commercial
  title: ''
  type: TermsOfService
  url: https://orasis-pharma.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://orasis-pharma.com/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orasis-pharmaceuticals-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orasis-pharmaceuticals-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Orasis Pharmaceuticals is a commercial-stage ophthalmic drug maker whose product is a prescription eye drop (QLOSI); its three HubSpot-hosted sites carry no /developers, /api or /docs section at all, and every contract-discovery path probed on orasis-pharma.com, qlosi.com and qlosiecp.com returned the CMS 404 page.
  evidence:
  - status: 404
    url: https://orasis-pharma.com/openapi.json
  - status: 404
    url: https://orasis-pharma.com/api-docs
  - status: 404
    url: https://orasis-pharma.com/.well-known/api-catalog
  - status: 404
    url: https://qlosi.com/.well-known/agent-card.json
  - status: 200
    url: https://orasis-pharma.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Orasis Pharmaceuticals is an ophthalmic pharmaceutical company with offices in the United States and Israel, focused on treatments for presbyopia — the age-related loss of near vision that affects roughly two billion people worldwide. Its lead product, QLOSI (pilocarpine hydrochloride ophthalmic solution) 0.4%, is a preservative-free, single-use-vial prescription eye drop approved by the FDA in October 2023 and commercially available in the United States, with a follow-on candidate (BESKA) submitted for approval in Australia. The company is backed by life-sciences investors including Sequoia Capital, Johnson & Johnson Innovation and Arboretum Ventures. Orasis sells a regulated pharmaceutical product, not software: it operates a corporate marketing site plus product sites for patients (qlosi.com) and eye care professionals (qlosiecp.com), and publishes no developer program, public API, SDK, webhook surface or machine-readable API contract of any kind.'
image: https://orasis-pharma.com/hubfs/HQ%20Only/Orasis_Pharmaceuticals_Logo_RGB.svg
layout: provider
modified: '2026-08-26'
name: Orasis Pharmaceuticals
nav: Providers
network: true
overview: 'Orasis Pharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Life Sciences, Ophthalmology, and Healthcare.


  Orasis Pharmaceuticals'' developer surface includes support, engineering blog, and 6 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orasis-pharmaceuticals/refs/heads/main/screenshots/orasis-pharmaceuticals-2026-09-02T150854.png
security:
- kind: domain-security
  name: Orasis Pharmaceuticals Domain Security
  slug: orasis-pharmaceuticals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: orasis-pharmaceuticals
tags:
- Company
- Pharmaceuticals
- Life Sciences
- Ophthalmology
- Healthcare
- Vision
- Presbyopia
- Biotechnology
- Israel
website: https://orasis-pharma.com/
---
