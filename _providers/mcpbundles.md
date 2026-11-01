---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 2
  name: Mcpbundles Agentic Access
  operation_count: 10
  slug: mcpbundles-agentic-access
  summary_line: 10 operations · 6 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The Local Runtime API from MCPBundles — 4 operation(s) for local runtime.
  name: MCPBundles Local Runtime API
  slug: mcpbundles-local-runtime-api
- description: The Tunnel API from MCPBundles — 3 operation(s) for tunnel.
  name: MCPBundles Tunnel API
  slug: mcpbundles-tunnel-api
- description: The Graph QL API from MCPBundles — 1 operation(s) for graph ql.
  name: MCPBundles Graph QL API
  slug: mcpbundles-graph-ql-api
artifact_total: 11
common:
- group: other
  href: https://artifacts.apis.io/mcpbundles/overlays/mcpbundles-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mcpbundles-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/mcpbundles/agentic-access/mcpbundles-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mcpbundles-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/mcpbundles/plans/mcpbundles-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mcpbundles-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mcpbundles/rules/mcpbundles-rules.yml
  title: ''
  type: Spectral
  url: rules/mcpbundles-rules.yml
- group: design
  href: https://artifacts.apis.io/mcpbundles/json-ld/mcpbundles-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mcpbundles-context.jsonld
- group: design
  href: https://artifacts.apis.io/mcpbundles/vocabulary/mcpbundles-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mcpbundles-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/mcpbundles/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/mcpbundles/data-model/mcpbundles-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mcpbundles-data-model.yml
- group: build
  href: https://artifacts.apis.io/mcpbundles/cli/mcpbundles-cli.yml
  title: ''
  type: CLI
  url: cli/mcpbundles-cli.yml
- group: auth
  href: https://artifacts.apis.io/mcpbundles/authentication/mcpbundles-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mcpbundles-authentication.yml
- group: design
  href: https://artifacts.apis.io/mcpbundles/errors/mcpbundles-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mcpbundles-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mcpbundles/conformance/mcpbundles-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mcpbundles-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mcpbundles/llms/mcpbundles-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mcpbundles-llms.txt
- group: agent
  href: https://artifacts.apis.io/mcpbundles/mcp/mcpbundles-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mcpbundles-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mcpbundles/well-known/mcpbundles-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mcpbundles-well-known.yml
- group: other
  href: https://artifacts.apis.io/mcpbundles/hosts/mcpbundles-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mcpbundles-hosts.yml
- group: other
  href: https://artifacts.apis.io/mcpbundles/vendors/mcpbundles-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mcpbundles-vendors.yml
- group: build
  href: https://artifacts.apis.io/mcpbundles/packages/mcpbundles-packages.yml
  title: ''
  type: SDKs
  url: packages/mcpbundles-packages.yml
- group: build
  href: https://artifacts.apis.io/mcpbundles/packages/mcpbundles-packages.yml
  title: ''
  type: Packages
  url: packages/mcpbundles-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.mcpbundles.com/security
- group: auth
  href: https://artifacts.apis.io/mcpbundles/security/mcpbundles-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mcpbundles-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mcpbundles/security/mcpbundles-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mcpbundles-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mcpbundles.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mcpbundles.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.mcpbundles.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mcpbundles.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mcpbundles.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mcpbundles.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.mcpbundles.com/help
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.mcpbundles.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.mcpbundles.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mcpbundles.com/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.mcpbundles.com/register
- group: start
  title: ''
  type: Login
  url: https://www.mcpbundles.com/login
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://mcpbundles.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: MCPBundles provides a searchable directory of Managed Cloud Platforms (MCP) and related tools. It offers a web interface and CLI to discover, connect, and manage MCP servers across various categories such as developer tools, marketing, analytics, collaboration, cloud, and social services. Users can publish their own MCP listings, explore integrations, and access documentation, pricing, and support resources. The platform aims to simplify MCP ecosystem navigation for developers and enterprises, enabling seamless tool integration and server management.
image: https://www.mcpbundles.com/og-image.png
jsonld:
- class_count: 2
  name: Mcpbundles Context
  property_count: 4
  slug: mcpbundles-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.mcpbundles.com.
  name: MCPBundles MCP Server
  slug: mcpbundles-mcp-yml
modified: '2026-10-18'
name: MCPBundles
nav: Providers
network: true
overview: 'MCPBundles publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Local Runtime API, Tunnel API, and Graph QL API. Tagged areas include Company, Directory, ManagedCloudPlatforms, Tools, and Integration.


  The MCPBundles catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MCPBundles'' developer surface includes CLI, authentication, documentation, engineering blog, pricing, support, API reference, and 27 more developer resources.'
plans:
- name: Mcpbundles Plans Pricing
  plan_count: 2
  slug: mcpbundles-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: MCPBundles API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: mcpbundles-rules
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 41.2
    developer_ergonomics: 77.9
    discoverability: 48.3
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
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
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mcpbundles Authentication
  slug: mcpbundles-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mcpbundles Domain Security
  slug: mcpbundles-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Mcpbundles Vulnerability Disclosure
  slug: mcpbundles-vulnerability-disclosure
  summary_line: no policy recorded
slug: mcpbundles
tags:
- Company
- Directory
- ManagedCloudPlatforms
- Tools
- Integration
website: https://mcpbundles.com/
---
