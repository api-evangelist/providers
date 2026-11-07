---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: JSON API for the D Fetcher vitamin D synthesis calculator.
  name: D Fetcher API
  slug: d-fetcher-api
- description: 'D Fetcher API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: D Fetcher API
  slug: dfetcher-com-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/dfetcher-com/rules/dfetcher-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dfetcher-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dfetcher-com/vocabulary/dfetcher-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dfetcher-com-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/dfetcher-com/changelog/dfetcher-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dfetcher-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/dfetcher-com/conformance/dfetcher-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dfetcher-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dfetcher-com/llms/dfetcher-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dfetcher-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dfetcher-com/mcp/dfetcher-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dfetcher-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/dfetcher-com/hosts/dfetcher-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dfetcher-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dfetcher-com/vendors/dfetcher-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dfetcher-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dfetcher-com/security/dfetcher-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dfetcher-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dfetcher.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dfetcher.com/api
- group: operate
  title: ''
  type: HelpCenter
  url: https://dfetcher.com/faq
- group: design
  title: ''
  type: Versioning
  url: https://dfetcher.com/changelog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dfetcher.com/privacy
created: '2026-11-05'
description: D Fetcher provides a simple web calculator and open JSON API to estimate how long you need sun exposure to achieve a target vitamin D dose. It uses real‑time UV index data, location lookup, skin type, body surface area and age to compute minutes of sunlight needed. The service is free, CORS‑open, and requires no API key, making it easy to integrate into health apps, wearables, or personal dashboards.
image: https://dfetcher.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at dfetcher.com.
  name: D Fetcher MCP Server
  slug: dfetcher-com-mcp-yml
modified: '2026-11-05'
name: D Fetcher
nav: Providers
network: true
overview: 'D Fetcher is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Vitamin D, Health, Calculator, OpenAPI, and Free.


  The D Fetcher catalog on APIs.io includes 1 Spectral governance ruleset.


  D Fetcher''s developer surface includes changelog, API reference, and 12 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 67
  extends:
  - spectral:oas
  name: D Fetcher API Rules
  rule_count: 26
  severity_counts:
    error: 24
    hint: 0
    info: 1
    warn: 1
  slug: dfetcher-com-rules
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 11.9
    discoverability: 56.7
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dfetcher Com Domain Security
  slug: dfetcher-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dfetcher-com
tags:
- Vitamin D
- Health
- Calculator
- OpenAPI
- Free
website: https://dfetcher.com/
---
