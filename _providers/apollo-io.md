---
access_model:
  confidence: high
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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 46
  human_in_the_loop: 1
  name: Apollo Io Agentic Access
  operation_count: 80
  slug: apollo-io-agentic-access
  summary_line: 80 operations · 46 acting · 1 human-in-the-loop
api_count: 5
apis:
- baseURL: https://api.apollo.io/api/v1
  baseurl_source: declared
  description: People and company enrichment, single and bulk. 4 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Enrichment API
  slug: apollo-io-enrichment-api
- baseURL: https://api.apollo.io/api/v1
  baseurl_source: declared
  description: Database search across Apollo's people, company, job-posting and news data. 6 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Search API
  slug: apollo-io-search-api
- baseURL: https://api.apollo.io/api/v1
  baseurl_source: declared
  description: Workspace CRM accounts — create, update, search, stages and ownership. 8 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Accounts API
  slug: apollo-io-accounts-api
- baseURL: https://api.apollo.io/api/v1
  baseurl_source: declared
  description: Workspace CRM contacts — create, update, search, stages and ownership. 10 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Contacts API
  slug: apollo-io-contacts-api
- baseURL: https://api.apollo.io/api/v1
  baseurl_source: declared
  description: Deals (opportunities), their stages, and the deals attached to a contact. 5 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Deals API
  slug: apollo-io-deals-api
- baseURL: https://api.apollo.io/api/v1
  baseurl_source: declared
  description: Outreach sequences — create, update, approve, abort, archive, enrollment and activity. 12 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Sequences API
  slug: apollo-io-sequences-api
- baseURL: https://api.apollo.io/api/v1
  baseurl_source: declared
  description: One-off email drafting, sending, send status and content retrieval. 4 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Emailer Messages API
  slug: apollo-io-emailer-messages-api
- baseURL: https://api.apollo.io/api/v1
  baseurl_source: declared
  description: Tasks against contacts, accounts and deals — create, search, update, complete, skip. 7 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Tasks API
  slug: apollo-io-tasks-api
- baseURL: https://api.apollo.io/api/v1
  baseurl_source: declared
  description: Phone-call records — log, search and update dialer activity. 3 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Calls API
  slug: apollo-io-calls-api
- baseURL: https://api.apollo.io/api/v1
  baseurl_source: declared
  description: Conversation intelligence — search recorded calls and meetings, read insights, export. 4 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Conversations API
  slug: apollo-io-conversations-api
- baseURL: https://api.apollo.io/api/v1
  baseurl_source: declared
  description: The Query Analytics Report endpoint — metrics, dimensions and filters over engagement data. 1 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Analytics API
  slug: apollo-io-analytics-api
- baseURL: https://api.apollo.io/api/v1
  baseurl_source: declared
  description: Field and custom-field definitions across contacts, accounts and opportunities. 4 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Fields API
  slug: apollo-io-fields-api
- baseURL: https://api.apollo.io/api/v1
  baseurl_source: declared
  description: Users, email accounts, lists and labels, notes, usage stats and webhook results. 12 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Miscellaneous API
  slug: apollo-io-miscellaneous-api
- description: Apollo's hosted Model Context Protocol server. A remote Streamable-HTTP endpoint at https://mcp.apollo.io/mcp, authenticated with OAuth 2.0 and no API key, exposing 51 published actions across search,
  name: Apollo MCP Server
  slug: apollo-mcp
- baseURL: https://api.apollo.io/api/v1
  baseurl_source: declared
  description: The Users API from Apollo.io — 1 operation(s) for users.
  name: Apollo.io Users API
  slug: apollo-io-users-api
artifact_total: 57
asyncapis:
- description: ''
  name: Apollo Io Webhooks
  slug: apollo-io-webhooks
collections:
- collection_type: open
  name: Apollo.io API
  slug: open-apollo-enrich
- collection_type: open
  name: Apollo.io Accounts API
  slug: open-apollo-io-accounts-api
- collection_type: open
  name: Apollo.io Analytics API
  slug: open-apollo-io-analytics-api
- collection_type: open
  name: Apollo.io Calls API
  slug: open-apollo-io-calls-api
- collection_type: open
  name: Apollo.io Contacts API
  slug: open-apollo-io-contacts-api
- collection_type: open
  name: Apollo.io Conversations API
  slug: open-apollo-io-conversations-api
- collection_type: open
  name: Apollo.io Deals API
  slug: open-apollo-io-deals-api
- collection_type: open
  name: Apollo.io Emailer Messages API
  slug: open-apollo-io-emailer-messages-api
- collection_type: open
  name: Apollo.io Enrichment API
  slug: open-apollo-io-enrichment-api
- collection_type: open
  name: Apollo.io Fields API
  slug: open-apollo-io-fields-api
- collection_type: open
  name: Apollo.io Miscellaneous API
  slug: open-apollo-io-miscellaneous-api
- collection_type: open
  name: Apollo.io Search API
  slug: open-apollo-io-search-api
- collection_type: open
  name: Apollo.io Sequences API
  slug: open-apollo-io-sequences-api
- collection_type: open
  name: Apollo.io Tasks API
  slug: open-apollo-io-tasks-api
common:
- group: other
  href: https://artifacts.apis.io/apollo-io/capabilities/apollo-io-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/apollo-io-capability-edges.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/apolloio/apollo-mcp-plugin/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.apollo.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apolloio
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.apollo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apollo.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apollo.io/reference/apollo-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apollo.io/docs/build-with-apollo
- group: operate
  title: ''
  type: Support
  url: https://knowledge.apollo.io/
- group: company
  title: ''
  type: Blog
  url: https://www.apollo.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apolloio
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apollo.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.apollo.io/lp/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.apollo.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apollo.io/terms/api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apollo.io/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://trust.apollo.io/
- group: auth
  href: https://artifacts.apis.io/apollo-io/security/apollo-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/apollo-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/apollo-io/security/apollo-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apollo-io-domain-security.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apollo.io/
- group: design
  href: https://artifacts.apis.io/apollo-io/lifecycle/apollo-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apollo-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/apollo-io/asyncapi/apollo-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/apollo-io-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/apollo-io/authentication/apollo-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apollo-io-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://docs.apollo.io/reference/authentication
- group: auth
  href: https://artifacts.apis.io/apollo-io/scopes/apollo-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/apollo-io-scopes.yml
- group: design
  href: https://artifacts.apis.io/apollo-io/conventions/apollo-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apollo-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/apollo-io/errors/apollo-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apollo-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apollo-io/data-model/apollo-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apollo-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/apollo-io/conformance/apollo-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apollo-io-conformance.yml
- group: operate
  href: https://artifacts.apis.io/apollo-io/rate-limits/apollo-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apollo-io-rate-limits.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.apollo.io/reference/rate-limits
- group: commercial
  href: https://artifacts.apis.io/apollo-io/plans/apollo-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apollo-io-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/apollo-io/finops/apollo-io-finops.yml
  title: ''
  type: FinOps
  url: finops/apollo-io-finops.yml
- group: start
  href: https://artifacts.apis.io/apollo-io/sandbox/apollo-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/apollo-io-sandbox.yml
- group: build
  href: https://artifacts.apis.io/apollo-io/cli/apollo-io-cli.yml
  title: ''
  type: CLI
  url: cli/apollo-io-cli.yml
- group: build
  href: https://artifacts.apis.io/apollo-io/packages/apollo-io-packages.yml
  title: ''
  type: Packages
  url: packages/apollo-io-packages.yml
- group: agent
  href: https://artifacts.apis.io/apollo-io/mcp/apollo-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apollo-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/apollo-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/apollo-io/agentic-access/apollo-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apollo-io-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/apollo-io/well-known/apollo-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apollo-io-well-known.yml
- group: agent
  href: https://artifacts.apis.io/apollo-io/llms/apollo-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apollo-io-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.apollo.io/llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: https://docs.apollo.io/openapi/apollo-rest-api.json
- group: company
  title: ''
  type: Blog
  url: https://www.apollo.io/magazine
created: '2026-05-08'
description: Apollo.io is a sales intelligence and go-to-market platform combining a database of 240M+ contacts and 30M+ companies with enrichment, sequencing, dialing and conversation intelligence. Its REST API publishes 80 operations at https://api.apollo.io/api/v1 across people and company search, single and bulk enrichment, CRM accounts, contacts and deals, outreach sequences, one-off emails, tasks, calls, conversations, custom fields, lists, analytics and usage stats — described by a first-party OpenAPI 3.1.0 document. Apollo also ships a hosted MCP server, a first-party CLI, and provider-published agent skills for both.
features:
- REST API at https://api.apollo.io/api/v1 — 80 operations, OpenAPI 3.1.0 published at https://docs.apollo.io/openapi/apollo-rest-api.json
- API key authentication via the x-api-key header; keys are scoped to an explicit endpoint list or marked master
- OAuth 2.0 authorization-code flow for partners, with 70 named scopes
- Hosted remote MCP server at https://mcp.apollo.io/mcp over Streamable HTTP with OAuth 2.0 — no API key, no local install
- First-party Apollo CLI (Homebrew tap and signed prebuilt binaries) with OAuth login
- Five provider-published agent skills — four in the MCP plug-in, one for the CLI
- 240M+ contacts and 30M+ companies searchable; enrichment is metered in credits
- Rate limits are per team and per endpoint, enforced in per-minute, per-hour and per-day windows, surfaced in x-rate-limit-* response headers
- Bulk enrichment endpoints take up to 10 records per call
- Asynchronous enrichment callbacks via webhook_url, with a 30-day poll-by-request_id fallback
- No sandbox host and no test mode — testing happens against production with a real key
- No client SDKs; Apollo documents generating one from the OpenAPI instead
finops:
- has_sources: true
  method: derived
  name: Apollo Io Finops
  primary_unit: ''
  service_category: ''
  slug: apollo-io-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apollo-io.png
layout: provider
mcp_servers:
- description: Prospect, enrich leads, and manage outreach sequences with Apollo.io. Connects Apollo's contact database, real-time enrichment engine, and sales engagement surface to an MCP client.
  name: Apollo.io MCP Server
  slug: apollo
modified: '2026-08-13'
name: Apollo.io
nav: Providers
network: true
overview: 'Apollo.io publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Enrichment API, Search API, Accounts API, and 12 more. Tagged areas include Sales Intelligence, Prospecting, Engagement, B2B Data, and Data Enrichment.


  The Apollo.io catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Apollo.io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Apollo Io Plans Pricing
  plan_count: 4
  slug: apollo-io-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 12
  name: Apollo Io Rate Limits
  slug: apollo-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Apollo.io API Rules
  rule_count: 61
  severity_counts:
    error: 49
    hint: 0
    info: 3
    warn: 9
  slug: apollo-io-rules
scopes:
- name: Apollo Io Scopes
  scope_count: 91
  slug: apollo-io-scopes
  summary_line: 91 scopes · authorizationCode
score:
  band: exemplar
  composite: 70.1
  coverage:
    artifact_dirs: 33
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.9
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 70.5
    developer_ergonomics: 69.0
    discoverability: 80.0
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 65.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 14
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/apollo-io/apollo-io-2026-06-20T172312.png
security:
- kind: authentication
  name: Apollo Io Authentication
  slug: apollo-io-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Apollo Io Domain Security
  slug: apollo-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Apollo Io Trust Center
  slug: apollo-io-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 5
skills:
- name: analytics
  slug: apollo-io-analytics
- name: apollo-cli
  slug: apollo-io-apollo-cli
- name: enrich-lead
  slug: apollo-io-enrich-lead
- name: prospect
  slug: apollo-io-prospect
- name: sequence-load
  slug: apollo-io-sequence-load
slug: apollo-io
tags:
- Sales Intelligence
- Prospecting
- Engagement
- B2B Data
- Data Enrichment
- CRM
- Sales Engagement
- Conversation Intelligence
- MCP
- Software-as-a-Service
- People Search
- Company Search
- Agents
- Go-To-Market
- Artificial Intelligence
- B2B Sales
- Lead Generation
- Sales Platform
website: https://www.apollo.io/
---
