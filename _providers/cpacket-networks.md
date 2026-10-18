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
  href: https://raw.githubusercontent.com/api-evangelist/cpacket-networks/refs/heads/main/hosts/cpacket-networks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cpacket-networks-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cpacket-networks/refs/heads/main/vendors/cpacket-networks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cpacket-networks-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cpacket.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cpacket.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.cpacket.com/tags/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cpacket-networks/refs/heads/main/security/cpacket-networks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cpacket-networks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cpacket.com/
coverage:
  checked: '2026-10-11'
  detail: cPacket Networks does not provide a public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.cpacket.com/
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: cPacket Networks provides advanced network observability, packet broker, and packet capture solutions powered by AI. Their platform offers unified visibility across on-prem, hybrid, and multi‑cloud environments, delivering real‑time analytics, security insights, and automated workflows. With a focus on AI‑driven operations, cPacket helps enterprises reduce mean time to resolution, improve security posture, and streamline network management through scalable, agentless solutions.
image: https://cdn.prod.website-files.com/663a897e92f30c4b099198f3/68e7e87f48b06b709b4d9128_home_hero_01.jpg
layout: provider
modified: '2026-10-11'
name: cPacket Networks
nav: Providers
network: true
overview: cPacket Networks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Network Observability, Packet Broker, Artificial Intelligence, and Cloud.
random_paper: 19
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 5
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
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cpacket Networks Domain Security
  slug: cpacket-networks-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cpacket-networks
tags:
- Company
- Network Observability
- Packet Broker
- Artificial Intelligence
- Cloud
website: https://www.cpacket.com/
---
