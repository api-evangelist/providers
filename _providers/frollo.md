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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: docs
  title: ''
  type: Documentation
  url: https://developer.frollo.com.au/
- group: auth
  href: https://artifacts.apis.io/frollo/security/frollo-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/frollo-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/frollo/well-known/frollo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/frollo-well-known.yml
- group: other
  href: https://artifacts.apis.io/frollo/hosts/frollo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/frollo-hosts.yml
- group: other
  href: https://artifacts.apis.io/frollo/vendors/frollo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/frollo-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.frollo.com.au/
- group: auth
  href: https://artifacts.apis.io/frollo/security/frollo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/frollo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/frollo/security/frollo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/frollo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://frollo.com.au/
- group: operate
  title: ''
  type: Support
  url: https://frollo.com.au/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://frollo.com.au/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/frollo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://frollo.com.au/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://frollo.com.au/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/frollo/workspace
coverage:
  checked: '2026-10-20'
  detail: Developer portal returned 404 for openapi.json and HTML for api.frollo.com.au/openapi.json, no machine-readable spec found.
  evidence:
  - status: 404
    url: https://developer.frollo.com.au/openapi.json
  - status: 200
    url: https://api.frollo.com.au/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Frollo Australia Pty LTD is Australia’s leading Open Banking provider, delivering businesses and mortgage brokers efficiency tools, exceptional customer experiences, and empowering consumers to achieve their financial goals through integrated financial insights and budgeting tools.
image: https://frollo.com.au/wp-content/uploads/2024/01/Frollo-Empowering-better-banking.png
layout: provider
modified: '2026-10-20'
name: Frollo Australia Pty LTD
nav: Providers
network: true
overview: 'Frollo Australia Pty LTD is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Open Banking, Finance, Australia, B2B, and Mortgage.


  Frollo Australia Pty LTD''s developer surface includes documentation, support, engineering blog, and 12 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 14.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 48.2
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 17.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 19.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/frollo/frollo-2026-11-03T132344.png
security:
- kind: domain-security
  name: Frollo Domain Security
  slug: frollo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Frollo Vulnerability Disclosure
  slug: frollo-vulnerability-disclosure
  summary_line: no policy recorded
slug: frollo
tags:
- Open Banking
- Finance
- Australia
- B2B
- Mortgage
website: https://frollo.com.au/
---
