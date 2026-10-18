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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Integration platform API (not publicly documented)
  name: Credence MedSystems API
  slug: credence-medsystems-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/credence-medsystems/refs/heads/main/llms/credence-medsystems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/credence-medsystems-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/credence-medsystems/refs/heads/main/hosts/credence-medsystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/credence-medsystems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/credence-medsystems/refs/heads/main/vendors/credence-medsystems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/credence-medsystems-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.credencemed.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.credencemed.com/about/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.credencemed.com/about/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.credencemed.com/about/industry-education/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/credence-medsystems/refs/heads/main/security/credence-medsystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/credence-medsystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.credencemed.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.credencemed.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Credence MedSystems is a healthcare technology company focused on providing advanced medical device integration platforms for hospitals and clinics. The firm offers middleware solutions that connect diagnostic equipment, electronic health records, and patient monitoring systems, enabling seamless data exchange and workflow automation. Their services aim to improve clinical efficiency, data accuracy, and patient outcomes through secure, scalable integration services.
image: https://www.credencemed.com/logo.png
layout: provider
modified: '2026-10-11'
name: Credence MedSystems
nav: Providers
network: true
overview: 'Credence MedSystems is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Devices, Integration, and Middleware.


  Credence MedSystems'' developer surface includes engineering blog and 8 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Credence Medsystems Domain Security
  slug: credence-medsystems-domain-security
  summary_line: TLSv1.3 · DMARC
slug: credence-medsystems
tags:
- Company
- Healthcare
- Medical Devices
- Integration
- Middleware
website: https://www.credencemed.com/
---
