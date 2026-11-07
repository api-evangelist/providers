---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/linxup/plans/linxup-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/linxup-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/linxup/llms/linxup-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/linxup-llms.txt
- group: other
  href: https://artifacts.apis.io/linxup/hosts/linxup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/linxup-hosts.yml
- group: other
  href: https://artifacts.apis.io/linxup/vendors/linxup-vendors.yml
  title: ''
  type: Vendors
  url: vendors/linxup-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linxup.com/about/terms
- group: operate
  title: ''
  type: Support
  url: https://www.linxup.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linxup.com/about/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.linxup.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.linxup.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.linxup.com/blog
- group: auth
  href: https://artifacts.apis.io/linxup/security/linxup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/linxup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://linxup.com/
coverage:
  checked: '2026-10-28'
  detail: The website provides only marketing pages and no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://www.linxup.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Linxup provides GPS fleet tracking, dash cam solutions, and asset management tools for businesses. Their platform offers real‑time vehicle location, driver safety monitoring, equipment tracking, and compliance reporting, helping companies improve operational efficiency and reduce costs. The service includes a web portal and mobile apps for fleet managers to activate devices, view dashboards, and integrate with third‑party systems.
image: https://www.linxup.com/site/templates/images/og-default.jpg
layout: provider
modified: '2026-10-28'
name: Linxup
nav: Providers
network: true
overview: 'Linxup is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include GPS, Fleet Tracking, Dash Cams, Asset Management, and Transportation.


  Linxup''s developer surface includes support, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Linxup Plans Pricing
  plan_count: 4
  slug: linxup-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 56.3
    operational_transparency: 0.0
  previous_composite: 19.6
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/linxup/linxup-2026-11-03T134921.png
security:
- kind: domain-security
  name: Linxup Domain Security
  slug: linxup-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: linxup
tags:
- GPS
- Fleet Tracking
- Dash Cams
- Asset Management
- Transportation
website: https://linxup.com/
---
