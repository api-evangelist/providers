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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.emirates.com/ae/english/information/cybersecurity/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/emirates/refs/heads/main/vendors/emirates-vendors.yml
  title: ''
  type: Vendors
  url: vendors/emirates-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/emirates/refs/heads/main/security/emirates-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/emirates-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/emirates/refs/heads/main/security/emirates-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emirates-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://emirates.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.emirates.com/english/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.emirates.com/english/information/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.emirates.com/english/information/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://www.emirates.com/english/help/
- group: company
  title: ''
  type: Blog
  url: https://www.emirates.com/english/blog/
created: '2026-09-22'
description: Emirates is a global airline based in Dubai, United Arab Emirates, offering passenger and cargo services to destinations worldwide. The airline is known for its modern fleet, premium cabin experience, and extensive network connecting six continents. It provides digital services such as flight booking, check‑in, flight status, and loyalty program management through its website and mobile apps.
layout: provider
modified: '2026-09-22'
name: Emirates
nav: Providers
network: true
overview: 'Emirates is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Airlines, Travel, Aviation, and Dubai.


  Emirates'' developer surface includes documentation, support, engineering blog, and 7 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 46.3
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-arab-emirates
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 13.6
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Emirates Domain Security
  slug: emirates-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Emirates Vulnerability Disclosure
  slug: emirates-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: emirates
tags:
- Company
- Airlines
- Travel
- Aviation
- Dubai
website: https://emirates.com/
---
