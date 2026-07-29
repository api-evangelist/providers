---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Nango Agentic Access
  operation_count: 21
  slug: nango-agentic-access
  summary_line: 21 operations · 14 acting
api_count: 6
apis:
- description: Nango provides a unified API platform for building product integrations with 600+ external APIs. It offers managed API authentication (OAuth and other auth methods), a syncing framework, proxy for API
  name: Nango
  slug: nango
- description: Trigger one-shot actions.
  name: Nango Actions API
  slug: nango-actions-api
- description: Manage end-user connections and credentials.
  name: Nango Connections API
  slug: nango-connections-api
- description: Manage integration definitions.
  name: Nango Integrations API
  slug: nango-integrations-api
- description: Proxy requests to upstream APIs with credential injection.
  name: Nango Proxy API
  slug: nango-proxy-api
- description: Manage and trigger data syncs.
  name: Nango Syncs API
  slug: nango-syncs-api
artifact_total: 30
collections:
- collection_type: open
  name: Nango API
  slug: open-nango
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nango-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nango-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nango-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nango-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nangohq
- group: docs
  title: ''
  type: Documentation
  url: https://nango.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://nango.dev/docs/getting-started/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://nango.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://nango.dev/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://nango.dev/docs/updates
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nango.dev/
- group: start
  title: ''
  type: Portal
  url: https://app.nango.dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nango.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nango.dev/privacy-policy
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/NangoHQ/nango
created: '2026-01-02'
description: Nango.dev is a developer infrastructure platform that simplifies building product integrations with external APIs. It provides the infrastructure to build reliable, scalable integrations fast, including API authentication, a syncing framework, webhook handling, and observability, supporting over 400 APIs with 600+ pre-built integrations.
features:
- 'Free: 10 connections, 100k proxy/runs/logs/storage/webhooks, 2 envs'
- 'Starter from $50/mo: 20 connections, 200k usage, 3 envs'
- 'Growth from $500/mo: 100 connections, 1M usage, 10 envs, priority support'
- 'Enterprise custom: unlimited, SOC 2, RBAC, SAML SSO, HIPAA option'
- Self-hosting available on Enterprise
- 400+ pre-built API integrations
- 'Auth: OAuth 2.0/1.0a, API Key, Basic, JWT, custom'
- Proxy API for authenticated calls without token management
- Sync engine for incremental data syncs
- Actions for one-shot operations
- Webhooks bridging external -> your app
- Functions (TypeScript) for custom logic
- Connect UI for embedded auth flows
- Admin dashboard for connection health
- Logs and metrics for each integration
- Open-source core (MIT license)
finops:
- name: Nango Finops
  service_category: Integrations Platform
  slug: nango-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nango.png
layout: provider
modified: '2026-05-04'
name: Nango
nav: Providers
network: true
overview: 'Nango publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Connections API, Integrations API, and 2 more. Tagged areas include AI Agents, Integrations, OAuth, Syncing, and Unified API.


  Nango''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, changelog, developer portal, and 8 more developer resources.'
plans:
- name: Nango Plans Pricing
  plan_count: 4
  slug: nango-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 3
  name: Nango Rate Limits
  slug: nango-rate-limits
score:
  band: developing
  composite: 49.7
  delta: -1.7
  facets:
    commercial_clarity: 71.1
    contract_quality: 50.0
    developer_ergonomics: 41.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 63.2
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nango/refs/heads/main/screenshots/nango-2026-06-20T185934.png
security:
- kind: authentication
  name: Nango Authentication
  slug: nango-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nango Domain Security
  slug: nango-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nango Vulnerability Disclosure
  slug: nango-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nango
tags:
- AI Agents
- Integrations
- OAuth
- Syncing
- Unified API
- Webhooks
website: https://app.nango.dev
---
