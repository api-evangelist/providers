---
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Paladinfi Com Agentic Access
  operation_count: 3
  slug: paladinfi-com-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://swap.paladinfi.com
  baseurl_source: declared
  description: The Health API from paladinfi-com — 1 operation(s) for health.
  name: paladinfi-com Health API
  slug: paladinfi-com-health-api
- baseURL: https://swap.paladinfi.com
  baseurl_source: declared
  description: The Trust Check API from paladinfi-com — 2 operation(s) for trust check.
  name: paladinfi-com Trust Check API
  slug: paladinfi-com-trust-check-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/paladinfi-com/agentic-access/paladinfi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/paladinfi-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/paladinfi-com/rules/paladinfi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/paladinfi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/paladinfi-com/json-ld/paladinfi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/paladinfi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/paladinfi-com/vocabulary/paladinfi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/paladinfi-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/paladinfi-com/data-model/paladinfi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/paladinfi-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/paladinfi-com/errors/paladinfi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/paladinfi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/paladinfi-com/conformance/paladinfi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/paladinfi-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/paladinfi-com/hosts/paladinfi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/paladinfi-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/paladinfi-com/packages/paladinfi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/paladinfi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/paladinfi-com/packages/paladinfi-com-packages.yml
  title: ''
  type: Packages
  url: packages/paladinfi-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/paladinfi-com/security/paladinfi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paladinfi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://paladinfi.com/
- group: company
  title: ''
  type: Blog
  url: https://paladinfi.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://paladinfi.com/docs/screen-wallets/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paladinfi
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paladinfi.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paladinfi.com/terms/
- group: start
  title: ''
  type: GettingStarted
  url: https://paladinfi.com/swap/
- group: operate
  title: ''
  type: Support
  url: https://paladinfi.com/contact/
created: '2026-10-30'
description: PaladinFi provides DeFi infrastructure for AI agents on Base, offering multi-aggregator swap routing with a flat 10 bps fee and a fail-closed risk gate that integrates OFAC, GoPlus, Etherscan and anomaly heuristics. The platform is MCP-native, supporting ElizaOS and Coinbase AgentKit plugins, and aims to guard users' positions with verifiable trust verdicts. It also offers a trust-check service, a swap demo, and open-source tools for developers, with documentation, blog, and community resources.
image: https://paladinfi.com/favicon.svg
json_schemas:
- name: Health
  property_count: 5
  slug: paladinfi-com-health
- name: TrustCheckOfacResponse
  property_count: 8
  slug: paladinfi-com-trust-check-ofac-response
- name: TrustCheckPreviewResponse
  property_count: 6
  slug: paladinfi-com-trust-check-preview-response
- name: TrustCheckRequest
  property_count: 2
  slug: paladinfi-com-trust-check-request
jsonld:
- class_count: 4
  name: Paladinfi Com Context
  property_count: 14
  slug: paladinfi-com-context
layout: provider
modified: '2026-10-30'
name: paladinfi-com
nav: Providers
network: true
overview: 'paladinfi-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Health API and Trust Check API. Tagged areas include Company, DeFi, AI, Infrastructure, and Finance.


  The paladinfi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  paladinfi-com''s developer surface includes engineering blog, documentation, getting-started guide, support, and 15 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: paladinfi-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: paladinfi-com-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 58.7
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 5.3
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
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Paladinfi Com Domain Security
  slug: paladinfi-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: paladinfi-com
tags:
- Company
- DeFi
- AI
- Infrastructure
- Finance
- Base
website: https://paladinfi.com/
---
