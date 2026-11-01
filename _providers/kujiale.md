---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/kujiale/well-known/kujiale-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kujiale-well-known.yml
- group: other
  href: https://artifacts.apis.io/kujiale/hosts/kujiale-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kujiale-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://www.kujiale.com/festatic/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kujiale.com/festatic/privacy_policy
- group: company
  title: ''
  type: Newsroom
  url: https://b.kujiale.com/news
- group: start
  title: ''
  type: Login
  url: https://www.kujiale.com/vc/account/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kujiale
- group: auth
  href: https://artifacts.apis.io/kujiale/security/kujiale-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kujiale-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kujiale.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.kujiale.com/api/mcp
  - status: 200
    url: https://www.kujiale.com/
  reason: partner-login
  state: gated
created: '2026-10-22'
description: Kujiale (酷家乐) is a Chinese technology company offering a cloud‑based 3D design platform for home decoration, interior design, commercial spaces and AI‑generated visualizations. It provides an online suite where users can create, render and collaborate on virtual models, leveraging AI to generate designs from text or images, and supports e‑commerce, architecture and marketing workflows. The platform serves both consumers and enterprises, integrating cloud rendering, AI tools and a marketplace for design assets. backed by coatue) and added to the network as a stub for full-pipeline profiling.
image: https://qhstaticssl.kujiale.com/image/jpeg/1752568141788/D4E4E6708A6C1A228332D8FA187B0421.jpg
layout: provider
modified: '2026-10-22'
name: Kujiale
nav: Providers
network: true
overview: Kujiale is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include 3DDesign, CloudDesign, AI, InteriorDesign, and HomeDecoration.
random_paper: 21
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kujiale Domain Security
  slug: kujiale-domain-security
  summary_line: TLSv1.2
slug: kujiale
tags:
- 3DDesign
- CloudDesign
- AI
- InteriorDesign
- HomeDecoration
website: https://www.kujiale.com/
---
