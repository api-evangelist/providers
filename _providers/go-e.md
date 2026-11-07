---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/go-e/llms/go-e-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/go-e-llms.txt
- group: auth
  href: https://artifacts.apis.io/go-e/well-known/go-e-auth-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/go-e-auth-security.txt
- group: agent
  href: https://artifacts.apis.io/go-e/well-known/go-e-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/go-e-well-known.yml
- group: other
  href: https://artifacts.apis.io/go-e/hosts/go-e-hosts.yml
  title: ''
  type: Hosts
  url: hosts/go-e-hosts.yml
- group: build
  href: https://artifacts.apis.io/go-e/packages/go-e-packages.yml
  title: ''
  type: SDKs
  url: packages/go-e-packages.yml
- group: build
  href: https://artifacts.apis.io/go-e/packages/go-e-packages.yml
  title: ''
  type: Packages
  url: packages/go-e-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://go-e.com/de-at/ueber-uns/news
- group: auth
  href: https://artifacts.apis.io/go-e/security/go-e-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/go-e-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://go-e.com/
- group: company
  title: ''
  type: Blog
  url: https://go-e.com/en/magazine
- group: operate
  title: ''
  type: Support
  url: https://go-e.com/en/support/contact
- group: docs
  title: ''
  type: Documentation
  url: https://go-e.com/en/about-us/company
- group: start
  title: ''
  type: GettingStarted
  url: https://go-e.com/en/solutions/for-customers/electric-car-charging-at-home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://go-e.com/en/data-protection
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://go-e.com/en/data-protection
coverage:
  checked: '2026-10-28'
  detail: The provider's website offers no developer documentation or API reference.
  evidence:
  - status: 200
    url: https://go-e.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: go-e GmbH designs and manufactures smart electric vehicle (EV) wallbox charging stations for home, business and multi‑unit installations. Their product range includes the Gemini, CORE, PRO and Controller series, supporting features such as PV‑surplus charging, shared charging, and integration with energy management systems. The company emphasizes sustainability, offers a reseller program, and provides extensive support resources including manuals, FAQs and a blog.
layout: provider
modified: '2026-10-28'
name: go-e
nav: Providers
network: true
overview: 'go-e is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EV Charging, Hardware, Sustainability, and Reseller.


  go-e''s developer surface includes engineering blog, support, documentation, getting-started guide, and 11 more developer resources.'
random_paper: 0
scopes:
- name: Go E Scopes
  scope_count: 0
  slug: go-e-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 52.7
    operational_transparency: 10.5
  previous_composite: 19.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 22.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/go-e/go-e-2026-11-03T132858.png
security:
- kind: authentication
  name: Go E Authentication
  slug: go-e-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Go E Domain Security
  slug: go-e-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: go-e
tags:
- Company
- EV Charging
- Hardware
- Sustainability
- Reseller
website: https://go-e.com/
---
