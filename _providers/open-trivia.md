---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Open Trivia Agentic Access
  operation_count: 5
  slug: open-trivia-agentic-access
  summary_line: 5 operations
api_count: 4
apis:
- baseURL: https://opentdb.com
  baseurl_source: declared
  description: Operations for discovering trivia category metadata and counts.
  name: Open Trivia Database Categories API
  slug: open-trivia-categories-api
- baseURL: https://opentdb.com
  baseurl_source: declared
  description: Operations for retrieving trivia questions from the database.
  name: Open Trivia Database Questions API
  slug: open-trivia-questions-api
- baseURL: https://opentdb.com
  baseurl_source: declared
  description: Operations for inspecting overall database statistics.
  name: Open Trivia Database Statistics API
  slug: open-trivia-statistics-api
- baseURL: https://opentdb.com
  baseurl_source: declared
  description: Operations for managing session tokens that prevent duplicate questions.
  name: Open Trivia Database Tokens API
  slug: open-trivia-tokens-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Open Trivia Database Categories API
  slug: open-open-trivia-categories-api
- collection_type: open
  name: Open Trivia Database Categories Questions API
  slug: open-open-trivia-questions-api
- collection_type: open
  name: Open Trivia Database Categories Statistics API
  slug: open-open-trivia-statistics-api
- collection_type: open
  name: Open Trivia Database Categories Tokens API
  slug: open-open-trivia-tokens-api
- collection_type: open
  name: Open Trivia Database API
  slug: open-open-trivia
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-trivia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-trivia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opentdb.com
- group: docs
  title: ''
  type: Documentation
  url: https://opentdb.com/api_config.php
- group: operate
  title: ''
  type: Support
  url: https://opentdb.com/contact.php
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opentdb.com/terms.php
- group: commercial
  title: ''
  type: License
  url: https://creativecommons.org/licenses/by-sa/4.0/
- group: other
  title: ''
  type: Donate
  url: https://ko-fi.com/pixeltailgames
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: Community SDKs and Integrations
  type: CommunityIntegrations
  url: https://github.com/topics/opentdb
- group: build
  title: Open Trivia DB Wrapper (TypeScript / JavaScript)
  type: SDKs
  url: https://github.com/Elitezen/open-trivia-db-wrapper
- group: build
  title: Python Trivia API (Python)
  type: SDKs
  url: https://github.com/MaT1g3R/Python-Trivia-API
- group: build
  title: OpenTDB4j (Java)
  type: SDKs
  url: https://github.com/crnvl/OpenTDB4j
- group: build
  title: opentdb-api (JavaScript)
  type: SDKs
  url: https://github.com/blobfysh/opentdb-api
- group: build
  title: MCP Server (Community — pipeworx-io)
  type: Tools
  url: https://github.com/pipeworx-io/mcp-trivia
- group: build
  title: Discord Trivia Bot (Community)
  type: Tools
  url: https://github.com/LakeYS/Discord-Trivia-Bot
- group: build
  title: OTDB Source Download Script (Community)
  type: Tools
  url: https://github.com/QuartzWarrior/OTDB-Source
- group: build
  title: Ignite Bowser Trivia App (TypeScript)
  type: CodeExamples
  url: https://github.com/robinheinze/ignite-trivia
- group: build
  title: React Native Trivia Quiz (JavaScript)
  type: CodeExamples
  url: https://github.com/computationalcore/react-native-trivia-quiz
- group: build
  title: Vue Quiz App (Vue 3)
  type: CodeExamples
  url: https://github.com/supershaneski/vue-quiz-app
created: '2026-05-28'
description: 'The Open Trivia Database (OpenTDB) is a free, user-contributed trivia question database operated by Pixeltail Games LLC. It offers a JSON REST API for retrieving thousands of community-verified trivia questions across 24 categories and three difficulty levels, with optional session tokens to prevent duplicate questions. The service is licensed Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0), is free at the point of use, and enforces a single throttling rule: one request per IP every five seconds.'
examples:
- key_count: 2
  name: Open Trivia Category Count Response Example
  slug: open-trivia-category-count-response-example
- key_count: 2
  name: Open Trivia Category Example
  slug: open-trivia-category-example
- key_count: 1
  name: Open Trivia Category List Response Example
  slug: open-trivia-category-list-response-example
- key_count: 4
  name: Open Trivia Category Question Count Example
  slug: open-trivia-category-question-count-example
- key_count: 2
  name: Open Trivia Global Count Response Example
  slug: open-trivia-global-count-response-example
- key_count: 4
  name: Open Trivia Global Counts Example
  slug: open-trivia-global-counts-example
- key_count: 6
  name: Open Trivia Question Example
  slug: open-trivia-question-example
- key_count: 2
  name: Open Trivia Question Response Example
  slug: open-trivia-question-response-example
- key_count: 3
  name: Open Trivia Token Response Example
  slug: open-trivia-token-response-example
image: https://opentdb.com/images/logo-banner.png
json_schemas:
- name: CategoryCountResponse
  property_count: 2
  slug: open-trivia-category-count-response
- name: CategoryListResponse
  property_count: 1
  slug: open-trivia-category-list-response
- name: CategoryQuestionCount
  property_count: 4
  slug: open-trivia-category-question-count
- name: Category
  property_count: 2
  slug: open-trivia-category
- name: GlobalCountResponse
  property_count: 2
  slug: open-trivia-global-count-response
- name: GlobalCounts
  property_count: 4
  slug: open-trivia-global-counts
- name: QuestionResponse
  property_count: 3
  slug: open-trivia-question-response
- name: Question
  property_count: 6
  slug: open-trivia-question
- name: TokenResponse
  property_count: 3
  slug: open-trivia-token-response
json_structures:
- name: Open Trivia Category Count Response Structure
  property_count: 2
  slug: open-trivia-category-count-response-structure
- name: Open Trivia Category List Response Structure
  property_count: 1
  slug: open-trivia-category-list-response-structure
- name: Open Trivia Category Question Count Structure
  property_count: 4
  slug: open-trivia-category-question-count-structure
- name: Open Trivia Category Structure
  property_count: 2
  slug: open-trivia-category-structure
- name: Open Trivia Global Count Response Structure
  property_count: 2
  slug: open-trivia-global-count-response-structure
- name: Open Trivia Global Counts Structure
  property_count: 4
  slug: open-trivia-global-counts-structure
- name: Open Trivia Question Response Structure
  property_count: 3
  slug: open-trivia-question-response-structure
- name: Open Trivia Question Structure
  property_count: 6
  slug: open-trivia-question-structure
- name: Open Trivia Token Response Structure
  property_count: 3
  slug: open-trivia-token-response-structure
jsonld:
- class_count: 9
  name: Open Trivia Context
  property_count: 25
  slug: open-trivia-context
layout: provider
modified: '2026-05-30'
name: Open Trivia Database
nav: Providers
network: true
overview: 'Open Trivia Database publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Questions API, Statistics API, and 1 more. Tagged areas include Trivia, Games And Comics, Quiz, Open Data, and Public APIs.


  The Open Trivia Database catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Open Trivia Database''s developer surface includes documentation, support, tooling, code examples, and 16 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 1
  name: Open Trivia Rate Limits
  slug: open-trivia-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Open Trivia Database API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: open-trivia-jsonschema-spectral-rules
- effective_rule_count: 77
  extends:
  - spectral:oas
  name: Open Trivia Database API Rules
  rule_count: 36
  severity_counts:
    error: 12
    hint: 0
    info: 6
    warn: 18
  slug: open-trivia-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 36.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 30.3
    developer_ergonomics: 26.2
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 21.1
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-trivia/refs/heads/main/screenshots/open-trivia-2026-06-20T190855.png
security:
- kind: domain-security
  name: Open Trivia Domain Security
  slug: open-trivia-domain-security
  summary_line: TLSv1.3 · HSTS
slug: open-trivia
tags:
- Trivia
- Games And Comics
- Quiz
- Open Data
- Public APIs
- Open-Source
website: https://opentdb.com
---
