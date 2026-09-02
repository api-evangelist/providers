---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: OAuth 2.0 identity API for now.gg Login. Publishers exchange an authorization code for a token and refresh_token, verify id_token/token server-side, and read user profile and session information for t
  name: now.gg User Account Service API
  slug: nowgg-user-account-service-api
- description: Server-to-server in-app purchase API for publishers using now.gg Payments. Backends verify a purchase token (verifyPurchase), mark a consumable as consumed (consumePurchase) and acknowledge a subscrip
  name: now.gg Payments Server API
  slug: nowgg-payments-server-api
artifact_total: 8
asyncapis:
- description: Outbound webhook contract for now.gg Payments. now.gg POSTs subscription and webshop order events to an endpoint the publisher implements and registers in nowStudio. Derived by API Evangelist from now
  name: now.gg Payments Callbacks (derived)
  slug: bluestacks-payments-asyncapi
- description: ''
  name: Bluestacks Payments Webhooks
  slug: bluestacks-payments-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.bluestacks.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.now.gg/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.now.gg/get-ready/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.now.gg/user-account-service/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.now.gg/get-ready/get-started
- group: start
  title: ''
  type: Console
  url: https://studio.now.gg/
- group: start
  title: ''
  type: SignUp
  url: https://docs.now.gg/nowstudio/create-a-developer-account
- group: operate
  title: ''
  type: Support
  url: https://support.bluestacks.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.bluestacks.com/blog.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bluestacks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/now-gg
- group: commercial
  title: ''
  type: TermsOfService
  url: https://now.gg/terms-and-privacy.html#terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://now.gg/terms-and-privacy.html#eu-privacy
- group: build
  title: ''
  type: Packages
  url: packages/bluestacks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bluestacks-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/bluestacks-cli.yml
- group: design
  title: ''
  type: Components
  url: components/bluestacks-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bluestacks-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bluestacks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bluestacks-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bluestacks-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bluestacks-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bluestacks-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bluestacks-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bluestacks-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bluestacks-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bluestacks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/bluestacks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bluestacks-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bluestacks-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bluestacks-payments-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/bluestacks-payments-asyncapi.yml
created: '2026-08-08'
description: 'BlueStacks is the Android app player and mobile-cloud gaming platform operated by now.gg, Inc. (Campbell, California). The consumer product runs Android apps and games on Windows and macOS, while the now.gg mobile cloud streams the same titles in a browser. The developer-facing surface is published at docs.now.gg and is built around nowStudio (the publisher console) and nowSDK (Unity and native Android modules for Payments, User Account Service, Rewarded Ads, Events and Utility). Two server-side REST surfaces are documented publicly: a User Account Service OAuth 2.0 API on now.gg for token generation, token verification, user info and session info, and a Payments API on payments-api.now.gg for server-side purchase verification, consumption and subscription acknowledgement. now.gg also calls developer-hosted webhooks for subscription and webshop order events, ships an official nowgg CLI on PyPI for uploading app builds, and publishes an embeddable JavaScript module for running
  cloud games in an iframe. BlueStacks AI is a separate, newer product line that packages a sandboxed local runtime for AI agents.'
image: https://cdn-www.bluestacks.com/bs-images/logo-icon.png
layout: provider
modified: '2026-08-08'
name: Bluestacks
nav: Providers
network: true
overview: 'Bluestacks publishes 1 API on the [APIs.io](https://apis.io/) network: now.gg Payments Server API. Tagged areas include Company, Gaming, Cloud Gaming, Android, and Mobile.


  The Bluestacks catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Bluestacks'' developer surface includes documentation, API reference, getting-started guide, developer console, signup flow, support, engineering blog, and 25 more developer resources.'
random_paper: 2
scopes:
- name: Bluestacks Scopes
  scope_count: 3
  slug: bluestacks-scopes
  summary_line: 3 scopes · authorizationCode/refreshToken
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 44.8
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 49.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 64.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bluestacks/refs/heads/main/screenshots/bluestacks-2026-08-17T080648.png
security:
- kind: authentication
  name: Bluestacks Authentication
  slug: bluestacks-authentication
  summary_line: oauth2/http/apiKey · 5 schemes
- kind: domain-security
  name: Bluestacks Domain Security
  slug: bluestacks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bluestacks Vulnerability Disclosure
  slug: bluestacks-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: bluestacks
tags:
- Company
- Gaming
- Cloud Gaming
- Android
- Mobile
- Payments
- In-App Purchases
- Subscription
- Developer Platform
- App Distribution
- Advertising
- Authentication
website: https://www.bluestacks.com/
---
