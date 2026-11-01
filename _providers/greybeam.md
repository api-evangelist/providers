---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
  score: 6.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Greybeam provides Snowflake cost optimization powered by DuckDB, routing eligible queries to DuckDB while keeping others on Snowflake.
  name: Greybeam API
  slug: greybeam-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/greybeam/plans/greybeam-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/greybeam-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/greybeam/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/greybeam/llms/greybeam-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/greybeam-llms.txt
- group: other
  href: https://artifacts.apis.io/greybeam/hosts/greybeam-hosts.yml
  title: ''
  type: Hosts
  url: hosts/greybeam-hosts.yml
- group: other
  href: https://artifacts.apis.io/greybeam/vendors/greybeam-vendors.yml
  title: ''
  type: Vendors
  url: vendors/greybeam-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.greybeam.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.greybeam.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.greybeam.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.greybeam.ai/blog
- group: auth
  href: https://artifacts.apis.io/greybeam/security/greybeam-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/greybeam-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.greybeam.ai/
coverage:
  checked: '2026-10-29'
  detail: The provider's website returns a JavaScript shell with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.greybeam.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Greybeam provides Snowflake cost optimization powered by DuckDB, routing eligible queries to DuckDB while keeping others on Snowflake. It claims to reduce compute costs by up to 86% on average without requiring data migration, offering a seamless integration for BI tools and data teams. Founded in 2024 in San Francisco, the company focuses on query routing, Apache Iceberg support, and improving overall data warehouse efficiency.
image: https://www.greybeam.ai/assets/greybeam_preview_img.png
layout: provider
modified: '2026-10-29'
name: Greybeam
nav: Providers
network: true
overview: 'Greybeam is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Snowflake, DuckDB, Cost Optimization, and Data Engineering.


  Greybeam''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Greybeam Plans Pricing
  plan_count: 5
  slug: greybeam-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
    skills: unknown
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
  name: Greybeam Domain Security
  slug: greybeam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: greybeam
tags:
- Company
- Snowflake
- DuckDB
- Cost Optimization
- Data Engineering
website: https://www.greybeam.ai/
---
