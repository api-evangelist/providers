---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
api_count: 2
apis:
- description: 'The AVEVA CONNECT cloud platform REST APIs provide access to industrial data services including account management, identity management, data ingress pipelines, data views, and time-series retrieval. '
  name: AVEVA CONNECT REST API
  slug: aveva-connect-rest-api
- description: The AVEVA PI System REST API (PI Web API) provides RESTful HTTP access to time- series sensor data, asset metadata, and event frames stored in PI Server. Supports GET, POST, PUT, PATCH, and DELETE ope
  name: AVEVA PI System REST API
  slug: aveva-pi-system-rest-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Newsroom
  url: https://www.aveva.com/en/about/news/
- group: design
  href: https://artifacts.apis.io/aveva/json-ld/aveva-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aveva-context.jsonld
- group: design
  href: https://artifacts.apis.io/aveva/vocabulary/aveva-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aveva-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/aveva/security/aveva-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aveva-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/aveva/llms/aveva-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aveva-llms.txt
- group: auth
  href: https://artifacts.apis.io/aveva/well-known/aveva-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aveva-security.txt
- group: agent
  href: https://artifacts.apis.io/aveva/well-known/aveva-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aveva-well-known.yml
- group: other
  href: https://artifacts.apis.io/aveva/hosts/aveva-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aveva-hosts.yml
- group: other
  href: https://artifacts.apis.io/aveva/vendors/aveva-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aveva-vendors.yml
- group: build
  href: https://artifacts.apis.io/aveva/packages/aveva-packages.yml
  title: ''
  type: SDKs
  url: packages/aveva-packages.yml
- group: build
  href: https://artifacts.apis.io/aveva/packages/aveva-packages.yml
  title: ''
  type: Packages
  url: packages/aveva-packages.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.aveva.com/en/about/about-aveva/leadership/
- group: auth
  href: https://artifacts.apis.io/aveva/security/aveva-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aveva-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/aveva/security/aveva-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aveva-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aveva/security/aveva-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aveva-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aveva.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aveva
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aveva.com/bundle/product-release-notes
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aveva.com/bundle/pi-web-api-reference/page/help.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aveva.com/en/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aveva.com/en/legal/terms-of-use/
- group: start
  title: ''
  type: Login
  url: https://community.aveva.com/login?ReturnUrl=%2F
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aveva.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aveva.com/en/perspectives/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aveva
- group: company
  title: ''
  type: About
  url: https://www.aveva.com/en/about/
- group: operate
  title: ''
  type: Support
  url: https://www.aveva.com/en/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aveva.com/en/contact/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it; its MCP endpoint (api.connect.aveva.com/mcp) answers 403, so access sits behind a customer login
  evidence:
  - status: 403
    url: https://api.connect.aveva.com/mcp
  - status: 200
    url: https://www.aveva.com
  reason: customer-only-docs
  state: gated
created: '2026-06-05'
description: AVEVA is an industrial software company (a subsidiary of Schneider Electric) providing engineering, operations, and data management software for energy, utilities, marine, and manufacturing industries. AVEVA's product portfolio includes System Platform (unified SCADA/MES/IIoT), Plant SCADA, MES, Edge, PI System (industrial data infrastructure), and CONNECT cloud services, all of which expose REST APIs for industrial data integration, asset management, and operational analytics.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aveva.png
jsonld:
- class_count: 3
  name: Aveva Context
  property_count: 25
  slug: aveva-context
layout: provider
modified: '2026-06-05'
name: AVEVA
nav: Providers
network: true
overview: 'AVEVA is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include SCADA, MES, Industrial Automation, Manufacturing, and Industrial IoT.


  The AVEVA catalog on APIs.io includes 1 JSON-LD context.


  AVEVA''s developer surface includes changelog, API reference, documentation, engineering blog, support, pricing, and 22 more developer resources.'
plans:
- name: Aveva Plans Pricing
  plan_count: 0
  slug: aveva-plans-pricing
random_paper: 3
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 46.3
    catalog_earned_first_party: 0.0
    catalog_gap: 68.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 35.5
    contract_governance: 3.8
    contract_quality: 10.7
    developer_ergonomics: 36.9
    discoverability: 75.0
    operational_transparency: 21.1
  previous_composite: 35.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 21.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aveva/aveva-2026-06-20T172722.png
security:
- kind: domain-security
  name: Aveva Domain Security
  slug: aveva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aveva Vulnerability Disclosure
  slug: aveva-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Aveva Trust Center
  slug: aveva-trust-center
  summary_line: trust center published
slug: aveva
tags:
- SCADA
- MES
- Industrial Automation
- Manufacturing
- Industrial IoT
- Industrial Data
- Energy
- Industrial
website: https://www.aveva.com
---
