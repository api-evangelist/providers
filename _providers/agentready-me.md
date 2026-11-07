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
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Agentready Me Agentic Access
  operation_count: 9
  slug: agentready-me-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 2
apis:
- baseURL: https://www.agentready.me
  baseurl_source: declared
  description: Public availability information for AgentReady checkout.
  name: AgentReady.me Commerce API
  slug: agentready-me-commerce-api
- baseURL: https://www.agentready.me
  baseurl_source: declared
  description: Free, evidence-status diagnostics with explicit static/runtime limitations.
  name: AgentReady.me Diagnostics API
  slug: agentready-me-diagnostics-api
- baseURL: https://www.agentready.me
  baseurl_source: declared
  description: Evidence-backed agent-readiness analysis for public URLs.
  name: AgentReady.me Scans API
  slug: agentready-me-scans-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/agentready-me/agentic-access/agentready-me-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentready-me-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentready-me/rules/agentready-me-rules.yml
  title: ''
  type: Spectral
  url: rules/agentready-me-rules.yml
- group: design
  href: https://artifacts.apis.io/agentready-me/json-ld/agentready-me-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentready-me-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentready-me/vocabulary/agentready-me-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentready-me-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentready-me/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentready-me/data-model/agentready-me-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentready-me-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentready-me/errors/agentready-me-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentready-me-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentready-me/conformance/agentready-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentready-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentready-me/llms/agentready-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentready-me-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentready-me/well-known/agentready-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentready-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentready-me/hosts/agentready-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentready-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentready-me/vendors/agentready-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentready-me-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.agentready.me/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Reload
- group: docs
  title: ''
  type: APIReference
  url: https://www.agentready.me/developers
- group: auth
  href: https://artifacts.apis.io/agentready-me/security/agentready-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentready-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agentready.me/
- group: docs
  title: ''
  type: Documentation
  url: https://www.agentready.me/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agentready.me/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agentready.me/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agentready.me/privacy
- group: operate
  title: ''
  type: Contact
  url: https://www.agentready.me/contact
- group: company
  title: ''
  type: About
  url: https://www.agentready.me/about
created: '2026-11-01'
description: AgentReady.me provides agent journey audits and verified fixes, helping AI agents discover, cite, and recommend websites. Their platform offers public scans, privacy‑focused assessments, and integration with tools like ChatGPT, Perplexity, and Google AI. Users can obtain copy‑paste prompts for various code assistants to improve site visibility for agents.
image: https://www.agentready.me/opengraph-image?3ab1fe76911c55e3
json_schemas:
- name: PublicScanRequest
  property_count: 0
  slug: agentready-me-public-scan-request
- name: ScanResult
  property_count: 0
  slug: agentready-me-scan-result
jsonld:
- class_count: 23
  name: Agentready Me Context
  property_count: 87
  slug: agentready-me-context
layout: provider
modified: '2026-11-01'
name: AgentReady.me
nav: Providers
network: true
overview: 'AgentReady.me publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Commerce API, Diagnostics API, and Scans API. Tagged areas include Artificial Intelligence, Agent Readiness, WebAudit, SEO, and Platform.


  The AgentReady.me catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentReady.me''s developer surface includes API reference, documentation, pricing, and 20 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: AgentReady.me API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: agentready-me-rules
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 59.8
    developer_ergonomics: 14.8
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentready Me Domain Security
  slug: agentready-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: scan
  slug: agentready-me-scan
slug: agentready-me
tags:
- Artificial Intelligence
- Agent Readiness
- WebAudit
- SEO
- Platform
website: https://www.agentready.me/
---
