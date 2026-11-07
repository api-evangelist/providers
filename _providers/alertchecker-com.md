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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/alertchecker-com/well-known/alertchecker-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alertchecker-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/alertchecker-com/hosts/alertchecker-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alertchecker-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/alertchecker-com/vendors/alertchecker-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alertchecker-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alertchecker.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alertchecker.com/privacy
- group: auth
  href: https://artifacts.apis.io/alertchecker-com/security/alertchecker-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alertchecker-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alertchecker.com/
- group: company
  title: ''
  type: Blog
  url: https://alertchecker.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://alertchecker.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://alertchecker.com/help
- group: operate
  title: ''
  type: Contact
  url: https://alertchecker.com/contact
coverage:
  checked: '2026-11-01'
  detail: No public API or documentation found; attempts to locate OpenAPI, GraphQL, or docs returned 404 pages.
  evidence:
  - status: 404
    url: https://alertchecker.com/redoc
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: AlertChecker is a web‑based service that lets users ask a simple yes/no question or describe a condition in natural language. It continuously monitors relevant public web information and notifies users by email or browser push when the answer changes to “yes”. Launched in September 2025, the platform supports natural‑language condition monitoring, public‑web data tracking, and multi‑channel alerts.
image: https://alertchecker.com/logo-icon.png
layout: provider
modified: '2026-11-01'
name: AlertChecker
nav: Providers
network: true
overview: 'AlertChecker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Monitoring, Notification, Natural-Language, Web, and Alerts.


  AlertChecker''s developer surface includes engineering blog, pricing, support, and 8 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 13.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alertchecker Com Domain Security
  slug: alertchecker-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alertchecker-com
tags:
- Monitoring
- Notification
- Natural-Language
- Web
- Alerts
website: https://alertchecker.com/
---
