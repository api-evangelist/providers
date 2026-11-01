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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/raydiant-com/well-known/raydiant-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/raydiant-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/raydiant-com/hosts/raydiant-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/raydiant-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/raydiant-com/vendors/raydiant-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/raydiant-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.displai.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.displai.ai/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.displai.ai/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.displai.ai/displai/tutorial/setup-a-screen/
- group: docs
  title: ''
  type: Documentation
  url: https://help.displai.ai/
- group: auth
  href: https://artifacts.apis.io/raydiant-com/security/raydiant-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/raydiant-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.raydiant.com/
coverage:
  checked: '2026-10-22'
  detail: The provider's documentation site renders via JavaScript, preventing machine-readable extraction.
  evidence:
  - status: 200
    url: https://www.displai.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Displai, the brand formerly known as Raydiant, provides digital signage, employee engagement tools, visitor insight analytics, and self‑service kiosks for brick‑and‑mortar businesses, including restaurants, retail, hospitality, commercial, education, and public services. It sells these solutions to enterprise brands that operate multiple locations.
image: https://srcdisplai.wpenginepowered.com/wp-content/uploads/2025/04/homepage-hero.webp
layout: provider
modified: '2026-10-21'
name: Raydiant
nav: Providers
network: true
overview: 'Raydiant is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Signage, Employee Engagement, Visitor Analytics, Kiosks, and Brick‑and‑Mortar.


  Raydiant''s developer surface includes engineering blog, getting-started guide, documentation, and 7 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Raydiant Com Domain Security
  slug: raydiant-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: raydiant-com
tags:
- Digital Signage
- Employee Engagement
- Visitor Analytics
- Kiosks
- Brick‑and‑Mortar
- Enterprise Solutions
- In‑Location Experience
website: https://www.raydiant.com/
---
