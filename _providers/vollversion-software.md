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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/vollversion-software/vendors/vollversion-software-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vollversion-software-vendors.yml
- group: auth
  href: https://artifacts.apis.io/vollversion-software/security/vollversion-software-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/vollversion-software-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vollversion-software/well-known/vollversion-software-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/vollversion-software-security.txt
- group: agent
  href: https://artifacts.apis.io/vollversion-software/well-known/vollversion-software-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vollversion-software-well-known.yml
- group: other
  href: https://artifacts.apis.io/vollversion-software/hosts/vollversion-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vollversion-software-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://vollversion-software.de/account/login
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vollversion-software.de/
- group: auth
  href: https://artifacts.apis.io/vollversion-software/security/vollversion-software-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vollversion-software-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vollversion-software/security/vollversion-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vollversion-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vollversion-software.de/
- group: company
  title: ''
  type: Blog
  url: https://vollversion-software.de/blogs/software-blog
- group: operate
  title: ''
  type: Support
  url: https://vollversion-software.de/pages/faq
- group: operate
  title: ''
  type: Contact
  url: https://vollversion-software.de/pages/contact
coverage:
  checked: '2026-10-19'
  detail: Vollversion-Software.de offers a retail storefront but provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://vollversion-software.de/
  reason: no-developer-program
  state: none
created: '2026-10-19'
description: Vollversion-Software.de is a German e‑commerce retailer that offers original Microsoft software products such as Windows operating systems and Microsoft Office suites through its online store. The company provides a storefront for customers to purchase digital licenses and product keys, featuring a wide catalog of Windows versions, Office editions, and Microsoft 365 subscriptions. It includes customer support, FAQ, affiliate programs, and a blog with software-related articles. The site is fully German‑language, targeting both private and business customers, and operates with standard service hours and contact options.
image: https://cdn.vollversion-software.de/media/f0/14/3a/1791466357/vollversion-logo-600x80.png?ts=1791466357
layout: provider
modified: '2026-10-19'
name: Vollversion-Software.de
nav: Providers
network: true
overview: 'Vollversion-Software.de is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Software Retail, German, and Microsoft.


  Vollversion-Software.de''s developer surface includes documentation, engineering blog, support, and 10 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 11.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vollversion-software/vollversion-software-2026-11-03T145919.png
security:
- kind: domain-security
  name: Vollversion Software Domain Security
  slug: vollversion-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vollversion Software Vulnerability Disclosure
  slug: vollversion-software-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vollversion-software
tags:
- Company
- E-Commerce
- Software Retail
- German
- Microsoft
website: https://vollversion-software.de/
---
