---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Mixmax Agentic Access
  operation_count: 24
  slug: mixmax-agentic-access
  summary_line: 24 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.mixmax.com/v1
  baseurl_source: declared
  description: Contact groups you own or that are shared with you — deprecated
  name: Mixmax Contact Groups API
  slug: mixmax-contact-groups-api
- baseURL: https://api.mixmax.com/v1
  baseurl_source: declared
  description: Mixmax Contacts (people you've emailed) — deprecated resource group
  name: Mixmax Contacts API
  slug: mixmax-contacts-api
- baseURL: https://api.mixmax.com/v1
  baseurl_source: declared
  description: File requests you've sent out
  name: Mixmax File Requests API
  slug: mixmax-file-requests-api
- baseURL: https://api.mixmax.com/v1
  baseurl_source: declared
  description: Meeting Copilot summaries and transcripts (requires mixmaxApi feature)
  name: Mixmax Meetings API
  slug: mixmax-meetings-api
- baseURL: https://api.mixmax.com/v1
  baseurl_source: declared
  description: Sequences you have access to, and their recipients
  name: Mixmax Sequences API
  slug: mixmax-sequences-api
- baseURL: https://api.mixmax.com/v1
  baseurl_source: declared
  description: Snippet tag management
  name: Mixmax Snippet Tags API
  slug: mixmax-snippet-tags-api
artifact_total: 22
asyncapis:
- description: ''
  name: Mixmax Webhooks
  slug: mixmax-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mixmax REST Contact Groups API
  slug: open-mixmax-contact-groups-api
- collection_type: open
  name: Mixmax REST Contact Groups Contacts API
  slug: open-mixmax-contacts-api
- collection_type: open
  name: Mixmax REST Contact Groups File Requests API
  slug: open-mixmax-file-requests-api
- collection_type: open
  name: Mixmax REST Contact Groups Meetings API
  slug: open-mixmax-meetings-api
- collection_type: open
  name: Mixmax REST Contact Groups Sequences API
  slug: open-mixmax-sequences-api
- collection_type: open
  name: Mixmax REST Contact Groups Snippet Tags API
  slug: open-mixmax-snippet-tags-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mixmax-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mixmax-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mixmax-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mixmax-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.mixmax.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mixmax-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/mixmax-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mixmax-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mixmax.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mixmax.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mixmax.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.mixmax.com/reference/getting-started-with-the-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.mixmax.com/reference/getting-started-with-the-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mixmaxhq
- group: operate
  title: ''
  type: Support
  url: https://success.mixmax.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mixmax.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mixmax.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.mixmax.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.mixmax.com/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mixmax.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mixmax.com/legal/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.mixmax.com/
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/mixmax-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mixmax-scopes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mixmax-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mixmax-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mixmax-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mixmax-problem-types.yml
created: '2026-07-17'
description: Mixmax is an AI-native sales engagement and execution platform that lives inside Gmail and Outlook, helping sales, customer success, recruiting, and other relationship-driven teams run their entire customer journey without context-switching. It combines email tracking and templates, multi-channel sequences, one-click scheduling, CRM automation, engagement signals, and Meeting Copilot summaries and transcripts. Mixmax exposes a public REST API (api.mixmax.com/v1) for lightweight real-time access to contacts, contact groups, sequences and recipients, file requests, meeting summaries and transcripts, and snippet tags, authenticated with an API token, plus message integrations and Sidebar/Widget SDKs for extending the product surface. Since April 2026 Mixmax also runs a first-party remote MCP server at mcp.mixmax.com/mcp — read-only, OAuth 2.0 with PKCE against its own OpenID Connect provider, scoped meetings:read — together with six installable Claude Skills, a rule-driven incoming
  and outgoing webhook surface with a documented event catalog, and published per-tier pricing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mixmax.png
layout: provider
mcp_servers:
- description: ''
  name: Mixmax MCP Server
  slug: mixmax-mcp-server
modified: '2026-08-13'
name: Mixmax
nav: Providers
network: true
overview: 'Mixmax publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Contact Groups API, Contacts API, File Requests API, and 3 more. Tagged areas include Company, Software-as-a-Service, MCP, Agents, and Webhook.


  The Mixmax catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mixmax''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Mixmax Plans Pricing
  plan_count: 6
  slug: mixmax-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Mixmax Rate Limits
  slug: mixmax-rate-limits
scopes:
- name: Mixmax Scopes
  scope_count: 0
  slug: mixmax-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 23
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 25.0
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mixmax/refs/heads/main/screenshots/mixmax-2026-08-07T183824.png
security:
- kind: authentication
  name: Mixmax Authentication
  slug: mixmax-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Mixmax Domain Security
  slug: mixmax-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Mixmax Trust Center
  slug: mixmax-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: mixmax
tags:
- Company
- Software-as-a-Service
- MCP
- Agents
- Webhook
- Authentication
- Sales Engagement
- Email
- Sales
- CRM
- Productivity
- Meetings
- Sequences
website: https://www.mixmax.com/
---
