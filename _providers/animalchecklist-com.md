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
  band_gated_from: agent-native
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 23
  human_in_the_loop: 1
  name: Animalchecklist Com Agentic Access
  operation_count: 41
  slug: animalchecklist-com-agentic-access
  summary_line: 41 operations · 23 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://animalchecklist.com/api/v1
  baseurl_source: declared
  description: Optional sign-in and private data rights.
  name: animalchecklist-com Account API
  slug: animalchecklist-com-account-api
- baseURL: https://animalchecklist.com/api/v1
  baseurl_source: declared
  description: Public animal data. No key, CORS open.
  name: animalchecklist-com Catalogue API
  slug: animalchecklist-com-catalogue-api
- baseURL: https://animalchecklist.com/api/v1
  baseurl_source: declared
  description: Client error reports.
  name: animalchecklist-com Diagnostics API
  slug: animalchecklist-com-diagnostics-api
- baseURL: https://animalchecklist.com/api/v1
  baseurl_source: declared
  description: The Leaderboard API from animalchecklist-com — 1 operation(s) for leaderboard.
  name: animalchecklist-com Leaderboard API
  slug: animalchecklist-com-leaderboard-api
- baseURL: https://animalchecklist.com/api/v1
  baseurl_source: declared
  description: The Quiz API from animalchecklist-com — 6 operation(s) for quiz.
  name: animalchecklist-com Quiz API
  slug: animalchecklist-com-quiz-api
- baseURL: https://animalchecklist.com/api/v1
  baseurl_source: declared
  description: Photo suggestions for signed-in accounts.
  name: animalchecklist-com Recognition API
  slug: animalchecklist-com-recognition-api
- baseURL: https://animalchecklist.com/api/v1
  baseurl_source: declared
  description: One person's private checklist. Needs their sync code.
  name: animalchecklist-com Sightings API
  slug: animalchecklist-com-sightings-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/animalchecklist-com/agentic-access/animalchecklist-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/animalchecklist-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/animalchecklist-com/rules/animalchecklist-com-rules.yml
  title: ''
  type: Spectral
  url: rules/animalchecklist-com-rules.yml
- group: design
  href: https://artifacts.apis.io/animalchecklist-com/json-ld/animalchecklist-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/animalchecklist-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/animalchecklist-com/vocabulary/animalchecklist-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/animalchecklist-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/animalchecklist-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/animalchecklist-com/data-model/animalchecklist-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/animalchecklist-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/animalchecklist-com/security/animalchecklist-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/animalchecklist-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/animalchecklist-com/errors/animalchecklist-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/animalchecklist-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/animalchecklist-com/conformance/animalchecklist-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/animalchecklist-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/animalchecklist-com/llms/animalchecklist-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/animalchecklist-com-llms.txt
- group: other
  href: https://artifacts.apis.io/animalchecklist-com/a2a/animalchecklist-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/animalchecklist-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/animalchecklist-com/mcp/animalchecklist-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/animalchecklist-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/animalchecklist-com/well-known/animalchecklist-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/animalchecklist-com-security.txt
- group: agent
  href: https://artifacts.apis.io/animalchecklist-com/well-known/animalchecklist-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/animalchecklist-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/animalchecklist-com/hosts/animalchecklist-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/animalchecklist-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/animalchecklist-com/vendors/animalchecklist-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/animalchecklist-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/animalchecklist-com/authentication/animalchecklist-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/animalchecklist-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/animalchecklist-com/security/animalchecklist-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/animalchecklist-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/animalchecklist-com/security/animalchecklist-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/animalchecklist-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://animalchecklist.com/
- group: docs
  title: ''
  type: Documentation
  url: https://animalchecklist.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://animalchecklist.com/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://animalchecklist.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://animalchecklist.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://animalchecklist.com/privacy
created: '2026-10-29'
description: Animal Checklist provides a free animal sighting checklist app and public API for browsing a catalog of over 950,000 animal entries. Users can search by common or scientific name, track sightings, and integrate with AI-powered photo recognition. The API offers keyless read access to the animal catalogue, with optional authenticated endpoints for syncing personal lists and photo recognition. It supports multiple languages, pagination, batch queries, and follows OpenAPI 3.1 specifications.
image: https://animalchecklist.com/og.png
json_schemas:
- name: Animal
  property_count: 17
  slug: animalchecklist-com-animal
- name: AnimalSummary
  property_count: 11
  slug: animalchecklist-com-animal-summary
- name: BreedDefinition
  property_count: 9
  slug: animalchecklist-com-breed-definition
- name: InatTaxonDetail
  property_count: 25
  slug: animalchecklist-com-inat-taxon-detail
- name: QuizState
  property_count: 8
  slug: animalchecklist-com-quiz-state
- name: ReferenceTaxon
  property_count: 16
  slug: animalchecklist-com-reference-taxon
jsonld:
- class_count: 15
  name: Animalchecklist Com Context
  property_count: 63
  slug: animalchecklist-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at animalchecklist.com.
  name: animalchecklist-com MCP Server
  slug: animalchecklist-com-mcp-yml
modified: '2026-10-29'
name: animalchecklist-com
nav: Providers
network: true
overview: 'animalchecklist-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Catalogue API, Diagnostics API, and 4 more. Tagged areas include Company, Animals, Checklist, Mobile App, and Free.


  The animalchecklist-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  animalchecklist-com''s developer surface includes authentication, documentation, API reference, support, and 21 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: animalchecklist-com API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: animalchecklist-com-rules
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 67.5
    developer_ergonomics: 24.4
    discoverability: 75.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/animalchecklist-com/animalchecklist-com-2026-11-03T120841.png
security:
- kind: authentication
  name: Animalchecklist Com Authentication
  slug: animalchecklist-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Animalchecklist Com Domain Security
  slug: animalchecklist-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Animalchecklist Com Vulnerability Disclosure
  slug: animalchecklist-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: animalchecklist-com-play-quiz-round
  slug: animalchecklist-com-play-quiz-round
- name: animalchecklist-com-recognize-animal
  slug: animalchecklist-com-recognize-animal
- name: animalchecklist-com-sightings-sync
  slug: animalchecklist-com-sightings-sync
slug: animalchecklist-com
tags:
- Company
- Animals
- Checklist
- Mobile App
- Free
website: https://animalchecklist.com/
---
