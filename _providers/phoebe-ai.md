---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for WithCoral platform providing AI services.
  name: Coral API
  slug: coral-api
- description: 'Phoebe API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: Phoebe API
  slug: phoebe-ai-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/phoebe-ai/plans/phoebe-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/phoebe-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/phoebe-ai/rules/phoebe-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/phoebe-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/phoebe-ai/vocabulary/phoebe-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/phoebe-ai-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/phoebe-ai/authentication/phoebe-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/phoebe-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/phoebe-ai/conformance/phoebe-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/phoebe-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/phoebe-ai/llms/phoebe-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/phoebe-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/phoebe-ai/mcp/phoebe-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/phoebe-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/phoebe-ai/well-known/phoebe-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/phoebe-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/phoebe-ai/well-known/phoebe-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/phoebe-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/phoebe-ai/hosts/phoebe-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/phoebe-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/phoebe-ai/vendors/phoebe-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/phoebe-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://withcoral.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://withcoral.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://withcoral.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://withcoral.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/withcoral/coral-releases/releases
- group: company
  title: ''
  type: Blog
  url: https://withcoral.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://withcoral.com/docs/reference/configuration
- group: start
  title: ''
  type: GettingStarted
  url: https://withcoral.com/docs/getting-started/install-locally
- group: auth
  href: https://artifacts.apis.io/phoebe-ai/security/phoebe-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/phoebe-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://withcoral.com
created: '2026-10-22'
description: Phoebe Technology Limited provides Coral, a trusted execution layer that enables enterprise AI agents to interact with sensitive systems. It adds permission controls, reusable workflows and efficiency optimizations for developers and organizations using AI agents. Coral connects directly to SaaS APIs and databases without requiring data migration.
image: https://withcoral.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at withcoral.com.
  name: Phoebe MCP Server
  slug: phoebe-ai-mcp-yml
modified: '2026-10-22'
name: Phoebe
nav: Providers
network: true
overview: 'Phoebe is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Machine-Learning, Platform, Ethics, and Enterprise.


  The Phoebe catalog on APIs.io includes 1 Spectral governance ruleset.


  Phoebe''s developer surface includes authentication, pricing, documentation, changelog, engineering blog, API reference, getting-started guide, and 14 more developer resources.'
plans:
- name: Phoebe Ai Plans Pricing
  plan_count: 2
  slug: phoebe-ai-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Phoebe API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: phoebe-ai-rules
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 42.9
    discoverability: 56.7
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Phoebe Ai Authentication
  slug: phoebe-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Phoebe Ai Domain Security
  slug: phoebe-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: phoebe-ai
tags:
- AI
- Machine-Learning
- Platform
- Ethics
- Enterprise
website: https://withcoral.com
---
