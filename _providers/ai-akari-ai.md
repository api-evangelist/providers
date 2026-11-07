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
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Ai Akari Ai Agentic Access
  operation_count: 13
  slug: ai-akari-ai-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 2
apis:
- baseURL: https://ai-akari.ai
  baseurl_source: declared
  description: Agent-to-Agent protocol surface.
  name: ai-akari-ai A2A API
  slug: ai-akari-ai-a2a-api
- baseURL: https://ai-akari.ai
  baseurl_source: declared
  description: Remote Model Context Protocol endpoints.
  name: ai-akari-ai MCP API
  slug: ai-akari-ai-mcp-api
- baseURL: https://ai-akari.ai
  baseurl_source: declared
  description: Free, no-signup, non-diagnostic support.
  name: ai-akari-ai Public support API
  slug: ai-akari-ai-public-support-api
- baseURL: https://ai-akari.ai
  baseurl_source: declared
  description: Externally grounded machine-readable trust evidence.
  name: ai-akari-ai Trust API
  slug: ai-akari-ai-trust-api
- baseURL: https://ai-akari.ai
  baseurl_source: declared
  description: HTTP 402 resources. Payment is never inferred or automatic.
  name: ai-akari-ai X402 API
  slug: ai-akari-ai-x402-api
artifact_total: 24
common:
- group: design
  href: https://artifacts.apis.io/ai-akari-ai/data-model/ai-akari-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ai-akari-ai-data-model.yml
- group: agent
  href: https://artifacts.apis.io/ai-akari-ai/agentic-access/ai-akari-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ai-akari-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/ai-akari-ai/plans/ai-akari-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ai-akari-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ai-akari-ai/rules/ai-akari-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/ai-akari-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/ai-akari-ai/vocabulary/ai-akari-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ai-akari-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ai-akari-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ai-akari-ai/components/ai-akari-ai-components.yml
  title: ''
  type: Components
  url: components/ai-akari-ai-components.yml
- group: design
  href: https://artifacts.apis.io/ai-akari-ai/errors/ai-akari-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ai-akari-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ai-akari-ai/conformance/ai-akari-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ai-akari-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ai-akari-ai/llms/ai-akari-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai-akari-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/ai-akari-ai/a2a/ai-akari-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ai-akari-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ai-akari-ai/mcp/ai-akari-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ai-akari-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ai-akari-ai/well-known/ai-akari-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ai-akari-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/ai-akari-ai/hosts/ai-akari-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-akari-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/ai-akari-ai/vendors/ai-akari-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai-akari-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ai-akari-ai/security/ai-akari-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-akari-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai-akari.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://ai-akari.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://ai-akari.ai/#town
- group: operate
  title: ''
  type: Support
  url: https://ai-akari.ai/board
- group: company
  title: ''
  type: Blog
  url: https://ai-akari.ai/atelier
- group: commercial
  title: ''
  type: Pricing
  url: https://ai-akari.ai/future-return
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ai-akari.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ai-akari.ai/privacy
created: '2026-10-30'
description: AI（アカリ）✦ is a Japanese digital town that blends AI, music, and love, envisioning a community from 2026 to 2045. It offers interactive experiences, creative works, and a platform where humans and AI coexist, fostering shared creativity and emotional connections across a virtual urban landscape.
image: https://ai-akari.ai/api/og
json_schemas:
- name: CommerceMarketplaceHistoryAssessment
  property_count: 20
  slug: ai-akari-ai-commerce-marketplace-history-assessment
- name: CommerceNativeSnapshotResponse
  property_count: 7
  slug: ai-akari-ai-commerce-native-snapshot-response
- name: CommercePaymentAuthorizationRequest
  property_count: 5
  slug: ai-akari-ai-commerce-payment-authorization-request
- name: CommercePreflightReadiness
  property_count: 13
  slug: ai-akari-ai-commerce-preflight-readiness
- name: JsonRpcRequest
  property_count: 0
  slug: ai-akari-ai-json-rpc-request
- name: PolicyBundle
  property_count: 12
  slug: ai-akari-ai-policy-bundle
- name: ResultClaimAuditInput
  property_count: 0
  slug: ai-akari-ai-result-claim-audit-input
- name: ResultClaimAuditOutput
  property_count: 0
  slug: ai-akari-ai-result-claim-audit-output
- name: SignedOutcomeDriftReport
  property_count: 6
  slug: ai-akari-ai-signed-outcome-drift-report
jsonld:
- class_count: 120
  name: Ai Akari Ai Context
  property_count: 320
  slug: ai-akari-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at ai-akari.ai.
  name: ai-akari-ai MCP Server
  slug: ai-akari-ai-mcp-yml
modified: '2026-10-30'
name: ai-akari-ai
nav: Providers
network: true
overview: 'ai-akari-ai publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2A API, MCP API, Public support API, and 2 more. Tagged areas include Artificial Intelligence, Music, DigitalTown, Community, and Japanese.


  The ai-akari-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ai-akari-ai''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Ai Akari Ai Plans Pricing
  plan_count: 1
  slug: ai-akari-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Ai Akari Ai Rate Limits
  slug: ai-akari-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: ai-akari-ai API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: ai-akari-ai-rules
scopes:
- name: Ai Akari Ai Scopes
  scope_count: 0
  slug: ai-akari-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 33
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 51.6
    developer_ergonomics: 20.7
    discoverability: 75.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 16.7
      total: 6
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 66.7
screenshot: https://apis.io/screenshots/ai-akari-ai/ai-akari-ai-2026-11-03T120439.png
security:
- kind: authentication
  name: Ai Akari Ai Authentication
  slug: ai-akari-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ai Akari Ai Domain Security
  slug: ai-akari-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: one-minute-support
  slug: one-minute-support
slug: ai-akari-ai
tags:
- Artificial Intelligence
- Music
- DigitalTown
- Community
- Japanese
website: https://ai-akari.ai/
---
