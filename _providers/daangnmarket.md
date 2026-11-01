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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/daangnmarket/security/daangnmarket-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/daangnmarket-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/daangnmarket/well-known/daangnmarket-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/daangnmarket-security.txt
- group: auth
  href: https://artifacts.apis.io/daangnmarket/well-known/daangnmarket-partner-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/daangnmarket-partner-security.txt
- group: auth
  href: https://artifacts.apis.io/daangnmarket/well-known/daangnmarket-community-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/daangnmarket-community-security.txt
- group: auth
  href: https://artifacts.apis.io/daangnmarket/well-known/daangnmarket-careers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/daangnmarket-careers-security.txt
- group: auth
  href: https://artifacts.apis.io/daangnmarket/well-known/daangnmarket-about-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/daangnmarket-about-security.txt
- group: agent
  href: https://artifacts.apis.io/daangnmarket/well-known/daangnmarket-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/daangnmarket-well-known.yml
- group: other
  href: https://artifacts.apis.io/daangnmarket/hosts/daangnmarket-hosts.yml
  title: ''
  type: Hosts
  url: hosts/daangnmarket-hosts.yml
- group: other
  href: https://artifacts.apis.io/daangnmarket/vendors/daangnmarket-vendors.yml
  title: ''
  type: Vendors
  url: vendors/daangnmarket-vendors.yml
- group: build
  href: https://artifacts.apis.io/daangnmarket/packages/daangnmarket-packages.yml
  title: ''
  type: SDKs
  url: packages/daangnmarket-packages.yml
- group: build
  href: https://artifacts.apis.io/daangnmarket/packages/daangnmarket-packages.yml
  title: ''
  type: Packages
  url: packages/daangnmarket-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.daangn.com/policy/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy-policy.daangn.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/daangn
- group: auth
  href: https://artifacts.apis.io/daangnmarket/security/daangnmarket-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/daangnmarket-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/daangnmarket/security/daangnmarket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daangnmarket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.daangn.com
coverage:
  checked: '2026-10-22'
  detail: The main website returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 200
    url: https://www.daangn.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Daangnmarket, operating as 당근마켓, is a South Korean mobile marketplace connecting local communities for buying and selling second‑hand goods, services, housing, and community activities. The platform offers a range of services including peer‑to‑peer transactions, local classifieds, real‑estate listings, job postings, and integrated payment solutions, all focused on fostering neighborhood connections and sustainable commerce.
image: https://www.daangn.com/_remix/img_og_fallback_kr-C3u-bwMc.png
layout: provider
modified: '2026-10-22'
name: Danggeun Market
nav: Providers
network: true
overview: Danggeun Market is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Mobile App, South Korea, and Community.
random_paper: 13
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  provenance:
    conformance: unknown
    mcp: derived
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
  name: Daangnmarket Domain Security
  slug: daangnmarket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Daangnmarket Vulnerability Disclosure
  slug: daangnmarket-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: daangnmarket
tags:
- Company
- Marketplace
- Mobile App
- South Korea
- Community
website: https://www.daangn.com
---
