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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/frank-energie/well-known/frank-energie-frankenergie-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/frank-energie-frankenergie-security.txt
- group: auth
  href: https://artifacts.apis.io/frank-energie/security/frank-energie-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/frank-energie-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/frank-energie/well-known/frank-energie-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/frank-energie-www-security.txt
- group: auth
  href: https://artifacts.apis.io/frank-energie/well-known/frank-energie-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/frank-energie-security.txt
- group: auth
  href: https://artifacts.apis.io/frank-energie/well-known/frank-energie-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/frank-energie-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/frank-energie/well-known/frank-energie-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/frank-energie-well-known.yml
- group: other
  href: https://artifacts.apis.io/frank-energie/hosts/frank-energie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/frank-energie-hosts.yml
- group: other
  href: https://artifacts.apis.io/frank-energie/vendors/frank-energie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/frank-energie-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.frankenergie.nl/nl/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.frankenergie.nl/nl
- group: docs
  title: ''
  type: Documentation
  url: https://dev.frankenergie.nl/
- group: auth
  href: https://artifacts.apis.io/frank-energie/security/frank-energie-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/frank-energie-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/frank-energie/security/frank-energie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/frank-energie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://frankenergie.nl/
coverage:
  checked: '2026-10-28'
  detail: Developer portal pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://dev.frankenergie.nl/nl
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Frank Energie is a Dutch energy provider that helps customers reduce their electricity costs by offering smart consumption advice and cheaper rates. The service focuses on using cheaper energy moments, providing tools to monitor usage, and promoting sustainable energy choices. It aims to make energy cheaper and consumption smarter for households and businesses across the Netherlands.
image: https://frankenergie.nl/images/og-image-default.png
layout: provider
modified: '2026-10-28'
name: Frank Energie
nav: Providers
network: true
overview: 'Frank Energie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Frank Energie''s developer surface includes documentation and 13 more developer resources.'
plans:
- name: Frank Energie Plans Pricing
  plan_count: 0
  slug: frank-energie-plans-pricing
random_paper: 14
scopes:
- name: Frank Energie Scopes
  scope_count: 0
  slug: frank-energie-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 39.3
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Frank Energie Authentication
  slug: frank-energie-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Frank Energie Domain Security
  slug: frank-energie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Frank Energie Vulnerability Disclosure
  slug: frank-energie-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: frank-energie
tags:
- Company
website: https://frankenergie.nl/
---
