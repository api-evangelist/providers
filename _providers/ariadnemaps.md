---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: People counting API providing occupancy monitoring and analytics.
  name: Ariadnemaps API
  slug: ariadnemaps-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ariadnemaps/refs/heads/main/plans/ariadnemaps-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ariadnemaps-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ariadnemaps/refs/heads/main/llms/ariadnemaps-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ariadnemaps-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ariadnemaps/refs/heads/main/hosts/ariadnemaps-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ariadnemaps-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ariadnemaps/refs/heads/main/vendors/ariadnemaps-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ariadnemaps-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ariadne.inc/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ariadne.inc/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ariadne.inc/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.ariadne.inc/login
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ariadne.inc/get-started/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ariadnemaps/refs/heads/main/security/ariadnemaps-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ariadnemaps-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ariadne.inc
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/ariadnemaps
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Ariadnemaps provides a privacy‑first people counting platform that uses hybrid fusion of phone‑signal sensing and time‑of‑flight depth sensors to deliver sub‑meter accuracy without cameras or personal data. The solution offers real‑time occupancy monitoring, queue management, and visitor flow analytics for venues such as retail stores, airports, and smart cities, complying with GDPR and EU AI Act requirements.
image: https://www.ariadne.inc/og/default.png
layout: provider
modified: '2026-09-26'
name: Ariadnemaps
nav: Providers
network: true
overview: 'Ariadnemaps publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, People Counting, PrivacyFirst, IoT, and Analytics.


  Ariadnemaps'' developer surface includes pricing, getting-started guide, and 9 more developer resources.'
plans:
- name: Ariadnemaps Plans Pricing
  plan_count: 1
  slug: ariadnemaps-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.3
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ariadnemaps Domain Security
  slug: ariadnemaps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ariadnemaps
tags:
- Company
- People Counting
- PrivacyFirst
- IoT
- Analytics
website: https://www.ariadne.inc
---
