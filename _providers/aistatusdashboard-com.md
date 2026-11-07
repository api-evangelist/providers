---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides status data for AI services as described on the How it works page. No public machine‑readable contract was found.
  name: AI Status API
  slug: ai-status-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/aistatusdashboard-com/llms/aistatusdashboard-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aistatusdashboard-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aistatusdashboard-com/hosts/aistatusdashboard-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aistatusdashboard-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aistatusdashboard.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aistatusdashboard.com/privacy
- group: auth
  href: https://artifacts.apis.io/aistatusdashboard-com/security/aistatusdashboard-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aistatusdashboard-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aistatusdashboard.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aistatusdashboard.com/how-it-works
- group: start
  title: ''
  type: GettingStarted
  url: https://aistatusdashboard.com/how-it-works
- group: operate
  title: ''
  type: StatusPage
  url: https://aistatusdashboard.com/
coverage:
  checked: '2026-11-01'
  detail: Docs page is a Next.js rendered HTML with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://aistatusdashboard.com/how-it-works
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AI Status provides a real‑time status dashboard for popular AI services such as ChatGPT, Claude, Gemini, and many others. It aggregates outage reports, reliability metrics, and alerts, presenting them in a clear, user‑friendly interface. The platform helps developers and businesses monitor AI service health, receive notifications, and understand incident histories, enabling proactive response to downtime.
image: https://aistatusdashboard.com/og/home
layout: provider
modified: '2026-11-01'
name: AI Status
nav: Providers
network: true
overview: 'AI Status is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Status, Monitoring, Dashboards, and Services.


  AI Status'' developer surface includes documentation, getting-started guide, and 7 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 15.9
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aistatusdashboard Com Domain Security
  slug: aistatusdashboard-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aistatusdashboard-com
tags:
- Artificial Intelligence
- Status
- Monitoring
- Dashboards
- Services
website: https://aistatusdashboard.com/
---
