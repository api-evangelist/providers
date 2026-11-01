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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/peppermint-robotics/hosts/peppermint-robotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/peppermint-robotics-hosts.yml
- group: other
  href: https://artifacts.apis.io/peppermint-robotics/vendors/peppermint-robotics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/peppermint-robotics-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.peppermintrobotics.com/europe/privacy-policy
- group: auth
  href: https://artifacts.apis.io/peppermint-robotics/security/peppermint-robotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/peppermint-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.peppermintrobotics.com/europe
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.peppermintrobotics.com/europe
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Peppermint Robotics designs and manufactures advanced robotic platforms for industrial automation and logistics. Founded in 2020, the company focuses on modular, AI‑driven robots that can be easily integrated into existing workflows, offering real‑time monitoring, remote control, and scalable solutions for warehouses, factories, and distribution centers. Their flagship product, the MintBot, combines precision navigation with customizable payload options, enabling clients to improve efficiency, reduce labor costs, and enhance safety across operations. Peppermint Robotics continues to innovate with cloud‑connected services, open APIs, and a growing ecosystem of third‑party integrations.
image: https://cdn.prod.website-files.com/66683173b040d2d54b46af65/675a6adcd3e1a5701674b97a_peppermint_robotics_v3.png
layout: provider
modified: '2026-10-24'
name: Peppermint Robotics
nav: Providers
network: true
overview: Peppermint Robotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Automation, AI, and Logistics.
random_paper: 14
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Peppermint Robotics Domain Security
  slug: peppermint-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: peppermint-robotics
tags:
- Company
- Robotics
- Automation
- AI
- Logistics
website: https://www.peppermintrobotics.com/europe
---
