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
api_count: 1
apis:
- description: Banksalad provides financial data aggregation APIs as described in their customer safety documentation.
  name: Banksalad API
  slug: banksalad-api
artifact_total: 2
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.banksalad.com/rss.xml
- group: other
  href: https://artifacts.apis.io/banksalad/hosts/banksalad-hosts.yml
  title: ''
  type: Hosts
  url: hosts/banksalad-hosts.yml
- group: other
  href: https://artifacts.apis.io/banksalad/vendors/banksalad-vendors.yml
  title: ''
  type: Vendors
  url: vendors/banksalad-vendors.yml
- group: build
  href: https://artifacts.apis.io/banksalad/packages/banksalad-packages.yml
  title: ''
  type: SDKs
  url: packages/banksalad-packages.yml
- group: build
  href: https://artifacts.apis.io/banksalad/packages/banksalad-packages.yml
  title: ''
  type: Packages
  url: packages/banksalad-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/banksalad
- group: auth
  href: https://artifacts.apis.io/banksalad/security/banksalad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/banksalad-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.banksalad.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.banksalad.com/customer-safety/
- group: company
  title: ''
  type: Blog
  url: https://blog.banksalad.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.banksalad.com/뱅크샐러드/서비스-이용-약관
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.banksalad.com/뱅크샐러드/개인정보처리방침
coverage:
  checked: '2026-09-27'
  detail: Customer safety documentation is rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.banksalad.com/customer-safety/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Banksalad is a South Korean fintech company offering a comprehensive financial platform that aggregates banking, credit card, loan, deposit, insurance, and health check services. It provides users with personalized financial product recommendations, comparison tools, and health screening, leveraging extensive data to help manage money and health assets efficiently.
image: https://cdn.banksalad.com/graphic/color/illustration/og-image/banksalad-web.png
layout: provider
modified: '2026-10-06'
name: Banksalad
nav: Providers
network: true
overview: 'Banksalad is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, South Korea, Financial Services, and Health Tech.


  Banksalad''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 57.1
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 14.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/banksalad/banksalad-2026-10-11T101530.png
security:
- kind: domain-security
  name: Banksalad Domain Security
  slug: banksalad-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: banksalad
tags:
- Company
- Fintech
- South Korea
- Financial Services
- Health Tech
website: https://www.banksalad.com
---
