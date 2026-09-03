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
  url: security/syzygy-plasmonics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.plasmonics.tech/
- group: operate
  title: ''
  type: Contact
  url: https://www.plasmonics.tech/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.plasmonics.tech/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.plasmonics.tech/terms-conditions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Syzygy-Plasmonics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/syzygy-plasmonics/
- group: other
  title: ''
  type: Patents
  url: https://www.plasmonics.tech/patents
- group: build
  title: ''
  type: CodeOfConduct
  url: https://www.plasmonics.tech/code-of-conduct-and-anti-corruption-policy
- group: other
  title: ''
  type: Listing
  url: https://forgeglobal.com/syzygy-plasmonics_stock/
coverage:
  checked: '2026-08-29'
  detail: Syzygy Plasmonics sells photocatalytic reactor hardware and SAF process licenses — its entire web presence is a single Next.js marketing page whose nav is SAF Solutions / Technology / Projects / Contact Us, with no developer, docs, or API section, no api./docs./developer. subdomain in DNS, and a GitHub org (Syzygy-Plasmonics) that has existed since 2020 with zero public repositories.
  evidence:
  - status: 200
    url: https://www.plasmonics.tech/
  - status: 404
    url: https://www.plasmonics.tech/openapi.json
  - status: 404
    url: https://www.plasmonics.tech/llms.txt
  - status: 200
    url: https://www.plasmonics.tech/.well-known/api-catalog
  - status: 404
    url: https://www.plasmonics.tech/.well-known/agent-card.json
  - status: 0
    url: https://api.plasmonics.tech/
  - status: 200
    url: https://github.com/Syzygy-Plasmonics
  reason: not-a-software-company
  state: none
created: '2026-08-29'
description: 'Syzygy Plasmonics is a Houston, Texas deep-decarbonization company commercializing photocatalytic chemical manufacturing. Its Rigel reactor cell uses photonic energy from renewable electricity in place of combustion heat to drive reforming reactions, and its NovaSAF / GHG e-Reforming pathway converts waste biogas into low-carbon sustainable aviation fuel, independently assessed as eligible for both ISCC EU RFNBO and Advanced BioSAF certification. Adjacent targets include hydrogen from ammonia e-cracking, syngas, methanol, butadiene and other commodity chemicals, sold as reactor hardware plus a licensing and front-end engineering support package. Syzygy is a hardware and process-licensing business, not a software vendor: as of 2026-08-29 it publishes no developer portal, API reference, SDK, or machine-readable specification of any kind.'
image: https://www.plasmonics.tech/Logo-Desktop-W.svg
layout: provider
modified: '2026-08-29'
name: Syzygy Plasmonics
nav: Providers
network: true
overview: Syzygy Plasmonics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Cleantech, Hydrogen, and Sustainable Aviation Fuel.
random_paper: 2
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/syzygy-plasmonics/refs/heads/main/screenshots/syzygy-plasmonics-2026-09-02T161649.png
security:
- kind: domain-security
  name: Syzygy Plasmonics Domain Security
  slug: syzygy-plasmonics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: syzygy-plasmonics
tags:
- Company
- Energy
- Cleantech
- Hydrogen
- Sustainable Aviation Fuel
- Chemicals
- Decarbonization
- Manufacturing
- Photocatalysis
website: https://www.plasmonics.tech/
---
