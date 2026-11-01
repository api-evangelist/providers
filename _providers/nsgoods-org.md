---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Nsgoods Org Agentic Access
  operation_count: 8
  slug: nsgoods-org-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 1
apis:
- baseURL: https://payable.nsgoods.org
  baseurl_source: declared
  description: The Health API from nsgoods-org — 1 operation(s) for health.
  name: nsgoods-org Health API
  slug: nsgoods-org-health-api
- baseURL: https://payable.nsgoods.org
  baseurl_source: declared
  description: The Payable API from nsgoods-org — 7 operation(s) for payable.
  name: nsgoods-org Payable API
  slug: nsgoods-org-payable-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/nsgoods-org/agentic-access/nsgoods-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nsgoods-org-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/nsgoods-org/rules/nsgoods-org-rules.yml
  title: ''
  type: Spectral
  url: rules/nsgoods-org-rules.yml
- group: design
  href: https://artifacts.apis.io/nsgoods-org/json-ld/nsgoods-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nsgoods-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/nsgoods-org/vocabulary/nsgoods-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nsgoods-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/nsgoods-org/data-model/nsgoods-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nsgoods-org-data-model.yml
- group: design
  href: https://artifacts.apis.io/nsgoods-org/errors/nsgoods-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nsgoods-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nsgoods-org/conformance/nsgoods-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nsgoods-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/nsgoods-org/llms/nsgoods-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nsgoods-org-llms.txt
- group: other
  href: https://artifacts.apis.io/nsgoods-org/a2a/nsgoods-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/nsgoods-org-a2a.yml
- group: agent
  href: https://artifacts.apis.io/nsgoods-org/well-known/nsgoods-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nsgoods-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/nsgoods-org/hosts/nsgoods-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nsgoods-org-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.nsgoods.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://x402.nsgoods.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://x402.nsgoods.org/privacy
- group: auth
  href: https://artifacts.apis.io/nsgoods-org/authentication/nsgoods-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nsgoods-org-authentication.yml
- group: auth
  href: https://artifacts.apis.io/nsgoods-org/security/nsgoods-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nsgoods-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nsgoods.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://x402.nsgoods.org/
- group: docs
  title: ''
  type: Documentation
  url: https://x402.nsgoods.org/
created: '2026-10-30'
description: nsgoods provides a suite of twelve x402 pay‑per‑call APIs for AI agents on Base and Solana, offering services such as crypto signals, market regimes, and data provenance. The platform delivers provable, signed responses, integrates with on‑chain verification, and supports free previews for each service. It targets AI agents needing reliable, verifiable financial and data signals, leveraging blockchain‑backed guarantees and transparent proof mechanisms.
json_schemas:
- name: AddressPreflight
  property_count: 0
  slug: nsgoods-org-address-preflight
- name: PayabilityResult
  property_count: 15
  slug: nsgoods-org-payability-result
jsonld:
- class_count: 1
  name: Nsgoods Org Context
  property_count: 15
  slug: nsgoods-org-context
layout: provider
modified: '2026-10-30'
name: nsgoods-org
nav: Providers
network: true
overview: 'nsgoods-org publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Health API and Payable API. Tagged areas include AI, Finance, Blockchain, Data, and Services.


  The nsgoods-org catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  nsgoods-org''s developer surface includes authentication, documentation, and 17 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: nsgoods-org API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: nsgoods-org-rules
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 53.5
    developer_ergonomics: 31.0
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Nsgoods Org Authentication
  slug: nsgoods-org-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nsgoods Org Domain Security
  slug: nsgoods-org-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nsgoods-org
tags:
- AI
- Finance
- Blockchain
- Data
- Services
- Company
website: https://nsgoods.org/
---
