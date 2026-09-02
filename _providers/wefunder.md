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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 24
  human_in_the_loop: 3
  name: Wefunder Agentic Access
  operation_count: 48
  slug: wefunder-agentic-access
  summary_line: 48 operations · 24 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: The Activity API from Wefunder — 3 operation(s) for activity.
  name: Wefunder Activity API
  slug: wefunder-activity-api
- description: The Attribution API from Wefunder — 2 operation(s) for attribution.
  name: Wefunder Attribution API
  slug: wefunder-attribution-api
- description: The Attribution Partners API from Wefunder — 5 operation(s) for attribution partners.
  name: Wefunder Attribution Partners API
  slug: wefunder-attribution-partners-api
- description: The Attribution Webhooks API from Wefunder — 5 operation(s) for attribution webhooks.
  name: Wefunder Attribution Webhooks API
  slug: wefunder-attribution-webhooks-api
- description: The Campaigns API from Wefunder — 1 operation(s) for campaigns.
  name: Wefunder Campaigns API
  slug: wefunder-campaigns-api
- description: The Explore API from Wefunder — 2 operation(s) for explore.
  name: Wefunder Explore API
  slug: wefunder-explore-api
- description: The Intents API from Wefunder — 2 operation(s) for intents.
  name: Wefunder Intents API
  slug: wefunder-intents-api
- description: The Investments API from Wefunder — 1 operation(s) for investments.
  name: Wefunder Investments API
  slug: wefunder-investments-api
- description: The Syndicate Deals API from Wefunder — 5 operation(s) for syndicate deals.
  name: Wefunder Syndicate Deals API
  slug: wefunder-syndicate-deals-api
- description: The Syndicate Members API from Wefunder — 12 operation(s) for syndicate members.
  name: Wefunder Syndicate Members API
  slug: wefunder-syndicate-members-api
- description: The Syndicate Statistics API from Wefunder — 1 operation(s) for syndicate statistics.
  name: Wefunder Syndicate Statistics API
  slug: wefunder-syndicate-statistics-api
- description: The Syndicates API from Wefunder — 2 operation(s) for syndicates.
  name: Wefunder Syndicates API
  slug: wefunder-syndicates-api
- description: The Users API from Wefunder — 1 operation(s) for users.
  name: Wefunder Users API
  slug: wefunder-users-api
artifact_total: 33
asyncapis:
- description: ''
  name: Wefunder Webhooks
  slug: wefunder-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wefunder API v2 Activity API
  slug: open-wefunder-activity-api
- collection_type: open
  name: Wefunder API v2 Activity Attribution API
  slug: open-wefunder-attribution-api
- collection_type: open
  name: Wefunder API v2 Activity Attribution Partners API
  slug: open-wefunder-attribution-partners-api
- collection_type: open
  name: Wefunder API v2 Activity Attribution Webhooks API
  slug: open-wefunder-attribution-webhooks-api
- collection_type: open
  name: Wefunder API v2 Activity Campaigns API
  slug: open-wefunder-campaigns-api
- collection_type: open
  name: Wefunder API v2 Activity Explore API
  slug: open-wefunder-explore-api
- collection_type: open
  name: Wefunder API v2 Activity Intents API
  slug: open-wefunder-intents-api
- collection_type: open
  name: Wefunder API v2 Activity Investments API
  slug: open-wefunder-investments-api
- collection_type: open
  name: Wefunder API v2 Activity Syndicate Deals API
  slug: open-wefunder-syndicate-deals-api
- collection_type: open
  name: Wefunder API v2 Activity Syndicate Members API
  slug: open-wefunder-syndicate-members-api
- collection_type: open
  name: Wefunder API v2 Activity Syndicate Statistics API
  slug: open-wefunder-syndicate-statistics-api
- collection_type: open
  name: Wefunder API v2 Activity Syndicates API
  slug: open-wefunder-syndicates-api
- collection_type: open
  name: Wefunder API v2 Activity Users API
  slug: open-wefunder-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/wefunder-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wefunder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wefunder.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wefunder.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wefunder.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/Wefunder/wefunder-node#quickstart-server-to-server
- group: operate
  title: ''
  type: Support
  url: https://help.wefunder.com
- group: company
  title: ''
  type: Blog
  url: https://wefunder.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Wefunder
- group: commercial
  title: ''
  type: Pricing
  url: https://wefunder.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wefunder.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wefunder.com/terms#privacy
- group: start
  title: ''
  type: SignUp
  url: https://wefunder.com/signup
- group: build
  title: ''
  type: Packages
  url: packages/wefunder-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wefunder-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wefunder-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wefunder-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wefunder-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/wefunder-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wefunder-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wefunder-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wefunder-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wefunder-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/wefunder-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wefunder-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wefunder-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wefunder-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wefunder-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wefunder-scopes.yml
created: '2026-07-17'
description: Wefunder is the largest SEC-registered funding portal, the home of the Community Round — a Public Benefit Corporation (YC W13) that has helped 4,400+ founders raise over $1B from more than one million everyday investors since 2012, with notable raises from Mercury, Substack, and Replit. Its OAuth 2.0 Wefunder API v2 (api.wefunder.com) exposes public offerings, investments, campaigns, syndicates, write intents, and campaign attribution with signed webhooks, backed by an official TypeScript SDK (@wefunder/sdk) and PKCE-first authorization.
image: https://wefunder.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Wefunder MCP Server
  slug: wefunder-mcp-server
modified: '2026-07-21'
name: Wefunder
nav: Providers
network: true
overview: 'Wefunder publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Attribution API, Attribution Partners API, and 10 more. Tagged areas include Company, Crowdfunding, Equity Crowdfunding, Investing, and Fintech.


  The Wefunder catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wefunder''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
random_paper: 3
scopes:
- name: Wefunder Scopes
  scope_count: 16
  slug: wefunder-scopes
  summary_line: 16 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 52.8
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 64.5
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wefunder/refs/heads/main/screenshots/wefunder-2026-08-17T082859.png
security:
- kind: authentication
  name: Wefunder Authentication
  slug: wefunder-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Wefunder Domain Security
  slug: wefunder-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wefunder
tags:
- Company
- Crowdfunding
- Equity Crowdfunding
- Investing
- Fintech
- Startups
- Fundraising
- Syndicates
- Regulation Crowdfunding
website: https://wefunder.com
---
