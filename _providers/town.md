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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: true
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
  score: 2.2
  scored_at: '2026-09-02'
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
random_paper: 15
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/town/refs/heads/main/screenshots/town-2026-09-02T164005.png
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
