---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: false
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
  score: 19.8
  scored_at: '2026-09-05'
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
overview: 'Quarterzip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Customer-Support, Onboarding, and User Activation.


  The Quarterzip catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Quarterzip''s developer surface includes documentation, API reference, getting-started guide, signup flow, changelog, authentication, and 14 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 50.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 37.7
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quarterzip/refs/heads/main/screenshots/quarterzip-2026-09-02T152730.png
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
- Customer-Support
- Onboarding
- User Activation
- Screen Sharing
- Voice
- Webhook
- SDK
- Developer Tools
website: https://quarterzip.ai
---
