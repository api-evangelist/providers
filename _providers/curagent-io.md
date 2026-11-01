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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Title Risk Analysis API
  name: Curagent API
  slug: curagent-api
- description: 'curagent-io API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: curagent-io API
  slug: curagent-io-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/curagent-io/plans/curagent-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/curagent-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/curagent-io/rules/curagent-io-rules.yml
  title: ''
  type: Spectral
  url: rules/curagent-io-rules.yml
- group: design
  href: https://artifacts.apis.io/curagent-io/vocabulary/curagent-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/curagent-io-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/curagent-io/authentication/curagent-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/curagent-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/curagent-io/conformance/curagent-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/curagent-io-conformance.yml
- group: other
  href: https://artifacts.apis.io/curagent-io/hosts/curagent-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curagent-io-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://curagent.io/Identity/Account/Login
- group: auth
  href: https://artifacts.apis.io/curagent-io/security/curagent-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curagent-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://curagent.io/
- group: docs
  title: ''
  type: Documentation
  url: https://curagent.io/#docs
- group: docs
  title: ''
  type: APIReference
  url: https://curagent.io/#docs
- group: commercial
  title: ''
  type: Pricing
  url: https://curagent.io/#pricing
- group: operate
  title: ''
  type: Support
  url: mailto:kyle@curagent.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.termsfeed.com/live/d0a757d0-f16a-4978-9aa0-d9a80e0ecbdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.termsfeed.com/live/aa0438ad-ef89-49a1-b7f4-4569e5cf2c84
coverage:
  checked: '2026-10-30'
  detail: Developers page provides human‑readable API reference but no OpenAPI or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://curagent.io/developers.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Curagent provides a Title Risk Analysis API that processes real estate closing packages such as deeds, title commitments, HOA estoppels, and other related documents. By uploading a package, users receive a detailed risk report highlighting missing conditions, exceptions, and guidance to resolve issues. The service targets title companies, real‑estate attorneys, and lenders needing fast, automated title risk assessment. It parses schedules, extracts requirements, flags expired letters, unpaid mortgages, and ensures cross‑document consistency of seller names, parcel IDs, and legal descriptions. A free tier offers three analyses with no setup.
image: https://curagent.io/curagent-icon-64.png
layout: provider
modified: '2026-10-30'
name: curagent-io
nav: Providers
network: true
overview: 'curagent-io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Title, Risk Analysis, API, and Document Processing.


  The curagent-io catalog on APIs.io includes 1 Spectral governance ruleset.


  curagent-io''s developer surface includes authentication, documentation, API reference, pricing, support, and 10 more developer resources.'
plans:
- name: Curagent Io Plans Pricing
  plan_count: 3
  slug: curagent-io-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: curagent-io API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: curagent-io-rules
scopes:
- name: Curagent Io Scopes
  scope_count: 0
  slug: curagent-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 63.5
    catalog_earned_first_party: 0.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 38.0
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Curagent Io Authentication
  slug: curagent-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Curagent Io Domain Security
  slug: curagent-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: curagent-io
tags:
- Real Estate
- Title
- Risk Analysis
- API
- Document Processing
- Company
website: https://curagent.io/
---
