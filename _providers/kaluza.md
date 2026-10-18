---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Kaluza's energy intelligence platform providing data, analytics, and integration capabilities.
  name: Kaluza Energy Platform API
  slug: kaluza-energy-platform-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kaluza/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kaluza/refs/heads/main/llms/kaluza-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kaluza-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kaluza/refs/heads/main/hosts/kaluza-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kaluza-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kaluza/refs/heads/main/vendors/kaluza-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kaluza-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kaluza.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kaluza.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.kaluza.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.kaluza.com/about-us/team
- group: company
  title: ''
  type: Blog
  url: https://www.kaluza.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kaluza.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kaluza/refs/heads/main/security/kaluza-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kaluza-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kaluza.com
coverage:
  checked: '2026-10-13'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.kaluza.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Kaluza provides intelligent energy data management and optimisation software, helping energy retailers and suppliers to automate decision‑making, improve customer engagement, and accelerate the transition to net‑zero. Their platform offers real‑time analytics, flexible pricing, and integration capabilities across meters, market data, and customer systems, enabling smarter energy services and operational efficiency.
image: https://cdn.prod.website-files.com/68ad7ea636513871784163e4/68d3cfc0513f287f333585de_2d474dac4bd95ce02f8d039a155a6655_Kaluza%20OpenG.png
layout: provider
modified: '2026-10-13'
name: Kaluza
nav: Providers
network: true
overview: 'Kaluza is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Software, Data, Optimisation, and Retail.


  Kaluza''s developer surface includes engineering blog, documentation, and 10 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 18.3
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kaluza Domain Security
  slug: kaluza-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kaluza
tags:
- Energy
- Software
- Data
- Optimisation
- Retail
website: https://www.kaluza.com
---
