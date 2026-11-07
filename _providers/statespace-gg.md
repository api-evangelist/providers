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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://statespace.com
  baseurl_source: declared
  description: 'Statespace API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: Statespace API
  slug: statespace-gg-api
artifact_total: 4
common:
- group: docs
  title: ''
  type: APIReference
  url: https://docs.statespace.com/reference/cli
- group: design
  href: https://artifacts.apis.io/statespace-gg/rules/statespace-gg-rules.yml
  title: ''
  type: Spectral
  url: rules/statespace-gg-rules.yml
- group: design
  href: https://artifacts.apis.io/statespace-gg/vocabulary/statespace-gg-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/statespace-gg-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/statespace-gg/conformance/statespace-gg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/statespace-gg-conformance.yml
- group: agent
  href: https://artifacts.apis.io/statespace-gg/llms/statespace-gg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/statespace-gg-llms.txt
- group: other
  href: https://artifacts.apis.io/statespace-gg/a2a/statespace-gg-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/statespace-gg-a2a.yml
- group: agent
  href: https://artifacts.apis.io/statespace-gg/mcp/statespace-gg-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/statespace-gg-mcp.yml
- group: agent
  href: https://artifacts.apis.io/statespace-gg/well-known/statespace-gg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/statespace-gg-well-known.yml
- group: other
  href: https://artifacts.apis.io/statespace-gg/hosts/statespace-gg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/statespace-gg-hosts.yml
- group: other
  href: https://artifacts.apis.io/statespace-gg/vendors/statespace-gg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/statespace-gg-vendors.yml
- group: build
  href: https://artifacts.apis.io/statespace-gg/packages/statespace-gg-packages.yml
  title: ''
  type: SDKs
  url: packages/statespace-gg-packages.yml
- group: build
  href: https://artifacts.apis.io/statespace-gg/packages/statespace-gg-packages.yml
  title: ''
  type: Packages
  url: packages/statespace-gg-packages.yml
- group: auth
  href: https://artifacts.apis.io/statespace-gg/security/statespace-gg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/statespace-gg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://statespace.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.statespace.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.statespace.com/getting-started/installation
- group: operate
  title: ''
  type: Support
  url: https://statespace.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://statespace.com/solutions/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/statespace-tech
- group: commercial
  title: ''
  type: Pricing
  url: https://statespace.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://statespace.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://statespace.com/privacy
created: '2026-10-21'
description: Statespace is a venture-backed technology company focused on providing advanced simulation and analytics platforms for complex systems. Their flagship product enables users to model, visualize, and optimize dynamic environments across industries such as aerospace, automotive, and defense. The platform integrates real-time data, AI-driven insights, and collaborative tools to accelerate decision-making and reduce development cycles. Statespace aims to empower engineers and researchers with scalable, cloud-native solutions for high-fidelity simulations.
image: https://statespace.com/opengraph.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.statespace.com.
  name: Statespace MCP Server
  slug: statespace-gg-mcp-yml
modified: '2026-10-21'
name: Statespace
nav: Providers
network: true
overview: 'Statespace is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Simulation, Analytics, Cloud, and Engineering.


  The Statespace catalog on APIs.io includes 1 Spectral governance ruleset.


  Statespace''s developer surface includes API reference, documentation, getting-started guide, support, engineering blog, pricing, and 16 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: Statespace API Rules
  rule_count: 25
  severity_counts:
    error: 23
    hint: 0
    info: 1
    warn: 1
  slug: statespace-gg-rules
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 11.7
    developer_ergonomics: 28.6
    discoverability: 75.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/statespace-gg/statespace-gg-2026-11-03T143752.png
security:
- kind: domain-security
  name: Statespace Gg Domain Security
  slug: statespace-gg-domain-security
  summary_line: TLSv1.3 · DMARC
slug: statespace-gg
tags:
- Company
- Simulation
- Analytics
- Cloud
- Engineering
website: https://statespace.com
---
