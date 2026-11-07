---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Enosix Agentic Access
  operation_count: 1
  slug: enosix-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: http://localhost:8081/
  baseurl_source: spec
  description: The Search API from enosix — 1 operation(s) for search.
  name: enosix Search API
  slug: enosix-search-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/enosix/agentic-access/enosix-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/enosix-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/enosix/plans/enosix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/enosix-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/enosix/rules/enosix-rules.yml
  title: ''
  type: Spectral
  url: rules/enosix-rules.yml
- group: design
  href: https://artifacts.apis.io/enosix/json-ld/enosix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/enosix-context.jsonld
- group: design
  href: https://artifacts.apis.io/enosix/vocabulary/enosix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/enosix-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/enosix/data-model/enosix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/enosix-data-model.yml
- group: operate
  href: https://artifacts.apis.io/enosix/changelog/enosix-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/enosix-changelog.yml
- group: auth
  href: https://artifacts.apis.io/enosix/authentication/enosix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/enosix-authentication.yml
- group: design
  href: https://artifacts.apis.io/enosix/errors/enosix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/enosix-problem-types.yml
- group: design
  href: https://artifacts.apis.io/enosix/conformance/enosix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/enosix-conformance.yml
- group: agent
  href: https://artifacts.apis.io/enosix/llms/enosix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/enosix-llms.txt
- group: other
  href: https://artifacts.apis.io/enosix/hosts/enosix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/enosix-hosts.yml
- group: other
  href: https://artifacts.apis.io/enosix/vendors/enosix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/enosix-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.enosix.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/enosix
- group: auth
  href: https://artifacts.apis.io/enosix/security/enosix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enosix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://enosix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.enosix.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.enosix.io/release
- group: start
  title: ''
  type: GettingStarted
  url: https://enosix.com/our-story/
- group: operate
  title: ''
  type: Support
  url: https://go.enosix.com/support
- group: company
  title: ''
  type: Blog
  url: https://enosix.com/our-results/
- group: commercial
  title: ''
  type: Pricing
  url: https://enosix.com/product-updates
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.enosix.io/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://enosix.com/privacy-policies/
created: '2026-10-20'
description: Enosix provides governed SAP AI execution for ECC and S/4HANA, delivering real‑time integration, workflow automation, and AI‑driven insights across revenue, customer service, B2B self‑service, product configuration, returns, warranty, field service, and classic CRM. The platform helps enterprises accelerate digital transformation with a secure, compliant, and scalable AI layer for SAP environments.
image: https://enosix.com/wp-content/uploads/2024/08/enosix-logo.jpg
json_schemas:
- name: SalesDocuments
  property_count: 2
  slug: enosix-sales-documents
jsonld:
- class_count: 3
  name: Enosix Context
  property_count: 56
  slug: enosix-context
layout: provider
modified: '2026-10-20'
name: enosix
nav: Providers
network: true
overview: 'enosix publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Search API. Tagged areas include Company, SAP, Artificial Intelligence, Integration, and Workflows.


  The enosix catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  enosix''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 18 more developer resources.'
plans:
- name: Enosix Plans Pricing
  plan_count: 2
  slug: enosix-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: enosix API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: enosix-rules
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 59.2
    catalog_earned_first_party: 8.0
    catalog_gap: 55.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 52.6
    developer_ergonomics: 34.5
    discoverability: 64.3
    operational_transparency: 18.4
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
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
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/enosix/enosix-2026-11-03T131529.png
security:
- kind: authentication
  name: Enosix Authentication
  slug: enosix-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Enosix Domain Security
  slug: enosix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: enosix
tags:
- Company
- SAP
- Artificial Intelligence
- Integration
- Workflows
website: https://enosix.com/
---
