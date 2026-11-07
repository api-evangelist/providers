---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: derived
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Veritahire Com Agentic Access
  operation_count: 13
  slug: veritahire-com-agentic-access
  summary_line: 13 operations · 2 acting
api_count: 1
apis:
- baseURL: https://veritahire.com
  baseurl_source: declared
  description: The Account API from veritahire-com — 1 operation(s) for account.
  name: veritahire-com Account API
  slug: veritahire-com-account-api
- baseURL: https://veritahire.com
  baseurl_source: declared
  description: The Employer profile API from veritahire-com — 1 operation(s) for employer profile.
  name: veritahire-com Employer profile API
  slug: veritahire-com-employer-profile-api
- baseURL: https://veritahire.com
  baseurl_source: declared
  description: The Free, no key API from veritahire-com — 8 operation(s) for free, no key.
  name: veritahire-com Free, no key API
  slug: veritahire-com-free-no-key-api
- baseURL: https://veritahire.com
  baseurl_source: declared
  description: The Hiring Market.php API from veritahire-com — 1 operation(s) for hiring market.php.
  name: veritahire-com Hiring Market.php API
  slug: veritahire-com-hiring-market-php-api
- baseURL: https://veritahire.com
  baseurl_source: declared
  description: The Hiring velocity API from veritahire-com — 1 operation(s) for hiring velocity.
  name: veritahire-com Hiring velocity API
  slug: veritahire-com-hiring-velocity-api
- baseURL: https://veritahire.com
  baseurl_source: declared
  description: The Postings API from veritahire-com — 1 operation(s) for postings.
  name: veritahire-com Postings API
  slug: veritahire-com-postings-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/veritahire-com/agentic-access/veritahire-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/veritahire-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/veritahire-com/plans/veritahire-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/veritahire-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/veritahire-com/rules/veritahire-com-rules.yml
  title: ''
  type: Spectral
  url: rules/veritahire-com-rules.yml
- group: design
  href: https://artifacts.apis.io/veritahire-com/json-ld/veritahire-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/veritahire-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/veritahire-com/vocabulary/veritahire-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/veritahire-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/veritahire-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/veritahire-com/data-model/veritahire-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/veritahire-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/veritahire-com/authentication/veritahire-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/veritahire-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/veritahire-com/errors/veritahire-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/veritahire-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/veritahire-com/conformance/veritahire-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/veritahire-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/veritahire-com/llms/veritahire-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/veritahire-com-llms.txt
- group: other
  href: https://artifacts.apis.io/veritahire-com/a2a/veritahire-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/veritahire-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/veritahire-com/mcp/veritahire-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/veritahire-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/veritahire-com/mcp/veritahire-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/veritahire-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/veritahire-com/well-known/veritahire-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/veritahire-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/veritahire-com/hosts/veritahire-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/veritahire-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://veritahire.com/terms.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://veritahire.com/privacy.php
- group: start
  title: ''
  type: DeveloperPortal
  url: https://veritahire.com/developers/
- group: auth
  href: https://artifacts.apis.io/veritahire-com/security/veritahire-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/veritahire-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://veritahire.com/
- group: docs
  title: ''
  type: Documentation
  url: https://veritahire.com/developers/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://veritahire.com/openapi.json
created: '2026-10-30'
description: VeritaHire provides a job search platform that connects job seekers with employers, offering real-time job listings, hiring signals, and data APIs. The service includes an API for accessing job data, pricing information, and hiring analytics, supporting integration for staffing firms and AI assistants. It emphasizes verified open daily job feeds and transparent pricing for API access.
json_schemas:
- name: EmployersPage
  property_count: 4
  slug: veritahire-com-employers-page
- name: JobsPage
  property_count: 4
  slug: veritahire-com-jobs-page
- name: VelocityPage
  property_count: 4
  slug: veritahire-com-velocity-page
jsonld:
- class_count: 8
  name: Veritahire Com Context
  property_count: 62
  slug: veritahire-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at veritahire.com.
  name: veritahire-com MCP Server
  slug: veritahire-com-mcp-yml
modified: '2026-10-30'
name: veritahire-com
nav: Providers
network: true
overview: 'veritahire-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Employer profile API, Free, no key API, and 3 more. Tagged areas include Company, Job, Hiring, and Data.


  The veritahire-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  veritahire-com''s developer surface includes authentication, documentation, API reference, and 20 more developer resources.'
plans:
- name: Veritahire Com Plans Pricing
  plan_count: 3
  slug: veritahire-com-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: veritahire-com API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 2
  slug: veritahire-com-rules
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 61.3
    developer_ergonomics: 26.8
    discoverability: 63.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 44.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/veritahire-com/veritahire-com-2026-11-03T145719.png
security:
- kind: authentication
  name: Veritahire Com Authentication
  slug: veritahire-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Veritahire Com Domain Security
  slug: veritahire-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: veritahire-com-obtain-competitive-hiring-report
  slug: veritahire-com-obtain-competitive-hiring-report
slug: veritahire-com
tags:
- Company
- Job
- Hiring
- Data
website: https://veritahire.com/
---
