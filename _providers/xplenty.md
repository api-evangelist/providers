---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API reference for Integrate.io data integration platform.
  name: Integrate.io API
  slug: integrate-io-api
- description: 'Integrate.io API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: Integrate.io API
  slug: xplenty-api
artifact_total: 7
asyncapis:
- description: ''
  name: Xplenty Webhooks
  slug: xplenty-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/xplenty/plans/xplenty-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/xplenty-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/xplenty/rules/xplenty-rules.yml
  title: ''
  type: Spectral
  url: rules/xplenty-rules.yml
- group: design
  href: https://artifacts.apis.io/xplenty/vocabulary/xplenty-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/xplenty-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/xplenty/asyncapi/xplenty-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/xplenty-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/xplenty/authentication/xplenty-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xplenty-authentication.yml
- group: design
  href: https://artifacts.apis.io/xplenty/conformance/xplenty-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xplenty-conformance.yml
- group: agent
  href: https://artifacts.apis.io/xplenty/llms/xplenty-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xplenty-llms.txt
- group: auth
  href: https://artifacts.apis.io/xplenty/well-known/xplenty-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/xplenty-status-security.txt
- group: agent
  href: https://artifacts.apis.io/xplenty/well-known/xplenty-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xplenty-well-known.yml
- group: other
  href: https://artifacts.apis.io/xplenty/hosts/xplenty-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xplenty-hosts.yml
- group: other
  href: https://artifacts.apis.io/xplenty/vendors/xplenty-vendors.yml
  title: ''
  type: Vendors
  url: vendors/xplenty-vendors.yml
- group: build
  href: https://artifacts.apis.io/xplenty/packages/xplenty-packages.yml
  title: ''
  type: SDKs
  url: packages/xplenty-packages.yml
- group: build
  href: https://artifacts.apis.io/xplenty/packages/xplenty-packages.yml
  title: ''
  type: Packages
  url: packages/xplenty-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.integrate.io/terms/
- group: operate
  title: ''
  type: Support
  url: https://www.integrate.io/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.xplenty.com/
- group: auth
  title: ''
  type: Security
  url: https://www.integrate.io/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.integrate.io/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.integrate.io/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://www.integrate.io/docs/
- group: company
  title: ''
  type: Blog
  url: https://www.integrate.io/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.integrate.io/docs/etl/category/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xplenty
- group: auth
  href: https://artifacts.apis.io/xplenty/security/xplenty-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xplenty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.integrate.io/
coverage:
  checked: '2026-10-22'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.integrate.io/docs/api-reference/clusters/list-clusters
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Integrate.io (formerly Xplenty) offers a low‑code, AI‑enhanced data integration platform that simplifies building, orchestrating, and monitoring data pipelines for ETL, ELT, CDC, and reverse‑ETL use cases. Users can connect to a wide range of sources and destinations via pre‑built connectors, apply AI‑driven transformations, and manage workflows through a visual interface or AI agents. The service targets data engineers, analysts, and business users seeking scalable, automated data pipelines, with features such as scheduling, monitoring, and governance to ensure reliable data movement across cloud and on‑prem environments.
image: https://www.integrate.io/og-default.png
layout: provider
modified: '2026-10-21'
name: Integrate.io
nav: Providers
network: true
overview: 'Integrate.io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data Integration, ETL, Low-Code, Artificial Intelligence, and Cloud.


  The Integrate.io catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Integrate.io''s developer surface includes authentication, support, pricing, documentation, engineering blog, getting-started guide, and 19 more developer resources.'
plans:
- name: Xplenty Plans Pricing
  plan_count: 1
  slug: xplenty-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Integrate.io API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: xplenty-rules
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 18.5
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 39.5
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
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Xplenty Authentication
  slug: xplenty-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Xplenty Domain Security
  slug: xplenty-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: xplenty
tags:
- Data Integration
- ETL
- Low-Code
- Artificial Intelligence
- Cloud
website: https://www.integrate.io/
---
