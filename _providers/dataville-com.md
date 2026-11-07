---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dataville Com Agentic Access
  operation_count: 9
  slug: dataville-com-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.dataville.com
  baseurl_source: declared
  description: Connect a Google Sheet and query it alongside the public datasets.
  name: Dataville Connected sheets API
  slug: dataville-com-connected-sheets-api
- baseURL: https://api.dataville.com
  baseurl_source: declared
  description: Keyword search and article lookup across every supported dataset.
  name: Dataville Data sources API
  slug: dataville-com-data-sources-api
- baseURL: https://api.dataville.com
  baseurl_source: declared
  description: SELECT-only SQL over the datasets — as JSON, or as a Parquet/CSV result a DuckDB client reads directly.
  name: Dataville Export and SQL API
  slug: dataville-com-export-and-sql-api
- baseURL: https://api.dataville.com
  baseurl_source: declared
  description: Usage and quota for your API key (or your IP when anonymous). Keys are created and revoked from the dashboard's **API Keys** page.
  name: Dataville Usage API
  slug: dataville-com-usage-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/dataville-com/agentic-access/dataville-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dataville-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dataville-com/plans/dataville-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dataville-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dataville-com/rules/dataville-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dataville-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dataville-com/json-ld/dataville-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dataville-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dataville-com/vocabulary/dataville-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dataville-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dataville-com/data-model/dataville-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dataville-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/dataville-com/authentication/dataville-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dataville-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dataville-com/errors/dataville-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dataville-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dataville-com/conformance/dataville-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dataville-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dataville-com/llms/dataville-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dataville-com-llms.txt
- group: other
  href: https://artifacts.apis.io/dataville-com/a2a/dataville-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dataville-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/dataville-com/hosts/dataville-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataville-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dataville-com/vendors/dataville-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dataville-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.dataville.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.dataville.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datavilleorg
- group: start
  title: ''
  type: SignUp
  url: https://app.dataville.com/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dataville.com/quickstart-claude
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dataville.com/api-reference/overview
- group: auth
  href: https://artifacts.apis.io/dataville-com/security/dataville-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataville-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataville.com/
- group: other
  title: ''
  type: Description
  url: https://www.dataville.com/
- group: other
  title: ''
  type: Image
  url: https://cdn.prod.website-files.com/69c2bdec2337adec732a9cc7/6ad277918f4d5280fc21b932_Connect%20to%20Trustworthy%20Data%20(1).png
- group: docs
  title: ''
  type: Documentation
  url: https://www.dataville.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dataville.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.dataville.com/blog
created: '2026-11-05'
description: Dataville provides APIs and a Managed Cloud Platform (MCP) that give developers access to trustworthy, production‑ready data from public knowledge sources, research datasets, financial filings and licensed collections. It serves developers building AI applications and knowledge creators who want to monetize their data with attribution and clear usage rights.
image: https://cdn.prod.website-files.com/69c2bdec2337adec732a9cc7/6ad277918f4d5280fc21b932_Connect%20to%20Trustworthy%20Data%20(1).png
json_schemas:
- name: DataSuccessResponse
  property_count: 4
  slug: dataville-com-data-success-response
jsonld:
- class_count: 9
  name: Dataville Com Context
  property_count: 28
  slug: dataville-com-context
layout: provider
modified: '2026-11-05'
name: Dataville
nav: Providers
network: true
overview: 'Dataville publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Connected sheets API, Data sources API, Export and SQL API, and 1 more. Tagged areas include Data API, AI Applications, Financial Filings, Research Data, and Knowledge Attribution.


  The Dataville catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dataville''s developer surface includes authentication, signup flow, getting-started guide, API reference, documentation, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Dataville Com Plans Pricing
  plan_count: 3
  slug: dataville-com-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Dataville API Rules
  rule_count: 58
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 2
  slug: dataville-com-rules
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 71.2
    catalog_earned_first_party: 12.0
    catalog_gap: 43.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 62.7
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dataville Com Authentication
  slug: dataville-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Dataville Com Domain Security
  slug: dataville-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dataville-com
tags:
- Data API
- AI Applications
- Financial Filings
- Research Data
- Knowledge Attribution
website: https://dataville.com/
---
