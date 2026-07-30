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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: Unified API to manage storage, endpoints, users, and roles across multiple Signiant products. Authenticates via OAuth 2.0 client_credentials, returning a one-hour JWT bearer token.
  name: Signiant Platform API
  slug: signiant-platform-api
- description: Automates system-to-system job creation, endpoint management, job notifications, and event webhooks for unattended, accelerated file transfers.
  name: Signiant Jet API
  slug: signiant-jet-api
- description: Automates Media Shuttle portal management and person-initiated transfers via the Platform API, Management API, and System-to-Person Automation API, with notification webhooks and a browser SDK for app
  name: Signiant Media Shuttle API
  slug: signiant-media-shuttle-api
- description: Schedules and runs jobs, manages users, and controls Signiant Manager software (Flight Deck) via a REST API.
  name: Signiant Flight Deck Manager REST API
  slug: signiant-flight-deck-manager-rest-api
artifact_total: 9
asyncapis:
- description: ''
  name: Signiant Webhooks
  slug: signiant-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signiant-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.signiant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.signiant.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.signiant.com/signiant-platform/api-documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.signiant.com/signiant-platform/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: authentication/signiant-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://support.signiant.com/
- group: company
  title: ''
  type: Blog
  url: https://www.signiant.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Signiant
- group: commercial
  title: ''
  type: Pricing
  url: https://www.signiant.com/platform-pricing_page/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.signiant.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.signiant.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.signiant.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.signiant.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.signiant.com/technology/security/
- group: build
  title: ''
  type: CodeSamples
  url: https://code-samples.developer.signiant.com/
- group: build
  title: ''
  type: Packages
  url: packages/signiant-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/signiant-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/signiant-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/signiant-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/signiant-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/signiant-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/signiant-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/signiant-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/signiant-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/signiant-llms.txt
- group: design
  title: ''
  type: Components
  url: components/signiant-components.yml
created: '2026-07-17'
description: 'Signiant provides intelligent file-movement software that helps the world''s top content creators and distributors move large files fast and securely over public and private networks. The SaaS Signiant Platform unifies four products behind a common OAuth-secured REST API: the Signiant Platform API (storage, endpoints, users, and roles across products), Jet (automated system-to-system transfers with event webhooks), Media Shuttle (person-initiated transfers with Platform, Management, and System-to-Person APIs plus a browser SDK), and Flight Deck (the Manager REST API for scheduling and running jobs). All APIs authenticate with a client_id/client_secret pair exchanged for a one-hour OAuth 2.0 JWT bearer token at platform-api-service.services.cloud.signiant.com, and access is governed by product-scoped account roles.'
image: https://www.signiant.com/wp-content/uploads/signiant-logo.png
layout: provider
mcp_servers:
- description: ''
  name: signiant-mcp.yml
  slug: signiant-mcpyml
modified: '2026-07-21'
name: Signiant
nav: Providers
network: true
overview: 'Signiant publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include File Transfer, Media Supply Chain, Managed File Transfer, Content Delivery, and Storage.


  The Signiant catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Signiant''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 20 more developer resources.'
random_paper: 41
score:
  band: developing
  composite: 51.1
  delta: 6.7
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 44.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Signiant Authentication
  slug: signiant-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Signiant Domain Security
  slug: signiant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Signiant Trust Center
  slug: signiant-trust-center
  summary_line: SOC 2, TPN (Trusted Partner Network), MPA (Motion Picture Association best practices)
slug: signiant
tags:
- File Transfer
- Media Supply Chain
- Managed File Transfer
- Content Delivery
- Storage
- Webhooks
- OAuth
- Media & Entertainment
website: https://developer.signiant.com/
---
