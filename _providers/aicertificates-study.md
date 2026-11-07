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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aicertificates Study Agentic Access
  operation_count: 3
  slug: aicertificates-study-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://aicertificates.study
  baseurl_source: declared
  description: Study guides and exam reference material
  name: AI Certificates Content API
  slug: aicertificates-study-content-api
- baseURL: https://aicertificates.study
  baseurl_source: declared
  description: The 12-question readiness check and its cohort statistics
  name: AI Certificates Readiness API
  slug: aicertificates-study-readiness-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/aicertificates-study/agentic-access/aicertificates-study-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aicertificates-study-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aicertificates-study/rules/aicertificates-study-rules.yml
  title: ''
  type: Spectral
  url: rules/aicertificates-study-rules.yml
- group: design
  href: https://artifacts.apis.io/aicertificates-study/json-ld/aicertificates-study-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aicertificates-study-context.jsonld
- group: design
  href: https://artifacts.apis.io/aicertificates-study/vocabulary/aicertificates-study-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aicertificates-study-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aicertificates-study/data-model/aicertificates-study-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aicertificates-study-data-model.yml
- group: design
  href: https://artifacts.apis.io/aicertificates-study/errors/aicertificates-study-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aicertificates-study-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aicertificates-study/conformance/aicertificates-study-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aicertificates-study-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aicertificates-study/llms/aicertificates-study-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aicertificates-study-llms.txt
- group: agent
  href: https://artifacts.apis.io/aicertificates-study/mcp/aicertificates-study-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aicertificates-study-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aicertificates-study/well-known/aicertificates-study-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aicertificates-study-well-known.yml
- group: other
  href: https://artifacts.apis.io/aicertificates-study/hosts/aicertificates-study-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aicertificates-study-hosts.yml
- group: other
  href: https://artifacts.apis.io/aicertificates-study/vendors/aicertificates-study-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aicertificates-study-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aicertificates.study/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aicertificates.study/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://aicertificates.study/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aicertificates.study/developers
- group: docs
  title: ''
  type: APIReference
  url: https://aicertificates.study/changelog
- group: auth
  href: https://artifacts.apis.io/aicertificates-study/security/aicertificates-study-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aicertificates-study-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aicertificates.study/
created: '2026-11-01'
description: AI Certificates provides free and paid practice exams for Anthropic Claude certifications. Run by Matthew Hartman, the site offers original practice questions written from official exam blueprints, detailed answer explanations, and readiness checks. It includes free exam forms for all four Claude tracks and premium full-access content, aiming to help candidates prepare ethically without using recalled exam content.
image: https://aicertificates.study/opengraph-image-1c1a04?364edca5f927e43a
json_schemas:
- name: ReadinessStats
  property_count: 1
  slug: aicertificates-study-readiness-stats
jsonld:
- class_count: 3
  name: Aicertificates Study Context
  property_count: 10
  slug: aicertificates-study-context
layout: provider
mcp_servers:
- description: Remote MCP server at aicertificates.study.
  name: AI Certificates MCP Server
  slug: aicertificates-study-mcp-yml
modified: '2026-11-01'
name: AI Certificates
nav: Providers
network: true
overview: 'AI Certificates publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Content API and Readiness API. Tagged areas include Education, Artificial Intelligence, Certification, Practice Exams, and Anthropic.


  The AI Certificates catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI Certificates'' developer surface includes documentation, API reference, and 17 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AI Certificates API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: aicertificates-study-rules
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 56.2
    catalog_earned_first_party: 0.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 56.3
    developer_ergonomics: 13.1
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aicertificates Study Domain Security
  slug: aicertificates-study-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aicertificates-study
tags:
- Education
- Artificial Intelligence
- Certification
- Practice Exams
- Anthropic
website: https://aicertificates.study/
---
