---
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Consent-enforced access to normalized patient‑authorized records. Production access is free and self‑serve with a FinchNode account.
  name: FinchNode Developer API
  slug: finchnode-developer-api
- baseURL: https://api.finchnode.com/api/v1
  baseurl_source: declared
  description: Production access is free and self-serve with a FinchNode account at https://finchnode.com/signup. Live access requires production credentials, a supported source, and patient authorization and consen
  name: FinchNode Developer API API
  slug: finchnode-developer-api-api
artifact_total: 16
asyncapis:
- description: ''
  name: Finchnode Com Webhooks
  slug: finchnode-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/finchnode-com/rules/finchnode-com-rules.yml
  title: ''
  type: Spectral
  url: rules/finchnode-com-rules.yml
- group: design
  href: https://artifacts.apis.io/finchnode-com/json-ld/finchnode-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/finchnode-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/finchnode-com/vocabulary/finchnode-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/finchnode-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/finchnode-com/conventions/finchnode-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/finchnode-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/finchnode-com/conformance/finchnode-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/finchnode-com-conformance.yml
- group: operate
  href: https://artifacts.apis.io/finchnode-com/rate-limits/finchnode-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/finchnode-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/finchnode-com/plans/finchnode-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/finchnode-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/finchnode-com/asyncapi/finchnode-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/finchnode-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/finchnode-com/data-model/finchnode-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/finchnode-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/finchnode-com/conventions/finchnode-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/finchnode-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/finchnode-com/authentication/finchnode-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/finchnode-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/finchnode-com/errors/finchnode-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/finchnode-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/finchnode-com/llms/finchnode-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/finchnode-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/finchnode-com/mcp/finchnode-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/finchnode-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/finchnode-com/hosts/finchnode-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/finchnode-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/finchnode-com/vendors/finchnode-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/finchnode-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/finchnode-com/security/finchnode-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finchnode-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://finchnode.com/
- group: docs
  title: ''
  type: Documentation
  url: https://finchnode.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://finchnode.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://finchnode.com/docs/get-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://finchnode.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://finchnode.com/signup
created: '2026-10-30'
description: FinchNode provides a free, production‑grade, patient‑authorized Electronic Health Record (EHR) API. Developers can self‑serve access to real patient‑authorized records via a unified API that normalizes data from 17+ EHR and payer integrations. The platform offers a synthetic sandbox, hosted consent, webhooks, and tiered pricing, with a free tier for one production application and a paid tier for expanded usage.
image: https://finchnode.com/og.png?v=finch1
json_schemas:
- name: ConformanceReport
  property_count: 13
  slug: finchnode-com-conformance-report
- name: ConformanceRun
  property_count: 15
  slug: finchnode-com-conformance-run
- name: ConnectSession
  property_count: 17
  slug: finchnode-com-connect-session
- name: ConsentReceipt
  property_count: 18
  slug: finchnode-com-consent-receipt
- name: TefcaExport
  property_count: 11
  slug: finchnode-com-tefca-export
- name: TefcaSession
  property_count: 16
  slug: finchnode-com-tefca-session
jsonld:
- class_count: 41
  name: Finchnode Com Context
  property_count: 128
  slug: finchnode-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.finchnode.com requiring an API key.
  name: finchnode-com MCP Server
  slug: finchnode-com-mcp-yml
modified: '2026-10-30'
name: finchnode-com
nav: Providers
network: true
overview: 'finchnode-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including FinchNode Developer API API, and 1 more. Tagged areas include Company, Healthcare, API, EHR, and OpenData.


  The finchnode-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  finchnode-com''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, and 17 more developer resources.'
plans:
- name: Finchnode Com Plans Pricing
  plan_count: 2
  slug: finchnode-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Finchnode Com Rate Limits
  slug: finchnode-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: finchnode-com API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 4
  slug: finchnode-com-rules
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 58.9
    developer_ergonomics: 42.9
    discoverability: 65.0
    operational_transparency: 39.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Finchnode Com Authentication
  slug: finchnode-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Finchnode Com Domain Security
  slug: finchnode-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finchnode-com
tags:
- Company
- Healthcare
- API
- EHR
- OpenData
website: https://finchnode.com/
---
