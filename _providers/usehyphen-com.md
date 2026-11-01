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
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/usehyphen-com/hosts/usehyphen-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usehyphen-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/usehyphen-com/vendors/usehyphen-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usehyphen-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/usehyphen-com/packages/usehyphen-com-packages.yml
  title: ''
  type: SDKs
  url: packages/usehyphen-com-packages.yml
- group: build
  href: https://artifacts.apis.io/usehyphen-com/packages/usehyphen-com-packages.yml
  title: ''
  type: Packages
  url: packages/usehyphen-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usehyphen.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usehyphen.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.usehyphen.com/log-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usehyphen
- group: auth
  href: https://artifacts.apis.io/usehyphen-com/security/usehyphen-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usehyphen-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usehyphen.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://usehyphen.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Hyphen provides automated restaurant solutions for the foodservice industry, offering its Makeline system and CulinaryOS to automate meal production and augment kitchen staff. The platform includes features such as order management, inventory monitoring and forecasting, labor and operations management, and menu and recipe development. It is aimed at restaurants and foodservice operators seeking to increase productivity, reduce waste, and handle peak demand.
image: https://cdn.prod.website-files.com/65aad9ed9c946a529975e7cd/661858776ea6adf2cf5002ee_features-landing-image-50pct.jpg
layout: provider
modified: '2026-10-24'
name: Hyphen
nav: Providers
network: true
overview: Hyphen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Food Production, Kitchen Management, Order Management, Inventory Forecasting, and Labor Management.
random_paper: 5
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Usehyphen Com Domain Security
  slug: usehyphen-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: usehyphen-com
tags:
- Food Production
- Kitchen Management
- Order Management
- Inventory Forecasting
- Labor Management
website: https://usehyphen.com
---
