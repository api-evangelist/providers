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
api_count: 1
apis:
- description: Rediem API documentation
  name: Rediem API
  slug: rediem-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/rediem/llms/rediem-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rediem-llms.txt
- group: auth
  href: https://artifacts.apis.io/rediem/well-known/rediem-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rediem-help-security.txt
- group: agent
  href: https://artifacts.apis.io/rediem/well-known/rediem-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rediem-well-known.yml
- group: other
  href: https://artifacts.apis.io/rediem/hosts/rediem-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rediem-hosts.yml
- group: other
  href: https://artifacts.apis.io/rediem/vendors/rediem-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rediem-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.rediem.co/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.rediem.co/en/articles/15089776-getting-started-loyalty-program-marketing-comms-strategy
- group: docs
  title: ''
  type: Documentation
  url: https://help.rediem.co/
- group: auth
  href: https://artifacts.apis.io/rediem/security/rediem-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rediem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rediem.co/
- group: company
  title: ''
  type: Blog
  url: https://www.rediem.co/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rediem.co/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rediem.co/terms-of-service
coverage:
  checked: '2026-10-29'
  detail: Help site pages require JavaScript rendering; curl and simple GETs return bot-protection shells, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://help.rediem.co/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Rediem is a community loyalty platform that enables brands to build personalized, omnichannel loyalty programs. It offers tools for zero‑party data collection, AI receipt scanning, quizzes, polls, surveys, and gamified experiences to deepen customer relationships. The no‑code builder lets teams launch and adapt programs without developer bottlenecks, while impact dashboards showcase social and environmental contributions. Rediem aims to transform loyalty from point‑based systems into community‑driven engagement, supporting brands in retaining customers and driving sustainable growth.
layout: provider
modified: '2026-10-29'
name: Rediem
nav: Providers
network: true
overview: 'Rediem is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Loyalty, Community, Marketing, and No-Code.


  Rediem''s developer surface includes support, getting-started guide, documentation, engineering blog, and 9 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 60.7
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rediem/rediem-2026-11-03T142102.png
security:
- kind: domain-security
  name: Rediem Domain Security
  slug: rediem-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rediem
tags:
- Company
- Loyalty
- Community
- Marketing
- No-Code
website: https://www.rediem.co/
---
