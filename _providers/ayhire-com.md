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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 112
  human_in_the_loop: 8
  name: Ayhire Com Agentic Access
  operation_count: 188
  slug: ayhire-com-agentic-access
  summary_line: 188 operations · 112 acting · 8 human-in-the-loop
api_count: 1
apis:
- baseURL: https://ayhire.com
  baseurl_source: declared
  description: Who is calling, this hour's usage, and revoking the key in use.
  name: ayhire-com Account API
  slug: ayhire-com-account-api
- baseURL: https://ayhire.com
  baseurl_source: declared
  description: 'A company''s public engineering ecosystem: its official GitHub organizations by reciprocal evidence, their public members and contributors, the people LinkedIn reports there, and identity matches for r'
  name: ayhire-com Company maps API
  slug: ayhire-com-company-maps-api
- baseURL: https://ayhire.com
  baseurl_source: declared
  description: Workspace webhooks and the workspace's ATS.
  name: ayhire-com Integrations API
  slug: ayhire-com-integrations-api
- baseURL: https://ayhire.com
  baseurl_source: declared
  description: Analyze developers from their public GitHub work, search the people AyHire has analyzed, and find the people behind repos.
  name: ayhire-com People API
  slug: ayhire-com-people-api
- baseURL: https://ayhire.com
  baseurl_source: declared
  description: Paid research jobs an agent can start, resume, check and cancel, within a budget declared up front.
  name: ayhire-com Research API
  slug: ayhire-com-research-api
- baseURL: https://ayhire.com
  baseurl_source: declared
  description: 'Open positions: their criteria, their searches, the people in them and your decisions.'
  name: ayhire-com Roles API
  slug: ayhire-com-roles-api
- baseURL: https://ayhire.com
  baseurl_source: declared
  description: People a workspace wants to hear about, and what changed.
  name: ayhire-com Watching API
  slug: ayhire-com-watching-api
- baseURL: https://ayhire.com
  baseurl_source: declared
  description: One workspace per company you hire for, shared with that company's team.
  name: ayhire-com Workspaces API
  slug: ayhire-com-workspaces-api
artifact_total: 21
common:
- group: docs
  title: ''
  type: Documentation
  url: https://ayhire.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://ayhire.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/ayhire-com/agentic-access/ayhire-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ayhire-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/ayhire-com/plans/ayhire-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ayhire-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ayhire-com/rules/ayhire-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ayhire-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ayhire-com/json-ld/ayhire-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ayhire-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ayhire-com/vocabulary/ayhire-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ayhire-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ayhire-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ayhire-com/data-model/ayhire-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ayhire-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/ayhire-com/authentication/ayhire-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ayhire-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/ayhire-com/errors/ayhire-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ayhire-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ayhire-com/conformance/ayhire-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ayhire-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ayhire-com/llms/ayhire-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ayhire-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ayhire-com/well-known/ayhire-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ayhire-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ayhire-com/hosts/ayhire-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ayhire-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ayhire-com/vendors/ayhire-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ayhire-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://ayhire.com/auth/sign-in
- group: auth
  href: https://artifacts.apis.io/ayhire-com/security/ayhire-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ayhire-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ayhire.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://ayhire.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ayhire.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ayhire.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://ayhire.com/blog
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://ayhire.com/openapi.json
  - status: 401
    url: https://ayhire.com/mcp
  - status: 200
    url: https://ayhire.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: AyHire is a platform that helps hiring managers find and evaluate software engineers by analyzing their public GitHub activity. It generates concise candidate summaries, explains why each engineer matches the role, and provides links to supporting evidence from their repositories. The service aims to reduce bias and speed up the recruitment process by surfacing real work and open‑source contributions.
image: https://ayhire.com/opengraph-image.png?opengraph-image.3zztm47x1_hxh.png
json_schemas:
- name: OutcomeEvent
  property_count: 18
  slug: ayhire-com-outcome-event
- name: RepositoryKnowledge
  property_count: 23
  slug: ayhire-com-repository-knowledge
- name: RoleFunnel
  property_count: 11
  slug: ayhire-com-role-funnel
- name: RolePerson
  property_count: 16
  slug: ayhire-com-role-person
- name: ScrapedCandidate
  property_count: 16
  slug: ayhire-com-scraped-candidate
- name: Watch
  property_count: 11
  slug: ayhire-com-watch
jsonld:
- class_count: 25
  name: Ayhire Com Context
  property_count: 160
  slug: ayhire-com-context
layout: provider
modified: '2026-10-30'
name: ayhire-com
nav: Providers
network: true
overview: 'ayhire-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Company maps API, Integrations API, and 5 more. Tagged areas include Company, Hiring, Developer Tools, Recruiting, and Open Source.


  The ayhire-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ayhire-com''s developer surface includes documentation, API reference, authentication, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Ayhire Com Plans Pricing
  plan_count: 4
  slug: ayhire-com-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: ayhire-com API Rules
  rule_count: 68
  severity_counts:
    error: 54
    hint: 0
    info: 5
    warn: 9
  slug: ayhire-com-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 65.0
    developer_ergonomics: 27.9
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ayhire-com/ayhire-com-2026-11-03T121451.png
security:
- kind: authentication
  name: Ayhire Com Authentication
  slug: ayhire-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ayhire Com Domain Security
  slug: ayhire-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: get-candidate
  slug: ayhire-com-getCandidate
slug: ayhire-com
tags:
- Company
- Hiring
- Developer Tools
- Recruiting
- Open Source
website: https://ayhire.com/
---
