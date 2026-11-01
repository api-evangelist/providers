---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Developer utility APIs providing IP geolocation, WHOIS, email validation, DNS lookup, and many other tools.
  name: Botoi API
  slug: botoi-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/botoi-com/rules/botoi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/botoi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/botoi-com/json-ld/botoi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/botoi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/botoi-com/vocabulary/botoi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/botoi-com-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/botoi-com/rate-limits/botoi-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/botoi-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/botoi-com/plans/botoi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/botoi-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/botoi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/botoi-com/data-model/botoi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/botoi-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/botoi-com/changelog/botoi-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/botoi-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/botoi-com/conventions/botoi-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/botoi-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/botoi-com/authentication/botoi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/botoi-com-authentication.yml
- group: operate
  href: https://artifacts.apis.io/botoi-com/lifecycle/botoi-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/botoi-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/botoi-com/lifecycle/botoi-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/botoi-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/botoi-com/errors/botoi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/botoi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/botoi-com/conformance/botoi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botoi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/botoi-com/llms/botoi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botoi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/botoi-com/mcp/botoi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/botoi-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/botoi-com/well-known/botoi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/botoi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/botoi-com/hosts/botoi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botoi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/botoi-com/vendors/botoi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botoi-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://botoi.com/api/security/
- group: build
  title: ''
  type: SDKs
  url: https://botoi.com/sdk/
- group: company
  title: ''
  type: Newsroom
  url: https://botoi.com/ar/tools/media/
- group: docs
  title: ''
  type: APIReference
  url: https://botoi.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/botoi-com/security/botoi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botoi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botoi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://botoi.com/api/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://api.botoi.com/docs
- group: company
  title: ''
  type: Blog
  url: https://botoi.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://botoi.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botoi.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://botoi.com/terms/
- group: start
  title: ''
  type: SignUp
  url: https://botoi.com/api/signup/
- group: start
  title: ''
  type: Login
  url: https://botoi.com/api/signin/
created: '2026-10-30'
description: Botoi provides a free suite of over 150 online tools and APIs for developers, designers, and content creators. Hosted on Cloudflare edge, it offers endpoints for IP geolocation, email validation, DNS lookup, hashing, JWT decoding, QR code generation, PDF conversion, and many more, all accessible with a single API key and sub‑50 ms latency. The platform emphasizes MCP‑native integration, supporting AI agents and multiple SDKs, with no credit‑card required for a free key.
image: https://botoi.com/og/default.png
jsonld:
- class_count: 1
  name: Botoi Com Context
  property_count: 4
  slug: botoi-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.botoi.com.
  name: botoi-com MCP Server
  slug: botoi-com-mcp-yml
modified: '2026-10-30'
name: botoi-com
nav: Providers
network: true
overview: 'botoi-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, Tools, Developer, and Free.


  The botoi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  botoi-com''s developer surface includes changelog, authentication, API reference, documentation, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Botoi Com Plans Pricing
  plan_count: 4
  slug: botoi-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Botoi Com Rate Limits
  slug: botoi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: botoi-com API Rules
  rule_count: 17
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 6
  slug: botoi-com-rules
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 80.7
    catalog_earned_first_party: 0.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 6.7
    developer_ergonomics: 54.0
    discoverability: 66.7
    operational_transparency: 53.2
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Botoi Com Authentication
  slug: botoi-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Botoi Com Domain Security
  slug: botoi-com-domain-security
  summary_line: TLSv1.3
skill_count: 5
skills:
- name: botoi-com-auth-signup-flow
  slug: botoi-com-auth-signup-flow
- name: botoi-com-billing-checkout
  slug: botoi-com-billing-checkout
- name: botoi-com-create-webhook-inbox
  slug: botoi-com-create-webhook-inbox
- name: botoi-com-generate-and-validate-uuid
  slug: botoi-com-generate-and-validate-uuid
- name: botoi-com-validate-payment-details
  slug: botoi-com-validate-payment-details
slug: botoi-com
tags:
- Company
- API
- Tools
- Developer
- Free
website: https://botoi.com/
---
