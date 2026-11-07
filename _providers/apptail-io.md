---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
- description: AppTail provides mobile app analytics, market intelligence, and ASO tools. Documentation is at https://apptail.io/
  name: AppTail API
  slug: apptail-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/apptail-io/plans/apptail-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apptail-io-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/apptail-io/hosts/apptail-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apptail-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/apptail-io/vendors/apptail-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apptail-io-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.apptail.io/signup
- group: auth
  href: https://artifacts.apis.io/apptail-io/security/apptail-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apptail-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apptail.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://apptail.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apptail.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apptail.io/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://apptail.io/support
coverage:
  checked: '2026-11-01'
  detail: Docs pages render via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://apptail.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AppTail provides mobile app analytics, market intelligence, and ASO tools to help developers and marketers understand app performance, track competitor metrics, and optimize app store visibility. The platform offers comprehensive dashboards, AI‑generated recommendations, and real‑time data on downloads, revenue, and user engagement across iOS and Android ecosystems.
image: https://apptail.io/img/oglogo.png
layout: provider
modified: '2026-11-01'
name: AppTail
nav: Providers
network: true
overview: 'AppTail is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mobile, Analytics, ASO, Market Intelligence, and Platform.


  AppTail''s developer surface includes signup flow, pricing, support, and 7 more developer resources.'
plans:
- name: Apptail Io Plans Pricing
  plan_count: 3
  slug: apptail-io-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 21.7
  provenance:
    mcp: derived
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
security:
- kind: domain-security
  name: Apptail Io Domain Security
  slug: apptail-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apptail-io
tags:
- Mobile
- Analytics
- ASO
- Market Intelligence
- Platform
website: https://apptail.io/
---
