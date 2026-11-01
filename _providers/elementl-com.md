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
    mcp_server: documented
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/elementl-com/plans/elementl-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elementl-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/elementl-com/llms/elementl-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elementl-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/elementl-com/well-known/elementl-com-dagstercloud-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/elementl-com-dagstercloud-security.txt
- group: agent
  href: https://artifacts.apis.io/elementl-com/well-known/elementl-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elementl-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/elementl-com/hosts/elementl-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/elementl-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/elementl-com/vendors/elementl-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/elementl-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dagster.io/terms
- group: operate
  title: ''
  type: Support
  url: https://dagster.io/support
- group: operate
  title: ''
  type: StatusPage
  url: https://dagstercloud.statuspage.io
- group: auth
  title: ''
  type: Security
  url: https://dagster.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dagster.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dagster.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://dagster.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://dagster.io/learn/azure-data-catalog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dagster.io/
- group: auth
  href: https://artifacts.apis.io/elementl-com/security/elementl-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elementl-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dagster.io
coverage:
  checked: '2026-10-26'
  detail: Documentation pages are rendered client‑side JavaScript, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://dagster.io/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Elementl builds Dagster, an open-source data orchestrator that helps engineers develop, test, and monitor reliable data pipelines. The platform provides a modern UI, robust scheduling, and integrations with many data tools, enabling teams to orchestrate complex workflows at scale.
layout: provider
modified: '2026-10-25'
name: Elementl
nav: Providers
network: true
overview: 'Elementl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Orchestration, Open Source, Workflow Automation, and Python.


  Elementl''s developer surface includes support, pricing, engineering blog, getting-started guide, documentation, and 12 more developer resources.'
plans:
- name: Elementl Com Plans Pricing
  plan_count: 3
  slug: elementl-com-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 26.3
  provenance:
    mcp: unknown
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
  name: Elementl Com Domain Security
  slug: elementl-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: elementl-com
tags:
- Company
- Data Orchestration
- Open Source
- Workflow Automation
- Python
website: https://dagster.io
---
