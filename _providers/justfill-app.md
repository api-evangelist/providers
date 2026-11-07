---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: JustFill PDF Automation API (MCP) for programmatic PDF form filling.
  name: JustFill API
  slug: justfill-api
- description: 'justfill-app API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: justfill-app API
  slug: justfill-app-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/justfill-app/plans/justfill-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/justfill-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/justfill-app/rules/justfill-app-rules.yml
  title: ''
  type: Spectral
  url: rules/justfill-app-rules.yml
- group: design
  href: https://artifacts.apis.io/justfill-app/json-ld/justfill-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/justfill-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/justfill-app/vocabulary/justfill-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/justfill-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/justfill-app/data-model/justfill-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/justfill-app-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://justfill.app/terms
- group: design
  href: https://artifacts.apis.io/justfill-app/conformance/justfill-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/justfill-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/justfill-app/llms/justfill-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/justfill-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/justfill-app/well-known/justfill-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/justfill-app-security.txt
- group: agent
  href: https://artifacts.apis.io/justfill-app/well-known/justfill-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/justfill-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/justfill-app/hosts/justfill-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/justfill-app-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://justfill.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://justfill.app/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://justfill.app/guides/canva-fillable-pdf
- group: start
  title: ''
  type: GettingStarted
  url: https://justfill.app/solutions/i-9-bulk-onboarding
- group: auth
  href: https://artifacts.apis.io/justfill-app/security/justfill-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/justfill-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/justfill-app/security/justfill-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/justfill-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://justfill.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://justfill.app/pricing
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts despite probing common spec URLs.
  evidence:
  - status: 404
    url: https://justfill.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: JustFill is an AI‑powered web application that fills out PDF forms, including scanned and non‑fillable documents. By detecting form fields visually, it lets users type data, upload CSV/Excel rows, and generate filled PDFs automatically. The service offers free and paid plans, supports voice dictation, batch processing, and ensures data security with encryption and limited retention. It operates entirely in the browser without requiring Adobe.
image: https://justfill.app/favicon.svg
json_schemas:
- name: GetApiAuthDataExportArchiveResponse
  property_count: 1
  slug: justfill-app-get-api-auth-data-export-archive-response
- name: GetApiAuthDataExportResponse
  property_count: 3
  slug: justfill-app-get-api-auth-data-export-response
jsonld:
- class_count: 2
  name: Justfill App Context
  property_count: 1
  slug: justfill-app-context
layout: provider
modified: '2026-10-30'
name: justfill-app
nav: Providers
network: true
overview: 'justfill-app is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, PDF, Form Filling, and Software-as-a-Service.


  The justfill-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  justfill-app''s developer surface includes documentation, getting-started guide, pricing, and 16 more developer resources.'
plans:
- name: Justfill App Plans Pricing
  plan_count: 5
  slug: justfill-app-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Justfill App Rate Limits
  slug: justfill-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: justfill-app API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: justfill-app-rules
scopes:
- name: Justfill App Scopes
  scope_count: 0
  slug: justfill-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 10.7
    discoverability: 64.3
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 35.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/justfill-app/justfill-app-2026-11-03T134256.png
security:
- kind: authentication
  name: Justfill App Authentication
  slug: justfill-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Justfill App Domain Security
  slug: justfill-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Justfill App Vulnerability Disclosure
  slug: justfill-app-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: justfill-app
tags:
- Company
- Artificial Intelligence
- PDF
- Form Filling
- Software-as-a-Service
website: https://justfill.app/
---
