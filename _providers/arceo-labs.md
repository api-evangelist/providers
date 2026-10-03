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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API reference for Cyber Resilience services as described on the company website.
  name: Cyber Resilience API
  slug: cyber-resilience-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arceo-labs/refs/heads/main/hosts/arceo-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arceo-labs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arceo-labs/refs/heads/main/vendors/arceo-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arceo-labs-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cyberresilience.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arceo-labs/refs/heads/main/security/arceo-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arceo-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cyberresilience.com
coverage:
  checked: 2026-09-25
  detail: Documentation pages are served as JavaScript-rendered HTML, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://cyberresilience.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Cyber Resilience provides cyber insurance and cybersecurity risk management tools to enterprises, including risk quantification, security investment prioritization, and multi‑entity portfolio risk assessment. Its solutions target risk managers, CISOs, and CFOs, offering AI‑driven models that translate technical security posture into financial impact and 24/7 in‑house claims support.
image: https://cyberresilience.com/wp-content/uploads/2026/01/homepage_hero_hero_xl_1-1.webp
layout: provider
modified: '2026-09-25'
name: Cyber Resilience
nav: Providers
network: true
overview: Cyber Resilience publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cyber Insurance, Risk Management, Security Investment Prioritization, Multi‑Entity Risk, and Enterprise Risk.
random_paper: 17
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arceo Labs Domain Security
  slug: arceo-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arceo-labs
tags:
- Cyber Insurance
- Risk Management
- Security Investment Prioritization
- Multi‑Entity Risk
- Enterprise Risk
- CISO
- CFO
website: https://cyberresilience.com
---
