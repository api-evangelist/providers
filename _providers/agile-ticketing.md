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
- description: API for Agile Ticketing platform, documented at the Help Center. No machine‑readable OpenAPI spec was found.
  name: Agile Ticketing API
  slug: agile-ticketing-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/agile-ticketing/llms/agile-ticketing-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agile-ticketing-llms.txt
- group: other
  href: https://artifacts.apis.io/agile-ticketing/hosts/agile-ticketing-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agile-ticketing-hosts.yml
- group: other
  href: https://artifacts.apis.io/agile-ticketing/vendors/agile-ticketing-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agile-ticketing-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agiletix.com/privacy-statement
- group: start
  title: ''
  type: GettingStarted
  url: https://help.agiletix.com/en_US/agile-ticketing-solutions-begin-here/group-pay-setup-and-use
- group: docs
  title: ''
  type: Documentation
  url: https://help.agiletix.com/
- group: auth
  href: https://artifacts.apis.io/agile-ticketing/security/agile-ticketing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agile-ticketing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agiletix.com/
- group: operate
  title: ''
  type: Support
  url: https://support.agiletix.com/auth/v3/signin?brand_id=38784&locale=en-us&return_to=https%3A%2F%2Fsupport.agiletix.com%2Fhc%2Fen-us&role=end_user
- group: company
  title: ''
  type: Blog
  url: https://agiletix.com/blogs/
coverage:
  checked: '2026-10-27'
  detail: Help Center pages provide documentation but no OpenAPI spec was discovered despite probing known paths.
  evidence:
  - status: 200
    url: https://support.agiletix.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Agile Ticketing Solutions provides a cloud‑based ticketing platform for venues, events, and hospitality venues, enabling online ordering of food, drinks, memberships, passes, and donations. Their platform integrates with POS, supports kiosk ordering, and offers Zapier integration for workflow automation, aiming to boost per‑capita spend and improve guest experiences.
image: https://agiletix.com/wp-content/uploads/2026/07/belcourt-logo.png
layout: provider
modified: '2026-10-27'
name: Agile Ticketing
nav: Providers
network: true
overview: 'Agile Ticketing is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ticketing, Hospitality, Event, and Point-of-Sale.


  Agile Ticketing''s developer surface includes getting-started guide, documentation, support, engineering blog, and 6 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/agile-ticketing/agile-ticketing-2026-11-03T120419.png
security:
- kind: domain-security
  name: Agile Ticketing Domain Security
  slug: agile-ticketing-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agile-ticketing
tags:
- Company
- Ticketing
- Hospitality
- Event
- Point-of-Sale
website: https://agiletix.com/
---
