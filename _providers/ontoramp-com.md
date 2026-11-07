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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Ontoramp Com Agentic Access
  operation_count: 10
  slug: ontoramp-com-agentic-access
  summary_line: 10 operations · 10 acting
api_count: 1
apis:
- baseURL: https://mcp.ontoramp.com
  baseurl_source: declared
  description: Agent-initiated purchase. Mint a Stripe Checkout link for a self-serve plan; payment completes on Stripe's hosted page (no API key required).
  name: ontoramp-com Commerce API
  slug: ontoramp-com-commerce-api
- baseURL: https://mcp.ontoramp.com
  baseurl_source: declared
  description: 'Request an assessment, submit a full tenant-isolated assessment questionnaire (Developer tier or above), log consequential decisions to a governed decision record, and evaluate decisions against your '
  name: ontoramp-com Decision Intelligence API
  slug: ontoramp-com-decision-intelligence-api
- baseURL: https://mcp.ontoramp.com
  baseurl_source: declared
  description: 'Governance maturity gap analysis, document compliance linting, and evidence-linked governance briefs. SOC 2 readiness, ISO 27001, NIST CSF. Free tier: fair-use monthly allowance.'
  name: ontoramp-com Governance Evaluator API
  slug: ontoramp-com-governance-evaluator-api
- baseURL: https://mcp.ontoramp.com
  baseurl_source: declared
  description: 'Search and traverse the client-safe tier of OntoRamp''s governed knowledge base for architecture assessment, compliance mapping, and control analysis. Free tier: fair-use monthly allowance.'
  name: ontoramp-com Knowledge Graph API
  slug: ontoramp-com-knowledge-graph-api
- baseURL: https://mcp.ontoramp.com
  baseurl_source: declared
  description: 'Run governance maturity simulations and retrieve domain-level assessment verdicts with evidence-backed rationale. Free tier: fair-use allowance; running projections is Org tier.'
  name: ontoramp-com Projection Engine API
  slug: ontoramp-com-projection-engine-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/ontoramp-com/agentic-access/ontoramp-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ontoramp-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/ontoramp-com/plans/ontoramp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ontoramp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ontoramp-com/rules/ontoramp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ontoramp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ontoramp-com/json-ld/ontoramp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ontoramp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ontoramp-com/vocabulary/ontoramp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ontoramp-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ontoramp-com/data-model/ontoramp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ontoramp-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/ontoramp-com/conventions/ontoramp-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ontoramp-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/ontoramp-com/conventions/ontoramp-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ontoramp-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/ontoramp-com/authentication/ontoramp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ontoramp-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/ontoramp-com/errors/ontoramp-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ontoramp-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ontoramp-com/conformance/ontoramp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ontoramp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ontoramp-com/llms/ontoramp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ontoramp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ontoramp-com/well-known/ontoramp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ontoramp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ontoramp-com/hosts/ontoramp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ontoramp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ontoramp-com/vendors/ontoramp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ontoramp-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ontoramp.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://ontoramp.com/support
- group: auth
  title: ''
  type: Security
  url: https://ontoramp.com/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ontoramp.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://ontoramp.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://ontoramp.com/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://ontoramp.com/docs
- group: auth
  href: https://artifacts.apis.io/ontoramp-com/security/ontoramp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ontoramp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ontoramp.com/
created: '2026-10-29'
description: OntoRamp provides a governance operating system for agentic AI, offering tools to assess, certify, and roadmap governance integrity. The platform delivers a 3D governance simulation, certification programs, and a marketplace of governance tools, helping organizations ensure responsible AI deployment and compliance with emerging standards.
image: https://ontoramp.com/opengraph-image?aa455c3aac66d993
json_schemas:
- name: CheckoutLink
  property_count: 1
  slug: ontoramp-com-checkout-link
- name: CheckoutRequest
  property_count: 5
  slug: ontoramp-com-checkout-request
- name: McpRequest
  property_count: 4
  slug: ontoramp-com-mcp-request
- name: McpResponse
  property_count: 3
  slug: ontoramp-com-mcp-response
jsonld:
- class_count: 19
  name: Ontoramp Com Context
  property_count: 48
  slug: ontoramp-com-context
layout: provider
modified: '2026-10-29'
name: ontoramp-com
nav: Providers
network: true
overview: 'ontoramp-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Commerce API, Decision Intelligence API, Governance Evaluator API, and 2 more. Tagged areas include Company, AI Governance, AI Agents, Compliance, and Certification.


  The ontoramp-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ontoramp-com''s developer surface includes authentication, support, pricing, getting-started guide, API reference, and 19 more developer resources.'
plans:
- name: Ontoramp Com Plans Pricing
  plan_count: 6
  slug: ontoramp-com-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: ontoramp-com API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: ontoramp-com-rules
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 61.2
    developer_ergonomics: 23.8
    discoverability: 73.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/ontoramp-com/ontoramp-com-2026-11-03T140614.png
security:
- kind: authentication
  name: Ontoramp Com Authentication
  slug: ontoramp-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ontoramp Com Domain Security
  slug: ontoramp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ontoramp-com
tags:
- Company
- AI Governance
- AI Agents
- Compliance
- Certification
website: https://ontoramp.com/
---
