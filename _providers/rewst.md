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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 33.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Inbound custom webhook triggers that start Rewst workflows. An external system sends an HTTP request (method configured per trigger) to a per-trigger URL; the normalized payload ({body, headers, metho
  name: Rewst Webhook Triggers
  slug: rewst-webhook-triggers
artifact_total: 7
asyncapis:
- description: ''
  name: Rewst Webhooks
  slug: rewst-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://rewst.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rewst.help/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rewst.help/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rewst.help/readme.md
- group: operate
  title: ''
  type: Support
  url: https://rewst.io/support/community
- group: company
  title: ''
  type: Blog
  url: https://rewst.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RewstApp
- group: commercial
  title: ''
  type: Pricing
  url: https://rewst.io/pricing
- group: start
  title: ''
  type: Login
  url: https://app.rewst.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rewst.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rewst.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rewst.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/rewst-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://rewst.io/trust-center
- group: auth
  title: ''
  type: Security
  url: https://rewst.io/vulnerability-disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rewst-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rewst-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rewst-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rewst-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rewst-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rewst-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rewst-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rewst-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rewst-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/rewst-packages.yml
- group: design
  title: ''
  type: Components
  url: components/rewst-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rewst-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rewst-llms.txt
created: '2026-07-17'
description: Rewst is a workflow automation and integration (iPaaS/RPA) platform built specifically for managed service providers (MSPs). It combines a visual workflow builder, a form builder, an app builder, 90+ managed MSP integrations (PSA, RMM, Microsoft 365, security tools), reusable automation packages called Crates, and RoboRewsty, an AI assistant, so MSP teams can automate repetitive operational tasks. Rewst's primary programmatic surface is inbound custom webhook triggers that start workflows, authenticated with an optional x-rewst-secret header and rate limited per trigger; it also offers a Generic GraphQL request action for calling external APIs from within workflows. Rewst is SOC 2 Type 2 compliant, publishes a live status page, and runs a Bugcrowd vulnerability-disclosure program. Backed by Sapphire Ventures.
image: https://avatars.githubusercontent.com/u/75550907?v=4
layout: provider
modified: '2026-07-21'
name: Rewst
nav: Providers
network: true
overview: 'Rewst publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Devops, Automation, iPaaS, and RPA.


  The Rewst catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rewst''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, authentication, and 22 more developer resources.'
random_paper: 21
rate_limits:
- limit_count: 0
  name: Rewst Rate Limits
  slug: rewst-rate-limits
score:
  band: thin
  composite: 41.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 22.6
    developer_ergonomics: 45.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 41.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Rewst Authentication
  slug: rewst-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Rewst Domain Security
  slug: rewst-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rewst Vulnerability Disclosure
  slug: rewst-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Rewst Trust Center
  slug: rewst-trust-center
  summary_line: SOC 2, GDPR
slug: rewst
tags:
- Company
- Devops
- Automation
- iPaaS
- RPA
- Workflow Automation
- MSP
- Integration
- Webhooks
website: https://rewst.io/
---
