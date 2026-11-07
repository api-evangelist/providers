---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 36
  human_in_the_loop: 3
  name: Aginera Ai Agentic Access
  operation_count: 102
  slug: aginera-ai-agentic-access
  summary_line: 102 operations · 36 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.aginera.ai/partner/v1
  baseurl_source: declared
  description: Account — credits.
  name: Aginera Billing API
  slug: aginera-ai-billing-api
- baseURL: https://api.aginera.ai/partner/v1
  baseurl_source: declared
  description: PDF→CAD conversion — converting and viewing are free; the DXF/DWG download is a one-time purchase per document on free accounts; the website's own pricing, on the user's account.
  name: Aginera CAD API
  slug: aginera-ai-cad-api
- baseURL: https://api.aginera.ai/partner/v1
  baseurl_source: declared
  description: Account — the calling credential and capabilities.
  name: Aginera Clients API
  slug: aginera-ai-clients-api
- baseURL: https://api.aginera.ai/partner/v1
  baseurl_source: declared
  description: Foundation — drawing ingestion.
  name: Aginera Documents API
  slug: aginera-ai-documents-api
- baseURL: https://api.aginera.ai/partner/v1
  baseurl_source: declared
  description: Takeoff API — export results.
  name: Aginera Exports API
  slug: aginera-ai-exports-api
- baseURL: https://api.aginera.ai/partner/v1
  baseurl_source: declared
  description: Foundation — containers for documents and takeoffs.
  name: Aginera Projects API
  slug: aginera-ai-projects-api
- baseURL: https://api.aginera.ai/partner/v1
  baseurl_source: declared
  description: Public taxonomy and enumerations.
  name: Aginera Reference API
  slug: aginera-ai-reference-api
- baseURL: https://api.aginera.ai/partner/v1
  baseurl_source: declared
  description: Takeoff API — run MEP quantity takeoffs and read items, routes and schedules.
  name: Aginera Takeoffs API
  slug: aginera-ai-takeoffs-api
- baseURL: https://api.aginera.ai/partner/v1
  baseurl_source: declared
  description: Account — usage reporting.
  name: Aginera Usage API
  slug: aginera-ai-usage-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/aginera-ai/agentic-access/aginera-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aginera-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/aginera-ai/plans/aginera-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aginera-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aginera-ai/rules/aginera-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/aginera-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/aginera-ai/json-ld/aginera-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aginera-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/aginera-ai/vocabulary/aginera-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aginera-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aginera-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aginera-ai/data-model/aginera-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aginera-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/aginera-ai/conventions/aginera-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aginera-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/aginera-ai/conventions/aginera-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aginera-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/aginera-ai/authentication/aginera-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aginera-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/aginera-ai/errors/aginera-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aginera-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aginera-ai/conformance/aginera-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aginera-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aginera-ai/llms/aginera-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aginera-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/aginera-ai/a2a/aginera-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aginera-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aginera-ai/well-known/aginera-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aginera-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/aginera-ai/hosts/aginera-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aginera-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/aginera-ai/vendors/aginera-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aginera-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aginera.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aginera.ai/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://aginera.ai/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://aginera.ai/docs/developer/api-reference
- group: auth
  href: https://artifacts.apis.io/aginera-ai/scopes/aginera-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aginera-ai-scopes.yml
- group: auth
  href: https://artifacts.apis.io/aginera-ai/security/aginera-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aginera-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aginera.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://aginera.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://aginera.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://aginera.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://aginera.ai/auth/signin
created: '2026-11-01'
description: Aginera provides AI‑powered MEP takeoff and estimating software for construction professionals. Its platform automates extraction of quantities, bills of materials, and cost estimates from PDF and CAD drawings, supporting electrical, mechanical, plumbing, and structural workflows. With features like PDF‑to‑BOM, CAD‑to‑3D, and integrations with popular design tools, Aginera helps contractors and designers accelerate pre‑construction planning, reduce manual effort, and improve accuracy across projects.
image: https://aginera.ai/opengraph-image.png
json_schemas:
- name: CadFileResult
  property_count: 0
  slug: aginera-ai-cad-file-result
- name: CadStatus
  property_count: 12
  slug: aginera-ai-cad-status
- name: Capabilities
  property_count: 14
  slug: aginera-ai-capabilities
- name: DocumentCreate
  property_count: 7
  slug: aginera-ai-document-create
- name: TakeoffItem
  property_count: 22
  slug: aginera-ai-takeoff-item
- name: Takeoff
  property_count: 18
  slug: aginera-ai-takeoff
jsonld:
- class_count: 54
  name: Aginera Ai Context
  property_count: 144
  slug: aginera-ai-context
layout: provider
modified: '2026-11-01'
name: Aginera
nav: Providers
network: true
overview: 'Aginera publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, CAD API, Clients API, and 6 more. Tagged areas include Artificial Intelligence, Construction, Estimating, MEP, and Software.


  The Aginera catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aginera''s developer surface includes authentication, getting-started guide, API reference, documentation, pricing, engineering blog, signup flow, and 21 more developer resources.'
plans:
- name: Aginera Ai Plans Pricing
  plan_count: 3
  slug: aginera-ai-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Aginera API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: aginera-ai-rules
scopes:
- name: Aginera Ai Scopes
  scope_count: 25
  slug: aginera-ai-scopes
  summary_line: 25 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 60.6
    developer_ergonomics: 29.2
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aginera Ai Authentication
  slug: aginera-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Aginera Ai Domain Security
  slug: aginera-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: aginera-ai-create-project
  slug: aginera-ai-create-project
- name: aginera-ai-request-access
  slug: aginera-ai-request-access
- name: aginera-ai-takeoff-processing
  slug: aginera-ai-takeoff-processing
- name: aginera-ai-upload-document
  slug: aginera-ai-upload-document
slug: aginera-ai
tags:
- Artificial Intelligence
- Construction
- Estimating
- MEP
- Software
website: https://aginera.ai/
---
