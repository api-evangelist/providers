---
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/lumber/llms/lumber-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lumber-llms.txt
- group: other
  href: https://artifacts.apis.io/lumber/hosts/lumber-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lumber-hosts.yml
- group: other
  href: https://artifacts.apis.io/lumber/vendors/lumber-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lumber-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lumberfi.com/tos
- group: operate
  title: ''
  type: StatusPage
  url: https://www.lumberfi.com/status
- group: auth
  title: ''
  type: Security
  url: https://www.lumberfi.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lumberfi.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.lumberfi.com/newsroom
- group: auth
  href: https://artifacts.apis.io/lumber/security/lumber-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lumber-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lumberfi.com/
- group: company
  title: ''
  type: Blog
  url: https://www.lumberfi.com/blog
- group: company
  title: ''
  type: Blog
  url: https://www.lumberfi.com/blog
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://lumberfi.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Lumber provides AI‑powered construction payroll and workforce management software, helping construction companies automate payroll, HR, benefits, compliance, and field operations. Their platform integrates with over 20 ERP, payroll, and HR applications, offering features like flexible pay cycles, certified payroll, union reporting, expense management, and real‑time job costing. Lumber aims to streamline finance and operations for the construction industry.
image: https://cdn.prod.website-files.com/64ba4b61a6e0ed8004b57d97/66e2e0cdd425738b241d6d98_Open%20Graph.png
layout: provider
modified: '2026-10-28'
name: Lumber
nav: Providers
network: true
overview: 'Lumber is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Payroll, Workforce Management, and SaaS.


  Lumber''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lumber Domain Security
  slug: lumber-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lumber
tags:
- Company
- Construction
- Payroll
- Workforce Management
- SaaS
website: https://lumberfi.com/
---
