---
access_model:
  confidence: high
  label: Free demo account, sales-gated production
  onboarding: self-serve
  pricing: unknown
  public: true
  source:
  - https://turquoise.health/signup/?signupContext=api
  - https://turquoise.health/api/docs/start-building.md
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Turquoise Health Agentic Access
  operation_count: 15
  slug: turquoise-health-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 2
apis:
- description: Hosted Model Context Protocol server exposing Turquoise's consumer pricing to AI agents over streamable HTTP. Five workflow-shaped tools — find_entity, compare_prices, provider_cost_detail, explain_pr
  name: Turquoise Connector (MCP)
  slug: turquoise-connector-mcp
- description: Turquoise's open library of Standard Service Packages, which gather all medical services, materials and fees associated with a healthcare procedure and represent them as a single standardized code. SS
  name: Standard Service Packages (SSP)
  slug: standard-service-packages-ssp
- description: The Consumer Pricing API from Turquoise Health — 15 operation(s) for consumer pricing.
  name: Turquoise Health Consumer Pricing API
  slug: turquoise-health-consumer-pricing-api
artifact_total: 13
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/turquoise-health-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://turquoise.health/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://turquoise.health/api/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://turquoise.health/api/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://turquoise.health/api/docs/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://turquoise.health/api/docs/start-building/
- group: company
  title: ''
  type: Blog
  url: https://turquoise.health/resources/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/turquoisehealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/turquoise-health/
- group: other
  title: ''
  type: X
  url: https://twitter.com/TurquoiseHC
- group: commercial
  title: ''
  type: Pricing
  url: https://turquoise.health/plans/providers
- group: start
  title: ''
  type: SignUp
  url: https://turquoise.health/signup/?signupContext=api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://turquoise.health/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://turquoise.health/legal/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/turquoise-health-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/turquoise-health-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/turquoise-health-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/turquoise-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/turquoise-health-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/turquoise-health-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/turquoise-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/turquoise-health-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/turquoise-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://app.vanta.com/turquoise.health/trust/4eadhio8ef1h3zwumb77kp
- group: auth
  title: ''
  type: TrustCenter
  url: security/turquoise-health-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/turquoise-health-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/turquoise-health-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/turquoise-health-consumer-pricing-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/turquoise-health-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/turquoise-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turquoise-health-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/turquoise-health-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/turquoise-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/turquoise-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/turquoise-health-finops.yml
created: '2026-06-13'
description: Turquoise Health is a healthcare price transparency platform. Its public developer surface is the Consumer Pricing API — a documented OpenAPI 3.1.0 REST API at api.turquoise.health covering providers, payers, networks, Standard Service Packages, and cash and insurer-negotiated rates for shoppable services, plus personalized out-of-pocket estimates computed by layering a member's live X12 270/271 eligibility and accumulators onto a negotiated rate. The same OAuth 2.0 client-credentials token also authenticates a hosted Model Context Protocol server at consumer-mcp.turquoise.health, which exposes five workflow-shaped pricing tools to AI agents. Turquoise also sells platform tiers for market intelligence, contract intelligence and precision contracting to providers, payers and life sciences organizations, generates CMS-compliant machine-readable files, and publishes free public tools including the Medicare Pricer, payer transparency scores and a hospital transparency tracker.
finops:
- name: Turquoise Health Finops
  service_category: ''
  slug: turquoise-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turquoise-health.png
jsonld:
- class_count: 17
  name: Turquoise Health Context
  property_count: 38
  slug: turquoise-health-context
layout: provider
mcp_servers:
- description: ''
  name: Turquoise Consumer Pricing MCP
  slug: turquoise-consumer-pricing-mcp
modified: '2026-08-14'
name: Turquoise Health
nav: Providers
network: true
overview: 'Turquoise Health publishes 1 API on the [APIs.io](https://apis.io/) network: Consumer Pricing API. Tagged areas include Healthcare, Price Transparency, Hospital Rates, Payer Rates, and Machine-Readable Files.


  The Turquoise Health catalog on APIs.io includes 1 JSON-LD context.


  Turquoise Health''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 29 more developer resources.'
plans:
- name: Turquoise Health Plans Pricing
  plan_count: 3
  slug: turquoise-health-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Turquoise Health Rate Limits
  slug: turquoise-health-rate-limits
scopes:
- name: Turquoise Health Scopes
  scope_count: 2
  slug: turquoise-health-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: strong
  composite: 60.7
  coverage:
    artifact_dirs: 24
    catalog_gap: 52.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 64.7
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 60.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/turquoise-health/refs/heads/main/screenshots/turquoise-health-2026-08-17T082500.png
security:
- kind: authentication
  name: Turquoise Health Authentication
  slug: turquoise-health-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Turquoise Health Domain Security
  slug: turquoise-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Turquoise Health Trust Center
  slug: turquoise-health-trust-center
  summary_line: SOC 2 Type II, HIPAA
slug: turquoise-health
tags:
- Healthcare
- Price Transparency
- Hospital Rates
- Payer Rates
- Machine-Readable Files
- FHIR
- Health Insurance
- Negotiated Rates
- Out-of-Pocket Costs
- MRF
- Consumer Pricing
- MCP
- Eligibility
- Standard Service Packages
- HIPAA
website: https://turquoise.health/
---
