---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/aureum-tech-com/security/aureum-tech-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aureum-tech-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/aureum-tech-com/llms/aureum-tech-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aureum-tech-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/aureum-tech-com/well-known/aureum-tech-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aureum-tech-com-security.txt
- group: agent
  href: https://artifacts.apis.io/aureum-tech-com/well-known/aureum-tech-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aureum-tech-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aureum-tech-com/hosts/aureum-tech-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aureum-tech-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aureum-tech-com/vendors/aureum-tech-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aureum-tech-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aureum-tech-com/security/aureum-tech-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aureum-tech-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aureum-tech-com/security/aureum-tech-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aureum-tech-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aureum-tech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aureum-tech.com/ueber-uns
- group: commercial
  title: ''
  type: Pricing
  url: https://aureum-tech.com/preise
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aureum-tech.com/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aureum-tech.com/datenschutz
- group: operate
  title: ''
  type: Support
  url: https://aureum-tech.com/kontakt
coverage:
  checked: '2026-11-02'
  detail: Aureum Technology GmbH provides IT services and does not expose a public API.
  evidence:
  - status: 200
    url: https://aureum-tech.com/
  reason: not-a-software-company
  state: none
created: '2026-11-02'
description: Aureum Technology GmbH is an IT system house based in Rodewisch, Germany, offering comprehensive IT services including network infrastructure, server virtualization, client management, IT support, security, backup, and digital solutions such as web design, AI, and blockchain development. They serve businesses, schools, and clubs across the Vogtland region, providing on-site and remote support with a focus on reliability and customer service.
image: https://aureum-tech.com/og.png
layout: provider
modified: '2026-11-02'
name: Aureum Technology GmbH
nav: Providers
network: true
overview: 'Aureum Technology GmbH is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IT Services, IT Support, and Germany.


  Aureum Technology GmbH''s developer surface includes documentation, pricing, support, and 11 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 39.3
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 16.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aureum Tech Com Domain Security
  slug: aureum-tech-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aureum Tech Com Vulnerability Disclosure
  slug: aureum-tech-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aureum-tech-com
tags:
- Company
- IT Services
- IT Support
- Germany
website: https://aureum-tech.com/
---
