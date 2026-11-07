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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/goalert/hosts/goalert-hosts.yml
  title: ''
  type: Hosts
  url: hosts/goalert-hosts.yml
- group: auth
  href: https://artifacts.apis.io/goalert/security/goalert-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goalert-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goalert.me/
- group: docs
  title: ''
  type: Documentation
  url: https://goalert.me/docs/
- group: operate
  title: ''
  type: Support
  url: https://goalert.me/contact/
coverage:
  checked: '2026-10-26'
  detail: Documentation at https://goalert.me/docs/ provides API information but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://goalert.me/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: GoAlert provides on‑call scheduling, automated escalations and notifications, helping teams engage the right person at the right time. The platform offers flexible alert routing, integration with monitoring tools, and a web UI for managing incidents and on‑call rotations. It aims to streamline incident response and improve reliability for engineering operations.
layout: provider
modified: '2026-10-26'
name: GoAlert
nav: Providers
network: true
overview: 'GoAlert is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include On-Call, Incident Management, Automation, Alerting, and Scheduling.


  GoAlert''s developer surface includes documentation, support, and 3 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 5.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/goalert/goalert-2026-11-03T132859.png
security:
- kind: domain-security
  name: Goalert Domain Security
  slug: goalert-domain-security
  summary_line: TLSv1.3 · DMARC
slug: goalert
tags:
- On-Call
- Incident Management
- Automation
- Alerting
- Scheduling
- Company
website: https://goalert.me/
---
