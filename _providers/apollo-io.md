---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 61.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 54
  human_in_the_loop: 1
  name: Apollo Io Agentic Access
  operation_count: 80
  slug: apollo-io-agentic-access
  summary_line: 80 operations · 54 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: People and company enrichment, single and bulk. 4 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Enrichment API
  slug: apollo-io-enrichment-api
- description: Database search across Apollo's people, company, job-posting and news data. 6 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Search API
  slug: apollo-io-search-api
- description: Workspace CRM accounts — create, update, search, stages and ownership. 8 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Accounts API
  slug: apollo-io-accounts-api
- description: Workspace CRM contacts — create, update, search, stages and ownership. 10 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Contacts API
  slug: apollo-io-contacts-api
- description: Deals (opportunities), their stages, and the deals attached to a contact. 5 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Deals API
  slug: apollo-io-deals-api
- description: Outreach sequences — create, update, approve, abort, archive, enrollment and activity. 12 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Sequences API
  slug: apollo-io-sequences-api
- description: One-off email drafting, sending, send status and content retrieval. 4 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Emailer Messages API
  slug: apollo-io-emailer-messages-api
- description: Tasks against contacts, accounts and deals — create, search, update, complete, skip. 7 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Tasks API
  slug: apollo-io-tasks-api
- description: Phone-call records — log, search and update dialer activity. 3 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Calls API
  slug: apollo-io-calls-api
- description: Conversation intelligence — search recorded calls and meetings, read insights, export. 4 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Conversations API
  slug: apollo-io-conversations-api
- description: The Query Analytics Report endpoint — metrics, dimensions and filters over engagement data. 1 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Analytics API
  slug: apollo-io-analytics-api
- description: Field and custom-field definitions across contacts, accounts and opportunities. 4 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Fields API
  slug: apollo-io-fields-api
- description: Users, email accounts, lists and labels, notes, usage stats and webhook results. 12 operation(s) from the published Apollo OpenAPI.
  name: Apollo.io Miscellaneous API
  slug: apollo-io-miscellaneous-api
- description: Apollo's hosted Model Context Protocol server. A remote Streamable-HTTP endpoint at https://mcp.apollo.io/mcp, authenticated with OAuth 2.0 and no API key, exposing 51 published actions across search,
  name: Apollo MCP Server
  slug: apollo-mcp
artifact_total: 49
asyncapis:
- description: ''
  name: Apollo Io Webhooks
  slug: apollo-io-webhooks
collections:
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
  title: ''
  type: TrustCenter
  url: security/apollo-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apollo-io-domain-security.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apollo.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apollo-io-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/apollo-io-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apollo-io-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://docs.apollo.io/reference/authentication
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/apollo-io-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apollo-io-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apollo-io-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apollo-io-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apollo-io-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apollo-io-rate-limits.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.apollo.io/reference/rate-limits
- group: commercial
  title: ''
  type: Plans
  url: plans/apollo-io-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/apollo-io-finops.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/apollo-io-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/apollo-io-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/apollo-io-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apollo-io-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apollo-io-agentic-access.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/apollo-io-well-known.yml
- group: agent
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
- name: Apollo Io Finops
  service_category: Sales Intelligence
  slug: apollo-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apollo-io.png
layout: provider
mcp_servers:
- description: ''
  name: apollo-io-mcp.yml
  slug: apollo-io-mcpyml
modified: '2026-08-13'
name: Apollo.io
nav: Providers
network: true
overview: 'Apollo.io publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Enrichment API, Search API, Accounts API, and 10 more. Tagged areas include Sales Intelligence, Prospecting, Engagement, B2B Data, and Enrichment.


  The Apollo.io catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Apollo.io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Apollo Io Plans Pricing
  plan_count: 4
  slug: apollo-io-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 12
  name: Apollo Io Rate Limits
  slug: apollo-io-rate-limits
scopes:
- name: Apollo Io Scopes
  scope_count: 91
  slug: apollo-io-scopes
  summary_line: 91 scopes · authorizationCode
score:
  band: exemplar
  composite: 66.5
  delta: 20.7
  facets:
    commercial_clarity: 76.3
    contract_quality: 74.6
    developer_ergonomics: 80.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/apollo-io/refs/heads/main/screenshots/apollo-io-2026-06-20T172312.png
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
slug: apollo-io
tags:
- Sales Intelligence
- Prospecting
- Engagement
- B2B Data
- Enrichment
- CRM
- Sales Engagement
- Conversation Intelligence
- MCP
- SaaS
website: https://www.apollo.io/
---
