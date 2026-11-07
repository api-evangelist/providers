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
    agent_card: conformant
    agent_skills: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Citeerbaar Nl Agentic Access
  operation_count: 14
  slug: citeerbaar-nl-agentic-access
  summary_line: 14 operations · 2 acting
api_count: 1
apis:
- baseURL: https://www.citeerbaar.nl/
  baseurl_source: declared
  description: JSON-RPC-endpoints voor MCP-clients en A2A-agents.
  name: Citeerbaar Agents API
  slug: citeerbaar-nl-agents-api
- baseURL: https://www.citeerbaar.nl/
  baseurl_source: declared
  description: Alleen-lezen JSON, CC BY 4.0, bronvermelding naar source_page.
  name: Citeerbaar Open data API
  slug: citeerbaar-nl-open-data-api
- baseURL: https://www.citeerbaar.nl/
  baseurl_source: declared
  description: Statuscontrole en deze beschrijving.
  name: Citeerbaar Status API
  slug: citeerbaar-nl-status-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/citeerbaar-nl/agentic-access/citeerbaar-nl-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/citeerbaar-nl-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/citeerbaar-nl/rules/citeerbaar-nl-rules.yml
  title: ''
  type: Spectral
  url: rules/citeerbaar-nl-rules.yml
- group: design
  href: https://artifacts.apis.io/citeerbaar-nl/json-ld/citeerbaar-nl-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/citeerbaar-nl-context.jsonld
- group: design
  href: https://artifacts.apis.io/citeerbaar-nl/vocabulary/citeerbaar-nl-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/citeerbaar-nl-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/citeerbaar-nl/data-model/citeerbaar-nl-data-model.yml
  title: ''
  type: DataModel
  url: data-model/citeerbaar-nl-data-model.yml
- group: auth
  href: https://artifacts.apis.io/citeerbaar-nl/security/citeerbaar-nl-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/citeerbaar-nl-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/citeerbaar-nl/errors/citeerbaar-nl-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/citeerbaar-nl-problem-types.yml
- group: design
  href: https://artifacts.apis.io/citeerbaar-nl/conformance/citeerbaar-nl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/citeerbaar-nl-conformance.yml
- group: agent
  href: https://artifacts.apis.io/citeerbaar-nl/llms/citeerbaar-nl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citeerbaar-nl-llms.txt
- group: other
  href: https://artifacts.apis.io/citeerbaar-nl/a2a/citeerbaar-nl-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/citeerbaar-nl-a2a.yml
- group: auth
  href: https://artifacts.apis.io/citeerbaar-nl/well-known/citeerbaar-nl-wildbos-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/citeerbaar-nl-wildbos-security.txt
- group: auth
  href: https://artifacts.apis.io/citeerbaar-nl/well-known/citeerbaar-nl-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/citeerbaar-nl-security.txt
- group: auth
  href: https://artifacts.apis.io/citeerbaar-nl/well-known/citeerbaar-nl-estrelle-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/citeerbaar-nl-estrelle-security.txt
- group: auth
  href: https://artifacts.apis.io/citeerbaar-nl/well-known/citeerbaar-nl-citeerbaar-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/citeerbaar-nl-citeerbaar-security.txt
- group: agent
  href: https://artifacts.apis.io/citeerbaar-nl/well-known/citeerbaar-nl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/citeerbaar-nl-well-known.yml
- group: other
  href: https://artifacts.apis.io/citeerbaar-nl/hosts/citeerbaar-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citeerbaar-nl-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.citeerbaar.nl/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.citeerbaar.nl/api/pricing.json
- group: company
  title: ''
  type: Blog
  url: https://www.citeerbaar.nl/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://www.citeerbaar.nl/docs/
- group: auth
  href: https://artifacts.apis.io/citeerbaar-nl/security/citeerbaar-nl-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/citeerbaar-nl-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/citeerbaar-nl/security/citeerbaar-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citeerbaar-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.citeerbaar.nl/
created: '2026-11-03'
description: Citeerbaar maakt bedrijven vindbaar en citeerbaar in AI‑systemen zoals ChatGPT, Claude, Copilot, Gemini en Google AI. Ze bieden technische SEO, content en digitale PR om bedrijven te laten verschijnen in AI‑overzichten en zoekresultaten, met een focus op de Nederlandse markt.
image: https://www.citeerbaar.nl/wp-content/themes/citeerbaar/assets/img/og/home.png?v=1778564891
json_schemas:
- name: Envelope
  property_count: 11
  slug: citeerbaar-nl-envelope
- name: EnvelopeZonderHash
  property_count: 10
  slug: citeerbaar-nl-envelope-zonder-hash
- name: FactsMeta
  property_count: 12
  slug: citeerbaar-nl-facts-meta
- name: JsonRpcResponse
  property_count: 4
  slug: citeerbaar-nl-json-rpc-response
jsonld:
- class_count: 5
  name: Citeerbaar Nl Context
  property_count: 34
  slug: citeerbaar-nl-context
layout: provider
modified: '2026-11-03'
name: Citeerbaar
nav: Providers
network: true
overview: 'Citeerbaar publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Agents API, Open data API, and Status API. Tagged areas include Artificial Intelligence, SEO, Digital-PR, Netherlands, and Citations.


  The Citeerbaar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Citeerbaar''s developer surface includes pricing, engineering blog, API reference, and 20 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Citeerbaar API Rules
  rule_count: 58
  severity_counts:
    error: 52
    hint: 0
    info: 3
    warn: 3
  slug: citeerbaar-nl-rules
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 61.6
    developer_ergonomics: 4.8
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Citeerbaar Nl Domain Security
  slug: citeerbaar-nl-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Citeerbaar Nl Vulnerability Disclosure
  slug: citeerbaar-nl-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: citeerbaar-nl
tags:
- Artificial Intelligence
- SEO
- Digital-PR
- Netherlands
- Citations
website: https://www.citeerbaar.nl/
---
