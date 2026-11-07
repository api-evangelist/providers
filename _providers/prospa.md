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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Prospa provides a developer API documented at https://developer.prospa.com/apis
  name: Prospa API
  slug: prospa-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/prospa/security/prospa-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/prospa-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/prospa/well-known/prospa-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prospa-security.txt
- group: auth
  href: https://artifacts.apis.io/prospa/well-known/prospa-register-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prospa-register-security.txt
- group: auth
  href: https://artifacts.apis.io/prospa/well-known/prospa-partners-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prospa-partners-security.txt
- group: auth
  href: https://artifacts.apis.io/prospa/well-known/prospa-online-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prospa-online-security.txt
- group: auth
  href: https://artifacts.apis.io/prospa/well-known/prospa-join-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prospa-join-security.txt
- group: auth
  href: https://artifacts.apis.io/prospa/well-known/prospa-identity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prospa-identity-security.txt
- group: auth
  href: https://artifacts.apis.io/prospa/well-known/prospa-developer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prospa-developer-security.txt
- group: auth
  href: https://artifacts.apis.io/prospa/well-known/prospa-application-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prospa-application-security.txt
- group: agent
  href: https://artifacts.apis.io/prospa/well-known/prospa-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/prospa-well-known.yml
- group: other
  href: https://artifacts.apis.io/prospa/hosts/prospa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prospa-hosts.yml
- group: other
  href: https://artifacts.apis.io/prospa/vendors/prospa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prospa-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://identity.prospa.com/Account/Login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.prospa.com/
- group: auth
  href: https://artifacts.apis.io/prospa/security/prospa-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/prospa-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/prospa/security/prospa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prospa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.prospa.com
- group: company
  title: ''
  type: Blog
  url: https://www.prospa.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.prospa.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.prospa.com/contact-us
coverage:
  checked: '2026-10-13'
  detail: Developer portal pages render via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://developer.prospa.com/apis
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Prospa is an Australian fintech company that provides small business loans, lines of credit, and business accounts. Their platform offers flexible funding solutions ranging from $5,000 to $1,000,000, integrated payment services, and accounting integrations such as Xero. Prospa aims to help SMEs grow by simplifying access to capital and financial management tools through a digital experience.
image: https://www.prospa.com/wp-content/uploads/2023/02/og_logo.png
layout: provider
modified: '2026-10-13'
name: Prospa
nav: Providers
network: true
overview: 'Prospa is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Small Business, Loans, and Australia.


  Prospa''s developer surface includes engineering blog, documentation, support, and 17 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 57.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 15.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/prospa/prospa-2026-11-03T141641.png
security:
- kind: domain-security
  name: Prospa Domain Security
  slug: prospa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Prospa Vulnerability Disclosure
  slug: prospa-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: prospa
tags:
- Company
- Fintech
- Small Business
- Loans
- Australia
website: https://www.prospa.com
---
