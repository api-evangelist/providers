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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autoxing/refs/heads/main/hosts/autoxing-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autoxing-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autoxing.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autoxing.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://autoxing.com/news/category/news
- group: docs
  title: ''
  type: Documentation
  url: https://doc.autoxing.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autoxing/refs/heads/main/security/autoxing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autoxing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autoxing.com
coverage:
  checked: 2026-09-26
  detail: Documentation at https://doc.autoxing.com/ provides no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://doc.autoxing.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: AutoXing is a leading provider of intelligent robot services based on autonomous driving technology. The company focuses on AGV and AMR robots for factories, logistics, restaurants, and hotels, aiming to empower smart retail and improve efficiency through AI-driven navigation and big data integration. AutoXing’s mission is to use smart technology to enable a better life, offering a range of autonomous delivery vehicles, robot chassis, and customized solutions for various industries.
layout: provider
modified: '2026-09-26'
name: Autoxing
nav: Providers
network: true
overview: 'Autoxing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Automation, Artificial Intelligence, Logistics, and Manufacturing.


  Autoxing''s developer surface includes documentation and 6 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autoxing Domain Security
  slug: autoxing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: autoxing
tags:
- Robotics
- Automation
- Artificial Intelligence
- Logistics
- Manufacturing
- Company
website: https://autoxing.com
---
