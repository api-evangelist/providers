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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/downtester-com/plans/downtester-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/downtester-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/downtester-com/hosts/downtester-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/downtester-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/downtester-com/vendors/downtester-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/downtester-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.downtester.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.downtester.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.downtester.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.downtester.com/login
- group: auth
  href: https://artifacts.apis.io/downtester-com/security/downtester-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/downtester-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://downtester.com/
coverage:
  checked: '2026-11-06'
  detail: Documentation pages are JavaScript-rendered single-page apps with no machine-readable spec.
  evidence:
  - status: 200
    url: https://www.downtester.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: 'downtester-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-11-05'
name: downtester-com
nav: Providers
network: true
overview: 'downtester-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  downtester-com''s developer surface includes pricing and 8 more developer resources.'
plans:
- name: Downtester Com Plans Pricing
  plan_count: 3
  slug: downtester-com-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 12.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Downtester Com Domain Security
  slug: downtester-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: downtester-com
tags:
- Company
website: https://downtester.com/
---
