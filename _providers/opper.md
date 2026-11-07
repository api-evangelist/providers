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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 80
  human_in_the_loop: 8
  name: Opper Agentic Access
  operation_count: 139
  slug: opper-agentic-access
  summary_line: 139 operations · 80 acting · 8 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: Caller identity, credits, and usage
  name: Opper AI Account API
  slug: opper-account-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: Async generation status and downloads
  name: Opper AI Artifacts API
  slug: opper-artifacts-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: Text-to-speech and speech-to-text
  name: Opper AI Audio API
  slug: opper-audio-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: The Compatibility API from Opper AI — 15 operation(s) for compatibility.
  name: Opper AI Compatibility API
  slug: opper-compatibility-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: Reusable file storage for media inputs and generated outputs
  name: Opper AI Files API
  slug: opper-files-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: Schema-driven function management and execution
  name: Opper AI Functions API
  slug: opper-functions-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: Recorded HTTP request/response generations
  name: Opper AI Generations API
  slug: opper-generations-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: Synchronous image generation
  name: Opper AI Images API
  slug: opper-images-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: Programmatic project and API-key management. Authenticates with an `op-mak-…` management token; available on the control_plane and enterprise plans.
  name: Opper AI Management API
  slug: opper-management-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: Model registry and capabilities
  name: Opper AI Models API
  slug: opper-models-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: The OCR API from Opper AI — 1 operation(s) for ocr.
  name: Opper AI OCR API
  slug: opper-ocr-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: The Rerank API from Opper AI — 1 operation(s) for rerank.
  name: Opper AI Rerank API
  slug: opper-rerank-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: Roundtable endpoint — fan out a query to multiple LLMs and combine results
  name: Opper AI Roundtable API
  slug: opper-roundtable-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: The Spans API from Opper AI — 3 operation(s) for spans.
  name: Opper AI Spans API
  slug: opper-spans-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: System health and status
  name: Opper AI System API
  slug: opper-system-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: Web search, fetch, and other utility tools
  name: Opper AI Tools API
  slug: opper-tools-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: The Traces API from Opper AI — 3 operation(s) for traces.
  name: Opper AI Traces API
  slug: opper-traces-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: The User delegation API from Opper AI — 30 operation(s) for user delegation.
  name: Opper AI User delegation API
  slug: opper-user-delegation-api
- baseURL: https://api.opper.ai/v3
  baseurl_source: declared
  description: Asynchronous video generation
  name: Opper AI Videos API
  slug: opper-videos-api
artifact_total: 38
common:
- group: commercial
  href: https://artifacts.apis.io/opper/finops/opper-finops.yml
  title: ''
  type: FinOps
  url: finops/opper-finops.yml
- group: build
  href: https://artifacts.apis.io/opper/integrations/opper-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/opper-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/opper/capabilities/opper-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/opper-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/opper/agentic-access/opper-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/opper-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/opper/plans/opper-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/opper-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/opper/rules/opper-rules.yml
  title: ''
  type: Spectral
  url: rules/opper-rules.yml
- group: design
  href: https://artifacts.apis.io/opper/json-ld/opper-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/opper-context.jsonld
- group: design
  href: https://artifacts.apis.io/opper/vocabulary/opper-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/opper-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/opper/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/opper/data-model/opper-data-model.yml
  title: ''
  type: DataModel
  url: data-model/opper-data-model.yml
- group: build
  href: https://artifacts.apis.io/opper/cli/opper-cli.yml
  title: ''
  type: CLI
  url: cli/opper-cli.yml
- group: design
  href: https://artifacts.apis.io/opper/conventions/opper-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/opper-conventions.yml
- group: design
  href: https://artifacts.apis.io/opper/conventions/opper-conventions.yml
  title: ''
  type: Conventions
  url: conventions/opper-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.opper.ai/
- group: auth
  title: ''
  type: Security
  url: https://opper.ai/security-overview
- group: auth
  href: https://artifacts.apis.io/opper/authentication/opper-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opper-authentication.yml
- group: design
  href: https://artifacts.apis.io/opper/errors/opper-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/opper-problem-types.yml
- group: design
  href: https://artifacts.apis.io/opper/conformance/opper-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opper-conformance.yml
- group: agent
  href: https://artifacts.apis.io/opper/llms/opper-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/opper-llms.txt
- group: other
  href: https://artifacts.apis.io/opper/a2a/opper-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/opper-a2a.yml
- group: auth
  href: https://artifacts.apis.io/opper/well-known/opper-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/opper-security.txt
- group: agent
  href: https://artifacts.apis.io/opper/well-known/opper-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/opper-well-known.yml
- group: other
  href: https://artifacts.apis.io/opper/hosts/opper-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opper-hosts.yml
- group: other
  href: https://artifacts.apis.io/opper/vendors/opper-vendors.yml
  title: ''
  type: Vendors
  url: vendors/opper-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opper.ai/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opper.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opper.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://opper.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://platform.opper.ai/auth/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opper-ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://opper.ai/changelog
- group: company
  title: ''
  type: Blog
  url: https://opper.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.opper.ai/overview/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opper.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.opper.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/opper/security/opper-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/opper-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/opper/security/opper-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/opper-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/opper/security/opper-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opper.ai/
created: '2026-10-15'
description: Opper AI provides a European AI gateway offering access to over 700 AI models via a GDPR‑compliant, ISO‑27001 certified API. It supports OpenAI‑compatible SDKs, pay‑as‑you‑go pricing, spend caps, model allowlists, and zero data retention, targeting developers building AI agents across Europe.
finops:
- has_sources: true
  method: derived
  name: Opper Finops
  primary_unit: platform fee on credit purchases
  service_category: ''
  slug: opper-finops
  template: false
image: https://opper.ai/images/opper-og.jpg
json_schemas:
- name: ChatRequest
  property_count: 20
  slug: opper-chat-request
- name: ModelResolveResponse
  property_count: 4
  slug: opper-model-resolve-response
- name: ModelsResponse
  property_count: 4
  slug: opper-models-response
- name: response.completed
  property_count: 3
  slug: opper-orstream-event-completed
- name: response.in_progress
  property_count: 3
  slug: opper-orstream-event-response-in-progress
- name: RoundtableResponse
  property_count: 4
  slug: opper-roundtable-response
jsonld:
- class_count: 120
  name: Opper Context
  property_count: 348
  slug: opper-context
layout: provider
modified: '2026-10-15'
name: Opper AI
nav: Providers
network: true
overview: 'Opper AI publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Artifacts API, Audio API, and 16 more. Tagged areas include Artificial Intelligence, Gateways, European, OpenAI-Compatible, and GDPR.


  The Opper AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Opper AI''s developer surface includes CLI, authentication, pricing, changelog, engineering blog, getting-started guide, documentation, and 32 more developer resources.'
plans:
- name: Opper Plans Pricing
  plan_count: 3
  slug: opper-plans-pricing
- name: Opper Price Estimates
  plan_count: 0
  slug: opper-price-estimates
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Opper AI API Rules
  rule_count: 60
  severity_counts:
    error: 44
    hint: 0
    info: 2
    warn: 14
  slug: opper-rules
score:
  band: strong
  composite: 56.4
  coverage:
    artifact_dirs: 31
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.3
  facets:
    access_clarity: 73.7
    contract_governance: 35.6
    contract_quality: 63.4
    developer_ergonomics: 36.3
    discoverability: 73.2
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 68.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/opper/opper-2026-11-03T140711.png
security:
- kind: authentication
  name: Opper Authentication
  slug: opper-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Opper Domain Security
  slug: opper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Opper Vulnerability Disclosure
  slug: opper-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Opper Trust Center
  slug: opper-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 3
skills:
- name: opper-create-and-deploy-dynamic-route
  slug: opper-create-and-deploy-dynamic-route
- name: opper-realtime-session-connect
  slug: opper-realtime-session-connect
- name: opper-upload-and-retrieve-file
  slug: opper-upload-and-retrieve-file
slug: opper
tags:
- Artificial Intelligence
- Gateways
- European
- OpenAI-Compatible
- GDPR
website: https://opper.ai/
---
