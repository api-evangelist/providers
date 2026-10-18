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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coco-robotics/refs/heads/main/well-known/coco-robotics-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coco-robotics-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coco-robotics/refs/heads/main/well-known/coco-robotics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coco-robotics-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coco-robotics/refs/heads/main/hosts/coco-robotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coco-robotics-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cocodelivery.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.cocodelivery.com/press
- group: company
  title: ''
  type: Blog
  url: https://www.cocodelivery.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coco-robotics/refs/heads/main/security/coco-robotics-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coco-robotics-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coco-robotics/refs/heads/main/security/coco-robotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coco-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cocodelivery.com/
coverage:
  checked: '2026-10-09'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.cocodelivery.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Coco Robotics builds the world’s largest fleet of autonomous delivery vehicles, offering self‑driving delivery services across major cities. Their platform enables affordable, reliable, clean, and fast last‑mile logistics for advertisers, merchants, and communities, aiming to transform urban delivery with AI‑powered robotics.
image: https://framerusercontent.com/assets/7ibf2PeV3erFTPA5Cn1q9XrTE.jpg
layout: provider
modified: '2026-10-09'
name: Coco Robotics
nav: Providers
network: true
overview: 'Coco Robotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Delivery, Autonomous Vehicles, Robotics, Advertising, and Fleet.


  Coco Robotics'' developer surface includes engineering blog and 9 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 10.5
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
  name: Coco Robotics Domain Security
  slug: coco-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Coco Robotics Vulnerability Disclosure
  slug: coco-robotics-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: coco-robotics
tags:
- Delivery
- Autonomous Vehicles
- Robotics
- Advertising
- Fleet
website: https://www.cocodelivery.com/
---
