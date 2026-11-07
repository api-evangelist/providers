---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: MCP endpoint exposing Asva AI brand visibility data to AI assistants via the Model Context Protocol.
  name: MCP Server
  slug: mcp-server
- description: 'Asva AI API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Asva AI API
  slug: asvaai-com-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/asvaai-com/plans/asvaai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/asvaai-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/asvaai-com/rules/asvaai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/asvaai-com-rules.yml
- group: design
  href: https://artifacts.apis.io/asvaai-com/json-ld/asvaai-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/asvaai-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/asvaai-com/vocabulary/asvaai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asvaai-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/asvaai-com/data-model/asvaai-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/asvaai-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://asvaai.com/security
- group: auth
  href: https://artifacts.apis.io/asvaai-com/authentication/asvaai-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/asvaai-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/asvaai-com/conformance/asvaai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asvaai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/asvaai-com/llms/asvaai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asvaai-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/asvaai-com/mcp/asvaai-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/asvaai-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/asvaai-com/well-known/asvaai-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/asvaai-com-security.txt
- group: agent
  href: https://artifacts.apis.io/asvaai-com/well-known/asvaai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asvaai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/asvaai-com/hosts/asvaai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asvaai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/asvaai-com/vendors/asvaai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asvaai-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.asvaai.com/register
- group: auth
  title: ''
  type: Security
  url: https://asvaai.com/security
- group: auth
  href: https://artifacts.apis.io/asvaai-com/security/asvaai-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/asvaai-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/asvaai-com/security/asvaai-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/asvaai-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/asvaai-com/security/asvaai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asvaai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asvaai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://asvaai.com/docs/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://asvaai.com/docs/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://asvaai.com/demo
- group: operate
  title: ''
  type: Support
  url: https://asvaai.com/company/contact
- group: company
  title: ''
  type: Blog
  url: https://asvaai.com/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://asvaai.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asvaai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asvaai.com/privacy
coverage:
  checked: '2026-11-02'
  detail: Documentation page provides an MCP endpoint but no OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract.
  evidence:
  - status: 200
    url: https://asvaai.com/docs/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Asva AI is a leading Answer Engine Optimization platform that helps brands monitor and improve their visibility across AI answer engines such as ChatGPT, Claude, Perplexion, Gemini, and over 50 other AI platforms. It provides tools for tracking brand mentions, citations, and AI-driven traffic, offering insights and recommendations to enhance AI search presence and brand reputation. The service includes brand visibility tracking, citation intelligence, prompt discovery, and AI traffic analysis, catering to businesses seeking to optimize their AI-driven marketing and SEO strategies.
image: https://asvaai.com/lovable-uploads/dbad9573-bcc3-4692-b5d8-9f8547bad91f.png
json_schemas:
- name: PostAcpV1ProductsSearchRequest
  property_count: 4
  slug: asvaai-com-post-acp-v1-products-search-request
- name: PostAcpV1ProductsSearchResponse
  property_count: 9
  slug: asvaai-com-post-acp-v1-products-search-response
jsonld:
- class_count: 2
  name: Asvaai Com Context
  property_count: 12
  slug: asvaai-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.asvaai.com.
  name: Asva AI MCP Server
  slug: asvaai-com-mcp-yml
modified: '2026-11-01'
name: Asva AI
nav: Providers
network: true
overview: 'Asva AI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketing, SEO, Brand Monitoring, and Analytics.


  The Asva AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Asva AI''s developer surface includes authentication, signup flow, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
plans:
- name: Asvaai Com Plans Pricing
  plan_count: 4
  slug: asvaai-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Asvaai Com Rate Limits
  slug: asvaai-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: Asva AI API Rules
  rule_count: 33
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 1
  slug: asvaai-com-rules
scopes:
- name: Asvaai Com Scopes
  scope_count: 0
  slug: asvaai-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 21.9
    developer_ergonomics: 29.8
    discoverability: 56.7
    operational_transparency: 5.3
  previous_composite: 48.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Asvaai Com Authentication
  slug: asvaai-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Asvaai Com Domain Security
  slug: asvaai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Asvaai Com Vulnerability Disclosure
  slug: asvaai-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Asvaai Com Trust Center
  slug: asvaai-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: asvaai-com
tags:
- Artificial Intelligence
- Marketing
- SEO
- Brand Monitoring
- Analytics
website: https://asvaai.com/
---
