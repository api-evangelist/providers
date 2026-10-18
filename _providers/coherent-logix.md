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
api_count: 1
apis:
- description: API reference for HyperX Logic products and services as described on the Getting Started page.
  name: HyperX Logic API
  slug: hyperx-logic-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coherent-logix/refs/heads/main/hosts/coherent-logix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coherent-logix-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://www.hyperxlogic.com/resources/support/
- group: company
  title: ''
  type: Newsroom
  url: https://www.hyperxlogic.com/press/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coherent-logix/refs/heads/main/security/coherent-logix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coherent-logix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hyperxlogic.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.hyperxlogic.com/technologies/hyperx-studio/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hyperxlogic.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hyperxlogic.com/terms-and-conditions/
- group: operate
  title: ''
  type: Contact
  url: https://www.hyperxlogic.com/contact/
coverage:
  checked: '2026-10-09'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.hyperxlogic.com/markets/space/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Coherent Logix, now operating as HyperX Logic, commercializes a revolutionary SoC microprocessor IP acquired from Coherent. Founded in October 2024, the company delivers AI edge computing, space, electronic warfare, and quantum AI network device security solutions, offering hardware, software, and development tools for advanced applications.
image: https://www.hyperxlogic.com/wp-content/uploads/banner-hyperx-difference.jpg
layout: provider
modified: '2026-10-09'
name: Coherent Logix
nav: Providers
network: true
overview: 'Coherent Logix is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, AI Edge Computing, Space Technology, and Electronic Warfare.


  Coherent Logix''s developer surface includes support, documentation, and 7 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coherent Logix Domain Security
  slug: coherent-logix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coherent-logix
tags:
- Company
- Semiconductors
- AI Edge Computing
- Space Technology
- Electronic Warfare
- Quantum Security
website: https://www.hyperxlogic.com
---
