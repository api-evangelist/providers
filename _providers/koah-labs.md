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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Beta REST API for Koah publisher team accounts. Resource-oriented URLs, JSON responses, standard HTTP verbs and status codes, Bearer token authentication. Covers publisher CRUD and daily reporting for
  name: Koah API
  slug: koah-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.koahlabs.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.koahlabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.koahlabs.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.koahlabs.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.koahlabs.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.koahlabs.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.koahlabs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/koahlabs
- group: start
  title: ''
  type: SignUp
  url: https://app.koah.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.koahlabs.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.koahlabs.com/legal/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.koahlabs.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/koah-labs-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/koah-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/koah-labs-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/koah-labs-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/koah-labs-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/koah-labs-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/koah-labs-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/koah-labs-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/koah-labs-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/koah-labs-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/koah-labs-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/koah-labs-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/koah-labs-plans-pricing.yml
- group: design
  title: ''
  type: Components
  url: components/koah-labs-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/koah-labs-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/koah-labs-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/koah-labs-domain-security.yml
- group: other
  title: ''
  type: ContentSignal
  url: https://www.koahlabs.com/robots.txt
created: '2026-07-17'
description: 'Koah Labs operates Koah, an advertising network purpose-built for AI applications. It ships two products: an Ad SDK that lets publishers monetize chat and agent experiences with native, intent-matched ad formats (action card, image card, poll, expandable, catalog, side rail) across JavaScript, React, React Native, Flutter, iOS and Android; and Conversion Tracking, a pixel that lets advertisers measure ROI across nine standard event types. A beta REST API at app.koah.ai/api lets publisher teams create and manage publishers programmatically and pull daily performance reports (queries, fill rate, impressions, clicks, CTR, eCPC, eCPM, revenue). Koah publishes agent-native developer surfaces including llms.txt on both its marketing and docs hosts and a first-party Claude Agent Skill for integration.'
image: https://www.koahlabs.com/opengraph-image
layout: provider
modified: '2026-08-13'
name: Koah Labs
nav: Providers
network: true
overview: 'Koah Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Advertising, Ad Network, and Monetization.


  Koah Labs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 24 more developer resources.'
plans:
- name: Koah Labs Plans Pricing
  plan_count: 0
  slug: koah-labs-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Koah Labs Rate Limits
  slug: koah-labs-rate-limits
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 33.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/koah-labs/refs/heads/main/screenshots/koah-labs-2026-07-25T224018.png
security:
- kind: authentication
  name: Koah Labs Authentication
  slug: koah-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Koah Labs Domain Security
  slug: koah-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: koah-labs
tags:
- Company
- Artificial Intelligence
- Advertising
- Ad Network
- Monetization
- Conversion Tracking
- SDK
- Agents
website: https://www.koahlabs.com
---
