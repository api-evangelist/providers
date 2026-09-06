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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taskhuman-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://taskhuman.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/taskhuman-lifecycle.yml
coverage:
  checked: '2026-08-29'
  detail: 'TaskHuman ceased operations and locked its own site down: every path on taskhuman.com now returns HTTP 401 behind an nginx HTTP Basic auth wall (realm "taskhuman2pro"), the API hosts recorded in certificate transparency (api.taskhuman.com, api.prod.taskhuman.com) no longer resolve, app.taskhuman.com and admin.taskhuman.com are dangling CNAMEs at deleted AWS endpoints, and status.taskhuman.com redirects to Atlassian''s unclaimed-Statuspage landing page.'
  evidence:
  - status: 401
    url: https://taskhuman.com/
  - status: 401
    url: https://taskhuman.com/robots.txt
  - status: 0
    url: https://api.taskhuman.com/
  - status: 200
    url: https://resources.taskhuman.com/
  reason: defunct
  state: none
created: '2026-08-29'
description: TaskHuman was a mobile-first, on-demand human coaching platform that connected employees with live 1:1 video coaching across wellbeing, fitness, leadership, professional growth, sales and mentorship topics, sold to employers as a benefit and delivered through iOS, Android and web apps plus Slack and Microsoft Teams integrations. The San Francisco Bay Area company raised roughly $35M from investors including U.S. Venture Partners and Madrona and marketed a coach network spanning more than a thousand skill areas. The company ceased operations in 2026; as of this profile the entire taskhuman.com origin answers HTTP 401 behind an nginx HTTP Basic authentication wall and the product's API and application hosts no longer resolve, so no developer program, documentation or machine-readable contract remains reachable.
layout: provider
modified: '2026-08-29'
name: TaskHuman
nav: Providers
network: true
overview: TaskHuman is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Coaching, Human Resources, Employee Benefits, and Wellbeing.
random_paper: 6
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Taskhuman Domain Security
  slug: taskhuman-domain-security
  summary_line: TLSv1.3 · DMARC
slug: taskhuman
tags:
- Company
- Coaching
- Human Resources
- Employee Benefits
- Wellbeing
- Learning and Development
- Video
- Defunct
website: https://taskhuman.com/
---
