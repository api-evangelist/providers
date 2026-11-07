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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The Enage API from Blub0x — 1 operation(s) for enage.
  name: Blub0x Enage API
  slug: blub0x-enage-api
- description: The Engage API from Blub0x — 10 operation(s) for engage.
  name: Blub0x Engage API
  slug: blub0x-engage-api
artifact_total: 5
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://knowledge.blub0x.com/MSRP_Pricing
- group: commercial
  href: https://artifacts.apis.io/blub0x/plans/blub0x-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blub0x-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.blub0x.com/feed/
- group: design
  href: https://artifacts.apis.io/blub0x/rules/blub0x-rules.yml
  title: ''
  type: Spectral
  url: rules/blub0x-rules.yml
- group: design
  href: https://artifacts.apis.io/blub0x/conformance/blub0x-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blub0x-conformance.yml
- group: other
  href: https://artifacts.apis.io/blub0x/hosts/blub0x-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blub0x-hosts.yml
- group: other
  href: https://artifacts.apis.io/blub0x/vendors/blub0x-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blub0x-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.blub0x.com/news/blubox-oracle/
- group: start
  title: ''
  type: GettingStarted
  url: https://bluinfo.z13.web.core.windows.net/AI_Generated_Docs/Setup/
- group: auth
  href: https://artifacts.apis.io/blub0x/security/blub0x-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blub0x-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blub0x.com
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge.blub0x.com
- group: docs
  title: ''
  type: APIReference
  url: https://knowledge.blub0x.com/Web_API
- group: operate
  title: ''
  type: Support
  url: https://www.blub0x.com/contact-blubox/
- group: company
  title: ''
  type: Blog
  url: https://knowledge.blub0x.com/Media/Blog/
coverage:
  checked: '2026-09-29'
  detail: Documentation pages are rendered via Docusaurus JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://knowledge.blub0x.com/Web_API
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-29'
description: BluBØX manufactures and services physical security products, offering the BluSKY platform—a patented, AI‑powered, cloud‑based security solution for residential, SMB and enterprise customers. The company provides hardware such as access control readers, video intercoms, elevator management systems, and related software services.
layout: provider
modified: '2026-10-06'
name: Blub0x
nav: Providers
network: true
overview: 'Blub0x is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Enage API and Engage API. Tagged areas include Physical Security, Cloud Security, Access Control, Elevator Management, and Artificial Intelligence.


  The Blub0x catalog on APIs.io includes 1 Spectral governance ruleset.


  Blub0x''s developer surface includes pricing, getting-started guide, documentation, API reference, support, engineering blog, and 9 more developer resources.'
plans:
- name: Blub0X Plans Pricing
  plan_count: 15
  slug: blub0x-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Blub0x API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: blub0x-rules
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 46.5
    catalog_earned_first_party: 12.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 9.4
    developer_ergonomics: 17.9
    discoverability: 54.5
    operational_transparency: 0.0
  previous_composite: 24.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/blub0x/blub0x-2026-10-11T102455.png
security:
- kind: domain-security
  name: Blub0X Domain Security
  slug: blub0x-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blub0x
tags:
- Physical Security
- Cloud Security
- Access Control
- Elevator Management
- Artificial Intelligence
website: https://www.blub0x.com
---
