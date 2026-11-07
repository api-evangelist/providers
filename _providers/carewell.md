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
- description: Carewell provides a developer API for accessing medical supply product data and order management.
  name: Carewell API
  slug: carewell-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/carewell/hosts/carewell-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carewell-hosts.yml
- group: other
  href: https://artifacts.apis.io/carewell/vendors/carewell-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carewell-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carewell.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carewell.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://www.carewell.com/login/?redirect_uri=%2Fen-US%2F
- group: start
  title: ''
  type: GettingStarted
  url: https://health.carewell.com/get-started/navigation?utm_source=carewell.com&utm_campaign=ecomm
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carewell
- group: auth
  href: https://artifacts.apis.io/carewell/security/carewell-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carewell-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carewell.com
coverage:
  checked: '2026-10-07'
  detail: The health.carewell.com API reference loads via a JavaScript SPA, returning only HTML shells for spec URLs.
  evidence:
  - status: 404
    url: https://health.carewell.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Carewell is an online medical supply retailer offering a wide range of incontinence, nutrition, wound care, and personal care products. It provides a concierge service to help customers navigate healthcare needs, supports FSA/HSA eligible purchases, and delivers supplies across the United States with free delivery and autoship options.
image: https://cdn.builder.io/api/v1/image/assets%2F3a5958f65346417f9899d3c37529e3c7%2Fbbfab659c3494c6798a3761178ad97e4
layout: provider
modified: '2026-10-07'
name: Carewell
nav: Providers
network: true
overview: 'Carewell is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical, Retail, E-Commerce, and Healthcare.


  Carewell''s developer surface includes getting-started guide and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 15.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/carewell/carewell-2026-11-03T123341.png
security:
- kind: domain-security
  name: Carewell Domain Security
  slug: carewell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carewell
tags:
- Company
- Medical
- Retail
- E-Commerce
- Healthcare
website: https://www.carewell.com
---
