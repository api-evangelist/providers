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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://intellova.com.au/dicta/pricing
- group: agent
  href: https://artifacts.apis.io/intellova/llms/intellova-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/intellova-llms.txt
- group: other
  href: https://artifacts.apis.io/intellova/hosts/intellova-hosts.yml
  title: ''
  type: Hosts
  url: hosts/intellova-hosts.yml
- group: other
  href: https://artifacts.apis.io/intellova/vendors/intellova-vendors.yml
  title: ''
  type: Vendors
  url: vendors/intellova-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://intellova.com.au/blog/tag/security
- group: auth
  href: https://artifacts.apis.io/intellova/security/intellova-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intellova-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://intellova.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.intellova.com.au/
- group: operate
  title: ''
  type: Support
  url: https://www.intellova.com.au/support/
- group: company
  title: ''
  type: Blog
  url: https://www.intellova.com.au/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.intellova.com.au/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.intellova.com.au/privacy/
coverage:
  checked: '2026-10-18'
  detail: Intellova's website and portal provide no public developer documentation or API reference.
  evidence:
  - status: 200
    url: https://www.intellova.com.au/
  reason: no-developer-program
  state: none
created: '2026-10-17'
description: Intellova provides data integration and automation solutions for Australian businesses, connecting CRMs, accounting tools, and other applications into a unified, analytics‑ready database hosted on AWS. Their platform supports AI insights, privacy‑compliant storage, and a range of services including data unification, reporting, and custom dashboards, aimed at streamlining decision‑making across enterprises.
image: https://intellova.com.au/opengraph-image?091bb3684a23439f
layout: provider
modified: '2026-10-17'
name: Intellova
nav: Providers
network: true
overview: 'Intellova is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Integration, Automation, Australian Business, and Cloud Services.


  Intellova''s developer surface includes pricing, support, engineering blog, and 9 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 10.5
  previous_composite: 15.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Intellova Domain Security
  slug: intellova-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: intellova
tags:
- Company
- Data Integration
- Automation
- Australian Business
- Cloud Services
website: https://intellova.com.au/
---
