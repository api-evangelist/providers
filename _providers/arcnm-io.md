---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 154
  human_in_the_loop: 11
  name: Arcnm Io Agentic Access
  operation_count: 245
  slug: arcnm-io-agentic-access
  summary_line: 245 operations · 154 acting · 11 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The calculations API from ARCNM — 42 operation(s) for calculations.
  name: ARCNM Calculations API
  slug: arcnm-io-calculations-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The calibration API from ARCNM — 18 operation(s) for calibration.
  name: ARCNM Calibration API
  slug: arcnm-io-calibration-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The datasets API from ARCNM — 3 operation(s) for datasets.
  name: ARCNM Datasets API
  slug: arcnm-io-datasets-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The environments API from ARCNM — 33 operation(s) for environments.
  name: ARCNM Environments API
  slug: arcnm-io-environments-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The folders API from ARCNM — 5 operation(s) for folders.
  name: ARCNM Folders API
  slug: arcnm-io-folders-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The geometry API from ARCNM — 2 operation(s) for geometry.
  name: ARCNM Geometry API
  slug: arcnm-io-geometry-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The import API from ARCNM — 4 operation(s) for import.
  name: ARCNM Import API
  slug: arcnm-io-import-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The machine-library API from ARCNM — 4 operation(s) for machine-library.
  name: ARCNM Machine Library API
  slug: arcnm-io-machine-library-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The machines API from ARCNM — 2 operation(s) for machines.
  name: ARCNM Machines API
  slug: arcnm-io-machines-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The materials API from ARCNM — 22 operation(s) for materials.
  name: ARCNM Materials API
  slug: arcnm-io-materials-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The nesting API from ARCNM — 13 operation(s) for nesting.
  name: ARCNM Nesting API
  slug: arcnm-io-nesting-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The parts API from ARCNM — 8 operation(s) for parts.
  name: ARCNM Parts API
  slug: arcnm-io-parts-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The remnants API from ARCNM — 5 operation(s) for remnants.
  name: ARCNM Remnants API
  slug: arcnm-io-remnants-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The subcontractors API from ARCNM — 3 operation(s) for subcontractors.
  name: ARCNM Subcontractors API
  slug: arcnm-io-subcontractors-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The tools API from ARCNM — 11 operation(s) for tools.
  name: ARCNM Tools API
  slug: arcnm-io-tools-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The upload-links API from ARCNM — 2 operation(s) for upload-links.
  name: ARCNM Upload Links API
  slug: arcnm-io-upload-links-api
- baseURL: https://api.arcnm.io/api/v1
  baseurl_source: declared
  description: The uploads API from ARCNM — 10 operation(s) for uploads.
  name: ARCNM Uploads API
  slug: arcnm-io-uploads-api
artifact_total: 31
common:
- group: auth
  href: https://artifacts.apis.io/arcnm-io/well-known/arcnm-io-n8n-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcnm-io-n8n-security.txt
- group: agent
  href: https://artifacts.apis.io/arcnm-io/agentic-access/arcnm-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/arcnm-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/arcnm-io/rate-limits/arcnm-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/arcnm-io-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/arcnm-io/rules/arcnm-io-rules.yml
  title: ''
  type: Spectral
  url: rules/arcnm-io-rules.yml
- group: design
  href: https://artifacts.apis.io/arcnm-io/json-ld/arcnm-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arcnm-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/arcnm-io/vocabulary/arcnm-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arcnm-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/arcnm-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/arcnm-io/data-model/arcnm-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arcnm-io-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://arcnm.io/docs/security
- group: auth
  href: https://artifacts.apis.io/arcnm-io/authentication/arcnm-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arcnm-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/arcnm-io/errors/arcnm-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arcnm-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/arcnm-io/conformance/arcnm-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arcnm-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arcnm-io/llms/arcnm-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arcnm-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/arcnm-io/well-known/arcnm-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcnm-io-security.txt
- group: auth
  href: https://artifacts.apis.io/arcnm-io/well-known/arcnm-io-omr-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcnm-io-omr-security.txt
- group: auth
  href: https://artifacts.apis.io/arcnm-io/well-known/arcnm-io-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcnm-io-chatgpt-security.txt
- group: agent
  href: https://artifacts.apis.io/arcnm-io/well-known/arcnm-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arcnm-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/arcnm-io/hosts/arcnm-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcnm-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/arcnm-io/vendors/arcnm-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcnm-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arcnm.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcnm.io/privacy
- group: start
  title: ''
  type: SignUp
  url: https://arcnm.io/signup
- group: auth
  href: https://artifacts.apis.io/arcnm-io/security/arcnm-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arcnm-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arcnm-io/security/arcnm-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcnm-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arcnm.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://arcnm.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://arcnm.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.arcnm.io/api/v1/openapi-public.json
- group: start
  title: ''
  type: GettingStarted
  url: https://arcnm.io/docs/connect
- group: operate
  title: ''
  type: Support
  url: mailto:hello@arcnm.io
- group: commercial
  title: ''
  type: Pricing
  url: https://arcnm.io/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arcnm
created: '2026-11-01'
description: ARCNM (legal name rattle mng GmbH) provides physics‑first should‑cost calculations for manufactured parts. By uploading a STEP model or CAD drawing the service extracts features, simulates process planning, and returns detailed cost breakdowns across lot sizes. It combines physics‑based manufacturing simulation with AI‑driven drawing interpretation, delivering auditable cost data for CNC milling, turning, sheet‑metal, additive manufacturing and more. The platform offers a REST API and MCP server for integration with ERP, PLM, and quoting workflows.
image: https://arcnm.io/web-app-manifest-512x512.png
json_schemas:
- name: CalculationCreate
  property_count: 20
  slug: arcnm-io-calculation-create
- name: CalculationDetailResponse
  property_count: 49
  slug: arcnm-io-calculation-detail-response
- name: CalculationTuningUpdate
  property_count: 34
  slug: arcnm-io-calculation-tuning-update
- name: EnvironmentDetail
  property_count: 45
  slug: arcnm-io-environment-detail
- name: EnvironmentEconomicsUpdate
  property_count: 24
  slug: arcnm-io-environment-economics-update
- name: UploadAndQuoteJSON
  property_count: 30
  slug: arcnm-io-upload-and-quote-json
jsonld:
- class_count: 120
  name: Arcnm Io Context
  property_count: 514
  slug: arcnm-io-context
layout: provider
modified: '2026-11-01'
name: ARCNM
nav: Providers
network: true
overview: 'ARCNM publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Calculations API, Calibration API, Datasets API, and 14 more. Tagged areas include Manufacturing, Costing, CAD, and Engineering.


  The ARCNM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ARCNM''s developer surface includes authentication, signup flow, documentation, API reference, getting-started guide, support, pricing, and 25 more developer resources.'
random_paper: 22
rate_limits:
- limit_count: 4
  name: Arcnm Io Rate Limits
  slug: arcnm-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: ARCNM API Rules
  rule_count: 54
  severity_counts:
    error: 42
    hint: 0
    info: 2
    warn: 10
  slug: arcnm-io-rules
scopes:
- name: Arcnm Io Scopes
  scope_count: 0
  slug: arcnm-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.8
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 52.8
    developer_ergonomics: 42.1
    discoverability: 57.1
    operational_transparency: 39.5
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 5.9
      total: 17
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arcnm Io Authentication
  slug: arcnm-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Arcnm Io Domain Security
  slug: arcnm-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arcnm Io Vulnerability Disclosure
  slug: arcnm-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: arcnm-io
tags:
- Manufacturing
- Costing
- CAD
- Engineering
website: https://arcnm.io/
---
