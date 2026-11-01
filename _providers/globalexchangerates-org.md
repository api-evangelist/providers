---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: unknown
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
  score: 12.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Globalexchangerates Org Agentic Access
  operation_count: 1
  slug: globalexchangerates-org-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Provides currency list and exchange rates.
  name: Global Exchange Rates API
  slug: global-exchange-rates-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/globalexchangerates-org/agentic-access/globalexchangerates-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/globalexchangerates-org-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/globalexchangerates-org/plans/globalexchangerates-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/globalexchangerates-org-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/globalexchangerates-org/rules/globalexchangerates-org-rules.yml
  title: ''
  type: Spectral
  url: rules/globalexchangerates-org-rules.yml
- group: design
  href: https://artifacts.apis.io/globalexchangerates-org/vocabulary/globalexchangerates-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/globalexchangerates-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/globalexchangerates-org/conformance/globalexchangerates-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/globalexchangerates-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/globalexchangerates-org/llms/globalexchangerates-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/globalexchangerates-org-llms.txt
- group: other
  href: https://artifacts.apis.io/globalexchangerates-org/hosts/globalexchangerates-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/globalexchangerates-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/globalexchangerates-org/vendors/globalexchangerates-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/globalexchangerates-org-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/globalexchangerates
- group: auth
  href: https://artifacts.apis.io/globalexchangerates-org/security/globalexchangerates-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/globalexchangerates-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://globalexchangerates.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.globalexchangerates.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.globalexchangerates.org/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.globalexchangerates.org/docs/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.globalexchangerates.org/get-started/
- group: operate
  title: ''
  type: Support
  url: https://www.globalexchangerates.org/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.globalexchangerates.org/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.globalexchangerates.org/plan/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.globalexchangerates.org/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.globalexchangerates.org/privacy-policy/
created: '2026-10-30'
description: Global Exchange Rates provides an official exchange rates API and ERP connectors, delivering reliable, up‑to‑date currency data sourced directly from central banks and tax authorities worldwide. The service supports JSON, XML and CSV formats, offers historical and real‑time rates, and integrates with major ERP systems such as Dynamics 365, SAP, and QuickBooks, targeting finance, accounting, and business intelligence applications.
image: https://www.globalexchangerates.org/assets/og-default.png
layout: provider
modified: '2026-10-30'
name: globalexchangerates-org
nav: Providers
network: true
overview: 'globalexchangerates-org is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, API, ExchangeRates, and ERP.


  The globalexchangerates-org catalog on APIs.io includes 1 Spectral governance ruleset.


  globalexchangerates-org''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Globalexchangerates Org Plans Pricing
  plan_count: 2
  slug: globalexchangerates-org-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: globalexchangerates-org API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: globalexchangerates-org-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 64.9
    catalog_earned_first_party: 0.0
    catalog_gap: 50.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.5
    contract_governance: 79.1
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 66.1
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Globalexchangerates Org Domain Security
  slug: globalexchangerates-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: globalexchangerates-org
tags:
- Company
- Finance
- API
- ExchangeRates
- ERP
website: https://globalexchangerates.org/
---
