---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-09-21'
api_count: 1
apis:
- baseURL: https://rowguard-api.rowguard-api.workers.dev
  baseurl_source: declared
  description: The CSV validation API from RowGuard API Catalog — 1 operation(s) for csv validation.
  name: RowGuard API Catalog CSV validation API
  slug: rowguard-csv-validation-api
- baseURL: https://rowguard-api.rowguard-api.workers.dev
  baseurl_source: declared
  description: The Example API from RowGuard API Catalog — 1 operation(s) for example.
  name: RowGuard API Catalog Example API
  slug: rowguard-example-api
- baseURL: https://rowguard-api.rowguard-api.workers.dev
  baseurl_source: declared
  description: The Healthz API from RowGuard API Catalog — 1 operation(s) for healthz.
  name: RowGuard API Catalog Healthz API
  slug: rowguard-healthz-api
artifact_total: 9
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rowguard/refs/heads/main/overlays/rowguard-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rowguard-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rowguard/refs/heads/main/mcp/rowguard-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rowguard-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rowguard/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rowguard/refs/heads/main/security/rowguard-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/rowguard-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rowguard/refs/heads/main/security/rowguard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rowguard-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rowguard/refs/heads/main/authentication/rowguard-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rowguard-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://rowguard-api.rowguard-api.workers.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://documenter.getpostman.com/view/58184962/2sBYAytUGg
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/dark-shadow-744867/rowguard-csv-validation-api/overview
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Frere527/rowguard-api-examples
- group: commercial
  title: ''
  type: Pricing
  url: https://rapidapi.com/Frere527/api/rowguard-csv-validation1
- group: operate
  title: ''
  type: RateLimits
  url: https://rapidapi.com/Frere527/api/rowguard-csv-validation1
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rapidapi.com/terms
- group: auth
  title: ''
  type: Security
  url: https://rowguard-api.rowguard-api.workers.dev/security
- group: start
  title: ''
  type: APIOnboarding
  url: https://rowguard-api.rowguard-api.workers.dev/.well-known/api-onboarding
- group: other
  title: ''
  type: APICatalog
  url: https://rowguard-api.rowguard-api.workers.dev/.well-known/api-catalog
- group: agent
  title: ''
  type: LLMsTxt
  url: https://rowguard-api.rowguard-api.workers.dev/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rowguard/refs/heads/main/well-known/rowguard-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rowguard-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rowguard/refs/heads/main/well-known/rowguard-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rowguard-security.txt
created: '2026-09-12'
description: RowGuard validates UTF-8 CSV data against a caller-supplied column schema before it is imported into a database or automation workflow. In one HTTP request it reports missing values, type and format errors, out-of-range numbers, disallowed values, duplicate identifiers, and spreadsheet-formula (CSV injection) risks, returning record- and column-level references and optionally the rows that passed. It stores no files and calls no AI model, and is distributed through the RapidAPI marketplace.
layout: provider
mcp_servers:
- description: ''
  name: RowGuard API Catalog MCP Server
  slug: rowguard-api-catalog-mcp-server
modified: '2026-09-13'
name: RowGuard API Catalog
nav: Providers
network: true
overview: 'RowGuard API Catalog publishes 3 APIs on the [APIs.io](https://apis.io/) network: CSV validation API, Example API, and Healthz API. Tagged areas include CSV, Validation, Data Quality, Import, and Automation.


  RowGuard API Catalog''s developer surface includes authentication, documentation, pricing, and 16 more developer resources.'
plans:
- name: Rowguard Plans Pricing
  plan_count: 4
  slug: rowguard-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 9
  name: Rowguard Rate Limits
  slug: rowguard-rate-limits
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 49.4
    discoverability: 83.3
    operational_transparency: 47.4
  previous_composite: 46.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Rowguard Authentication
  slug: rowguard-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rowguard Domain Security
  slug: rowguard-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Rowguard Vulnerability Disclosure
  slug: rowguard-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: rowguard
tags:
- CSV
- Validation
- Data Quality
- Import
- Automation
website: https://rowguard-api.rowguard-api.workers.dev/
---
