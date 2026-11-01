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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/quicklogic/llms/quicklogic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quicklogic-llms.txt
- group: other
  href: https://artifacts.apis.io/quicklogic/hosts/quicklogic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quicklogic-hosts.yml
- group: other
  href: https://artifacts.apis.io/quicklogic/vendors/quicklogic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/quicklogic-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quicklogic.com/legal-notice/
- group: operate
  title: ''
  type: Support
  url: https://www.quicklogic.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quicklogic.com/privacy-policy/
- group: other
  title: ''
  type: Leadership
  url: https://www.quicklogic.com/company/management/
- group: docs
  title: ''
  type: Documentation
  url: https://www.quicklogic.com/support/documentation/
- group: company
  title: ''
  type: Blog
  url: https://www.quicklogic.com/company/blog/
- group: auth
  href: https://artifacts.apis.io/quicklogic/security/quicklogic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quicklogic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quicklogic.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.quicklogic.com/
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: QuickLogic provides purpose‑built eFPGA IP, specialized FPGA devices, and associated user tools. It offers custom FPGA devices, rad‑hard eFPGA IP, and FPGA chiplets for aerospace, defense, critical infrastructure, and edge IoT/AI‑ML applications.
image: https://www.quicklogic.com/wp-content/uploads/2025/11/OpenGraph-Thumbs-homepage.jpg
layout: provider
modified: '2026-10-23'
name: QuickLogic
nav: Providers
network: true
overview: 'QuickLogic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include eFPGA, FPGA, Semiconductor, Custom FPGA, and Rad‑Hard.


  QuickLogic''s developer surface includes support, documentation, engineering blog, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Quicklogic Domain Security
  slug: quicklogic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quicklogic
tags:
- eFPGA
- FPGA
- Semiconductor
- Custom FPGA
- Rad‑Hard
- Chiplets
- Security
- Development Boards
website: https://www.quicklogic.com/
---
