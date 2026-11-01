---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
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
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Propzapi Com Agentic Access
  operation_count: 22
  slug: propzapi-com-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 1
apis:
- description: REST API for rendering HTML/CSS templates into images and PDFs.
  name: propzapi API
  slug: propzapi-api
- baseURL: https://api.propzapi.com
  baseurl_source: declared
  description: The account API from propzapi-com — 2 operation(s) for account.
  name: propzapi-com Account API
  slug: propzapi-com-account-api
- baseURL: https://api.propzapi.com
  baseurl_source: declared
  description: The billing API from propzapi-com — 2 operation(s) for billing.
  name: propzapi-com Billing API
  slug: propzapi-com-billing-api
- baseURL: https://api.propzapi.com
  baseurl_source: declared
  description: The images API from propzapi-com — 7 operation(s) for images.
  name: propzapi-com Images API
  slug: propzapi-com-images-api
- baseURL: https://api.propzapi.com
  baseurl_source: declared
  description: The meta API from propzapi-com — 2 operation(s) for meta.
  name: propzapi-com Meta API
  slug: propzapi-com-meta-api
- baseURL: https://api.propzapi.com
  baseurl_source: declared
  description: The qr API from propzapi-com — 3 operation(s) for qr.
  name: propzapi-com Qr API
  slug: propzapi-com-qr-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/propzapi-com/agentic-access/propzapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/propzapi-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/propzapi-com/plans/propzapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/propzapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/propzapi-com/rules/propzapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/propzapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/propzapi-com/json-ld/propzapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/propzapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/propzapi-com/vocabulary/propzapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/propzapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/propzapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/propzapi-com/data-model/propzapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/propzapi-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://propzapi.com/contact
- group: auth
  href: https://artifacts.apis.io/propzapi-com/authentication/propzapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/propzapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/propzapi-com/errors/propzapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/propzapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/propzapi-com/conformance/propzapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/propzapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/propzapi-com/llms/propzapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/propzapi-com-llms.txt
- group: build
  href: https://artifacts.apis.io/propzapi-com/mcp/propzapi-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/propzapi-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/propzapi-com/mcp/propzapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/propzapi-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/propzapi-com/well-known/propzapi-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/propzapi-com-security.txt
- group: auth
  href: https://artifacts.apis.io/propzapi-com/well-known/propzapi-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/propzapi-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/propzapi-com/well-known/propzapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/propzapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/propzapi-com/hosts/propzapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/propzapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/propzapi-com/vendors/propzapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/propzapi-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/propzapi-com/packages/propzapi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/propzapi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/propzapi-com/packages/propzapi-com-packages.yml
  title: ''
  type: Packages
  url: packages/propzapi-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://propzapi.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://propzapi.com/legal/privacy
- group: auth
  href: https://artifacts.apis.io/propzapi-com/security/propzapi-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/propzapi-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/propzapi-com/security/propzapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/propzapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://propzapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://propzapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.propzapi.com/openapi.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://propzapi.com/app
- group: commercial
  title: ''
  type: Pricing
  url: https://propzapi.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://propzapi.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://propzapi.com/app?login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paperandbeyond23-gif
created: '2026-10-31'
description: Propzapi provides a RESTful image generation API that renders HTML/CSS templates into PNG, JPEG, WebP, or PDF images. Designed for developers and AI agents, it offers a free trial with 50 images, pay‑as‑you‑go pricing, and no credit‑card requirement. The service includes built‑in templates, customizable rendering options, and an MCP tool for seamless integration with Claude, Cursor, and other AI platforms. It emphasizes low latency, high fidelity, and transparent credit metering, making it suitable for social cards, Open Graph images, certificates, and more.
image: https://propzapi.com/logo.png?v=2
jsonld:
- class_count: 2
  name: Propzapi Com Context
  property_count: 6
  slug: propzapi-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.propzapi.com.
  name: propzapi-com MCP Server
  slug: propzapi-com-mcp-yml
modified: '2026-10-31'
name: propzapi-com
nav: Providers
network: true
overview: 'propzapi-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Billing API, Images API, and 3 more. Tagged areas include Company, Image Generation, Rendering, AI Agents, and API.


  The propzapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  propzapi-com''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, signup flow, and 27 more developer resources.'
plans:
- name: Propzapi Com Plans Pricing
  plan_count: 4
  slug: propzapi-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Propzapi Com Rate Limits
  slug: propzapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: propzapi-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: propzapi-com-rules
scopes:
- name: Propzapi Com Scopes
  scope_count: 0
  slug: propzapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 73.5
    catalog_earned_first_party: 0.0
    catalog_gap: 41.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 39.3
    developer_ergonomics: 54.0
    discoverability: 65.0
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Propzapi Com Authentication
  slug: propzapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Propzapi Com Domain Security
  slug: propzapi-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Propzapi Com Vulnerability Disclosure
  slug: propzapi-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: generate-image
  slug: propzapi-com-generate_image
- name: list-templates
  slug: propzapi-com-list_templates
slug: propzapi-com
tags:
- Company
- Image Generation
- Rendering
- AI Agents
- API
website: https://propzapi.com/
---
