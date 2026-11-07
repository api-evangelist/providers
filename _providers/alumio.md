---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Alumio integration platform, documented at Alumio Docs
  name: Alumio API
  slug: alumio-api-2
- description: 'Alumio API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Alumio API
  slug: alumio-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/alumio/plans/alumio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alumio-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/alumio/rules/alumio-rules.yml
  title: ''
  type: Spectral
  url: rules/alumio-rules.yml
- group: design
  href: https://artifacts.apis.io/alumio/json-ld/alumio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/alumio-context.jsonld
- group: design
  href: https://artifacts.apis.io/alumio/vocabulary/alumio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/alumio-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/alumio/data-model/alumio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/alumio-data-model.yml
- group: operate
  href: https://artifacts.apis.io/alumio/changelog/alumio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/alumio-changelog.yml
- group: design
  href: https://artifacts.apis.io/alumio/conformance/alumio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alumio-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alumio/llms/alumio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alumio-llms.txt
- group: other
  href: https://artifacts.apis.io/alumio/a2a/alumio-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/alumio-a2a.yml
- group: agent
  href: https://artifacts.apis.io/alumio/mcp/alumio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alumio-mcp.yml
- group: agent
  href: https://artifacts.apis.io/alumio/well-known/alumio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alumio-well-known.yml
- group: other
  href: https://artifacts.apis.io/alumio/hosts/alumio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alumio-hosts.yml
- group: other
  href: https://artifacts.apis.io/alumio/vendors/alumio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alumio-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alumio.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alumio.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.alumio.com/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.alumio.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.alumio.com/release-notes
- group: company
  title: ''
  type: Blog
  url: https://www.alumio.com/blog/what-is-edi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.alumio.com/documentation/getting-started/dashboard
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alumio.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.aha.io/api
- group: auth
  href: https://artifacts.apis.io/alumio/security/alumio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alumio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alumio.com/
coverage:
  checked: '2026-10-19'
  detail: Docs are rendered as a JavaScript SPA, no machine‑readable OpenAPI spec found.
  evidence:
  - status: 0
    url: https://api.alumio.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: Alumio provides a cloud‑based integration platform (iPaaS) that enables businesses to connect, orchestrate, and govern critical data flows across a wide range of applications, services, and APIs. Its visual Route Builder lets users design integration workflows without code, supporting multi‑entity environments for agencies, system integrators, and ISVs. Alumio focuses on secure, scalable integrations for e‑commerce, ERP, CRM, PIM, AI‑driven pricing, and more, delivering enterprise‑grade reliability for complex B2B processes.
json_schemas:
- name: GetApiV1FeaturesApp1Response
  property_count: 2
  slug: alumio-get-api-v1-features-app1-response
- name: GetApiV1ReleasesAppR1FeaturesResponse
  property_count: 5
  slug: alumio-get-api-v1-releases-app-r1-features-response
jsonld:
- class_count: 2
  name: Alumio Context
  property_count: 2
  slug: alumio-context
layout: provider
mcp_servers:
- description: Remote MCP server at alumio.main-kill-isr.mintlify.me.
  name: Alumio MCP Server
  slug: alumio-mcp-yml
modified: '2026-10-19'
name: Alumio
nav: Providers
network: true
overview: 'Alumio is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, iPaaS, and Enterprise.


  The Alumio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Alumio''s developer surface includes changelog, pricing, engineering blog, getting-started guide, documentation, API reference, and 18 more developer resources.'
plans:
- name: Alumio Plans Pricing
  plan_count: 2
  slug: alumio-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Alumio API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: alumio-rules
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.8
    catalog_earned_first_party: 8.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 20.4
    developer_ergonomics: 23.8
    discoverability: 55.8
    operational_transparency: 7.9
  previous_composite: 31.9
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/alumio/alumio-2026-11-03T120744.png
security:
- kind: domain-security
  name: Alumio Domain Security
  slug: alumio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: alumio
tags:
- Company
- Integration
- iPaaS
- Enterprise
website: https://alumio.com/
---
