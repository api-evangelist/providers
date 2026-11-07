---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 71.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Cuvo Co Agentic Access
  operation_count: 25
  slug: cuvo-co-agentic-access
  summary_line: 25 operations · 8 acting
api_count: 1
apis:
- baseURL: https://cuvo.co
  baseurl_source: declared
  description: Agent2Agent JSON-RPC endpoint
  name: Cuvo Health A2a API
  slug: cuvo-co-a2a-api
- baseURL: https://cuvo.co
  baseurl_source: declared
  description: Agentic Commerce Protocol checkout ($0 discovery call)
  name: Cuvo Health Acp API
  slug: cuvo-co-acp-api
- baseURL: https://cuvo.co
  baseurl_source: declared
  description: Published site content for agents
  name: Cuvo Health Content API
  slug: cuvo-co-content-api
- baseURL: https://cuvo.co
  baseurl_source: declared
  description: Agent discovery documents
  name: Cuvo Health Discovery API
  slug: cuvo-co-discovery-api
- baseURL: https://cuvo.co
  baseurl_source: declared
  description: Model Context Protocol server
  name: Cuvo Health MCP API
  slug: cuvo-co-mcp-api
- baseURL: https://cuvo.co
  baseurl_source: declared
  description: Deployment health
  name: Cuvo Health Status API
  slug: cuvo-co-status-api
artifact_total: 24
asyncapis:
- description: ''
  name: Cuvo Co Webhooks
  slug: cuvo-co-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/cuvo-co/agentic-access/cuvo-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cuvo-co-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/cuvo-co/rate-limits/cuvo-co-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cuvo-co-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cuvo-co/plans/cuvo-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cuvo-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cuvo-co/rules/cuvo-co-rules.yml
  title: ''
  type: Spectral
  url: rules/cuvo-co-rules.yml
- group: design
  href: https://artifacts.apis.io/cuvo-co/json-ld/cuvo-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cuvo-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/cuvo-co/vocabulary/cuvo-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cuvo-co-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cuvo-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cuvo-co/asyncapi/cuvo-co-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cuvo-co-webhooks.yml
- group: design
  href: https://artifacts.apis.io/cuvo-co/data-model/cuvo-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cuvo-co-data-model.yml
- group: build
  href: https://artifacts.apis.io/cuvo-co/cli/cuvo-co-cli.yml
  title: ''
  type: CLI
  url: cli/cuvo-co-cli.yml
- group: operate
  href: https://artifacts.apis.io/cuvo-co/changelog/cuvo-co-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cuvo-co-changelog.yml
- group: design
  href: https://artifacts.apis.io/cuvo-co/conventions/cuvo-co-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cuvo-co-conventions.yml
- group: design
  href: https://artifacts.apis.io/cuvo-co/conventions/cuvo-co-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cuvo-co-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cuvo.co/compliance
- group: auth
  href: https://artifacts.apis.io/cuvo-co/authentication/cuvo-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cuvo-co-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.cuvo.co/docs/versioning
- group: design
  href: https://artifacts.apis.io/cuvo-co/lifecycle/cuvo-co-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cuvo-co-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cuvo-co/errors/cuvo-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cuvo-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cuvo-co/conformance/cuvo-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cuvo-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cuvo-co/llms/cuvo-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cuvo-co-llms.txt
- group: other
  href: https://artifacts.apis.io/cuvo-co/a2a/cuvo-co-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cuvo-co-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cuvo-co/mcp/cuvo-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cuvo-co-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cuvo-co/well-known/cuvo-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cuvo-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/cuvo-co/hosts/cuvo-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cuvo-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/cuvo-co/vendors/cuvo-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cuvo-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cuvo.co/terms
- group: auth
  title: ''
  type: Security
  url: https://cuvo.co/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cuvo.co/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cuvo.co/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.cuvo.co/docs/changelog
- group: company
  title: ''
  type: Blog
  url: https://cuvo.co/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cuvo.co/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cuvo.co/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cuvo.co/docs/reference
- group: auth
  href: https://artifacts.apis.io/cuvo-co/security/cuvo-co-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cuvo-co-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cuvo-co/security/cuvo-co-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cuvo-co-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cuvo-co/security/cuvo-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cuvo-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cuvo.co/
created: '2026-11-04'
description: Cuvo Health is a white‑label telehealth platform that enables med spas, DTC brands and clinics to launch fully‑compliant telehealth services. It provides licensed providers, pharmacy fulfillment, GLP‑1, HRT, peptide programs, $25 consults, and a turnkey software suite across all 50 US states, with no revenue share for partners.
image: https://cuvo.co/seo/og-image.png
json_schemas:
- name: AcpCheckoutSession
  property_count: 14
  slug: cuvo-co-acp-checkout-session
- name: AcpDiscovery
  property_count: 4
  slug: cuvo-co-acp-discovery
- name: AgentSkillsIndex
  property_count: 3
  slug: cuvo-co-agent-skills-index
- name: AiCatalog
  property_count: 4
  slug: cuvo-co-ai-catalog
- name: AskResponse
  property_count: 4
  slug: cuvo-co-ask-response
- name: McpServerCard
  property_count: 7
  slug: cuvo-co-mcp-server-card
jsonld:
- class_count: 20
  name: Cuvo Co Context
  property_count: 69
  slug: cuvo-co-context
layout: provider
mcp_servers:
- description: Remote MCP server at cuvo.co.
  name: Cuvo Health MCP Server
  slug: cuvo-co-mcp-yml
modified: '2026-11-04'
name: Cuvo Health
nav: Providers
network: true
overview: 'Cuvo Health publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, Acp API, Content API, and 3 more. Tagged areas include Telehealth, White‑Label Platform, Pharmacy Fulfillment, and Brand Licensing.


  The Cuvo Health catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Cuvo Health''s developer surface includes CLI, changelog, authentication, pricing, engineering blog, getting-started guide, documentation, and 31 more developer resources.'
plans:
- name: Cuvo Co Plans Pricing
  plan_count: 6
  slug: cuvo-co-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Cuvo Co Rate Limits
  slug: cuvo-co-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Cuvo Health API Rules
  rule_count: 61
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 4
  slug: cuvo-co-rules
score:
  band: strong
  composite: 63.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 68.6
    developer_ergonomics: 51.8
    discoverability: 56.7
    operational_transparency: 73.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cuvo Co Authentication
  slug: cuvo-co-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cuvo Co Domain Security
  slug: cuvo-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cuvo Co Vulnerability Disclosure
  slug: cuvo-co-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Cuvo Co Trust Center
  slug: cuvo-co-trust-center
  summary_line: SOC 2, HIPAA
skill_count: 1
skills:
- name: cuvo-co-acp-checkout-complete
  slug: cuvo-co-acp-checkout-complete
slug: cuvo-co
tags:
- Telehealth
- White‑Label Platform
- Pharmacy Fulfillment
- Brand Licensing
website: https://cuvo.co/
---
