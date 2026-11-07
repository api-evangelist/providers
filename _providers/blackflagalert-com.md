---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    auth_clarity: false
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
  score: 20.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Open API v2 for Black Flag Alert providing company credit risk data.
  name: Black Flag Alert API
  slug: black-flag-alert-api
- baseURL: https://blackflagalert.com
  baseurl_source: declared
  description: 'England & Wales company credit-risk intelligence for AI agents and integrations. R-Score (0-100) combines filed accounts, filing behaviour, charges, CCJs and winding-up activity into one number. Auth:'
  name: Black Flag Alert Open API v2 API
  slug: black-flag-alert-open-api-v2-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/blackflagalert-com/plans/blackflagalert-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blackflagalert-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/blackflagalert-com/rules/blackflagalert-com-rules.yml
  title: ''
  type: Spectral
  url: rules/blackflagalert-com-rules.yml
- group: design
  href: https://artifacts.apis.io/blackflagalert-com/json-ld/blackflagalert-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blackflagalert-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/blackflagalert-com/vocabulary/blackflagalert-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blackflagalert-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/blackflagalert-com/data-model/blackflagalert-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blackflagalert-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/blackflagalert-com/errors/blackflagalert-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blackflagalert-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blackflagalert-com/conformance/blackflagalert-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blackflagalert-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blackflagalert-com/llms/blackflagalert-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blackflagalert-com-llms.txt
- group: other
  href: https://artifacts.apis.io/blackflagalert-com/hosts/blackflagalert-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blackflagalert-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blackflagalert-com/vendors/blackflagalert-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blackflagalert-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blackflagalert.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blackflagalert.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://blackflagalert.com/pricing
- group: start
  title: ''
  type: Login
  url: https://blackflagalert.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://blackflagalert.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://blackflagalert.com/developers
- group: auth
  href: https://artifacts.apis.io/blackflagalert-com/security/blackflagalert-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blackflagalert-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blackflagalert.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://blackflagalert.com/openapi.json
  - status: 401
    url: https://blackflagalert.com/api/mcp
  - status: 200
    url: https://blackflagalert.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Black Flag Alert provides free credit checks for UK companies using primary public records. Operated by Plainview Ventures Limited, it computes an in‑house R‑Score from filed accounts, court judgments and other signals, covering around 3.4 million companies in England & Wales. The service is freemium with core access free and no paid tiers planned. It emphasizes no‑footprint searches and auditable scoring methodology, with detailed principles and a methodology whitepaper available.
image: https://blackflagalert.com/logo.png
json_schemas:
- name: BatchRequest
  property_count: 1
  slug: blackflagalert-com-batch-request
- name: SignupRequest
  property_count: 2
  slug: blackflagalert-com-signup-request
jsonld:
- class_count: 4
  name: Blackflagalert Com Context
  property_count: 9
  slug: blackflagalert-com-context
layout: provider
modified: '2026-11-02'
name: Black Flag Alert
nav: Providers
network: true
overview: 'Black Flag Alert publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Open API v2 API, and 1 more. Tagged areas include Credit Intelligence, Company Data, Risk Scoring, UK Companies, and Financial Services.


  The Black Flag Alert catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Black Flag Alert''s developer surface includes pricing, documentation, API reference, and 15 more developer resources.'
plans:
- name: Blackflagalert Com Plans Pricing
  plan_count: 1
  slug: blackflagalert-com-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Black Flag Alert API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: blackflagalert-com-rules
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 64.8
    catalog_earned_first_party: 8.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 51.2
    developer_ergonomics: 8.3
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blackflagalert Com Domain Security
  slug: blackflagalert-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blackflagalert-com
tags:
- Credit Intelligence
- Company Data
- Risk Scoring
- UK Companies
- Financial Services
website: https://blackflagalert.com/
---
