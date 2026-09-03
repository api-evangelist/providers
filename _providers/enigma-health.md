---
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enigma-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://enigma-health.org/
- group: design
  title: ''
  type: Conformance
  url: conformance/enigma-health-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/enigma-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/enigma-health-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enigma-health-llms.txt
coverage:
  checked: '2026-09-02'
  detail: enigma-health.org serves a one-page WordPress 'Coming Soon' splash whose Yoast sitemap lists only the home page and the untouched default /sample-page/, and no api./docs./developer./app./portal. subdomain resolves at all, so this pre-launch openEHR startup has no developer surface to read.
  evidence:
  - status: 200
    url: https://enigma-health.org/
  - status: 200
    url: https://enigma-health.org/page-sitemap.xml
  - status: 404
    url: https://enigma-health.org/developers
  - status: 404
    url: https://enigma-health.org/openapi.json
  - status: 404
    url: https://enigma-health.org/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: 'Enigma Health (Enigma Global eHealth) is a Netherlands-based digital health startup building a secure, private eHealth portal intended to connect patients, doctors and healthcare institutions, and to give patients lifelong, worldwide access to their own electronic health record together with a digital vaccine passport kept in sync with that record. Founded by Dutch GP and global-health researcher Remko Schats and incubated at UtrechtInc, the company is a Startup level Industry Partner of the openEHR International Foundation, placing its intended data layer on the openEHR clinical data platform standard rather than a proprietary record format. As of September 2026 the company is pre-launch: enigma-health.org serves a single ''Coming Soon'' page and Enigma Health publishes no API, SDK, developer portal or machine-readable contract.'
image: https://enigma-health.org/wp-content/uploads/2023/03/Enigma-Health--scaled.jpg
layout: provider
modified: '2026-09-02'
name: Enigma Health
nav: Providers
network: true
overview: Enigma Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Electronic Health Records, and openEHR.
plans:
- name: Enigma Health Plans Pricing
  plan_count: 0
  slug: enigma-health-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Enigma Health Rate Limits
  slug: enigma-health-rate-limits
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Enigma Health Domain Security
  slug: enigma-health-domain-security
  summary_line: TLSv1.2
slug: enigma-health
tags:
- Company
- Health
- Healthcare
- Electronic Health Records
- openEHR
- Digital Health
- Interoperability
- Patient Data
- Netherlands
- Startup
website: https://enigma-health.org/
---
