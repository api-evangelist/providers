---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.town.com
- group: start
  title: ''
  type: SignUp
  url: https://www.town.com/sign-up
- group: auth
  title: ''
  type: TrustCenter
  url: security/town-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/town-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/town-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/town-robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/town-llms.txt
created: '2026-07-17'
description: 'Town is a personal AI assistant that works across email, calendar, Slack, docs, WhatsApp, and the web. Users connect their accounts and Town — through a personal agent called a "Townie" — learns how they work, then suggests and runs automated "routines" (meeting briefs, email drafting, follow-ups, scheduling) on their behalf. Founded by Jean-Denis Greze (former Plaid CTO) and Tony Vincent (former Google product/AI lead), Town raised a $55M Series A led by Andreessen Horowitz (June 2026) with Forerunner Ventures, First Round, Alt Capital, and Conviction participating. Town publishes no public developer program: the product is fully auth-gated, api.town.com is a Convex backend deployment rather than a public API, and its robots.txt carries explicit Content-Signal declarations restricting AI training on its content.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/town.png
layout: provider
modified: '2026-07-21'
name: Town
nav: Providers
network: true
overview: 'Town is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agents, Personal Assistant, and Productivity.


  Town''s developer surface includes signup flow and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 11.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Town Domain Security
  slug: town-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Town Trust Center
  slug: town-trust-center
  summary_line: trust center published
slug: town
tags:
- Company
- Artificial Intelligence
- Agents
- Personal Assistant
- Productivity
- Email
- Calendar
- Automation
website: https://www.town.com
---
