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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Button Agentic Access
  operation_count: 8
  slug: button-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 6
apis:
- description: The Accounts API from Button — 2 operation(s) for accounts.
  name: Button Accounts API
  slug: button-accounts-api
- description: The Brands Api API from Button — 1 operation(s) for brands api.
  name: Button Brands Api API
  slug: button-brands-api-api
- description: The Create API from Button — 2 operation(s) for create.
  name: Button Create API
  slug: button-create-api
- description: The Links Api API from Button — 1 operation(s) for links api.
  name: Button Links Api API
  slug: button-links-api-api
- description: The Offers API from Button — 1 operation(s) for offers.
  name: Button Offers API
  slug: button-offers-api
- description: The Transactions API from Button — 1 operation(s) for transactions.
  name: Button Transactions API
  slug: button-transactions-api
arazzos:
- description: Fetch the real-time affiliate offers available to a Publisher user, then generate a fully attributable Button-wrapped link to the chosen Brand destination.
  name: Fetch offers and generate an attributable link
  slug: button-offer-to-link
- description: List your Button billing accounts (one per currency), then page through all commission transactions across every account to reconcile affiliate earnings.
  name: Reconcile affiliate commission transactions
  slug: button-reconcile-transactions
artifact_total: 21
asyncapis:
- description: Button delivers signed HTTP POST webhooks to a Publisher-configured URL when a transaction takes place based on traffic the Publisher drove to a Brand. Each delivery carries a Transaction in three pos
  name: Button Transaction Webhooks
  slug: button-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: billing-api Accounts API
  slug: open-button-accounts-api
- collection_type: open
  name: billing-api Accounts Brands Api API
  slug: open-button-brands-api-api
- collection_type: open
  name: billing-api Accounts Create API
  slug: open-button-create-api
- collection_type: open
  name: billing-api Accounts Links Api API
  slug: open-button-links-api-api
- collection_type: open
  name: billing-api Accounts Offers API
  slug: open-button-offers-api
- collection_type: open
  name: billing-api Accounts Transactions API
  slug: open-button-transactions-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.usebutton.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.usebutton.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.usebutton.com/docs/publishers-getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.usebutton.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.usebutton.com/docs/publishers-getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.usebutton.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/button
- group: operate
  title: ''
  type: Support
  url: https://www.usebutton.com/contact-us
- group: auth
  title: ''
  type: Security
  url: https://www.usebutton.com/support/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usebutton.com/support/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usebutton.com/support/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.usebutton.com/support/gdpr-notice
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.usebutton.com/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/button-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/button-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/button-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/button-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/button-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/button-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/button-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/button-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/button-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/button-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/button-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/button-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/button-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/button-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/button-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/button-billing-api-overlay.yaml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/button-offer-to-link.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/button-reconcile-transactions.yml
created: '2026-07-17'
description: Button is a mobile commerce and affiliate attribution platform connecting publishers, retailers, advertisers, and creators. Its AI-driven intelligence platform identifies and routes users to the highest-converting destination, powering smart routing, in-app priority, privacy-safe first-party attribution and analytics, and the CuratedBy Button publisher tool that combines affiliate, retail media, and seller budgets. For developers, Button exposes REST APIs for brand details, real-time affiliate offers, attributable link and shortlink generation, and billing and commission transaction reporting, plus native iOS and Android SDKs, merchant libraries, and signed transaction webhooks that close the loop on the user's commerce journey.
image: https://github.com/button.png
layout: provider
mcp_servers:
- description: ''
  name: button-mcp.yml
  slug: button-mcpyml
modified: '2026-07-18'
name: Button
nav: Providers
network: true
overview: 'Button publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Brands Api API, Create API, and 3 more. Tagged areas include Commerce, Affiliate Marketing, Mobile, Attribution, and Deep Linking.


  The Button catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Button''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 25 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 45.3
  delta: -4.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 16.7
    contract_quality: 64.8
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 28.9
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/button/refs/heads/main/screenshots/button-2026-07-25T204122.png
security:
- kind: authentication
  name: Button Authentication
  slug: button-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Button Domain Security
  slug: button-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Button Vulnerability Disclosure
  slug: button-vulnerability-disclosure
  summary_line: contact published
slug: button
tags:
- Commerce
- Affiliate Marketing
- Mobile
- Attribution
- Deep Linking
- Retail Media
- Analytics
- Advertising
- Links
website: https://www.usebutton.com
---
