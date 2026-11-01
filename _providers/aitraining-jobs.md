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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-10-31'
api_count: 4
apis:
- description: Open data on AI training job listings and advertised pay.
  name: AITraining.jobs Data API
  slug: aitraining-jobs-data-api
- baseURL: https://aitraining.jobs
  baseurl_source: declared
  description: The Pay.csv API from AITraining.jobs — 1 operation(s) for pay.csv.
  name: AITraining.jobs Pay.csv API
  slug: aitraining-jobs-pay-csv-api
- baseURL: https://aitraining.jobs
  baseurl_source: declared
  description: The Pay.json API from AITraining.jobs — 1 operation(s) for pay.json.
  name: AITraining.jobs Pay.json API
  slug: aitraining-jobs-pay-json-api
- baseURL: https://aitraining.jobs
  baseurl_source: declared
  description: The Roles.json API from AITraining.jobs — 1 operation(s) for roles.json.
  name: AITraining.jobs Roles.json API
  slug: aitraining-jobs-roles-json-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/aitraining-jobs/conformance/aitraining-jobs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aitraining-jobs-conformance.yml
- group: other
  href: https://artifacts.apis.io/aitraining-jobs/overlays/aitraining-jobs-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aitraining-jobs-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/aitraining-jobs/llms/aitraining-jobs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aitraining-jobs-llms.txt
- group: agent
  href: https://artifacts.apis.io/aitraining-jobs/mcp/aitraining-jobs-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aitraining-jobs-mcp.yml
- group: other
  href: https://artifacts.apis.io/aitraining-jobs/hosts/aitraining-jobs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aitraining-jobs-hosts.yml
- group: other
  href: https://artifacts.apis.io/aitraining-jobs/vendors/aitraining-jobs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aitraining-jobs-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://aitraining.jobs/jobs/registered-nurse-4c1e4cf12fb3
- group: auth
  href: https://artifacts.apis.io/aitraining-jobs/security/aitraining-jobs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aitraining-jobs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aitraining.jobs/
- group: docs
  title: ''
  type: Documentation
  url: https://aitraining.jobs/data
- group: docs
  title: ''
  type: APIReference
  url: https://aitraining.jobs/data
- group: start
  title: ''
  type: GettingStarted
  url: https://aitraining.jobs/how-it-works
- group: commercial
  title: ''
  type: Pricing
  url: https://aitraining.jobs/pay
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aitraining.jobs/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aitraining.jobs/legal/privacy
created: '2026-10-11'
description: AITraining.jobs aggregates open data on AI‑training job listings and advertised pay across dozens of platforms. It provides daily‑updated role counts, hourly‑pay ranges, and research reports, helping workers compare opportunities and understand market trends. The site offers free access to role listings, pay data, and research without requiring sign‑up, and it invites companies to promote their jobs.
image: https://aitraining.jobs/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at aitraining.jobs.
  name: AITraining.jobs MCP Server
  slug: aitraining-jobs-mcp-yml
modified: '2026-10-11'
name: AITraining.jobs
nav: Providers
network: true
overview: 'AITraining.jobs is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Pay.csv API, Pay.json API, Roles.json API, and 1 more. Tagged areas include Company, Artificial Intelligence, Job, Data, and Training.


  AITraining.jobs'' developer surface includes signup flow, documentation, API reference, getting-started guide, pricing, and 10 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.2
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 44.7
    developer_ergonomics: 28.6
    discoverability: 70.0
    operational_transparency: 0.0
  previous_composite: 23.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aitraining Jobs Domain Security
  slug: aitraining-jobs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aitraining-jobs
tags:
- Company
- Artificial Intelligence
- Job
- Data
- Training
website: https://aitraining.jobs/
---
