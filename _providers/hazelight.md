---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
  score: 7.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: GraphQL API for Hazelight's online store providing product and order data.
  name: Hazelight Store API
  slug: hazelight-store-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hazelight/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hazelight/refs/heads/main/llms/hazelight-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hazelight-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hazelight/refs/heads/main/well-known/hazelight-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hazelight-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hazelight/refs/heads/main/hosts/hazelight-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hazelight-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hazelight/refs/heads/main/vendors/hazelight-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hazelight-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://hazelight.se/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hazelight/refs/heads/main/security/hazelight-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hazelight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hazelight.se/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hazelight.se/privacy-policy
created: '2026-10-14'
description: Hazelight is a Swedish video game development studio founded in 2014, known for creating cooperative multiplayer games that emphasize narrative and emotional storytelling. Their flagship titles include "A Way Out" and "It Takes Two," both of which have received critical acclaim for innovative gameplay mechanics and award-winning design. Hazelight focuses on delivering high-quality, story-driven experiences that bring players together, fostering collaboration and shared adventure across platforms.
image: https://hazelight.se/__og-image__/image/og.png
layout: provider
modified: '2026-10-14'
name: Hazelight
nav: Providers
network: true
overview: Hazelight is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Video Games, Cooperative, and Sweden.
random_paper: 14
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hazelight Domain Security
  slug: hazelight-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hazelight
tags:
- Company
- Gaming
- Video Games
- Cooperative
- Sweden
- Studio
website: https://hazelight.se/
---
