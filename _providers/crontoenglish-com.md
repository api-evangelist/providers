---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Crontoenglish Com Agentic Access
  operation_count: 3
  slug: crontoenglish-com-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://crontoenglish.com
  baseurl_source: declared
  description: The Build API from Cron Translator — 1 operation(s) for build.
  name: Cron Translator Build API
  slug: crontoenglish-com-build-api
- baseURL: https://crontoenglish.com
  baseurl_source: declared
  description: The Explain API from Cron Translator — 1 operation(s) for explain.
  name: Cron Translator Explain API
  slug: crontoenglish-com-explain-api
- baseURL: https://crontoenglish.com
  baseurl_source: declared
  description: The Next Runs API from Cron Translator — 1 operation(s) for next runs.
  name: Cron Translator Next Runs API
  slug: crontoenglish-com-next-runs-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/crontoenglish-com/agentic-access/crontoenglish-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crontoenglish-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/crontoenglish-com/rules/crontoenglish-com-rules.yml
  title: ''
  type: Spectral
  url: rules/crontoenglish-com-rules.yml
- group: operate
  href: https://artifacts.apis.io/crontoenglish-com/changelog/crontoenglish-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/crontoenglish-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/crontoenglish-com/errors/crontoenglish-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crontoenglish-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crontoenglish-com/conformance/crontoenglish-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crontoenglish-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crontoenglish-com/llms/crontoenglish-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crontoenglish-com-llms.txt
- group: other
  href: https://artifacts.apis.io/crontoenglish-com/hosts/crontoenglish-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crontoenglish-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/crontoenglish-com/vendors/crontoenglish-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crontoenglish-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/crontoenglish-com/security/crontoenglish-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crontoenglish-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crontoenglish.com/
- group: docs
  title: ''
  type: Documentation
  url: https://crontoenglish.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://crontoenglish.com/.well-known/openapi.json
- group: agent
  title: ''
  type: MCP
  url: https://crontoenglish.com/api/mcp
- group: agent
  title: ''
  type: llms.txt
  url: https://crontoenglish.com/llms.txt
created: '2026-11-04'
description: Cron Translator is a free web tool that translates cron expressions into plain English and back, providing next run times, timezone handling, and handling of common cron pitfalls. It offers a JSON API and an MCP server for programmatic access, supporting explain, next-runs, and build operations without authentication.
layout: provider
modified: '2026-11-04'
name: Cron Translator
nav: Providers
network: true
overview: 'Cron Translator publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Build API, Explain API, and Next Runs API. Tagged areas include Cron, Translator, CronExpressions, and Scheduler.


  The Cron Translator catalog on APIs.io includes 1 Spectral governance ruleset.


  Cron Translator''s developer surface includes changelog, documentation, API reference, and 11 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Cron Translator API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: crontoenglish-com-rules
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 49.6
    developer_ergonomics: 16.7
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crontoenglish Com Domain Security
  slug: crontoenglish-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: crontoenglish-com
tags:
- Cron
- Translator
- CronExpressions
- Scheduler
website: https://crontoenglish.com/
---
