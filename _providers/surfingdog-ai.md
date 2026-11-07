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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 65.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 105
  human_in_the_loop: 9
  name: Surfingdog Ai Agentic Access
  operation_count: 177
  slug: surfingdog-ai-agentic-access
  summary_line: 177 operations · 105 acting · 9 human-in-the-loop
api_count: 2
apis:
- baseURL: https://network.surfingdog.ai
  baseurl_source: declared
  description: 'Once a month, what AI agents can do at the websites checked: counts only, open data under CC BY 4.0 (credit "Surfing Dog census, surfingdog.ai, CC BY 4.0").'
  name: surfingdog-ai Census API
  slug: surfingdog-ai-census-api
- baseURL: https://network.surfingdog.ai
  baseurl_source: declared
  description: Finding businesses.
  name: surfingdog-ai Directory API
  slug: surfingdog-ai-directory-api
- baseURL: https://inbox.surfingdog.ai
  baseurl_source: declared
  description: The integrations API from surfingdog-ai — 18 operation(s) for integrations.
  name: surfingdog-ai Integrations API
  slug: surfingdog-ai-integrations-api
- baseURL: https://inbox.surfingdog.ai
  baseurl_source: declared
  description: The keys API from surfingdog-ai — 3 operation(s) for keys.
  name: surfingdog-ai Keys API
  slug: surfingdog-ai-keys-api
- baseURL: https://inbox.surfingdog.ai
  baseurl_source: declared
  description: The owner API from surfingdog-ai — 60 operation(s) for owner.
  name: surfingdog-ai Owner API
  slug: surfingdog-ai-owner-api
- baseURL: https://network.surfingdog.ai
  baseurl_source: declared
  description: 'For a business''s owner and its AI: whether agents find its inbox from its domain.'
  name: surfingdog-ai Owners API
  slug: surfingdog-ai-owners-api
- baseURL: https://network.surfingdog.ai
  baseurl_source: declared
  description: Finding the products businesses list from their own inboxes, and who offers each barcode.
  name: surfingdog-ai Products API
  slug: surfingdog-ai-products-api
- baseURL: https://inbox.surfingdog.ai
  baseurl_source: declared
  description: The public API from surfingdog-ai — 29 operation(s) for public.
  name: surfingdog-ai Public API
  slug: surfingdog-ai-public-api
- baseURL: https://network.surfingdog.ai
  baseurl_source: declared
  description: 'How a business''s doors went, as agents say: private to the business.'
  name: surfingdog-ai Reports API
  slug: surfingdog-ai-reports-api
- baseURL: https://network.surfingdog.ai
  baseurl_source: declared
  description: How the directory is ordered.
  name: surfingdog-ai Rules API
  slug: surfingdog-ai-rules-api
- baseURL: https://network.surfingdog.ai
  baseurl_source: declared
  description: 'The agentic score: how far an agent can go with a business, by published rules.'
  name: surfingdog-ai Score API
  slug: surfingdog-ai-score-api
- baseURL: https://inbox.surfingdog.ai
  baseurl_source: declared
  description: The setup API from surfingdog-ai — 18 operation(s) for setup.
  name: surfingdog-ai Setup API
  slug: surfingdog-ai-setup-api
- baseURL: https://inbox.surfingdog.ai
  baseurl_source: declared
  description: The stays API from surfingdog-ai — 7 operation(s) for stays.
  name: surfingdog-ai Stays API
  slug: surfingdog-ai-stays-api
artifact_total: 31
common:
- group: agent
  href: https://artifacts.apis.io/surfingdog-ai/agentic-access/surfingdog-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/surfingdog-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/surfingdog-ai/rate-limits/surfingdog-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/surfingdog-ai-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/surfingdog-ai/rules/surfingdog-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/surfingdog-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/surfingdog-ai/json-ld/surfingdog-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/surfingdog-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/surfingdog-ai/vocabulary/surfingdog-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/surfingdog-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/surfingdog-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/surfingdog-ai/data-model/surfingdog-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/surfingdog-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/surfingdog-ai/conventions/surfingdog-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/surfingdog-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/surfingdog-ai/conventions/surfingdog-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/surfingdog-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/surfingdog-ai/security/surfingdog-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/surfingdog-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/surfingdog-ai/authentication/surfingdog-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/surfingdog-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/surfingdog-ai/scopes/surfingdog-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/surfingdog-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/surfingdog-ai/errors/surfingdog-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/surfingdog-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/surfingdog-ai/conformance/surfingdog-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/surfingdog-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/surfingdog-ai/llms/surfingdog-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/surfingdog-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/surfingdog-ai/a2a/surfingdog-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/surfingdog-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/surfingdog-ai/mcp/surfingdog-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/surfingdog-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/surfingdog-ai/mcp/surfingdog-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/surfingdog-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/surfingdog-ai/well-known/surfingdog-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/surfingdog-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/surfingdog-ai/well-known/surfingdog-ai-inbox-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/surfingdog-ai-inbox-security.txt
- group: agent
  href: https://artifacts.apis.io/surfingdog-ai/well-known/surfingdog-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/surfingdog-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/surfingdog-ai/hosts/surfingdog-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/surfingdog-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/surfingdog-ai/vendors/surfingdog-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/surfingdog-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/surfingdog-ai/packages/surfingdog-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/surfingdog-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/surfingdog-ai/packages/surfingdog-ai-packages.yml
  title: ''
  type: Packages
  url: packages/surfingdog-ai-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://surfingdog.ai/trust/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://surfingdog.ai/terms/
- group: operate
  title: ''
  type: Support
  url: https://surfingdog.ai/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://surfingdog.ai/privacy/
- group: start
  title: ''
  type: Login
  url: https://app.surfingdog.ai/signin
- group: auth
  href: https://artifacts.apis.io/surfingdog-ai/security/surfingdog-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/surfingdog-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/surfingdog-ai/security/surfingdog-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/surfingdog-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://surfingdog.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://surfingdog.ai/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://surfingdog.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://surfingdog.ai/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://surfingdog.ai/docs/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://surfingdog.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/surfingdogai
created: '2026-10-30'
description: Surfing Dog AI provides an open-source, self‑hostable inbox that enables AI agents to interact with businesses through REST, MCP, and email. It tracks and lists agent‑ready businesses, offering searchable directories, trust networks, and integration capabilities for calendars, payments, and property systems. The platform powers a network where agents can discover, book, and communicate with businesses, while owners can manage items, rules, and AI‑driven workflows. Documentation, API reference, and quick‑start guides are publicly available, and the service runs on Cloudflare Workers and Node, exposing a public OpenAPI spec at https://inbox.surfingdog.ai/openapi.json.
image: https://surfingdog.ai/favicon.svg
json_schemas:
- name: DoorHistory
  property_count: 2
  slug: surfingdog-ai-door-history
- name: Listing
  property_count: 46
  slug: surfingdog-ai-listing
- name: OfferPage
  property_count: 6
  slug: surfingdog-ai-offer-page
- name: PayWith
  property_count: 5
  slug: surfingdog-ai-pay-with
- name: ProductPage
  property_count: 5
  slug: surfingdog-ai-product-page
- name: ReadAllowance
  property_count: 4
  slug: surfingdog-ai-read-allowance
- name: __schema0
  property_count: 0
  slug: surfingdog-ai-schema0
jsonld:
- class_count: 18
  name: Surfingdog Ai Context
  property_count: 118
  slug: surfingdog-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at surfingdog.ai.
  name: surfingdog-ai MCP Server
  slug: surfingdog-ai-mcp-yml
modified: '2026-10-30'
name: surfingdog-ai
nav: Providers
network: true
overview: 'surfingdog-ai publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Census API, Directory API, Integrations API, and 10 more. Tagged areas include Company, Artificial Intelligence, Agent Ready, Directory, and Inbox.


  The surfingdog-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  surfingdog-ai''s developer surface includes authentication, support, documentation, API reference, getting-started guide, engineering blog, and 33 more developer resources.'
plans:
- name: Surfingdog Ai Plans Pricing
  plan_count: 0
  slug: surfingdog-ai-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Surfingdog Ai Rate Limits
  slug: surfingdog-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: surfingdog-ai API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 3
  slug: surfingdog-ai-rules
scopes:
- name: Surfingdog Ai Scopes
  scope_count: 0
  slug: surfingdog-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 34
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 57.8
    developer_ergonomics: 48.1
    discoverability: 75.0
    operational_transparency: 34.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 53.8
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: unknown
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
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/surfingdog-ai/surfingdog-ai-2026-11-03T144111.png
security:
- kind: authentication
  name: Surfingdog Ai Authentication
  slug: surfingdog-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Surfingdog Ai Domain Security
  slug: surfingdog-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Surfingdog Ai Vulnerability Disclosure
  slug: surfingdog-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: search-businesses
  slug: surfingdog-ai-search_businesses
slug: surfingdog-ai
tags:
- Company
- Artificial Intelligence
- Agent Ready
- Directory
- Inbox
website: https://surfingdog.ai/
---
