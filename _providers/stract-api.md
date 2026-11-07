---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Stract Api Agentic Access
  operation_count: 2
  slug: stract-api-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- baseURL: https://api.stract-api.com
  baseurl_source: declared
  description: The My User API from Stract API — 1 operation(s) for my user.
  name: Stract API My User API
  slug: stract-api-my-user-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/stract-api/vocabulary/stract-api-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/stract-api-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/stract-api/data-model/stract-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stract-api-data-model.yml
- group: agent
  href: https://artifacts.apis.io/stract-api/agentic-access/stract-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/stract-api-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/stract-api/plans/stract-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stract-api-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/stract-api/rules/stract-api-rules.yml
  title: ''
  type: Spectral
  url: rules/stract-api-rules.yml
- group: auth
  href: https://artifacts.apis.io/stract-api/authentication/stract-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stract-api-authentication.yml
- group: design
  href: https://artifacts.apis.io/stract-api/errors/stract-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stract-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/stract-api/conformance/stract-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stract-api-conformance.yml
- group: agent
  href: https://artifacts.apis.io/stract-api/llms/stract-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stract-api-llms.txt
- group: agent
  href: https://artifacts.apis.io/stract-api/well-known/stract-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stract-api-well-known.yml
- group: other
  href: https://artifacts.apis.io/stract-api/hosts/stract-api-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stract-api-hosts.yml
- group: other
  href: https://artifacts.apis.io/stract-api/vendors/stract-api-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stract-api-vendors.yml
- group: auth
  href: https://artifacts.apis.io/stract-api/security/stract-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stract-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stract-api.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.stract-api.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stract-api.com
- group: docs
  title: ''
  type: APIReference
  url: https://stract-api.com/guide/
- group: start
  title: ''
  type: GettingStarted
  url: https://stract-api.com/guide/quick-start-api/
- group: operate
  title: ''
  type: Support
  url: https://stract-api.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://stract-api.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://stract-api.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stract-api.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stract-api.com/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/stract-api/workspace
created: '2026-10-27'
description: Stract API provides AI-powered document extraction, turning unstructured files like PDFs, scans, spreadsheets, and audio into structured data such as CSV or JSON. Users can upload documents, specify the data they need, and receive organized results quickly via a point‑and‑click UI or API integration. The platform serves lawyers, developers, marketers, researchers, and other professionals, offering customizable models, SOC 2 compliance, and pricing plans for various volumes.
image: https://stract-api.com/og_logo.png
layout: provider
modified: '2026-10-27'
name: Stract API
nav: Providers
network: true
overview: 'Stract API publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: My User API. Tagged areas include Company, Artificial Intelligence, Document Processing, Data Extraction, and Software-as-a-Service.


  The Stract API catalog on APIs.io includes 1 Spectral governance ruleset.


  Stract API''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Stract Api Plans Pricing
  plan_count: 3
  slug: stract-api-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Stract API API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: stract-api-rules
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 47.8
    developer_ergonomics: 36.9
    discoverability: 73.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/stract-api/stract-api-2026-11-03T143855.png
security:
- kind: authentication
  name: Stract Api Authentication
  slug: stract-api-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Stract Api Domain Security
  slug: stract-api-domain-security
  summary_line: TLSv1.3
slug: stract-api
tags:
- Company
- Artificial Intelligence
- Document Processing
- Data Extraction
- Software-as-a-Service
website: https://stract-api.com
---
