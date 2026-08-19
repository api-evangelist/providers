---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.1
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: The core Bolt merchant API. Covers Bolt shopper accounts (profile, addresses, payment methods), merchant configuration and callbacks, order token creation, shipment tracking, transaction authorize/cap
  name: Bolt API
  slug: bolt-api
- description: The Embeddable Checkout v1 API used by merchants building their own checkout UI on top of Bolt. Exposes shopper account lookup and management, address and payment-method operations, OAuth token exchan
  name: Bolt Embeddable Checkout v1 API
  slug: embeddable-checkout-v1
- description: The v3 generation of the Bolt Embeddable Checkout API, served under a /v3 path with a templated environment server variable. Reorganises the surface around Accounts, Payments (including guest payments
  name: Bolt Embeddable Checkout v3 API
  slug: embeddable-checkout-v3
- description: The Bolt Tokenizer endpoint, hosted on the separate bolttk.com domain so raw card data never touches the merchant server. Publishes an RSA public key for client-side encryption and exchanges an encryp
  name: Bolt Tokenizer API
  slug: tokenizer
- description: 'Bolt exposes two Model Context Protocol surfaces: a hosted documentation MCP server advertised at help.boltapp.com/mcp with search_docs, get_doc_page and list_doc_sections tools, and a Speakeasy-gener'
  name: Bolt MCP Servers
  slug: mcp
artifact_total: 14
asyncapis:
- description: ''
  name: Bolt Financial Webhooks
  slug: bolt-financial-webhooks
collections:
- collection_type: open
  name: Bolt API Reference
  slug: open-bolt-financial-bolt-api
- collection_type: open
  name: Embedded API Reference
  slug: open-bolt-financial-embeddable-checkout-v1
- collection_type: open
  name: Bolt API Reference
  slug: open-bolt-financial-embeddable-checkout-v3
- collection_type: open
  name: Tokenizer Endpoint
  slug: open-bolt-financial-tokenizer
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bolt-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bolt.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.boltapp.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://help.boltapp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.boltapp.com/api-bolt/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.boltapp.com/getting-started/introduction/
- group: operate
  title: ''
  type: Support
  url: https://help.boltapp.com/support
- group: company
  title: ''
  type: Blog
  url: https://boltapp.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BoltApp
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/bolt-inc/bolt-public
- group: commercial
  title: ''
  type: Pricing
  url: https://help.boltapp.com/dashboard/billing/fees/
- group: start
  title: ''
  type: SignUp
  url: https://merchant.boltapp.com/onboarding
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boltapp.com/end-user-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boltapp.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bolt.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bolt-financial-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/bolt-financial-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bolt-financial-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bolt-financial-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bolt-financial-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/bolt-financial-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bolt-financial-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/bolt-financial-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/bolt-financial-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bolt-financial-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bolt-financial-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bolt-financial-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bolt-financial-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/bolt-financial-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bolt-financial-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/bolt-financial-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bolt-financial-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bolt-financial-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-31'
description: 'Bolt Financial, Inc. is an American commerce technology company that gives retailers a one-click, identity-powered checkout backed by a shopper account network, payments processing, tokenization and fraud protection. Merchants integrate Bolt either through platform plugins (Adobe Commerce/Magento, BigCommerce, Salesforce Commerce Cloud, Shopify, WooCommerce) or directly against a REST API surface that covers shopper accounts, order tokens, transaction authorize/capture/refund/void, subscriptions, product catalog, merchant statements, webhooks and a hosted card tokenizer. Bolt publishes OpenAPI 3.0 definitions for its Bolt API, Embeddable Checkout v1 and v3, and Tokenizer endpoints, ships first-party SDKs for TypeScript, Python, C#, Go, PHP, iOS/Swift, Android/Kotlin, React Native, Unity and Unreal, and maintains an explicit agent-facing surface: an llms.txt index, a hosted documentation MCP server and two published agent skills.'
image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-site/company-images/bolt-financial.png
layout: provider
mcp_servers:
- description: ''
  name: bolt-financial-mcp.yml
  slug: bolt-financial-mcpyml
modified: '2026-07-31'
name: Bolt Financial
nav: Providers
network: true
overview: 'Bolt Financial publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Bolt API, Bolt Embeddable Checkout v1 API, Bolt Embeddable Checkout v3 API, and 1 more. Tagged areas include Company, Payments, Checkout, eCommerce, and Fintech.


  The Bolt Financial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bolt Financial''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 70
scopes:
- name: Bolt Financial Scopes
  scope_count: 4
  slug: bolt-financial-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 62.6
  delta: 2.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 30.3
    contract_quality: 64.6
    developer_ergonomics: 77.4
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 42.1
  previous_composite: 60.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 78.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bolt-financial/refs/heads/main/screenshots/bolt-financial-2026-08-07T162709.png
security:
- kind: authentication
  name: Bolt Financial Authentication
  slug: bolt-financial-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Bolt Financial Domain Security
  slug: bolt-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bolt-financial
tags:
- Company
- Payments
- Checkout
- eCommerce
- Fintech
- Subscriptions
- Tokenization
- Fraud
- Identity
- Webhooks
website: https://www.bolt.com
---
