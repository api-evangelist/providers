---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Counter Dev Agentic Access
  operation_count: 8
  slug: counter-dev-agentic-access
  summary_line: 8 operations · 5 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: The Account API from Counter — 4 operation(s) for account.
  name: Counter Account API
  slug: counter-dev-account-api
- description: The Stats API from Counter — 2 operation(s) for stats.
  name: Counter Stats API
  slug: counter-dev-stats-api
- description: The Tracking API from Counter — 2 operation(s) for tracking.
  name: Counter Tracking API
  slug: counter-dev-tracking-api
artifact_total: 15
asyncapis:
- description: 'Counter publishes NO AsyncAPI of its own. This document is DERIVED by API Evangelist from the AGPL-3.0 server source at https://github.com/ihucos/counter.dev/blob/master/backend/endpoints/dump.go and '
  name: Counter Stats Stream
  slug: counter-dev-stats-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Counter Account API
  slug: open-counter-dev-account-api
- collection_type: open
  name: Counter Account Stats API
  slug: open-counter-dev-stats-api
- collection_type: open
  name: Counter Account Tracking API
  slug: open-counter-dev-tracking-api
- collection_type: open
  name: Counter API
  slug: open-counter-dev
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/counter-dev-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/counter-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/counter-dev-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ihucos/counter.dev
- group: company
  title: ''
  type: Website
  url: https://counter.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://counter.dev/help/integration.html
- group: commercial
  title: ''
  type: Plans
  url: plans/counter-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/counter-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/counter-dev-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://counter.dev/blog
- group: build
  title: ''
  type: Packages
  url: packages/counter-dev-packages.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/counter-dev-stats-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/counter-dev-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/counter-dev-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/counter-dev-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/counter-dev-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/counter-dev-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/counter-dev-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/counter-dev-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/counter-dev-cli.yml
- group: design
  title: ''
  type: Components
  url: components/counter-dev-components.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://counter.dev/help/integration.html
- group: operate
  title: ''
  type: HelpCenter
  url: https://counter.dev/help/
- group: operate
  title: ''
  type: Support
  url: https://github.com/ihucos/counter.dev/issues
- group: start
  title: ''
  type: SignUp
  url: https://counter.dev/welcome.html?sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://counter.dev/pages/privacy.html
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ihucos/counter.dev
- group: commercial
  title: ''
  type: License
  url: https://github.com/ihucos/counter.dev/blob/master/LICENSE
created: '2026-06-21'
description: Counter (counter.dev) is an open-source, privacy-friendly web analytics service. A lightweight tracking snippet POSTs a single aggregated hit per visit to a public collect endpoint (t.counter.dev), and a token-authenticated dashboard data feed returns aggregated stats. Counter uses no cookies, no logging, and no IP fingerprinting. It is AGPL-3.0 licensed and can be self-hosted; the hosted service is pay-what-you-want.
finops:
- name: Counter Dev Finops
  service_category: Analytics
  slug: counter-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/counter-dev.png
layout: provider
modified: '2026-08-13'
name: Counter
nav: Providers
network: true
overview: 'Counter publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Stats API, and Tracking API. Tagged areas include Web Analytics, Privacy, Open Source, Tracking, and Self-Hosted.


  The Counter catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Counter''s developer surface includes authentication, documentation, engineering blog, sandbox, CLI, getting-started guide, support, and 22 more developer resources.'
plans:
- name: Counter Dev Plans Pricing
  plan_count: 2
  slug: counter-dev-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 3
  name: Counter Dev Rate Limits
  slug: counter-dev-rate-limits
score:
  band: developing
  composite: 51.2
  delta: -1.9
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 16.7
    contract_quality: 59.2
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 34.2
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/counter-dev/refs/heads/main/screenshots/counter-dev-2026-07-25T210507.png
security:
- kind: authentication
  name: Counter Dev Authentication
  slug: counter-dev-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Counter Dev Domain Security
  slug: counter-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: counter-dev
tags:
- Web Analytics
- Privacy
- Open Source
- Tracking
- Self-Hosted
website: https://counter.dev/
---
