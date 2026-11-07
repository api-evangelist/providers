---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: unknown
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Decionis Policy Evaluation API
  name: Policy Evaluation API
  slug: policy-evaluation-api
- description: Decionis Commerce Gate API
  name: Commerce Gate API
  slug: commerce-gate-api
- baseURL: https://api.decionis.com
  baseurl_source: declared
  description: Decionis evaluates captured execution intent against versioned policies
  name: Decionis Policy Evaluation API .well-known API
  slug: decionis-policy-evaluation-api-well-known-api
- baseURL: https://api.decionis.com/v1
  baseurl_source: declared
  description: 'OpenAPI contract for importing Decionis as a governed verification tool in Vertex AI Agent Engine or ADK workflows. This route is a thin adapter over Decionis Protocol: it normalizes agent intent, for'
  name: Decionis Vertex Extension Verify API Openapi API
  slug: decionis-vertex-extension-verify-api-openapi-api
artifact_total: 22
common:
- group: design
  href: https://artifacts.apis.io/decionis-com/rules/decionis-com-rules.yml
  title: ''
  type: Spectral
  url: rules/decionis-com-rules.yml
- group: design
  href: https://artifacts.apis.io/decionis-com/json-ld/decionis-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/decionis-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/decionis-com/vocabulary/decionis-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/decionis-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/decionis-com/conventions/decionis-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/decionis-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/decionis-com/conventions/decionis-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/decionis-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/decionis-com/conformance/decionis-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/decionis-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/decionis-com/plans/decionis-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/decionis-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/decionis-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/decionis-com/data-model/decionis-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/decionis-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://decionis.com/trust
- group: design
  href: https://artifacts.apis.io/decionis-com/errors/decionis-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/decionis-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/decionis-com/llms/decionis-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/decionis-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/decionis-com/well-known/decionis-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/decionis-com-security.txt
- group: auth
  href: https://artifacts.apis.io/decionis-com/well-known/decionis-com-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/decionis-com-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/decionis-com/well-known/decionis-com-decionis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/decionis-com-decionis-security.txt
- group: auth
  href: https://artifacts.apis.io/decionis-com/well-known/decionis-com-commerce-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/decionis-com-commerce-security.txt
- group: agent
  href: https://artifacts.apis.io/decionis-com/well-known/decionis-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/decionis-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/decionis-com/hosts/decionis-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/decionis-com-hosts.yml
- group: design
  title: ''
  type: Webhooks
  url: https://decionis.com/integrations/webhooks
- group: auth
  title: ''
  type: Security
  url: https://decionis.com/marketplace/aws/security
- group: start
  title: ''
  type: Sandbox
  url: https://decionis.com/sandbox
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@decionis/sdk
- group: company
  title: ''
  type: Newsroom
  url: https://decionis.com/press
- group: start
  title: ''
  type: Login
  url: https://decionis.com/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/decionis
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.decionis.com<!--
- group: auth
  href: https://artifacts.apis.io/decionis-com/security/decionis-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/decionis-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/decionis-com/security/decionis-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/decionis-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/decionis-com/security/decionis-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decionis-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decionis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.decionis.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.decionis.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://decionis.com/start
- group: operate
  title: ''
  type: Support
  url: https://decionis.com/contact
- group: company
  title: ''
  type: Blog
  url: https://decionis.com/research
- group: commercial
  title: ''
  type: Pricing
  url: https://decionis.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://decionis.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://decionis.com/privacy
created: '2026-10-30'
description: Decionis provides AI‑driven autonomous decision‑making for enterprises, allowing policies to approve or block actions such as payments, trades, price changes, or inspections before they are executed. Their platform offers real‑time policy enforcement, signed decision dossiers, and integrations with major services like AWS, SAP, and Adobe, targeting developers, finance, and operations teams.
image: https://decionis.com/api/og/homepage
json_schemas:
- name: CommerceMarketplaceHistoryAssessment
  property_count: 20
  slug: decionis-com-commerce-marketplace-history-assessment
- name: CommerceNativeSnapshotResponse
  property_count: 7
  slug: decionis-com-commerce-native-snapshot-response
- name: CommercePaymentAuthorizationRequest
  property_count: 5
  slug: decionis-com-commerce-payment-authorization-request
- name: CommercePreflightReadiness
  property_count: 13
  slug: decionis-com-commerce-preflight-readiness
- name: PolicyBundle
  property_count: 12
  slug: decionis-com-policy-bundle
- name: SignedOutcomeDriftReport
  property_count: 6
  slug: decionis-com-signed-outcome-drift-report
- name: VertexAuthorityDriftEventRequest
  property_count: 9
  slug: decionis-com-vertex-authority-drift-event-request
- name: VertexAuthorityExecutionTokenVerifyResponse
  property_count: 9
  slug: decionis-com-vertex-authority-execution-token-verify-response
- name: VertexAuthorityOverrideRequest
  property_count: 13
  slug: decionis-com-vertex-authority-override-request
- name: VertexBoundExecutionRequest
  property_count: 17
  slug: decionis-com-vertex-bound-execution-request
- name: VertexVerifyRequest
  property_count: 15
  slug: decionis-com-vertex-verify-request
- name: VertexVerifyResponse
  property_count: 35
  slug: decionis-com-vertex-verify-response
jsonld:
- class_count: 120
  name: Decionis Com Context
  property_count: 320
  slug: decionis-com-context
layout: provider
modified: '2026-10-30'
name: decionis-com
nav: Providers
network: true
overview: 'decionis-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Decionis Policy Evaluation API .well-known API, Decionis Vertex Extension Verify API Openapi API, and 2 more. Tagged areas include Artificial Intelligence, Decision-Making, Enterprise, Automation, and Finance.


  The decionis-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  decionis-com''s developer surface includes sandbox, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 31 more developer resources.'
plans:
- name: Decionis Com Plans Pricing
  plan_count: 2
  slug: decionis-com-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: decionis-com API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 5
  slug: decionis-com-rules
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -14.0
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 45.6
    developer_ergonomics: 39.8
    discoverability: 74.1
    operational_transparency: 11.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 63.7
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 66.7
screenshot: https://apis.io/screenshots/decionis-com/decionis-com-2026-11-03T130405.png
security:
- kind: domain-security
  name: Decionis Com Domain Security
  slug: decionis-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Decionis Com Vulnerability Disclosure
  slug: decionis-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Decionis Com Trust Center
  slug: decionis-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: decionis-com
tags:
- Artificial Intelligence
- Decision-Making
- Enterprise
- Automation
- Finance
website: https://decionis.com/
---
