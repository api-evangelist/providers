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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/sesamesoftware/llms/sesamesoftware-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sesamesoftware-llms.txt
- group: other
  href: https://artifacts.apis.io/sesamesoftware/hosts/sesamesoftware-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sesamesoftware-hosts.yml
- group: other
  href: https://artifacts.apis.io/sesamesoftware/vendors/sesamesoftware-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sesamesoftware-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.sesamesoftware.com/blog
- group: auth
  href: https://artifacts.apis.io/sesamesoftware/security/sesamesoftware-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sesamesoftware-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sesamesoftware.com/
coverage:
  checked: '2026-10-21'
  detail: The website is built on Wix and renders content via JavaScript, preventing machine‑readable API specifications from being discovered.
  evidence:
  - status: 301
    url: https://www.sesamesoftware.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Sesame Software provides data management tools that back up, replicate, migrate, and integrate data from Salesforce, NetSuite, Oracle, Microsoft Dynamics and over 20 other endpoints into a customer‑owned database. It serves enterprises that need to automate data movement, ensure compliance, and maintain control over where their data resides.
image: https://static.wixstatic.com/media/ed693f_15162d894b17444980615f07d667be82~mv2.png/v1/fill/w_1200,h_630,al_c/ed693f_15162d894b17444980615f07d667be82~mv2.png
layout: provider
modified: '2026-10-21'
name: Sesame Software
nav: Providers
network: true
overview: 'Sesame Software is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data Backup, Data Replication, Data Migration, Data Integration, and Enterprise Data Management.


  Sesame Software''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sesamesoftware/sesamesoftware-2026-11-03T143057.png
security:
- kind: domain-security
  name: Sesamesoftware Domain Security
  slug: sesamesoftware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sesamesoftware
tags:
- Data Backup
- Data Replication
- Data Migration
- Data Integration
- Enterprise Data Management
- Salesforce
- NetSuite
website: https://sesamesoftware.com/
---
