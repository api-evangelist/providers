---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Kitforai Agentic Access
  operation_count: 8
  slug: kitforai-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 1
apis:
- baseURL: https://kitforai.com
  baseurl_source: spec
  description: The Batch API from Kit For AI — 1 operation(s) for batch.
  name: Kit For AI Batch API
  slug: kitforai-batch-api
- baseURL: https://kitforai.com
  baseurl_source: spec
  description: The Convert API from Kit For AI — 1 operation(s) for convert.
  name: Kit For AI Convert API
  slug: kitforai-convert-api
- baseURL: https://kitforai.com
  baseurl_source: spec
  description: The Knowledge Bases API from Kit For AI — 4 operation(s) for knowledge bases.
  name: Kit For AI Knowledge Bases API
  slug: kitforai-knowledge-bases-api
artifact_total: 10
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://kitforai.com/llm-setup
- group: agent
  href: https://artifacts.apis.io/kitforai/agentic-access/kitforai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kitforai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/kitforai/plans/kitforai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kitforai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/kitforai/rules/kitforai-rules.yml
  title: ''
  type: Spectral
  url: rules/kitforai-rules.yml
- group: design
  href: https://artifacts.apis.io/kitforai/json-ld/kitforai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kitforai-context.jsonld
- group: design
  href: https://artifacts.apis.io/kitforai/vocabulary/kitforai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kitforai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/kitforai/data-model/kitforai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kitforai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/kitforai/changelog/kitforai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kitforai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/kitforai/authentication/kitforai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kitforai-authentication.yml
- group: design
  href: https://artifacts.apis.io/kitforai/errors/kitforai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kitforai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kitforai/conformance/kitforai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kitforai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kitforai/llms/kitforai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kitforai-llms.txt
- group: other
  href: https://artifacts.apis.io/kitforai/hosts/kitforai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kitforai-hosts.yml
- group: other
  href: https://artifacts.apis.io/kitforai/vendors/kitforai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kitforai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://kitforai.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://kitforai.com/changelog
- group: auth
  href: https://artifacts.apis.io/kitforai/security/kitforai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kitforai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kitforai/security/kitforai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kitforai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kitforai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://kitforai.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://kitforai.com/reference
- group: company
  title: ''
  type: Blog
  url: https://kitforai.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://kitforai.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://kitforai.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kitforai.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kitforai.com/legal/privacy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://kitforai.com/api/mcp
  - status: 200
    url: https://kitforai.com/
  reason: no-developer-program
  state: none
created: '2026-10-17'
description: Kit For AI provides a memory layer for AI agents, enabling document conversion, OCR, JSON extraction, and structured data shaping for knowledge bases. It offers tools to turn web pages, PDFs, and images into clean, model‑ready text, supporting retrieval‑augmented generation (RAG) and the Model Context Protocol (MCP). The platform includes a developer portal, pricing plans, and comprehensive documentation for integration with LLMs.
image: https://kitforai.com/opengraph-image.png?opengraph-image.d09baca4.png
jsonld:
- class_count: 2
  name: Kitforai Context
  property_count: 2
  slug: kitforai-context
layout: provider
modified: '2026-10-17'
name: Kit For AI
nav: Providers
network: true
overview: 'Kit For AI publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Batch API, Convert API, and Knowledge Bases API. Tagged areas include Artificial Intelligence, Memory, Document Conversion, RAG, and Knowledge Base.


  The Kit For AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kit For AI''s developer surface includes getting-started guide, changelog, authentication, documentation, API reference, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Kitforai Plans Pricing
  plan_count: 4
  slug: kitforai-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Kit For AI API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: kitforai-rules
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 51.2
    developer_ergonomics: 42.9
    discoverability: 48.2
    operational_transparency: 26.3
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Kitforai Authentication
  slug: kitforai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Kitforai Domain Security
  slug: kitforai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Kitforai Vulnerability Disclosure
  slug: kitforai-vulnerability-disclosure
  summary_line: no policy recorded
slug: kitforai
tags:
- Artificial Intelligence
- Memory
- Document Conversion
- RAG
- Knowledge Base
website: https://kitforai.com/
---
