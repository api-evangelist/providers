---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://catalogguard.noahcortezj-c.workers.dev
  baseurl_source: declared
  description: The Catalog API from Catalog Guard API — 2 operation(s) for catalog.
  name: Catalog Guard API Catalog API
  slug: catalog-guard-api-catalog-api
artifact_total: 8
collections:
- collection_type: open
  name: Guard Catalog API
  slug: open-catalog-guard-api-catalog-api
common:
- group: other
  href: https://artifacts.apis.io/catalog-guard-api/capabilities/catalog-guard-api-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/catalog-guard-api-capability-edges.yml
- group: docs
  title: ''
  type: Documentation
  url: https://catalogguard.noahcortezj-c.workers.dev/api/v1/catalog/docs
- group: docs
  title: ''
  type: APIReference
  url: https://catalogguard.noahcortezj-c.workers.dev/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://catalogguard.noahcortezj-c.workers.dev/api/v1/catalog/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://catalogguard.noahcortezj-c.workers.dev/diagnostic
- group: commercial
  title: ''
  type: TermsOfService
  url: https://catalogguard.noahcortezj-c.workers.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://catalogguard.noahcortezj-c.workers.dev/privacy
- group: other
  title: ''
  type: APIsJson
  url: https://catalogguard.noahcortezj-c.workers.dev/apis.json
- group: docs
  href: https://artifacts.apis.io/catalog-guard-api/openapi/_original/catalog-guard-api-catalog-check-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/catalog-guard-api-catalog-check-openapi.json
- group: docs
  href: https://artifacts.apis.io/catalog-guard-api/overlays/catalog-guard-api-catalog-check-overlay.yaml
  title: ''
  type: OpenAPIOverlay
  url: overlays/catalog-guard-api-catalog-check-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/catalog-guard-api/authentication/catalog-guard-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/catalog-guard-api-authentication.yml
- group: design
  href: https://artifacts.apis.io/catalog-guard-api/conventions/catalog-guard-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/catalog-guard-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/catalog-guard-api/errors/catalog-guard-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/catalog-guard-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/catalog-guard-api/lifecycle/catalog-guard-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/catalog-guard-api-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/catalog-guard-api/rate-limits/catalog-guard-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/catalog-guard-api-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/catalog-guard-api/conformance/catalog-guard-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/catalog-guard-api-conformance.yml
- group: design
  href: https://artifacts.apis.io/catalog-guard-api/data-model/catalog-guard-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/catalog-guard-api-data-model.yml
- group: build
  href: https://artifacts.apis.io/catalog-guard-api/examples/catalog-guard-api-examples.yml
  title: ''
  type: Examples
  url: examples/catalog-guard-api-examples.yml
- group: agent
  href: https://artifacts.apis.io/catalog-guard-api/mcp/catalog-guard-api-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/catalog-guard-api-mcp.yml
- group: build
  href: https://artifacts.apis.io/catalog-guard-api/mcp/catalog-guard-api-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/catalog-guard-api-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/catalog-guard-api/llms/catalog-guard-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/catalog-guard-api-llms.txt
- group: agent
  href: https://artifacts.apis.io/catalog-guard-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/catalog-guard-api/security/catalog-guard-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catalog-guard-api-domain-security.yml
created: '2026-07-31'
description: 'A bounded, fail-closed catalog preflight and validation service for Shopify-shaped supplier product CSVs. Exposes an unauthenticated JSON HTTP API that validates raw CSV text or normalized product rows and returns a deterministic result: safe rows, blockers and warnings, each finding carrying a row index, field, stable code and message. Ambiguous input is refused rather than guessed — unclosed quotes, malformed rows, duplicate headers, duplicate normalized SKUs and incomplete variant pairs all become blockers, and supplier categories are treated as audit-only rather than mapped to a Shopify taxonomy. The service does not accept file uploads, credentials, payment data or store connections, holds no storage, and never imports or modifies a catalog; every successful response repeats those disclosures inline as machine-readable fields. Access is controlled by input bounds and a best-effort rate limit rather than by identity. Commercially it is fronted by a free in-browser CSV preflight,
  a $149 bounded human CSV Diagnostic, and a separate free Shopify store-launch referral path.'
image: https://catalogguard.noahcortezj-c.workers.dev/og.png
layout: provider
modified: '2026-08-09'
name: Catalog Guard API
nav: Providers
network: true
overview: 'Catalog Guard API publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Catalog API. Tagged areas include E-Commerce, catalog-validation, Shopify, Data Quality, and CSV validation.


  The Catalog Guard API catalog on APIs.io includes 1 Spectral governance ruleset.


  Catalog Guard API''s developer surface includes documentation, API reference, getting-started guide, pricing, authentication, code examples, and 17 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 1
  name: Catalog Guard Api Rate Limits
  slug: catalog-guard-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 68
  extends:
  - spectral:oas
  name: Catalog Guard API API Rules
  rule_count: 27
  severity_counts:
    error: 25
    hint: 0
    info: 1
    warn: 1
  slug: catalog-guard-api-rules
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 46.5
    catalog_earned_first_party: 8.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 42.3
    discoverability: 60.7
    operational_transparency: 21.1
  previous_composite: 37.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/catalog-guard-api/catalog-guard-api-2026-09-02T145033.png
security:
- kind: authentication
  name: Catalog Guard Api Authentication
  slug: catalog-guard-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Catalog Guard Api Domain Security
  slug: catalog-guard-api-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Preflight a supplier catalog CSV before a Shopify import
  slug: catalog-guard-api-preflight-supplier-csv
- name: Triage Catalog Guard blockers into a supplier fix list
  slug: catalog-guard-api-triage-blockers
slug: catalog-guard-api
tags:
- E-Commerce
- catalog-validation
- Shopify
- Data Quality
- CSV validation
- product-data-qa
- data-preflight
- Data Validation
- Retail
---
