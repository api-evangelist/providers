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
api_count: 1
apis:
- description: SyncBuilder provides an integration platform with a public API (details not publicly documented).
  name: SyncBuilder API
  slug: syncbuilder-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/syncbuilder/plans/syncbuilder-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/syncbuilder-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/syncbuilder/llms/syncbuilder-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/syncbuilder-llms.txt
- group: other
  href: https://artifacts.apis.io/syncbuilder/hosts/syncbuilder-hosts.yml
  title: ''
  type: Hosts
  url: hosts/syncbuilder-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://syncbuilder.com/terms
- group: auth
  title: ''
  type: Security
  url: https://syncbuilder.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://syncbuilder.com/privacy
- group: start
  title: ''
  type: Login
  url: https://syncbuilder.com/go/login
- group: auth
  href: https://artifacts.apis.io/syncbuilder/security/syncbuilder-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/syncbuilder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://syncbuilder.com/
- group: docs
  title: ''
  type: APIReference
  url: https://syncbuilder.com/api-management
- group: start
  title: ''
  type: GettingStarted
  url: https://syncbuilder.com/workflow-automation
- group: operate
  title: ''
  type: Support
  url: https://syncbuilder.com/contact
- group: company
  title: ''
  type: Blog
  url: https://syncbuilder.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://syncbuilder.com/pricing
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found at standard endpoints on api.syncbuilder.com.
  evidence:
  - status: 404
    url: https://api.syncbuilder.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: SyncBuilder provides an integration platform that enables businesses to synchronize data across databases, ERP systems, and a wide range of internal applications. Users can build workflows with a drag‑and‑drop interface, leverage pre‑built templates, and connect over 100 apps including Shopify, SAP, Magento, and more. The service supports REST, SOAP, EDI, file drops, and email channels, offering scalable, secure, and GDPR‑compliant data integration for enterprises.
image: https://syncbuilder.com/og.jpg
layout: provider
modified: '2026-10-19'
name: SyncBuilder
nav: Providers
network: true
overview: 'SyncBuilder is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, Data Sync, ERP, and Automation.


  SyncBuilder''s developer surface includes API reference, getting-started guide, support, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Syncbuilder Plans Pricing
  plan_count: 4
  slug: syncbuilder-plans-pricing
random_paper: 12
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 10.5
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
  name: Syncbuilder Domain Security
  slug: syncbuilder-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: syncbuilder
tags:
- Company
- Integration
- Data Sync
- ERP
- Automation
website: https://syncbuilder.com/
---
