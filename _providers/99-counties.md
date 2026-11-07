---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Agent-driven commerce for the 99 Counties Shopify store via the Universal Commerce Protocol over MCP — catalog search, cart, checkout, fulfillment, and buyer-approved order completion.
  name: 99 Counties Commerce (UCP)
  slug: 99-counties-commerce-ucp
- description: '99 Counties API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: 99 Counties API
  slug: 99-counties-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/99-counties/rate-limits/99-counties-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/99-counties-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/99-counties/rules/99-counties-rules.yml
  title: ''
  type: Spectral
  url: rules/99-counties-rules.yml
- group: design
  href: https://artifacts.apis.io/99-counties/json-ld/99-counties-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/99-counties-context.jsonld
- group: design
  href: https://artifacts.apis.io/99-counties/vocabulary/99-counties-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/99-counties-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/99-counties/data-model/99-counties-data-model.yml
  title: ''
  type: DataModel
  url: data-model/99-counties-data-model.yml
- group: other
  href: https://artifacts.apis.io/99-counties/hosts/99-counties-hosts.yml
  title: ''
  type: Hosts
  url: hosts/99-counties-hosts.yml
- group: other
  href: https://artifacts.apis.io/99-counties/vendors/99-counties-vendors.yml
  title: ''
  type: Vendors
  url: vendors/99-counties-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://shopify.dev/docs/agents/get-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://99counties.com/blogs/main
- group: company
  title: ''
  type: BlogRSS
  url: https://99counties.com/blogs/main.atom
- group: company
  title: ''
  type: Website
  url: https://99counties.com
- group: docs
  title: ''
  type: Documentation
  url: https://99counties.com/agents.md
- group: agent
  href: https://artifacts.apis.io/99-counties/llms/99-counties-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/99-counties-llms.txt
- group: agent
  href: https://artifacts.apis.io/99-counties/mcp/99-counties-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/99-counties-mcp.yml
- group: agent
  href: https://artifacts.apis.io/99-counties/well-known/99-counties-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/99-counties-well-known.yml
- group: auth
  href: https://artifacts.apis.io/99-counties/authentication/99-counties-authentication.yml
  title: ''
  type: Authentication
  url: authentication/99-counties-authentication.yml
- group: auth
  href: https://artifacts.apis.io/99-counties/scopes/99-counties-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/99-counties-scopes.yml
- group: design
  href: https://artifacts.apis.io/99-counties/conventions/99-counties-conventions.yml
  title: ''
  type: Conventions
  url: conventions/99-counties-conventions.yml
- group: design
  href: https://artifacts.apis.io/99-counties/conformance/99-counties-conformance.yml
  title: ''
  type: Conformance
  url: conformance/99-counties-conformance.yml
- group: design
  href: https://artifacts.apis.io/99-counties/lifecycle/99-counties-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/99-counties-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/99-counties/skills/99-counties-ucp-shopping.md
  title: ''
  type: AgentSkill
  url: skills/99-counties-ucp-shopping.md
- group: auth
  href: https://artifacts.apis.io/99-counties/security/99-counties-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/99-counties-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://99counties.com/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://99counties.com/account/register
- group: start
  title: ''
  type: Login
  url: https://99counties.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://99counties.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://99counties.com/policies/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://99counties.com/pages/faqs
- group: docs
  title: ''
  type: APIReference
  url: https://99counties.com/.well-known/ucp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/99counties
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI or other machine-readable contract found; only external UCP schema references are provided.
  evidence:
  - status: 404
    url: https://99counties.com/openapi.json
  - status: 404
    url: https://99counties.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: 99 Counties is a regenerative-agriculture meat company selling 100% grass-fed and grass-finished beef and bison, pasture-raised pork, poultry, and lamb, plus wild-caught seafood, sourced from small family farms across Iowa, Wisconsin, and Minnesota. Its Shopify storefront exposes an agent-native commerce surface implementing the Universal Commerce Protocol (UCP) over a published MCP endpoint, alongside Shopify Customer Account OAuth 2.0 / OpenID Connect and standard read-only product and collection JSON. It was surfaced through the API Evangelist VC-portfolio pipeline and enriched from its live public agent-commerce surfaces.
image: https://cdn.shopify.com/s/files/1/0350/7175/4378/files/Beef_Sub_Nav_f7d12905-6f5c-4d2a-a699-a144b387aabc.jpg?v=1665766002
json_schemas:
- name: GetWellKnownCustomerAccountApiResponse
  property_count: 1
  slug: 99-counties-get-well-known-customer-account-api-response
- name: PostCustomerApi202610GraphqlResponse
  property_count: 1
  slug: 99-counties-post-customer-api202610-graphql-response
- name: PostOrgidApi202610GraphqlJsonRequest
  property_count: 1
  slug: 99-counties-post-orgid-api202610-graphql-json-request
- name: PostOrgidApi202610GraphqlJsonResponse
  property_count: 4
  slug: 99-counties-post-orgid-api202610-graphql-json-response
- name: PostWebhooksOrdersRequest
  property_count: 1
  slug: 99-counties-post-webhooks-orders-request
- name: PostWebhooksOrdersResponse
  property_count: 2
  slug: 99-counties-post-webhooks-orders-response
jsonld:
- class_count: 11
  name: 99 Counties Context
  property_count: 10
  slug: 99-counties-context
layout: provider
mcp_servers:
- description: Remote MCP server at 99counties.com over HTTP; 5 tools listed.
  name: 99 Counties MCP Server
  slug: 99-counties-ucp
modified: '2026-10-06'
name: 99 Counties
nav: Providers
network: true
overview: '99 Counties is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Agentic Commerce, Regenerative Agriculture, and Food and Beverage.


  The 99 Counties catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  99 Counties'' developer surface includes getting-started guide, engineering blog, documentation, authentication, signup flow, support, API reference, and 23 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 1
  name: 99 Counties Rate Limits
  slug: 99-counties-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: 99 Counties API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: 99-counties-rules
scopes:
- name: 99 Counties Scopes
  scope_count: 4
  slug: 99-counties-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 25.0
    developer_ergonomics: 37.5
    discoverability: 66.7
    operational_transparency: 23.7
  previous_composite: 39.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: platform-generated
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/99-counties/99-counties-2026-08-07T160727.png
security:
- kind: authentication
  name: 99 Counties Authentication
  slug: 99-counties-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: 99 Counties Domain Security
  slug: 99-counties-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Shop 99 Counties via UCP
  slug: 99-counties-ucp-shopping
slug: 99-counties
tags:
- Company
- E-Commerce
- Agentic Commerce
- Regenerative Agriculture
- Food and Beverage
- Shopify
- MCP
- Universal Commerce Protocol
website: https://99counties.com
---
