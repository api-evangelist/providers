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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: 12Backlinks Com Agentic Access
  operation_count: 10
  slug: 12backlinks-com-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- baseURL: https://12backlinks.com
  baseurl_source: declared
  description: The Account API from 12backlinks — 1 operation(s) for account.
  name: 12backlinks Account API
  slug: 12backlinks-com-account-api
- baseURL: https://12backlinks.com
  baseurl_source: declared
  description: The Analyses API from 12backlinks — 1 operation(s) for analyses.
  name: 12backlinks Analyses API
  slug: 12backlinks-com-analyses-api
- baseURL: https://12backlinks.com
  baseurl_source: declared
  description: The Batches API from 12backlinks — 2 operation(s) for batches.
  name: 12backlinks Batches API
  slug: 12backlinks-com-batches-api
- baseURL: https://12backlinks.com
  baseurl_source: declared
  description: The Link Gaps API from 12backlinks — 3 operation(s) for link gaps.
  name: 12backlinks Link Gaps API
  slug: 12backlinks-com-link-gaps-api
- baseURL: https://12backlinks.com
  baseurl_source: declared
  description: The Markets API from 12backlinks — 1 operation(s) for markets.
  name: 12backlinks Markets API
  slug: 12backlinks-com-markets-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/12backlinks-com/agentic-access/12backlinks-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/12backlinks-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/12backlinks-com/rules/12backlinks-com-rules.yml
  title: ''
  type: Spectral
  url: rules/12backlinks-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/12backlinks-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/12backlinks-com/conventions/12backlinks-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/12backlinks-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/12backlinks-com/conventions/12backlinks-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/12backlinks-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/12backlinks-com/authentication/12backlinks-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/12backlinks-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/12backlinks-com/errors/12backlinks-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/12backlinks-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/12backlinks-com/conformance/12backlinks-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/12backlinks-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/12backlinks-com/hosts/12backlinks-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/12backlinks-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/12backlinks-com/vendors/12backlinks-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/12backlinks-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/12backlinks-com/security/12backlinks-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/12backlinks-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://12backlinks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://12backlinks.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://12backlinks.com/api/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://12backlinks.com/terms
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://12backlinks.com/api/mcp
  - status: 200
    url: https://12backlinks.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: 12backlinks provides a French-language SEO tool that helps users determine how many backlinks are needed to rank on the first page of Google for a given keyword. The service offers a bulk analysis feature, explains the concept of backlinks as votes of trust, and emphasizes the importance of quality content and links for SEO success. It exposes an API and MCP for programmatic access to backlink calculations.
image: https://12backlinks.com/logo.png
layout: provider
modified: '2026-10-31'
name: 12backlinks
nav: Providers
network: true
overview: '12backlinks publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Analyses API, Batches API, and 2 more. Tagged areas include SEO, Backlinks, Marketing, and French.


  The 12backlinks catalog on APIs.io includes 1 Spectral governance ruleset.


  12backlinks'' developer surface includes authentication, documentation, API reference, and 12 more developer resources.'
plans:
- name: 12Backlinks Com Plans Pricing
  plan_count: 0
  slug: 12backlinks-com-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: 12backlinks API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: 12backlinks-com-rules
scopes:
- name: 12Backlinks Com Scopes
  scope_count: 0
  slug: 12backlinks-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 5.3
    contract_governance: 31.8
    contract_quality: 49.2
    developer_ergonomics: 26.7
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 12Backlinks Com Authentication
  slug: 12backlinks-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 12Backlinks Com Domain Security
  slug: 12backlinks-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: 12backlinks-main
  slug: 12backlinks-com-main
slug: 12backlinks-com
tags:
- SEO
- Backlinks
- Marketing
- French
website: https://12backlinks.com/
---
