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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Brincdrones live operations platform.
  name: Brincdrones LiveOps API
  slug: brincdrones-liveops-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://brincdrones.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brincdrones/refs/heads/main/well-known/brincdrones-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brincdrones-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brincdrones/refs/heads/main/well-known/brincdrones-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brincdrones-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brincdrones/refs/heads/main/hosts/brincdrones-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brincdrones-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brincdrones/refs/heads/main/vendors/brincdrones-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brincdrones-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brincdrones.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://brincdrones.com/news/brinc-drones/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brincdrones/refs/heads/main/security/brincdrones-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brincdrones-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brincdrones/refs/heads/main/security/brincdrones-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brincdrones-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brincdrones.com
coverage:
  checked: '2026-10-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, or MCP spec could be found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.liveops.brincdrones.com/openapi.json
  - status: 404
    url: https://api.liveops.brincdrones.com/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Brincdrones is a startup that focuses on providing drone-based solutions for various industries, including aerial surveying, inspection, and delivery services. The company aims to leverage advanced drone technology and data analytics to offer efficient, cost-effective, and scalable solutions for clients ranging from construction firms to logistics providers. While detailed public information is limited, Brincdrones appears to be positioned within the emerging market of commercial drone applications, seeking to address industry-specific challenges through innovative aerial platforms and services.
image: https://brincdrones.com/wp-content/uploads/2026/03/Home-page.jpg
layout: provider
modified: '2026-10-06'
name: Brincdrones
nav: Providers
network: true
overview: Brincdrones is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Drone, AerialSurvey, Inspection, and Delivery.
random_paper: 11
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brincdrones Domain Security
  slug: brincdrones-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Brincdrones Vulnerability Disclosure
  slug: brincdrones-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: brincdrones
tags:
- Company
- Drone
- AerialSurvey
- Inspection
- Delivery
- Technology
website: https://brincdrones.com
---
