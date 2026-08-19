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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Kard Agentic Access
  operation_count: 59
  slug: kard-agentic-access
  summary_line: 59 operations · 33 acting
api_count: 16
apis:
- description: The attributions API from Kard — 1 operation(s) for attributions.
  name: Kard attributions API
  slug: kard-attributions-api
- description: The Files API from Kard — 2 operation(s) for files.
  name: Kard Files API
  slug: kard-files-api
- description: The notifications > Notifications API from Kard — 2 operation(s) for notifications > notifications.
  name: Kard notifications > Notifications API
  slug: kard-notifications-notifications-api
- description: The notifications > Subscriptions API from Kard — 2 operation(s) for notifications > subscriptions.
  name: Kard notifications > Subscriptions API
  slug: kard-notifications-subscriptions-api
- description: The Organizations API from Kard — 1 operation(s) for organizations.
  name: Kard Organizations API
  slug: kard-organizations-api
- description: The Organizations > Children API from Kard — 2 operation(s) for organizations > children.
  name: Kard Organizations > Children API
  slug: kard-organizations-children-api
- description: The Organizations > ContentStrategies API from Kard — 2 operation(s) for organizations > contentstrategies.
  name: Kard Organizations > ContentStrategies API
  slug: kard-organizations-contentstrategies-api
- description: The Organizations > Placements API from Kard — 2 operation(s) for organizations > placements.
  name: Kard Organizations > Placements API
  slug: kard-organizations-placements-api
- description: The Ping API from Kard — 1 operation(s) for ping.
  name: Kard Ping API
  slug: kard-ping-api
- description: The rewards API from Kard — 9 operation(s) for rewards.
  name: Kard rewards API
  slug: kard-rewards-api
- description: The transactions API from Kard — 7 operation(s) for transactions.
  name: Kard transactions API
  slug: kard-transactions-api
- description: The users API from Kard — 5 operation(s) for users.
  name: Kard users API
  slug: kard-users-api
- description: The users > attributions API from Kard — 4 operation(s) for users > attributions.
  name: Kard users > attributions API
  slug: kard-users-attributions-api
- description: The users > Rewards API from Kard — 2 operation(s) for users > rewards.
  name: Kard users > Rewards API
  slug: kard-users-rewards-api
- description: The users > uploads API from Kard — 3 operation(s) for users > uploads.
  name: Kard users > uploads API
  slug: kard-users-uploads-api
- description: The users > WebView API from Kard — 1 operation(s) for users > webview.
  name: Kard users > WebView API
  slug: kard-users-webview-api
artifact_total: 40
asyncapis:
- description: ''
  name: Kard Notifications Webhooks
  slug: kard-notifications-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Reference attributions API
  slug: open-kard-attributions-api
- collection_type: open
  name: API Reference attributions Files API
  slug: open-kard-files-api
- collection_type: open
  name: API Reference attributions notifications > Notifications API
  slug: open-kard-notifications-notifications-api
- collection_type: open
  name: API Reference attributions notifications > Subscriptions API
  slug: open-kard-notifications-subscriptions-api
- collection_type: open
  name: API Reference attributions Organizations API
  slug: open-kard-organizations-api
- collection_type: open
  name: API Reference attributions Organizations > Children API
  slug: open-kard-organizations-children-api
- collection_type: open
  name: API Reference attributions Organizations > ContentStrategies API
  slug: open-kard-organizations-contentstrategies-api
- collection_type: open
  name: API Reference attributions Organizations > Placements API
  slug: open-kard-organizations-placements-api
- collection_type: open
  name: API Reference attributions Ping API
  slug: open-kard-ping-api
- collection_type: open
  name: API Reference attributions rewards API
  slug: open-kard-rewards-api
- collection_type: open
  name: API Reference attributions transactions API
  slug: open-kard-transactions-api
- collection_type: open
  name: API Reference attributions users API
  slug: open-kard-users-api
- collection_type: open
  name: API Reference attributions users > attributions API
  slug: open-kard-users-attributions-api
- collection_type: open
  name: API Reference attributions users > Rewards API
  slug: open-kard-users-rewards-api
- collection_type: open
  name: API Reference attributions users > uploads API
  slug: open-kard-users-uploads-api
- collection_type: open
  name: API Reference attributions users > WebView API
  slug: open-kard-users-webview-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/kard-api-reference-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://getkard.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getkard.com/home
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getkard.com/home
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getkard.com/api/transactions/create
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getkard.com/api/integration-guides/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://www.getkard.com/docs/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/kard-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kard-scopes.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kard-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/kard-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kard-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kard-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kard-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/kard-api-catalog.json
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kard-security.txt
- group: design
  title: ''
  type: Components
  url: components/kard-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kard-notifications-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kard-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kard-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kard-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kard-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getkard.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/kard-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kard-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://getkard.com/security
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kard-agentic-access.yml
- group: build
  title: ''
  type: Postman
  url: https://github.com/kard-financial/kard-postman
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kard-financial
- group: company
  title: ''
  type: Blog
  url: https://www.getkard.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.getkard.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.getkard.com/demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getkard.com/privacy-policy
created: '2026-07-17'
description: Kard is an independent commerce media network and card-linked-offers (CLO) rewards platform. Its Rewards API lets fintechs, banks, and card issuers enroll cardholders, submit transactions for closed-loop offer matching, surface personalized offers and redemption locations, run attributions and placements, and receive earned-reward webhook notifications — powering embedded loyalty and cashback programs without building the matching infrastructure. Marketers use the same network to reach 47M+ cardholders with performance-based, transaction-driven offers.
image: https://cdn.prod.website-files.com/6501e86bc5fd522771731f1e/6900e3183a88a4d43e5f8952_Preview-image.png
layout: provider
mcp_servers:
- description: ''
  name: kard-mcp.yml
  slug: kard-mcpyml
modified: '2026-07-19'
name: Kard
nav: Providers
network: true
overview: 'Kard publishes 16 APIs on the [APIs.io](https://apis.io/) network, including attributions API, Files API, notifications > Notifications API, and 13 more. Tagged areas include Company, Rewards, Card-Linked Offers, Loyalty, and Fintech.


  The Kard catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kard''s developer surface includes documentation, API reference, getting-started guide, quickstart, authentication, engineering blog, support, and 28 more developer resources.'
random_paper: 120
scopes:
- name: Kard Scopes
  scope_count: 13
  slug: kard-scopes
  summary_line: 13 scopes · clientCredentials
score:
  band: strong
  composite: 55.8
  delta: 2.2
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 16.7
    contract_quality: 64.1
    developer_ergonomics: 70.8
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 44.7
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 57.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kard/refs/heads/main/screenshots/kard-2026-07-25T223510.png
security:
- kind: authentication
  name: Kard Authentication
  slug: kard-authentication
  summary_line: oauth2/http-bearer · 2 schemes
- kind: domain-security
  name: Kard Domain Security
  slug: kard-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Kard Vulnerability Disclosure
  slug: kard-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kard
tags:
- Company
- Rewards
- Card-Linked Offers
- Loyalty
- Fintech
- Commerce Media
- Advertising
- Transactions
- Cashback
- Webhooks
website: https://getkard.com/
---
