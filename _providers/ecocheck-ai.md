---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ecocheck Ai Agentic Access
  operation_count: 12
  slug: ecocheck-ai-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- baseURL: https://ecocheck.ai/agent-api
  baseurl_source: declared
  description: The About API from EcoCheck — 1 operation(s) for about.
  name: EcoCheck About API
  slug: ecocheck-ai-about-api
- baseURL: https://ecocheck.ai/agent-api
  baseurl_source: declared
  description: The Articles API from EcoCheck — 2 operation(s) for articles.
  name: EcoCheck Articles API
  slug: ecocheck-ai-articles-api
- baseURL: https://ecocheck.ai/agent-api
  baseurl_source: declared
  description: The Cbam API from EcoCheck — 3 operation(s) for cbam.
  name: EcoCheck Cbam API
  slug: ecocheck-ai-cbam-api
- baseURL: https://ecocheck.ai/agent-api
  baseurl_source: declared
  description: The Health API from EcoCheck — 1 operation(s) for health.
  name: EcoCheck Health API
  slug: ecocheck-ai-health-api
- baseURL: https://ecocheck.ai/agent-api
  baseurl_source: declared
  description: The Obligation API from EcoCheck — 1 operation(s) for obligation.
  name: EcoCheck Obligation API
  slug: ecocheck-ai-obligation-api
- baseURL: https://ecocheck.ai/agent-api
  baseurl_source: declared
  description: The Pricing API from EcoCheck — 1 operation(s) for pricing.
  name: EcoCheck Pricing API
  slug: ecocheck-ai-pricing-api
- baseURL: https://ecocheck.ai/agent-api
  baseurl_source: declared
  description: The Regulations API from EcoCheck — 1 operation(s) for regulations.
  name: EcoCheck Regulations API
  slug: ecocheck-ai-regulations-api
- baseURL: https://ecocheck.ai/agent-api
  baseurl_source: declared
  description: The Search API from EcoCheck — 1 operation(s) for search.
  name: EcoCheck Search API
  slug: ecocheck-ai-search-api
- baseURL: https://ecocheck.ai/agent-api
  baseurl_source: declared
  description: The Services API from EcoCheck — 1 operation(s) for services.
  name: EcoCheck Services API
  slug: ecocheck-ai-services-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/ecocheck-ai/agentic-access/ecocheck-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ecocheck-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/ecocheck-ai/plans/ecocheck-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ecocheck-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ecocheck-ai/rules/ecocheck-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/ecocheck-ai-rules.yml
- group: auth
  title: ''
  type: Security
  url: https://ecocheck.ai/chinh-sach-bao-mat
- group: design
  href: https://artifacts.apis.io/ecocheck-ai/errors/ecocheck-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ecocheck-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ecocheck-ai/conformance/ecocheck-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ecocheck-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ecocheck-ai/llms/ecocheck-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ecocheck-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/ecocheck-ai/a2a/ecocheck-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ecocheck-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ecocheck-ai/mcp/ecocheck-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ecocheck-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/ecocheck-ai/well-known/ecocheck-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ecocheck-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/ecocheck-ai/well-known/ecocheck-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ecocheck-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/ecocheck-ai/hosts/ecocheck-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecocheck-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/ecocheck-ai/vendors/ecocheck-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ecocheck-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ecocheck.ai/ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ecocheck.ai/ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://ecocheck.ai/solutions/pricing
- group: start
  title: ''
  type: Login
  url: https://ecocheck.ai/auth/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://ecocheck.ai/ai/docs
- group: company
  title: ''
  type: Blog
  url: https://ecocheck.ai/article/blog
- group: docs
  title: ''
  type: APIReference
  url: https://ecocheck.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/ecocheck-ai/security/ecocheck-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ecocheck-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ecocheck-ai/security/ecocheck-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecocheck-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ecocheck.ai/
created: '2026-11-06'
description: EcoCheck provides greenhouse gas emissions inventory and management software for Vietnamese enterprises, automating Scope 1, 2, 3 calculations, generating reports compliant with Vietnamese regulations (NĐ 06/TT 38) and international standards (ISO 14064, ISO 14067, CBAM). The platform offers tiered pricing, integrates with AWS Cognito, and supports carbon footprint tracking for products and operations.
image: https://ecocheck.ai/assets/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at ecocheck.ai.
  name: EcoCheck MCP Server
  slug: ecocheck-ai-mcp-yml
modified: '2026-11-06'
name: EcoCheck
nav: Providers
network: true
overview: 'EcoCheck publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including About API, Articles API, Cbam API, and 6 more. Tagged areas include Company, Greenhouse Gas, Emissions, Vietnam, and Software-as-a-Service.


  The EcoCheck catalog on APIs.io includes 1 Spectral governance ruleset.


  EcoCheck''s developer surface includes pricing, documentation, engineering blog, API reference, and 19 more developer resources.'
plans:
- name: Ecocheck Ai Plans Pricing
  plan_count: 4
  slug: ecocheck-ai-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: EcoCheck API Rules
  rule_count: 35
  severity_counts:
    error: 32
    hint: 0
    info: 2
    warn: 1
  slug: ecocheck-ai-rules
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 41.3
    developer_ergonomics: 19.0
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ecocheck Ai Domain Security
  slug: ecocheck-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ecocheck Ai Vulnerability Disclosure
  slug: ecocheck-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ecocheck-ai
tags:
- Company
- Greenhouse Gas
- Emissions
- Vietnam
- Software-as-a-Service
- Climate
website: https://ecocheck.ai/
---
