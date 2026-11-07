---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
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
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 44
  human_in_the_loop: 3
  name: Prospectapis Agentic Access
  operation_count: 107
  slug: prospectapis-agentic-access
  summary_line: 107 operations · 44 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: The Pricing API from ProspectAPIs — 1 operation(s) for pricing.
  name: ProspectAPIs Pricing API
  slug: prospectapis-pricing-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: The Watchlists API from ProspectAPIs — 3 operation(s) for watchlists.
  name: ProspectAPIs Watchlists API
  slug: prospectapis-watchlists-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: Your balance, feedback and the API version.
  name: ProspectAPIs Account API
  slug: prospectapis-account-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: 'Reads about your own connected account and the people you act on: skills, profile views, social selling index and post insights.'
  name: ProspectAPIs Account insights API
  slug: prospectapis-account-insights-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: A company's live ads on the public Meta, Google, LinkedIn and TikTok ad libraries, keyed on its domain.
  name: ProspectAPIs Ads API
  slug: prospectapis-ads-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: Cited company profiles, one record per domain, built from public sources with a source on every field.
  name: ProspectAPIs Companies API
  slug: prospectapis-companies-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: 'Connect your own account once, then the people writes and the page-followers read act on it. Free: connecting, checking and disconnecting cost nothing.'
  name: ProspectAPIs Connected account API
  slug: prospectapis-connected-account-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: Check email addresses for deliverability before you send.
  name: ProspectAPIs Email verification API
  slug: prospectapis-email-verification-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: 'Event discovery: public Luma and Partiful events by city, in one record shape, read without an account.'
  name: ProspectAPIs Events API
  slug: prospectapis-events-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: Search and read funding rounds.
  name: ProspectAPIs Funding API
  slug: prospectapis-funding-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: The Health API from ProspectAPIs — 1 operation(s) for health.
  name: ProspectAPIs Health API
  slug: prospectapis-health-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: 'Launch events as prospecting triggers: a company said it launched (stage post) or is about to (stage pre). Not available yet: 503 until GET /pricing reports launches available.'
  name: ProspectAPIs Launches API
  slug: prospectapis-launches-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: Read your connected account's conversations and threads. One published price per read.
  name: ProspectAPIs Messaging reads API
  slug: prospectapis-messaging-reads-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: 'Keyless endpoints: the price list and liveness.'
  name: ProspectAPIs Meta API
  slug: prospectapis-meta-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: 'Live reads of people and pages: each call fetches fresh at request time. $0.012 per live read.'
  name: ProspectAPIs People reads API
  slug: prospectapis-people-reads-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: 'Act on your own connected account: message, invite, follow, visit, post, react, comment, repost, quote. One published price per route.'
  name: ProspectAPIs People writes API
  slug: prospectapis-people-writes-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: The ProspectAPIs API API from ProspectAPIs — 2 operation(s) for prospectapis api.
  name: ProspectAPIs ProspectAPIs API
  slug: prospectapis-prospectapis-api-api
- baseURL: https://api.prospectapis.com
  baseurl_source: declared
  description: Start and poll cited prospect research briefs.
  name: ProspectAPIs Research API
  slug: prospectapis-research-api
artifact_total: 36
asyncapis:
- description: ''
  name: Prospectapis Webhooks
  slug: prospectapis-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/prospectapis/agentic-access/prospectapis-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/prospectapis-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/prospectapis/finops/prospectapis-finops.yml
  title: ''
  type: FinOps
  url: finops/prospectapis-finops.yml
- group: operate
  href: https://artifacts.apis.io/prospectapis/rate-limits/prospectapis-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/prospectapis-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/prospectapis/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/prospectapis/asyncapi/prospectapis-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/prospectapis-webhooks.yml
- group: design
  href: https://artifacts.apis.io/prospectapis/conventions/prospectapis-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/prospectapis-conventions.yml
- group: design
  href: https://artifacts.apis.io/prospectapis/errors/prospectapis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/prospectapis-problem-types.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://prospectapis.com/faq#getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://prospectapis.com/docs/reference
- group: commercial
  href: https://artifacts.apis.io/prospectapis/plans/prospectapis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/prospectapis-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/prospectapis/rules/prospectapis-rules.yml
  title: ''
  type: Spectral
  url: rules/prospectapis-rules.yml
- group: design
  href: https://artifacts.apis.io/prospectapis/json-ld/prospectapis-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/prospectapis-context.jsonld
- group: design
  href: https://artifacts.apis.io/prospectapis/vocabulary/prospectapis-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/prospectapis-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/prospectapis/data-model/prospectapis-data-model.yml
  title: ''
  type: DataModel
  url: data-model/prospectapis-data-model.yml
- group: operate
  href: https://artifacts.apis.io/prospectapis/changelog/prospectapis-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/prospectapis-changelog.yml
- group: design
  href: https://artifacts.apis.io/prospectapis/conventions/prospectapis-conventions.yml
  title: ''
  type: Conventions
  url: conventions/prospectapis-conventions.yml
- group: auth
  href: https://artifacts.apis.io/prospectapis/security/prospectapis-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/prospectapis-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/prospectapis/authentication/prospectapis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/prospectapis-authentication.yml
- group: design
  href: https://artifacts.apis.io/prospectapis/lifecycle/prospectapis-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/prospectapis-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/prospectapis/conformance/prospectapis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/prospectapis-conformance.yml
- group: agent
  href: https://artifacts.apis.io/prospectapis/llms/prospectapis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/prospectapis-llms.txt
- group: other
  href: https://artifacts.apis.io/prospectapis/a2a/prospectapis-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/prospectapis-a2a.yml
- group: auth
  href: https://artifacts.apis.io/prospectapis/well-known/prospectapis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prospectapis-security.txt
- group: agent
  href: https://artifacts.apis.io/prospectapis/well-known/prospectapis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/prospectapis-well-known.yml
- group: other
  href: https://artifacts.apis.io/prospectapis/hosts/prospectapis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prospectapis-hosts.yml
- group: other
  href: https://artifacts.apis.io/prospectapis/vendors/prospectapis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prospectapis-vendors.yml
- group: build
  href: https://artifacts.apis.io/prospectapis/packages/prospectapis-packages.yml
  title: ''
  type: SDKs
  url: packages/prospectapis-packages.yml
- group: build
  href: https://artifacts.apis.io/prospectapis/packages/prospectapis-packages.yml
  title: ''
  type: Packages
  url: packages/prospectapis-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://prospectapis.com/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: https://prospectapis.com/llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: https://prospectapis.com/mcp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ProspectAPIs
- group: auth
  href: https://artifacts.apis.io/prospectapis/security/prospectapis-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/prospectapis-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/prospectapis/security/prospectapis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prospectapis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prospectapis.com
- group: docs
  title: ''
  type: Documentation
  url: https://prospectapis.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://prospectapis.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://prospectapis.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://prospectapis.com/signup
- group: start
  title: ''
  type: Login
  url: https://prospectapis.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://prospectapis.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prospectapis.com/privacy
coverage:
  checked: '2026-10-14'
  detail: The API documentation is a JavaScript‑rendered site with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 404
    url: https://api.prospectapis.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: ProspectAPIs provides a funding signals and prospect research API that lets developers search for funding rounds at $0.02 per record after a free tier of 100 records per month. Users can receive new round notifications via webhooks and obtain cited research briefs on companies for $0.15 each. The service targets investors, analysts, and businesses seeking up‑to‑date financing information, offering both a searchable database and automated alerts. It aims to streamline due‑diligence and market intelligence workflows through a simple RESTful interface. ProspectAPIs also offers comprehensive documentation, SDKs in multiple languages, and a developer portal for easy integration.
finops:
- has_sources: true
  method: derived
  name: Prospectapis Finops
  primary_unit: seat
  service_category: ''
  slug: prospectapis-finops
  template: false
image: https://prospectapis.com/opengraph-image-12o0cb?041bc0296eca8283
json_schemas:
- name: GetHealthResponse
  property_count: 1
  slug: prospectapis-get-health-response
- name: GetV1V1IdResponse
  property_count: 6
  slug: prospectapis-get-v1-v1-id-response
- name: PostV1V1IdRequest
  property_count: 3
  slug: prospectapis-post-v1-v1-id-request
- name: PostV1V1IdResponse
  property_count: 6
  slug: prospectapis-post-v1-v1-id-response
jsonld:
- class_count: 4
  name: Prospectapis Context
  property_count: 10
  slug: prospectapis-context
layout: provider
mcp_servers:
- description: Local (stdio) MCP server published on npm as prospectapis-mcp (MIT), 14 tools, one per REST endpoint, using the same API key and prepaid balance as the REST API. npx prospectapis-mcp. Source https://g
  name: ProspectAPIs MCP Server
  slug: prospectapis-mcp-server
modified: '2026-10-14'
name: ProspectAPIs
nav: Providers
network: true
overview: 'ProspectAPIs publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Pricing API, Watchlists API, Account API, and 15 more. Tagged areas include Company, Funding, Research, Data, and Funding Data.


  The ProspectAPIs catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  ProspectAPIs'' developer surface includes getting-started guide, API reference, changelog, authentication, documentation, pricing, engineering blog, and 35 more developer resources.'
plans:
- name: Prospectapis Plans Pricing
  plan_count: 4
  slug: prospectapis-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Prospectapis Rate Limits
  slug: prospectapis-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: ProspectAPIs API Rules
  rule_count: 68
  severity_counts:
    error: 49
    hint: 0
    info: 3
    warn: 16
  slug: prospectapis-rules
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 33
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.2
  facets:
    access_clarity: 61.8
    contract_governance: 22.0
    contract_quality: 58.9
    developer_ergonomics: 36.3
    discoverability: 73.2
    operational_transparency: 60.5
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 26.3
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/prospectapis/prospectapis-2026-11-03T141638.png
security:
- kind: authentication
  name: Prospectapis Authentication
  slug: prospectapis-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Prospectapis Domain Security
  slug: prospectapis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Prospectapis Vulnerability Disclosure
  slug: prospectapis-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: prospectapis-connect-account-login
  slug: prospectapis-connect-account-login
- name: prospectapis-event-search-and-enrich
  slug: prospectapis-event-search-and-enrich
- name: prospectapis-get-person-profile
  slug: prospectapis-get-person-profile
slug: prospectapis
tags:
- Company
- Funding
- Research
- Data
- Funding Data
- Prospect Research
- Email Verification
- LinkedIn data
- Watchlist
- MCP
website: https://prospectapis.com
---
