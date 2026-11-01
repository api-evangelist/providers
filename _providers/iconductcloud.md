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
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/iconductcloud/plans/iconductcloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iconductcloud-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/iconductcloud/changelog/iconductcloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/iconductcloud-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://iconductcloud.com/security/
- group: agent
  href: https://artifacts.apis.io/iconductcloud/llms/iconductcloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iconductcloud-llms.txt
- group: other
  href: https://artifacts.apis.io/iconductcloud/hosts/iconductcloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iconductcloud-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://iconductcloud.com/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://iconductcloud.com/release-notes/
- group: auth
  href: https://artifacts.apis.io/iconductcloud/security/iconductcloud-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/iconductcloud-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/iconductcloud/security/iconductcloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iconductcloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iconductcloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://iconductcloud.com/how-it-works/
- group: start
  title: ''
  type: GettingStarted
  url: https://iconductcloud.com/why-iconduct/
- group: operate
  title: ''
  type: Support
  url: https://iconductcloud.com/support/
- group: company
  title: ''
  type: Blog
  url: https://iconductcloud.com/articles/
- group: commercial
  title: ''
  type: Pricing
  url: https://iconductcloud.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://iconductcloud.com/contact-us/
coverage:
  checked: '2026-10-20'
  detail: The API reference page https://iconductcloud.com/api-docs/ returns an error and appears to be a JavaScript‑rendered portal with no machine‑readable spec.
  evidence:
  - status: error
    url: https://iconductcloud.com/api-docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: IConduct Ltd provides an integration platform that connects enterprise systems, enabling seamless data flow and operational orchestration. Based in Israel, Iconductcloud offers connectors across various applications, robust security, and tools for developers to build and manage integrations. The platform supports complex enterprise organizations, delivering stable integration infrastructure essential for AI-driven initiatives and digital transformation.
image: http://iconductcloud.com/wp-content/uploads/2023/05/Wilcalaf_a_hyper_realistic_technological_world_map_16e1cd9d-28ed-4fef-9c63-15a4a83089d1-600x800.png
layout: provider
modified: '2026-10-20'
name: IConduct Ltd
nav: Providers
network: true
overview: 'IConduct Ltd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, Platform, Enterprise, Israel, and API.


  IConduct Ltd''s developer surface includes changelog, documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Iconductcloud Plans Pricing
  plan_count: 9
  slug: iconductcloud-plans-pricing
random_paper: 0
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Iconductcloud Domain Security
  slug: iconductcloud-domain-security
  summary_line: TLSv1.3
- kind: trust-center
  name: Iconductcloud Trust Center
  slug: iconductcloud-trust-center
  summary_line: SOC 2, ISO 27001
slug: iconductcloud
tags:
- Integration
- Platform
- Enterprise
- Israel
- API
website: https://iconductcloud.com/
---
