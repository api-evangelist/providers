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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: Brands report new orders, order updates (including partial returns), and cancellations to Button server-to-server, passing the Button Attribution Token (btn_ref) captured by the Merchant Library; docu
  name: Button Order API
  slug: button-order-api
- description: The Accounts API from Button — 2 operation(s) for accounts.
  name: Button Accounts API
  slug: usebutton-accounts-api
- description: The Brands Api API from Button — 1 operation(s) for brands api.
  name: Button Brands Api API
  slug: usebutton-brands-api-api
- description: The Create API from Button — 2 operation(s) for create.
  name: Button Create API
  slug: usebutton-create-api
- description: The Links Api API from Button — 1 operation(s) for links api.
  name: Button Links Api API
  slug: usebutton-links-api-api
- description: The Offers API from Button — 1 operation(s) for offers.
  name: Button Offers API
  slug: usebutton-offers-api
- description: The Transactions API from Button — 1 operation(s) for transactions.
  name: Button Transactions API
  slug: usebutton-transactions-api
artifact_total: 19
asyncapis:
- description: ''
  name: Usebutton Webhooks
  slug: usebutton-webhooks
collections:
- collection_type: postman
  name: billing-api Accounts API
  slug: postman-usebutton-accounts-api
- collection_type: postman
  name: billing-api Accounts Brands Api API
  slug: postman-usebutton-brands-api-api
- collection_type: postman
  name: billing-api Accounts Create API
  slug: postman-usebutton-create-api
- collection_type: postman
  name: billing-api Accounts Links Api API
  slug: postman-usebutton-links-api-api
- collection_type: postman
  name: billing-api Accounts Offers API
  slug: postman-usebutton-offers-api
- collection_type: postman
  name: billing-api Accounts Transactions API
  slug: postman-usebutton-transactions-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/button/overview
- group: company
  title: ''
  type: Website
  url: https://usebutton.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.usebutton.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.usebutton.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.usebutton.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.usebutton.com/reference/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.usebutton.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.usebutton.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/button
- group: start
  title: ''
  type: Login
  url: https://app.usebutton.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usebutton.com/support/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usebutton.com/support/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usebutton.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/usebutton-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.usebutton.com/changelog
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/usebutton-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/usebutton-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/usebutton-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/usebutton-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/usebutton-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/usebutton-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/usebutton-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/usebutton-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/usebutton-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/usebutton-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/usebutton-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/usebutton-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.usebutton.com/support/security
- group: auth
  title: ''
  type: Security
  url: https://www.usebutton.com/support/security
- group: design
  title: ''
  type: DataModel
  url: data-model/usebutton-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/usebutton-offers-to-link.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/usebutton-billing-reconciliation.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/usebutton-creator-shortlinks.md
- group: auth
  title: ''
  type: TrustCenter
  url: security/usebutton-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/usebutton-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usebutton-domain-security.yml
created: '2026-07-17'
description: 'Button (usebutton.com) is a mobile commerce technology company whose platform connects Publishers and Brands in a two-sided marketplace: publishers deep-link their users into retailer apps and sites with full attribution, and brands acquire and re-engage customers through those optimized journeys. Its server-to-server APIs cover personalized Offers, attributed Link and Shortlink generation (including Amazon creator links), Brand partnership details, Billing/affiliation transaction reporting, and Order reporting, complemented by Publisher SDKs, Merchant Libraries, and HMAC-signed transaction webhooks.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usebutton.png
layout: provider
mcp_servers:
- description: ''
  name: usebutton-mcp.yml
  slug: usebutton-mcpyml
modified: '2026-07-21'
name: Button
nav: Providers
network: true
overview: 'Button publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Brands Api API, Create API, and 3 more. Tagged areas include Commerce, Mobile Commerce, Affiliate, Attribution, and Deep Linking.


  The Button catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Button''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 29 more developer resources.'
random_paper: 29
score:
  band: strong
  composite: 59.8
  delta: -0.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.2
    developer_ergonomics: 73.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 60.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Usebutton Authentication
  slug: usebutton-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Usebutton Domain Security
  slug: usebutton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Usebutton Vulnerability Disclosure
  slug: usebutton-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Usebutton Trust Center
  slug: usebutton-trust-center
  summary_line: SOC 2, GDPR
slug: usebutton
tags:
- Commerce
- Mobile Commerce
- Affiliate
- Attribution
- Deep Linking
- Offers
- Publishers
- Retail
website: https://usebutton.com
---
