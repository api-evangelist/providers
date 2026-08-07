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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Quarterzip Webhooks
  slug: quarterzip-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://quarterzip.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.quarterzip.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.quarterzip.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.quarterzip.ai/sdk-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.quarterzip.ai/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://app.quarterzip.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/quarterzip-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quarterzip-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/quarterzip-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quarterzip-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/quarterzip-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/quarterzip-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/quarterzip-packages.yml
- group: design
  title: ''
  type: Components
  url: components/quarterzip-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/quarterzip-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.quarterzip.ai/
- group: design
  title: ''
  type: Conformance
  url: conformance/quarterzip-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.quarterzip.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/quarterzip-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quarterzip-domain-security.yml
created: '2026-07-17'
description: Quarterzip builds AI screenshare agents that deliver real-time, in-product user assistance. Its agent sees a user's screen, guides them by voice, and executes the steps alongside them in real time, powering onboarding, activation, and customer support at scale without additional headcount. Teams embed Quarterzip through a hosted Link URL or a client-side JavaScript SDK that launches a draggable in-app call (window.Quarterzip.open/close), and receive signed call.completed webhooks (Standard Webhooks HMAC) carrying transcripts and call ratings for CRM and analytics integration. Customers include Bloomreach, Apollo, Dovetail, Airspeed, and Zuper. Quarterzip is ISO 27001 certified.
image: https://cdn.prod.website-files.com/6894695956f5ee5691443986/6a4b45ff2d315efec1742406_poster.jpg
layout: provider
modified: '2026-07-20'
name: Quarterzip
nav: Providers
network: true
overview: 'Quarterzip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Customer Support, Onboarding, and User Activation.


  The Quarterzip catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Quarterzip''s developer surface includes documentation, API reference, getting-started guide, signup flow, changelog, authentication, and 14 more developer resources.'
random_paper: 94
score:
  band: thin
  composite: 40.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.6
    developer_ergonomics: 52.2
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 40.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 30.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Quarterzip Authentication
  slug: quarterzip-authentication
  summary_line: workspace-token/hmac-signature · 2 schemes
- kind: domain-security
  name: Quarterzip Domain Security
  slug: quarterzip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Quarterzip Trust Center
  slug: quarterzip-trust-center
  summary_line: ISO 27001
slug: quarterzip
tags:
- Company
- AI Agents
- Customer Support
- Onboarding
- User Activation
- Screen Sharing
- Voice
- Webhooks
- SDK
- Developer Tools
website: https://quarterzip.ai
---
