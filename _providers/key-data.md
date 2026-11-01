---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: 'This collection provides access to the Key Data Dashboard API, covering three core data domains: OTA Data, Direct Market Data, Property Manager Data.'
  name: Key Data API
  slug: key-data-api-2
- baseURL: https://api.keydata.co
  baseurl_source: declared
  description: 'Key Data API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Key Data API
  slug: key-data-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/key-data/rules/key-data-rules.yml
  title: ''
  type: Spectral
  url: rules/key-data-rules.yml
- group: design
  href: https://artifacts.apis.io/key-data/vocabulary/key-data-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/key-data-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/key-data/authentication/key-data-authentication.yml
  title: ''
  type: Authentication
  url: authentication/key-data-authentication.yml
- group: design
  href: https://artifacts.apis.io/key-data/conformance/key-data-conformance.yml
  title: ''
  type: Conformance
  url: conformance/key-data-conformance.yml
- group: other
  href: https://artifacts.apis.io/key-data/hosts/key-data-hosts.yml
  title: ''
  type: Hosts
  url: hosts/key-data-hosts.yml
- group: other
  href: https://artifacts.apis.io/key-data/vendors/key-data-vendors.yml
  title: ''
  type: Vendors
  url: vendors/key-data-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.keydata.co/company/press
- group: auth
  href: https://artifacts.apis.io/key-data/security/key-data-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/key-data-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://keydata.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.keydatadashboard.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.keydatadashboard.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.keydatadashboard.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.keydata.co/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://support.keydata.co/en/knowledge
- group: company
  title: ''
  type: Blog
  url: https://www.keydata.co/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.keydata.co/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.keydata.co/terms
coverage:
  checked: '2026-10-28'
  detail: The developer portal documents the API but no OpenAPI/AsyncAPI/GraphQL spec is publicly available.
  evidence:
  - status: 200
    url: https://developer.keydatadashboard.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Key Data provides real-time short-term rental data and analytics for professional property managers, vacation rental owners, and tourism organizations. Their platform aggregates data from major booking sites like VRBO and Airbnb, delivering insights to optimize property performance, market positioning, and revenue. The service includes industry reports, ROI calculators, and an API for developers to integrate rental market data into their applications.
image: https://cdn.prod.website-files.com/5f63854d5970333ed31b1b06/6a5911dfd6ddc4d1b3dda298_KeyData%20-preview.png
layout: provider
modified: '2026-10-28'
name: Key Data
nav: Providers
network: true
overview: 'Key Data is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include short-term rentals, real-time data, analytics, property management, and vacation rentals.


  The Key Data catalog on APIs.io includes 1 Spectral governance ruleset.


  Key Data''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 11 more developer resources.'
plans:
- name: Key Data Plans Pricing
  plan_count: 0
  slug: key-data-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Key Data Rate Limits
  slug: key-data-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Key Data API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: key-data-rules
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 11.9
    developer_ergonomics: 57.1
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Key Data Authentication
  slug: key-data-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Key Data Domain Security
  slug: key-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: key-data
tags:
- short-term rentals
- real-time data
- analytics
- property management
- vacation rentals
website: https://keydata.co/
---
