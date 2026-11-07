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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
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
  score: 36.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Scheduling API. Public operations let anyone, including AI assistants, look up open times and book a meeting.
  name: Tempi API
  slug: tempi-api
- baseURL: https://meettempi.com
  baseurl_source: declared
  description: 'Scheduling API. Public operations let anyone, including AI assistants, look up open times and book a meeting. Account operations need an API key (`Authorization: Bearer bk_...`) from Settings → API ke'
  name: Tempi API API
  slug: tempi-api-api
artifact_total: 6
asyncapis:
- description: ''
  name: Meettempi Com Webhooks
  slug: meettempi-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/meettempi-com/rules/meettempi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/meettempi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/meettempi-com/json-ld/meettempi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/meettempi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/meettempi-com/vocabulary/meettempi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/meettempi-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/meettempi-com/asyncapi/meettempi-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/meettempi-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/meettempi-com/data-model/meettempi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/meettempi-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/meettempi-com/changelog/meettempi-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/meettempi-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/meettempi-com/errors/meettempi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/meettempi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/meettempi-com/conformance/meettempi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/meettempi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/meettempi-com/llms/meettempi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/meettempi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/meettempi-com/well-known/meettempi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/meettempi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/meettempi-com/hosts/meettempi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meettempi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/meettempi-com/vendors/meettempi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/meettempi-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://meettempi.com/features/webhooks
- group: start
  title: ''
  type: Login
  url: https://meettempi.com/login
- group: docs
  title: ''
  type: APIReference
  url: https://meettempi.com/changelog
- group: auth
  href: https://artifacts.apis.io/meettempi-com/security/meettempi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meettempi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meettempi.com/
- group: operate
  title: ''
  type: Support
  url: https://meettempi.com/
- group: company
  title: ''
  type: Blog
  url: https://meettempi.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://meettempi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://meettempi.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.meettempi.com
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://meettempi.com/mcp
  - status: 200
    url: https://meettempi.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: MeetTempi offers a scheduling link platform that lets teams and AI assistants create shareable booking links, integrating with Google, Outlook, and iCloud calendars. Users can book meetings directly or via AI assistants through MCP, supporting recurring meetings and round‑robin scheduling. The service streamlines coordination by syncing booked times to calendars and provides a public API for developers to embed scheduling functionality into their applications, enhancing productivity for both human teams and AI assistants.
image: https://meettempi.com/og.png
jsonld:
- class_count: 1
  name: Meettempi Com Context
  property_count: 1
  slug: meettempi-com-context
layout: provider
modified: '2026-10-30'
name: meettempi-com
nav: Providers
network: true
overview: 'meettempi-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Tempi API API, and 1 more. Tagged areas include Company, Scheduling, Artificial Intelligence, Calendar, and Collaboration.


  The meettempi-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  meettempi-com''s developer surface includes changelog, API reference, support, engineering blog, and 18 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: meettempi-com API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: meettempi-com-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 45.5
    developer_ergonomics: 7.1
    discoverability: 73.2
    operational_transparency: 27.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 36.6
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/meettempi-com/meettempi-com-2026-11-03T135436.png
security:
- kind: domain-security
  name: Meettempi Com Domain Security
  slug: meettempi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: meettempi-com
tags:
- Company
- Scheduling
- Artificial Intelligence
- Calendar
- Collaboration
website: https://meettempi.com/
---
