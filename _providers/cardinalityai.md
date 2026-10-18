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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cardinalityai/refs/heads/main/hosts/cardinalityai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cardinalityai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cardyai.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cardyai.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.cardyai.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cardinalityai/refs/heads/main/security/cardinalityai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cardinalityai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cardyai.com
coverage:
  checked: '2026-10-07'
  detail: Homepage is a JavaScript‑rendered Angular app with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://www.cardyai.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Cardinalityai provides AI‑powered case management SaaS solutions for government agencies, nonprofits, and health plans. Their platform modernizes social services workflows, offering modular low‑code tools, rules engines, and integrated APIs to improve citizen outcomes, reduce fraud, and accelerate implementation across multiple states.
image: https://www.cardyai.com/assets/images/OG_cardy.png
layout: provider
modified: '2026-10-07'
name: Cardinalityai
nav: Providers
network: true
overview: Cardinalityai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Software-as-a-Service, Case Management, and Government.
random_paper: 10
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cardinalityai Domain Security
  slug: cardinalityai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cardinalityai
tags:
- Company
- Artificial Intelligence
- Software-as-a-Service
- Case Management
- Government
website: https://www.cardyai.com
---
