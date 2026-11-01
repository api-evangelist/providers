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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Portrait Analytics API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Portrait Analytics API
  slug: portrait-analytics-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/portrait-analytics/rules/portrait-analytics-rules.yml
  title: ''
  type: Spectral
  url: rules/portrait-analytics-rules.yml
- group: design
  href: https://artifacts.apis.io/portrait-analytics/vocabulary/portrait-analytics-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/portrait-analytics-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/portrait-analytics/cli/portrait-analytics-cli.yml
  title: ''
  type: CLI
  url: cli/portrait-analytics-cli.yml
- group: design
  href: https://artifacts.apis.io/portrait-analytics/conformance/portrait-analytics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/portrait-analytics-conformance.yml
- group: agent
  href: https://artifacts.apis.io/portrait-analytics/llms/portrait-analytics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/portrait-analytics-llms.txt
- group: agent
  href: https://artifacts.apis.io/portrait-analytics/well-known/portrait-analytics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/portrait-analytics-well-known.yml
- group: other
  href: https://artifacts.apis.io/portrait-analytics/hosts/portrait-analytics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/portrait-analytics-hosts.yml
- group: other
  href: https://artifacts.apis.io/portrait-analytics/vendors/portrait-analytics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/portrait-analytics-vendors.yml
- group: auth
  href: https://artifacts.apis.io/portrait-analytics/security/portrait-analytics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/portrait-analytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://portraitresearch.com/
- group: docs
  title: ''
  type: APIReference
  url: https://portraitresearch.com/documentation/reference/
- group: docs
  title: ''
  type: Documentation
  url: https://portraitresearch.com/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://portraitresearch.com/documentation/getting-started/welcome/
- group: company
  title: ''
  type: Blog
  url: https://portraitresearch.com/blog/category/china-hpc-production/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://portraitresearch.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://portraitresearch.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://portraitresearch.com/security/
- group: commercial
  title: ''
  type: Pricing
  url: https://portraitresearch.com/request-trial/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/portraitresearch/workspace/portrait-api
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec was found; attempts to fetch common spec URLs returned 403 or 404.
  evidence:
  - status: 403
    url: https://api.portraitresearch.com/openapi.json
  - status: 404
    url: https://portraitresearch.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Portrait Analytics provides an AI‑powered research platform for fundamental investors, offering tools such as Mosaic for shortlist generation, deep research reports, screening criteria, thesis monitoring, and company research. The service aggregates data sources, generates structured reports with citations, and supports integrations via an API to embed insights into workflows. Backed by unusual‑ventures, the company aims to reduce hallucinations in AI outputs and deliver accurate, citation‑rich analysis for investment decisions.
image: https://portraitresearch.com/static/img/home-og-v5.24a350efba06.png
layout: provider
modified: '2026-10-29'
name: Portrait Analytics
nav: Providers
network: true
overview: 'Portrait Analytics is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Finance, Research, and Investment.


  The Portrait Analytics catalog on APIs.io includes 1 Spectral governance ruleset.


  Portrait Analytics'' developer surface includes CLI, API reference, documentation, getting-started guide, engineering blog, support, pricing, and 12 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Portrait Analytics API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: portrait-analytics-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 35.6
    contract_quality: 10.4
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
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
- kind: domain-security
  name: Portrait Analytics Domain Security
  slug: portrait-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: portrait-analytics
tags:
- Company
- AI
- Finance
- Research
- Investment
- Data
website: https://portraitresearch.com/
---
