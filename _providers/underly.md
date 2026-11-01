---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Underly Agentic Access
  operation_count: 16
  slug: underly-agentic-access
  summary_line: 16 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.underly.app/v1
  baseurl_source: declared
  description: The Analyses API from Underly — 7 operation(s) for analyses.
  name: Underly Analyses API
  slug: underly-analyses-api
artifact_total: 15
asyncapis:
- description: ''
  name: Underly Webhooks
  slug: underly-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/underly/agentic-access/underly-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/underly-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/underly/rate-limits/underly-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/underly-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/underly/plans/underly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/underly-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/underly/rules/underly-rules.yml
  title: ''
  type: Spectral
  url: rules/underly-rules.yml
- group: design
  href: https://artifacts.apis.io/underly/json-ld/underly-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/underly-context.jsonld
- group: design
  href: https://artifacts.apis.io/underly/vocabulary/underly-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/underly-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/underly/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/underly/asyncapi/underly-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/underly-webhooks.yml
- group: design
  href: https://artifacts.apis.io/underly/data-model/underly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/underly-data-model.yml
- group: operate
  href: https://artifacts.apis.io/underly/changelog/underly-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/underly-changelog.yml
- group: design
  href: https://artifacts.apis.io/underly/conventions/underly-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/underly-conventions.yml
- group: design
  href: https://artifacts.apis.io/underly/conventions/underly-conventions.yml
  title: ''
  type: Conventions
  url: conventions/underly-conventions.yml
- group: auth
  href: https://artifacts.apis.io/underly/authentication/underly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/underly-authentication.yml
- group: design
  href: https://artifacts.apis.io/underly/errors/underly-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/underly-problem-types.yml
- group: design
  href: https://artifacts.apis.io/underly/conformance/underly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/underly-conformance.yml
- group: agent
  href: https://artifacts.apis.io/underly/llms/underly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/underly-llms.txt
- group: other
  href: https://artifacts.apis.io/underly/hosts/underly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/underly-hosts.yml
- group: other
  href: https://artifacts.apis.io/underly/vendors/underly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/underly-vendors.yml
- group: build
  href: https://artifacts.apis.io/underly/packages/underly-packages.yml
  title: ''
  type: SDKs
  url: packages/underly-packages.yml
- group: build
  href: https://artifacts.apis.io/underly/packages/underly-packages.yml
  title: ''
  type: Packages
  url: packages/underly-packages.yml
- group: start
  title: ''
  type: Login
  url: https://underly.app/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://underly.app/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://underly.app/docs/api
- group: auth
  href: https://artifacts.apis.io/underly/security/underly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/underly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://underly.app
- group: commercial
  title: ''
  type: Pricing
  url: https://underly.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://underly.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://underly.app/privacy
created: '2026-10-30'
description: Underly provides automated bank statement analysis for lenders, brokers, and accountants, extracting true revenue, positions, NSF events, and exportable data. By parsing every line of a bank statement against printed balances, Underly delivers accurate financial insights that streamline underwriting, risk assessment, and accounting workflows. The platform is built to integrate with lending and accounting systems, offering real‑time verification and compliance reporting.
image: https://underly.app/_next/static/immutable/media/social-image.3o7a6ninl_6dd.png
json_schemas:
- name: AnalysisListItem
  property_count: 10
  slug: underly-analysis-list-item
- name: Analysis
  property_count: 9
  slug: underly-analysis
- name: Intake
  property_count: 3
  slug: underly-intake
- name: Position
  property_count: 12
  slug: underly-position
- name: TransactionPage
  property_count: 4
  slug: underly-transaction-page
jsonld:
- class_count: 7
  name: Underly Context
  property_count: 31
  slug: underly-context
layout: provider
modified: '2026-10-30'
name: Underly
nav: Providers
network: true
overview: 'Underly publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Analyses API. Tagged areas include FinTech, Banking, Data Analysis, Lending, and Accounting.


  The Underly catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Underly''s developer surface includes changelog, authentication, API reference, pricing, and 24 more developer resources.'
plans:
- name: Underly Plans Pricing
  plan_count: 2
  slug: underly-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Underly Rate Limits
  slug: underly-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Underly API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: underly-rules
scopes:
- name: Underly Scopes
  scope_count: 0
  slug: underly-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 69.2
    developer_ergonomics: 32.6
    discoverability: 66.1
    operational_transparency: 44.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 33.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Underly Authentication
  slug: underly-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Underly Domain Security
  slug: underly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: underly
tags:
- FinTech
- Banking
- Data Analysis
- Lending
- Accounting
website: https://underly.app
---
