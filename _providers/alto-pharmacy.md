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
  url: security/alto-pharmacy-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alto-pharmacy-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.alto.com/
- group: company
  title: ''
  type: Blog
  url: https://www.alto.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scriptdash
- group: operate
  title: ''
  type: Support
  url: https://www.alto.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alto.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alto.com/legal/privacy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/alto-pharmacy_stock/
coverage:
  checked: '2026-08-06'
  detail: Alto's Partner Solutions page advertises "intake and transfer APIs" and "Surescripts or transfer API intake" but routes every technical inquiry to partnerships@alto.com — there is no developer portal, no API reference and no spec anywhere on alto.com, and the live API host api.alto.com answers a bare plaintext "404 page not found" on every documented path while serving 200 only on /healthz.
  evidence:
  - status: 200
    url: https://www.alto.com/blog/post/partner-solutions
  - status: 404
    url: https://api.alto.com/openapi.json
  - status: 200
    url: https://api.alto.com/healthz
  - status: 404
    url: https://api.alto.com/graphql
  - status: 404
    url: https://www.alto.com/llms.txt
  - status: 404
    url: https://www.alto.com/.well-known/agent-card.json
  - status: 0
    url: https://developer.alto.com/
  reason: sales-gate
  state: gated
created: '2026-08-06'
description: Alto Pharmacy is a San Francisco-based digital pharmacy and pharmacy-technology company (founded 2015 as ScriptDash) that combines a full-service licensed pharmacy with a proprietary pharmacy operating system, Alto OS. Alto fills retail, specialty and fertility prescriptions with same-day courier delivery, pharmacist care and automated benefits investigation, and it sells that stack to industry partners as Alto Hub+, Alto Dispensing and Alto Complete — hub services, dispensing and end-to-end pharmacy-as-a-service for pharmaceutical manufacturers, health plans, health systems and digital health companies. Alto markets intake, transfer and Surescripts-based integrations to those partners, but publishes no public developer portal, API documentation or machine-readable specification; technical access runs through its partnerships team.
image: https://www.alto.com/logo
layout: provider
modified: '2026-08-06'
name: Alto Pharmacy
nav: Providers
network: true
overview: 'Alto Pharmacy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmacy, Digital Health, Healthcare, and Prescriptions.


  Alto Pharmacy''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.5
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alto-pharmacy/refs/heads/main/screenshots/alto-pharmacy-2026-08-07T161250.png
security:
- kind: domain-security
  name: Alto Pharmacy Domain Security
  slug: alto-pharmacy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alto-pharmacy
tags:
- Company
- Pharmacy
- Digital Health
- Healthcare
- Prescriptions
- Specialty Pharmacy
- Fertility
- Medication Delivery
- Pharmacy Technology
- Health Plans
website: https://www.alto.com/
---
