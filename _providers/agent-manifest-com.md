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
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Agent Manifest API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Agent Manifest API
  slug: agent-manifest-com-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/agent-manifest-com/rules/agent-manifest-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agent-manifest-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agent-manifest-com/vocabulary/agent-manifest-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agent-manifest-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agent-manifest-com/conformance/agent-manifest-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agent-manifest-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agent-manifest-com/llms/agent-manifest-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agent-manifest-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agent-manifest-com/a2a/agent-manifest-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agent-manifest-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agent-manifest-com/well-known/agent-manifest-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agent-manifest-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agent-manifest-com/hosts/agent-manifest-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agent-manifest-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agent-manifest-com/vendors/agent-manifest-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agent-manifest-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AMProtocol
- group: auth
  href: https://artifacts.apis.io/agent-manifest-com/security/agent-manifest-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agent-manifest-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agent-manifest.com/
coverage:
  checked: '2026-11-01'
  detail: No public API specification or documentation was found on the provider's API hosts.
  evidence:
  - status: 404
    url: https://api.agent-manifest.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: Agent Manifest provides the Agent Manifest Protocol, a specification, registry, validator, and CLI tools for autonomous API discovery. It offers a well‑known .well‑known/agent-manifest.json endpoint, a public registry of APIs, and tools for publishing and validating manifests. The platform includes documentation, SDKs, and examples to help developers integrate the protocol into their services.
layout: provider
modified: '2026-10-31'
name: Agent Manifest
nav: Providers
network: true
overview: 'Agent Manifest is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Protocol, Registry, Validation, and Open Source.


  The Agent Manifest catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Agent Manifest API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: agent-manifest-com-rules
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 30.8
    catalog_earned_first_party: 0.0
    catalog_gap: 84.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 2.6
  previous_composite: 10.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agent Manifest Com Domain Security
  slug: agent-manifest-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agent-manifest-com
tags:
- Protocol
- Registry
- Validation
- Open Source
website: https://agent-manifest.com/
---
