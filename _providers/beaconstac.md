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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: HTTP API to programmatically create custom and dynamic QR Codes (20+ types), manage landing pages and forms, retrieve real-time scan analytics (device, location, timing), and configure webhooks. Token
  name: Uniqode QR Code API
  slug: uniqode-qr-code-api
artifact_total: 5
asyncapis:
- description: ''
  name: Beaconstac Webhooks
  slug: beaconstac-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beaconstac-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uniqode.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.uniqode.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.uniqode.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.uniqode.com/
- group: company
  title: ''
  type: Blog
  url: https://www.uniqode.com/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.uniqode.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.uniqode.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.uniqode.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.uniqode.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uniqode.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uniqode.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/beaconstac
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uniqode.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.uniqode.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/beaconstac-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beaconstac-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beaconstac-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beaconstac-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/beaconstac-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/beaconstac-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/beaconstac-packages.yml
- group: design
  title: ''
  type: Components
  url: components/beaconstac-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/beaconstac-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beaconstac-llms.txt
created: '2026-07-17'
description: Beaconstac (now Uniqode) is a B2B SaaS platform for creating, customizing, and tracking dynamic QR Codes and Digital Business Cards at scale, connecting physical touchpoints to measurable digital experiences for 50,000+ brands. Its HTTP API lets developers programmatically create 20+ QR Code types (static and dynamic), manage landing pages and forms, retrieve real-time scan analytics (device, location, timing), and configure webhooks. Authentication is a dashboard-issued API token sent in the Authorization header alongside an Organization ID. The company is SOC 2 Type II, ISO 27001:2022, HIPAA, and GDPR compliant. Formerly MobStac / Beaconstac; backed by Accel.
image: https://cdn.prod.website-files.com/6669ecc72092c5122374cf32/6731094d55afbe708065f595_uniqode-opengraph.png
layout: provider
modified: '2026-07-18'
name: Beaconstac
nav: Providers
network: true
overview: 'Beaconstac publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Big Data, QR Codes, Digital Business Cards, and Marketing.


  The Beaconstac catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Beaconstac''s developer surface includes documentation, API reference, engineering blog, support, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 26
score:
  band: developing
  composite: 47.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 41.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 47.2
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beaconstac/refs/heads/main/screenshots/beaconstac-2026-07-25T202531.png
security:
- kind: authentication
  name: Beaconstac Authentication
  slug: beaconstac-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Beaconstac Domain Security
  slug: beaconstac-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Beaconstac Trust Center
  slug: beaconstac-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, ISO 27001:2022, HIPAA, GDPR
slug: beaconstac
tags:
- Company
- Big Data
- QR Codes
- Digital Business Cards
- Marketing
- Analytics
- SaaS
- Proximity
website: https://www.uniqode.com
---
