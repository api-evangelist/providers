---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Targetwise Ai Agentic Access
  operation_count: 12
  slug: targetwise-ai-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 1
apis:
- baseURL: https://targetwise.ai
  baseurl_source: declared
  description: Free authenticated account-status checks.
  name: targetwise-ai Account API
  slug: targetwise-ai-account-api
- baseURL: https://targetwise.ai
  baseurl_source: declared
  description: Resolve company form fields.
  name: targetwise-ai Autocomplete API
  slug: targetwise-ai-autocomplete-api
- baseURL: https://targetwise.ai
  baseurl_source: declared
  description: Bounded company identity search.
  name: targetwise-ai Companies API
  slug: targetwise-ai-companies-api
- baseURL: https://targetwise.ai
  baseurl_source: declared
  description: Bounded employee search and selective contact details.
  name: targetwise-ai Employees API
  slug: targetwise-ai-employees-api
- baseURL: https://targetwise.ai
  baseurl_source: declared
  description: Normalize one selected company or known contact.
  name: targetwise-ai Enrichment API
  slug: targetwise-ai-enrichment-api
- baseURL: https://targetwise.ai
  baseurl_source: declared
  description: Bounded candidate discovery. Search before enriching.
  name: targetwise-ai Prospecting API
  slug: targetwise-ai-prospecting-api
- baseURL: https://targetwise.ai
  baseurl_source: declared
  description: Resolve one specific field or permitted business email.
  name: targetwise-ai Resolution API
  slug: targetwise-ai-resolution-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/targetwise-ai/agentic-access/targetwise-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/targetwise-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/targetwise-ai/rules/targetwise-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/targetwise-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/targetwise-ai/json-ld/targetwise-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/targetwise-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/targetwise-ai/vocabulary/targetwise-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/targetwise-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/targetwise-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/targetwise-ai/data-model/targetwise-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/targetwise-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/targetwise-ai/errors/targetwise-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/targetwise-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/targetwise-ai/conformance/targetwise-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/targetwise-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/targetwise-ai/llms/targetwise-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/targetwise-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/targetwise-ai/well-known/targetwise-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/targetwise-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/targetwise-ai/hosts/targetwise-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/targetwise-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/targetwise-ai/vendors/targetwise-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/targetwise-ai-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://targetwise.ai/trust
- group: auth
  href: https://artifacts.apis.io/targetwise-ai/authentication/targetwise-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/targetwise-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/targetwise-ai/security/targetwise-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/targetwise-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://targetwise.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://targetwise.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://targetwise.ai/developers
- group: docs
  title: ''
  type: APIReference
  url: https://targetwise.ai/developers/api
- group: start
  title: ''
  type: GettingStarted
  url: https://targetwise.ai/developers/quickstart
- group: operate
  title: ''
  type: Support
  url: https://targetwise.ai/company/contact
- group: company
  title: ''
  type: Blog
  url: https://targetwise.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://targetwise.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://targetwise.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://targetwise.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://targetwise.ai/legal/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://targetwise.ai/api/mcp
  - status: 200
    url: https://targetwise.ai/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: TargetWise provides B2B contact data enrichment through a REST API and MCP, delivering work email addresses, business phone numbers, and company information by aggregating over 15 specialist data sources. The platform enables software, automation, and AI agents to enrich leads and CRM records with accurate, normalized contact data, offering waterfall enrichment, company context, and reverse‑email lookup capabilities.
image: https://targetwise.ai/opengraph-image.png?3d6d3b838f3a1e40
json_schemas:
- name: AccountStatus
  property_count: 16
  slug: targetwise-ai-account-status
jsonld:
- class_count: 2
  name: Targetwise Ai Context
  property_count: 17
  slug: targetwise-ai-context
layout: provider
modified: '2026-10-31'
name: targetwise-ai
nav: Providers
network: true
overview: 'targetwise-ai publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Autocomplete API, Companies API, and 4 more. Tagged areas include B2B, Data Enrichment, Contact API, MCP, and SaaS.


  The targetwise-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  targetwise-ai''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 19 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: targetwise-ai API Rules
  rule_count: 17
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 0
  slug: targetwise-ai-rules
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 68.4
    catalog_earned_first_party: 0.0
    catalog_gap: 46.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 70.9
    contract_quality: 55.4
    developer_ergonomics: 63.6
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Targetwise Ai Authentication
  slug: targetwise-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Targetwise Ai Domain Security
  slug: targetwise-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: company-enrichment
  slug: targetwise-ai-company-enrichment
- name: find-work-email
  slug: targetwise-ai-find-work-email
- name: reverse-email-lookup
  slug: targetwise-ai-reverse-email-lookup
- name: search-companies
  slug: targetwise-ai-search-companies
slug: targetwise-ai
tags:
- B2B
- Data Enrichment
- Contact API
- MCP
- SaaS
website: https://targetwise.ai/
---
