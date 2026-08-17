---
access_model:
  confidence: high
  label: Paid ($1,000/month) · Invitation and approval onboarding
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - https://dashboard.osmaura.com/signals/docs
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Osmaura Agentic Access
  operation_count: 4
  slug: osmaura-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: A read-only REST API returning tenant-scoped, human-reviewed prospect editions. Each edition is a dated, ranked batch of prospect dossiers (20 in a normal edition) split into normalized identity, obse
  name: Osmaura Prospect API
  slug: osmaura-prospect-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/osmaura-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/osmaura-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/osmaura-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://osmaura.com
- group: start
  title: ''
  type: SignUp
  url: https://cal.com/osmaura-ycs26/intro-meeting
- group: operate
  title: ''
  type: Support
  url: mailto:founders@osmaura.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.osmaura.com/signals
- group: docs
  title: ''
  type: Documentation
  url: https://dashboard.osmaura.com/signals/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dashboard.osmaura.com/signals/docs#prospects
- group: start
  title: ''
  type: GettingStarted
  url: https://dashboard.osmaura.com/signals/docs#quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://dashboard.osmaura.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/osmaura-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/osmaura-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/osmaura-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/osmaura-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/osmaura-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://dashboard.osmaura.com/signals/docs#legacy
- group: design
  title: ''
  type: Conformance
  url: conformance/osmaura-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/osmaura-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/osmaura-llms.txt
created: '2026-07-17'
description: Osmaura is a Y Combinator (Summer 2026) startup building opportunity intelligence for corporate law firms. It monitors public web signals, the government record, and a firm's own context to identify companies approaching a legal need before they begin looking for outside counsel, then briefs the right partner on why the moment may matter. Coverage centers on regulatory change, market movement such as hiring and funding, litigation activity, and company milestones, mapped to practice areas including immigration, startups, and commercial litigation. Osmaura ships a production REST API — the Osmaura Prospect API — documented publicly with an OpenAPI 3.1 definition. It returns dated, human-reviewed "editions" of ranked prospect dossiers that deliberately keep source-backed data separate from analyst conclusions, and every government-derived record carries an official link, a reproducible record locator, and a data-through date. Access is bearer-key authenticated, scoped to one organization,
  gated behind a $1,000/month plan, and reached through a private invitation link. Founded by MIT graduates Kali Abeje and Jity Woldemichael.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/osmaura.png
layout: provider
modified: '2026-08-14'
name: Osmaura
nav: Providers
network: true
overview: 'Osmaura publishes 1 API on the [APIs.io](https://apis.io/) network: Prospect API. Tagged areas include Company, Legal, LegalTech, Artificial Intelligence, and Sales Enablement.


  Osmaura''s developer surface includes authentication, signup flow, support, documentation, API reference, getting-started guide, pricing, and 14 more developer resources.'
plans:
- name: Osmaura Plans Pricing
  plan_count: 1
  slug: osmaura-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Osmaura Rate Limits
  slug: osmaura-rate-limits
score:
  band: thin
  composite: 41.9
  delta: 33.4
  facets:
    commercial_clarity: 44.7
    contract_quality: 49.3
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 8.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/osmaura/refs/heads/main/screenshots/osmaura-2026-08-07T191010.png
security:
- kind: authentication
  name: Osmaura Authentication
  slug: osmaura-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Osmaura Domain Security
  slug: osmaura-domain-security
  summary_line: TLSv1.3 · DMARC
slug: osmaura
tags:
- Company
- Legal
- LegalTech
- Artificial Intelligence
- Sales Enablement
- Business Development
- Y Combinator
- Market Intelligence
- Data
- Government Data
- Prospecting
website: https://osmaura.com
---
