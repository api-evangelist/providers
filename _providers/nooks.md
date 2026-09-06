---
access_model:
  confidence: medium
  label: Public API, sales-gated pricing
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://developer.nooks.in/
  - https://www.nooks.ai/pricing
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Nooks Agentic Access
  operation_count: 37
  slug: nooks-agentic-access
  summary_line: 37 operations · 13 acting
api_count: 1
apis:
- description: Nooks operates a hosted, remote Model Context Protocol server at https://mcp.nooks.in/. It is OAuth-protected — an anonymous `tools/list` returns HTTP 401 `invalid_token` — and publishes RFC 9728 prot
  name: Nooks MCP Server
  slug: nooks-mcp-server
- baseURL: https://partner-api.nooks.in/v1
  baseurl_source: declared
  description: Access account (company) records
  name: Nooks Accounts API
  slug: nooks-accounts-api
- baseURL: https://partner-api.nooks.in/v1
  baseurl_source: declared
  description: Access call disposition definitions
  name: Nooks Call Dispositions API
  slug: nooks-calldispositions-api
- baseURL: https://partner-api.nooks.in/v1
  baseurl_source: declared
  description: Access call records
  name: Nooks Calls API
  slug: nooks-calls-api
- baseURL: https://partner-api.nooks.in/v1
  baseurl_source: declared
  description: Access email records
  name: Nooks Emails API
  slug: nooks-emails-api
- baseURL: https://partner-api.nooks.in/v1
  baseurl_source: declared
  description: Access email template content
  name: Nooks Email Templates API
  slug: nooks-emailtemplates-api
- baseURL: https://partner-api.nooks.in/v1
  baseurl_source: declared
  description: Inspect the authenticated principal
  name: Nooks Introspection API
  slug: nooks-introspection-api
- baseURL: https://partner-api.nooks.in/v1
  baseurl_source: declared
  description: Manage mailboxes (email aliases)
  name: Nooks Mailboxes API
  slug: nooks-mailboxes-api
- baseURL: https://partner-api.nooks.in/v1
  baseurl_source: declared
  description: The Nooks Sequencing API API from Nooks — 0 operation(s) for nooks sequencing api.
  name: Nooks Nooks Sequencing API
  slug: nooks-nooks-sequencing-api-api
- baseURL: https://partner-api.nooks.in/v1
  baseurl_source: declared
  description: Create CRM notes on prospects and accounts
  name: Nooks Notes API
  slug: nooks-notes-api
- baseURL: https://partner-api.nooks.in/v1
  baseurl_source: declared
  description: Manage prospects
  name: Nooks Prospects API
  slug: nooks-prospects-api
- baseURL: https://partner-api.nooks.in/v1
  baseurl_source: declared
  description: Manage sales sequences
  name: Nooks Sequences API
  slug: nooks-sequences-api
- baseURL: https://partner-api.nooks.in/v1
  baseurl_source: declared
  description: Track prospect enrollments in sequences
  name: Nooks Sequence States API
  slug: nooks-sequencestates-api
- baseURL: https://partner-api.nooks.in/v1
  baseurl_source: declared
  description: Access sequence step definitions
  name: Nooks Sequence Steps API
  slug: nooks-sequencesteps-api
- baseURL: https://partner-api.nooks.in/v1
  baseurl_source: declared
  description: Manage tasks (one-off calls and email activities)
  name: Nooks Tasks API
  slug: nooks-tasks-api
- baseURL: https://partner-api.nooks.in/v1
  baseurl_source: declared
  description: Manage workspace users
  name: Nooks Users API
  slug: nooks-users-api
artifact_total: 26
asyncapis:
- description: ''
  name: Nooks Webhooks
  slug: nooks-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/nooks-sequencing-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.nooks.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.nooks.in/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nooks.in/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.nooks.in/
- group: operate
  title: ''
  type: Support
  url: https://nooks.help.usepylon.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://nooks.help.usepylon.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NooksApp
- group: start
  title: ''
  type: Login
  url: https://app.nooks.in
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nooks.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.nooks.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nooks.ai/terms-of-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nooks.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nooks.in/
- group: auth
  title: ''
  type: TrustCenter
  url: security/nooks-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.nooks.ai/
- group: auth
  title: ''
  type: Security
  url: https://www.nooks.ai/responsible-disclosure-process
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nooks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nooks-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nooks-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nooks-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/nooks-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nooks-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nooks-agentic-access.yml
created: '2026-07-17'
description: Nooks is an AI-native revenue/sales engagement platform positioned as "The Agent Workspace for Intelligent Outbound," where sales representatives and AI agents collaborate on prospecting, sequencing, dialing, and coaching inside a single workspace. Its products include an AI Parallel Dialer, AI Sequencing, AI Coaching, Signals Intelligence, and a Virtual Salesfloor, aimed at helping revenue and SDR teams build more pipeline with less manual work. Nooks publishes a public Nooks Sequencing API (the "Nooks External API") documented with a Scalar-rendered OpenAPI 3.1.0 contract at developer.nooks.in, served from partner-api.nooks.in/v1, covering sequences, sequence steps, sequence states, prospects, accounts, notes, tasks, calls, call dispositions, emails, email templates, mailboxes, and users. Authentication accepts either a workspace-scoped `nooks-api-` API key or an OAuth 2.0 authorization-code + PKCE access token from oauth.nooks.in, with 24 published scopes, RFC 8414 authorization-server
  metadata, and a JWKS endpoint. Nooks also operates an OAuth-protected remote MCP server at mcp.nooks.in, a signed `call.logged` webhook, an Atlassian Statuspage at status.nooks.in, and a SafeBase trust center with SOC 2 Type 2, SOC 3, ISO/IEC 27001:2022, GDPR, CCPA, and EU-US DPF coverage plus a Bugcrowd responsible-disclosure program. Nooks is backed by Kleiner Perkins and runs its application at app.nooks.in.
image: https://cdn.prod.website-files.com/697107c16c913fd77cf0aacd/69b2e1b1625a9e823d1edf5f_6995c9952aa828323555083c_OG%20Image%20(1).png
layout: provider
mcp_servers:
- description: ''
  name: Nooks MCP Server
  slug: nooks-mcp-server
modified: '2026-08-14'
name: Nooks
nav: Providers
network: true
overview: 'Nooks publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Call Dispositions API, Calls API, and 12 more. Tagged areas include Company, Artificial Intelligence, Sales Engagement, Sales Dialer, and AI SDR.


  The Nooks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nooks'' developer surface includes documentation, API reference, support, pricing, engineering blog, and 20 more developer resources.'
plans:
- name: Nooks Plans Pricing
  plan_count: 0
  slug: nooks-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 8
  name: Nooks Rate Limits
  slug: nooks-rate-limits
scopes:
- name: Nooks Scopes
  scope_count: 24
  slug: nooks-scopes
  summary_line: 24 scopes · authorizationCode
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 68.8
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 68.4
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nooks/refs/heads/main/screenshots/nooks-2026-08-07T185457.png
security:
- kind: authentication
  name: Nooks Authentication
  slug: nooks-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Nooks Domain Security
  slug: nooks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nooks Vulnerability Disclosure
  slug: nooks-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
- kind: trust-center
  name: Nooks Trust Center
  slug: nooks-trust-center
  summary_line: SOC 2 Type 2, SOC 3, ISO/IEC 27001:2022, GDPR, CCPA, EU-US DPF
slug: nooks
tags:
- Company
- Artificial Intelligence
- Sales Engagement
- Sales Dialer
- AI SDR
- Outbound Sales
- Sales Coaching
- Revenue Operations
- Sales Sequencing
- CRM Integration
- Agents
- MCP
website: https://www.nooks.ai
---
