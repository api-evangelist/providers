---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: GraphQL API for Shelly IoT platform
  name: Shelly API
  slug: shelly-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shelly/refs/heads/main/llms/shelly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shelly-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shelly/refs/heads/main/well-known/shelly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shelly-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/shelly/refs/heads/main/hosts/shelly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shelly-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/shelly/refs/heads/main/vendors/shelly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shelly-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shelly.com/blogs/use-cases/privacy-security-on-demand
- group: docs
  title: ''
  type: Documentation
  url: https://www.shelly.com/blogs/documentation
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.shelly.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shelly/refs/heads/main/security/shelly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shelly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shelly.com/
created: '2026-09-23'
description: Shelly is a global IoT company that designs and manufactures smart home devices, including Wi‑Fi and Bluetooth switches, plugs, sensors, energy meters, and controllers. Their products enable users to automate lighting, climate, security, and energy management through mobile apps and integrations with platforms like Home Assistant and major voice assistants.
image: https://www.shelly.com/cdn/shop/files/share-general.jpg?v=1726139769
layout: provider
modified: '2026-09-23'
name: Shelly
nav: Providers
network: true
overview: 'Shelly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Smart Home, Devices, and Automation.


  Shelly''s developer surface includes documentation and 8 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 13.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Shelly Domain Security
  slug: shelly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shelly
tags:
- Company
- IoT
- Smart Home
- Devices
- Automation
website: https://www.shelly.com/
---
