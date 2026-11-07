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
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Derod Org Agentic Access
  operation_count: 1
  slug: derod-org-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://derod.org/api
  baseurl_source: declared
  description: The Json Rpc API from DERO Project — 1 operation(s) for json rpc.
  name: DERO Project Json Rpc API
  slug: derod-org-json-rpc-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/derod-org/agentic-access/derod-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/derod-org-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/derod-org/rules/derod-org-rules.yml
  title: ''
  type: Spectral
  url: rules/derod-org-rules.yml
- group: design
  href: https://artifacts.apis.io/derod-org/json-ld/derod-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/derod-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/derod-org/vocabulary/derod-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/derod-org-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/derod-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/derod-org/data-model/derod-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/derod-org-data-model.yml
- group: design
  href: https://artifacts.apis.io/derod-org/conformance/derod-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/derod-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/derod-org/llms/derod-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/derod-org-llms.txt
- group: other
  href: https://artifacts.apis.io/derod-org/a2a/derod-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/derod-org-a2a.yml
- group: other
  href: https://artifacts.apis.io/derod-org/hosts/derod-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/derod-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/derod-org/vendors/derod-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/derod-org-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://derod.org/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/civilware
- group: auth
  href: https://artifacts.apis.io/derod-org/security/derod-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/derod-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://derod.org/
created: '2026-11-05'
description: Community-maintained documentation for the DERO blockchain, covering nodes, mining, wallets, smart contracts, and privacy technology. DERO is a privacy-focused Layer-1 blockchain with homomorphic encryption, enabling private smart contracts and TELA decentralized applications.
image: https://derod.org/assets/og-image.png
json_schemas:
- name: JsonRpcRequest
  property_count: 4
  slug: derod-org-json-rpc-request
- name: JsonRpcResponse
  property_count: 4
  slug: derod-org-json-rpc-response
jsonld:
- class_count: 16
  name: Derod Org Context
  property_count: 59
  slug: derod-org-context
layout: provider
modified: '2026-11-05'
name: DERO Project
nav: Providers
network: true
overview: 'DERO Project publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Json Rpc API. Tagged areas include Blockchain, Privacy, Smart Contracts, Homomorphic Encryption, and decentralized-apps.


  The DERO Project catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: DERO Project API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: derod-org-rules
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 57.7
    developer_ergonomics: 6.4
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Derod Org Domain Security
  slug: derod-org-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: derod-org
tags:
- Blockchain
- Privacy
- Smart Contracts
- Homomorphic Encryption
- decentralized-apps
website: https://derod.org/
---
