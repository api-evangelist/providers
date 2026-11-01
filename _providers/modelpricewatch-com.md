---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Read-only JSON feeds for LLM model pricing.
  name: Model Price Watch API
  slug: model-price-watch-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/modelpricewatch-com/plans/modelpricewatch-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/modelpricewatch-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/modelpricewatch-com/changelog/modelpricewatch-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/modelpricewatch-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/modelpricewatch-com/conformance/modelpricewatch-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/modelpricewatch-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/modelpricewatch-com/llms/modelpricewatch-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/modelpricewatch-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/modelpricewatch-com/mcp/modelpricewatch-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/modelpricewatch-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/modelpricewatch-com/well-known/modelpricewatch-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/modelpricewatch-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/modelpricewatch-com/hosts/modelpricewatch-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/modelpricewatch-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/modelpricewatch-com/vendors/modelpricewatch-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/modelpricewatch-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/modelpricewatch-com/packages/modelpricewatch-com-packages.yml
  title: ''
  type: SDKs
  url: packages/modelpricewatch-com-packages.yml
- group: build
  href: https://artifacts.apis.io/modelpricewatch-com/packages/modelpricewatch-com-packages.yml
  title: ''
  type: Packages
  url: packages/modelpricewatch-com-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modelpricewatch.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://modelpricewatch.com/news/
- group: operate
  title: ''
  type: ChangeLog
  url: https://modelpricewatch.com/providers/ibm/changelog/
- group: auth
  href: https://artifacts.apis.io/modelpricewatch-com/security/modelpricewatch-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/modelpricewatch-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://modelpricewatch.com/
created: '2026-10-30'
description: Model Price Watch provides a neutral, verified reference for LLM API pricing, tracking live token prices, context windows, benchmarks, and price history for hundreds of models across dozens of providers. The site offers a sortable table, detailed model pages, and an API for programmatic access to pricing data, aiming to help developers compare and choose LLM services efficiently.
image: https://modelpricewatch.com/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at modelpricewatch.com.
  name: modelpricewatch-com MCP Server
  slug: modelpricewatch-com-mcp-yml
modified: '2026-10-30'
name: modelpricewatch-com
nav: Providers
network: true
overview: 'modelpricewatch-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, LLM, Pricing, API, and Data.


  modelpricewatch-com''s developer surface includes changelog and 14 more developer resources.'
plans:
- name: Modelpricewatch Com Plans Pricing
  plan_count: 4
  slug: modelpricewatch-com-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 66.7
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Modelpricewatch Com Domain Security
  slug: modelpricewatch-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: modelpricewatch-com
tags:
- Company
- LLM
- Pricing
- API
- Data
website: https://modelpricewatch.com/
---
