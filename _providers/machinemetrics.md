---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
api_count: 5
apis:
- baseURL: https://api.machinemetrics.com
  baseurl_source: declared
  description: The MachineMetrics API API from MachineMetrics — 1 operation(s) for machinemetrics api.
  name: MachineMetrics MachineMetrics API
  slug: machinemetrics-machinemetrics-api-api
- baseURL: https://api.machinemetrics.com
  baseurl_source: declared
  description: The Mmdevcli API from MachineMetrics — 1 operation(s) for mmdevcli.
  name: MachineMetrics Mmdevcli API
  slug: machinemetrics-mmdevcli-api
- baseURL: https://api.machinemetrics.com
  baseurl_source: declared
  description: The Ping API from MachineMetrics — 1 operation(s) for ping.
  name: MachineMetrics Ping API
  slug: machinemetrics-ping-api
- baseURL: https://api.machinemetrics.com
  baseurl_source: declared
  description: The Reports API from MachineMetrics — 1 operation(s) for reports.
  name: MachineMetrics Reports API
  slug: machinemetrics-reports-api
- baseURL: https://api.machinemetrics.com
  baseurl_source: declared
  description: The Graph QL API from MachineMetrics — 1 operation(s) for graph ql.
  name: MachineMetrics Graph QL API
  slug: machinemetrics-graph-ql-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/machinemetrics/rules/machinemetrics-rules.yml
  title: ''
  type: Spectral
  url: rules/machinemetrics-rules.yml
- group: design
  href: https://artifacts.apis.io/machinemetrics/json-ld/machinemetrics-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/machinemetrics-context.jsonld
- group: design
  href: https://artifacts.apis.io/machinemetrics/vocabulary/machinemetrics-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/machinemetrics-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/machinemetrics/data-model/machinemetrics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/machinemetrics-data-model.yml
- group: build
  href: https://artifacts.apis.io/machinemetrics/cli/machinemetrics-cli.yml
  title: ''
  type: CLI
  url: cli/machinemetrics-cli.yml
- group: auth
  href: https://artifacts.apis.io/machinemetrics/authentication/machinemetrics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/machinemetrics-authentication.yml
- group: design
  href: https://artifacts.apis.io/machinemetrics/conformance/machinemetrics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/machinemetrics-conformance.yml
- group: agent
  href: https://artifacts.apis.io/machinemetrics/llms/machinemetrics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/machinemetrics-llms.txt
- group: auth
  href: https://artifacts.apis.io/machinemetrics/well-known/machinemetrics-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/machinemetrics-status-security.txt
- group: agent
  href: https://artifacts.apis.io/machinemetrics/well-known/machinemetrics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/machinemetrics-well-known.yml
- group: other
  href: https://artifacts.apis.io/machinemetrics/hosts/machinemetrics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/machinemetrics-hosts.yml
- group: other
  href: https://artifacts.apis.io/machinemetrics/vendors/machinemetrics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/machinemetrics-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.machinemetrics.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.machinemetrics.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.machinemetrics.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.machinemetrics.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.machinemetrics.com/newsroom
- group: start
  title: ''
  type: Login
  url: https://app.machinemetrics.com/login
- group: other
  title: ''
  type: Leadership
  url: https://www.machinemetrics.com/team
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.machinemetrics.com/release-notes
- group: company
  title: ''
  type: Blog
  url: https://www.machinemetrics.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://developers.machinemetrics.com/docs/data-and-apis/graphql/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.machinemetrics.com/docs/data-and-apis/expected-setup-allocation
- group: docs
  title: ''
  type: Documentation
  url: https://developers.machinemetrics.com/
- group: auth
  href: https://artifacts.apis.io/machinemetrics/security/machinemetrics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/machinemetrics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.machinemetrics.com
coverage:
  checked: '2026-10-12'
  detail: OpenAPI spec not found at https://api.machinemetrics.com/openapi.json (404) and GraphQL endpoint requires authentication.
  evidence:
  - status: 404
    url: https://api.machinemetrics.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: MachineMetrics provides an AI‑powered manufacturing operations platform that connects machines, operators, and enterprise systems in real time. Their MaximaOS solution offers production scheduling, work order management, operator guidance, downtime tracking, OEE analytics, and tool‑life monitoring across multiple sites. By leveraging live machine data and AI, they help manufacturers close the execution gap, improve utilization, and accelerate decision‑making. The platform serves industries such as aerospace, automotive, contract manufacturing, medical devices, and heavy equipment, supporting over 10,000 machines globally.
image: https://www.machinemetrics.com/hubfs/Homepage.png
json_schemas:
- name: PostReportsProductionRequest
  property_count: 3
  slug: machinemetrics-post-reports-production-request
jsonld:
- class_count: 1
  name: Machinemetrics Context
  property_count: 3
  slug: machinemetrics-context
layout: provider
modified: '2026-10-12'
name: MachineMetrics
nav: Providers
network: true
overview: 'MachineMetrics is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including MachineMetrics API, Mmdevcli API, Ping API, and 2 more. Tagged areas include Company, Manufacturing, Artificial Intelligence, MES, and IoT.


  The MachineMetrics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MachineMetrics'' developer surface includes CLI, authentication, support, pricing, changelog, engineering blog, API reference, and 19 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: MachineMetrics API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: machinemetrics-rules
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 56.2
    catalog_earned_first_party: 0.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 17.1
    contract_governance: 35.6
    contract_quality: 19.0
    developer_ergonomics: 36.9
    discoverability: 80.4
    operational_transparency: 26.3
  previous_composite: 40.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/machinemetrics/machinemetrics-2026-11-03T135158.png
security:
- kind: authentication
  name: Machinemetrics Authentication
  slug: machinemetrics-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Machinemetrics Domain Security
  slug: machinemetrics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: machinemetrics
tags:
- Company
- Manufacturing
- Artificial Intelligence
- MES
- IoT
- Software-as-a-Service
website: https://www.machinemetrics.com
---
