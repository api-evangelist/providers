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
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
asyncapis:
- description: ''
  name: Dashamail Ru Webhooks
  slug: dashamail-ru-webhooks
common:
- group: design
  href: https://artifacts.apis.io/dashamail-ru/asyncapi/dashamail-ru-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dashamail-ru-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/dashamail-ru/llms/dashamail-ru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dashamail-ru-llms.txt
- group: other
  href: https://artifacts.apis.io/dashamail-ru/hosts/dashamail-ru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dashamail-ru-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dashamail.ru/
- group: auth
  href: https://artifacts.apis.io/dashamail-ru/security/dashamail-ru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dashamail-ru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dashamail.ru/
coverage:
  checked: '2026-11-04'
  detail: Documentation is rendered via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.dashamail.ru/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: DashaMail is a Russian email‑marketing service offering a robust platform for sending newsletters, transactional messages, and automated campaigns. It provides a user‑friendly interface, a rich set of templates, a block editor, detailed analytics, and real‑time support via online chat. The service emphasizes ease of use, speed, and a variety of features such as segmentation, A/B testing, and integration with popular tools, catering to businesses seeking effective email outreach within Russia.
layout: provider
modified: '2026-11-04'
name: DashaMail
nav: Providers
network: true
overview: 'DashaMail is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, Marketing, Automation, and Russian.


  The DashaMail catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DashaMail''s developer surface includes documentation and 5 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 7.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dashamail Ru Domain Security
  slug: dashamail-ru-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dashamail-ru
tags:
- Company
- Email
- Marketing
- Automation
- Russian
website: https://dashamail.ru/
---
