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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bezal Ai Agentic Access
  operation_count: 6
  slug: bezal-ai-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- baseURL: https://bezal.ai/api/v1
  baseurl_source: declared
  description: The Businesses API from Bezal — 2 operation(s) for businesses.
  name: Bezal Businesses API
  slug: bezal-ai-businesses-api
- baseURL: https://bezal.ai/api/v1
  baseurl_source: declared
  description: The Categories API from Bezal — 1 operation(s) for categories.
  name: Bezal Categories API
  slug: bezal-ai-categories-api
- baseURL: https://bezal.ai/api/v1
  baseurl_source: declared
  description: The Health API from Bezal — 1 operation(s) for health.
  name: Bezal Health API
  slug: bezal-ai-health-api
- baseURL: https://bezal.ai/api/v1
  baseurl_source: declared
  description: The Requests API from Bezal — 1 operation(s) for requests.
  name: Bezal Requests API
  slug: bezal-ai-requests-api
- baseURL: https://bezal.ai/api/v1
  baseurl_source: declared
  description: The Open API API from Bezal — 1 operation(s) for open api.
  name: Bezal Open API
  slug: bezal-ai-open-api-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/bezal-ai/agentic-access/bezal-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bezal-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bezal-ai/rules/bezal-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/bezal-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/bezal-ai/json-ld/bezal-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bezal-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/bezal-ai/vocabulary/bezal-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bezal-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bezal-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bezal-ai/data-model/bezal-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bezal-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/bezal-ai/errors/bezal-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bezal-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bezal-ai/conformance/bezal-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bezal-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bezal-ai/llms/bezal-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bezal-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/bezal-ai/well-known/bezal-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bezal-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bezal-ai/hosts/bezal-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bezal-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bezal-ai/vendors/bezal-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bezal-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://bezal.ai/login
- group: auth
  href: https://artifacts.apis.io/bezal-ai/authentication/bezal-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bezal-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bezal-ai/security/bezal-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bezal-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bezal.ai/
created: '2026-11-02'
description: Bezal provides an AI‑powered platform that acts as a virtual operations manager for local businesses. Their AI assistant, Jewel, helps find clients, drafts outreach, manages contacts, and runs back‑office tasks through simple conversational interactions, aiming to streamline lead generation and customer engagement for small enterprises.
image: https://bezal.ai/opengraph-image?eafa2e7f5d50e988
json_schemas:
- name: Business
  property_count: 19
  slug: bezal-ai-business
- name: Category
  property_count: 2
  slug: bezal-ai-category
- name: Health
  property_count: 4
  slug: bezal-ai-health
jsonld:
- class_count: 5
  name: Bezal Ai Context
  property_count: 27
  slug: bezal-ai-context
layout: provider
modified: '2026-11-02'
name: Bezal
nav: Providers
network: true
overview: 'Bezal publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Businesses API, Categories API, Health API, and 2 more. Tagged areas include Company, Artificial Intelligence, Software-as-a-Service, Local Business, and Lead Generation.


  The Bezal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bezal''s developer surface includes authentication and 15 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Bezal API Rules
  rule_count: 55
  severity_counts:
    error: 52
    hint: 0
    info: 2
    warn: 1
  slug: bezal-ai-rules
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    contract_governance: 22.0
    contract_quality: 61.9
    developer_ergonomics: 13.7
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bezal Ai Authentication
  slug: bezal-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Bezal Ai Domain Security
  slug: bezal-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: bezal-ai-create-quote-request
  slug: bezal-ai-create-quote-request
slug: bezal-ai
tags:
- Company
- Artificial Intelligence
- Software-as-a-Service
- Local Business
- Lead Generation
- Automation
website: https://bezal.ai/
---
