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
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/human-behavior-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.humanbehavior.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.humanbehavior.co/docs/setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.humanbehavior.co/docs/setup
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.humanbehavior.co/docs/setup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.humanbehavior.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.humanbehavior.co/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/humanbehavior-gh
- group: operate
  title: ''
  type: Support
  url: mailto:team@humanbehavior.co
- group: build
  title: ''
  type: Packages
  url: packages/human-behavior-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/human-behavior-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/human-behavior-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/human-behavior-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/human-behavior-llms.txt
created: '2026-07-17'
description: Human Behavior Inc. is an AI-powered product analytics platform that uses autonomous agents to watch session replays, auto-instrument event tracking, map product workflows, and surface friction, bugs, and rage clicks without manual instrumentation. Developers integrate it with a first-party JavaScript session-recording SDK (humanbehavior-js) that initializes with an API key and streams events to the platform's ingestion endpoint, with framework guides for React, Next.js, Vue, Svelte, Angular, and more, plus optional PostHog ingestion. Backed by $5M from Y Combinator, Vercel, and General Catalyst.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/human-behavior.png
layout: provider
modified: '2026-07-19'
name: Human Behavior
nav: Providers
network: true
overview: 'Human Behavior is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Product Analytics, Session Replay, and Artificial Intelligence.


  Human Behavior''s developer surface includes documentation, getting-started guide, pricing, signup flow, support, authentication, and 8 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 19.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/human-behavior/refs/heads/main/screenshots/human-behavior-2026-07-25T221646.png
security:
- kind: authentication
  name: Human Behavior Authentication
  slug: human-behavior-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Human Behavior Domain Security
  slug: human-behavior-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: human-behavior
tags:
- Company
- Analytics
- Product Analytics
- Session Replay
- Artificial Intelligence
- Developer Tools
- SDK
website: https://www.humanbehavior.co
---
