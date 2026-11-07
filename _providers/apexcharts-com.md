---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: ApexCharts provides a JavaScript charting library with a client‑side API for creating interactive charts; no server‑side API is offered.
  name: ApexCharts JavaScript Library
  slug: apexcharts-js
- description: 'ApexCharts API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: ApexCharts API
  slug: apexcharts-com-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/apexcharts-com/plans/apexcharts-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apexcharts-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apexcharts-com/rules/apexcharts-com-rules.yml
  title: ''
  type: Spectral
  url: rules/apexcharts-com-rules.yml
- group: design
  href: https://artifacts.apis.io/apexcharts-com/vocabulary/apexcharts-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apexcharts-com-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/apexcharts-com/changelog/apexcharts-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apexcharts-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/apexcharts-com/conformance/apexcharts-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apexcharts-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apexcharts-com/llms/apexcharts-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apexcharts-com-llms.txt
- group: other
  href: https://artifacts.apis.io/apexcharts-com/hosts/apexcharts-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apexcharts-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/apexcharts-com/packages/apexcharts-com-packages.yml
  title: ''
  type: SDKs
  url: packages/apexcharts-com-packages.yml
- group: build
  href: https://artifacts.apis.io/apexcharts-com/packages/apexcharts-com-packages.yml
  title: ''
  type: Packages
  url: packages/apexcharts-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apexcharts.com/legal/terms/
- group: start
  title: ''
  type: SignUp
  url: https://apexcharts.com/recipes/register-a-brand-theme-across-apex-products/
- group: auth
  title: ''
  type: Security
  url: https://apexcharts.com/legal/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apexcharts.com/legal/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://apexcharts.com/blog/releases/
- group: start
  title: ''
  type: GettingStarted
  url: https://apexcharts.com/docs/installation/
- group: auth
  href: https://artifacts.apis.io/apexcharts-com/security/apexcharts-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apexcharts-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apexcharts.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apexcharts.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://apexcharts.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://apexcharts.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://apexcharts.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apexcharts
coverage:
  checked: '2026-11-01'
  detail: Public documentation exists but no machine‑readable OpenAPI, GraphQL, or AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://apexcharts.com/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ApexCharts provides a modern JavaScript charting library that enables developers to create interactive, responsive charts and visualizations with a simple API. It supports multiple frameworks including vanilla JavaScript, React, Vue, Angular, and offers a variety of chart types such as line, area, bar, pie, heatmap, and more. The library is open-source, actively maintained, and includes extensive documentation, demos, pricing plans for commercial use, and a community of contributors.
image: https://apexcharts.com/favicon-96x96.png
layout: provider
modified: '2026-11-01'
name: ApexCharts
nav: Providers
network: true
overview: 'ApexCharts is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include JavaScript, Charts, Data Visualization, Open Source, and Library.


  The ApexCharts catalog on APIs.io includes 1 Spectral governance ruleset.


  ApexCharts'' developer surface includes changelog, signup flow, getting-started guide, documentation, pricing, engineering blog, support, and 15 more developer resources.'
plans:
- name: Apexcharts Com Plans Pricing
  plan_count: 4
  slug: apexcharts-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Apexcharts Com Rate Limits
  slug: apexcharts-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: ApexCharts API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: apexcharts-com-rules
scopes:
- name: Apexcharts Com Scopes
  scope_count: 0
  slug: apexcharts-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 15.8
  previous_composite: 38.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apexcharts Com Authentication
  slug: apexcharts-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Apexcharts Com Domain Security
  slug: apexcharts-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apexcharts-com
tags:
- JavaScript
- Charts
- Data Visualization
- Open Source
- Library
website: https://apexcharts.com/
---
