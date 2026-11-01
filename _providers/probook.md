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
- description: API for Probook platform enabling integration with home services automation.
  name: Probook API
  slug: probook-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/probook/hosts/probook-hosts.yml
  title: ''
  type: Hosts
  url: hosts/probook-hosts.yml
- group: other
  href: https://artifacts.apis.io/probook/vendors/probook-vendors.yml
  title: ''
  type: Vendors
  url: vendors/probook-vendors.yml
- group: auth
  href: https://artifacts.apis.io/probook/security/probook-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/probook-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.probook.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.probook.ai/platform
- group: docs
  title: ''
  type: Documentation
  url: https://www.probook.ai/letter
- group: start
  title: ''
  type: GettingStarted
  url: https://www.probook.ai/demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.probook.ai/privacy
coverage:
  checked: '2026-10-29'
  detail: The provider's website offers no developer documentation or API reference.
  evidence:
  - status: 200
    url: https://www.probook.ai
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Probook is an AI operating system for home services, enabling businesses to automate customer interactions, dispatch, and front‑office operations. The platform combines large language models with domain‑specific workflows to deliver a seamless experience for tradespeople and their customers. Founded by industry veterans, Probook focuses on real‑world deployment, on‑site configuration, and outcome‑based guarantees, positioning itself as a trusted partner for the home services market.
layout: provider
modified: '2026-10-29'
name: Probook
nav: Providers
network: true
overview: 'Probook is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Home-Services, Automation, and Platform.


  Probook''s developer surface includes documentation, getting-started guide, and 6 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Probook Domain Security
  slug: probook-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: probook
tags:
- Company
- AI
- Home-Services
- Automation
- Platform
- Trades
website: https://www.probook.ai
---
