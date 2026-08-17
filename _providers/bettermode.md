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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'Bettermode''s public GraphQL API for reading and writing community data — spaces, posts, members, reactions, tags, and collections — plus app installation and signed webhooks. Single POST endpoint per '
  name: Bettermode GraphQL API
  slug: bettermode-graphql-api
artifact_total: 6
asyncapis:
- description: ''
  name: Bettermode Webhooks
  slug: bettermode-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bettermode.com/docs/guide/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bettermode.com/docs/guide/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.bettermode.com/docs/operations/schema/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.bettermode.com/docs/guide/graphql/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: authentication/bettermode-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bettermode-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bettermode-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bettermode-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bettermode.com/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bettermode-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/bettermode-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bettermode-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/bettermode-cli.yml
- group: design
  title: ''
  type: Components
  url: components/bettermode-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bettermode-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bettermode-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/bettermode-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://bettermode.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/bettermode-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bettermode-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tribeplatform
- group: company
  title: ''
  type: Blog
  url: https://bettermode.com/blog
- group: operate
  title: ''
  type: Support
  url: https://bettermode.com/hub/knowledge-base
- group: commercial
  title: ''
  type: Pricing
  url: https://bettermode.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://bettermode.com/account/signup
- group: start
  title: ''
  type: Login
  url: https://bettermode.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bettermode.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bettermode.com/legal/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://bettermode.com/
created: '2026-07-17'
description: Bettermode is an all-in-one customer community platform (formerly Tribe) that lets organizations launch branded, no-code communities to turn engagement into measurable retention and growth. It combines discussion forums, Q&A, knowledge base, member directories, events, wishlists, changelogs, and roadmaps with analytics and out-of-the-box integrations (Salesforce, HubSpot, Intercom, Segment). For developers, Bettermode exposes a GraphQL API (US and EU regions), an Apps framework with signed webhooks, embedding and custom-script surfaces, first-party @tribeplatform SDKs/UI kits, and a CLI. More than 50,000 organizations use Bettermode. Backed by Bessemer Venture Partners and CRV.
image: https://bettermode.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Bettermode
nav: Providers
network: true
overview: 'Bettermode publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Community, Customer Community, Community Platform, Customer Engagement, and Customer Success.


  The Bettermode catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bettermode''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, engineering blog, support, and 22 more developer resources.'
random_paper: 24
rate_limits:
- limit_count: 8
  name: Bettermode Rate Limits
  slug: bettermode-rate-limits
score:
  band: developing
  composite: 55.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 65.2
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 60.5
  previous_composite: 55.0
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bettermode/refs/heads/main/screenshots/bettermode-2026-07-25T202811.png
security:
- kind: authentication
  name: Bettermode Authentication
  slug: bettermode-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Bettermode Domain Security
  slug: bettermode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bettermode Trust Center
  slug: bettermode-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: bettermode
tags:
- Community
- Customer Community
- Community Platform
- Customer Engagement
- Customer Success
- GraphQL
- Webhooks
- No-Code
- SaaS
- Developer
website: https://bettermode.com/
---
