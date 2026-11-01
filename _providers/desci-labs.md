---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Desci Labs Agentic Access
  operation_count: 12
  slug: desci-labs-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- baseURL: https://beta.dpid.org/api
  baseurl_source: declared
  description: '**Data utilities** - IPFS-related utilities like folder tree listing by dPID or CID. Useful for directory browsing UIs and content explorers.'
  name: DeSci Labs Data API
  slug: desci-labs-data-api
- baseURL: https://beta.dpid.org/api
  baseurl_source: declared
  description: '**Research discovery and browse functionality** - Ideal for browse pages, search, and analytics. Paginated lists of research objects with optional metadata resolution, version history, and filtering c'
  name: DeSci Labs Query API
  slug: desci-labs-query-api
- baseURL: https://beta.dpid.org/api
  baseurl_source: declared
  description: '**Individual research object resolution** - Perfect for detail pages, file access, and direct DPID links. Get complete research objects with full version history, specific files, or content in differe'
  name: DeSci Labs Resolve API
  slug: desci-labs-resolve-api
artifact_total: 12
collections:
- collection_type: open
  name: dPID Resolver Data API
  slug: open-desci-labs-data-api
- collection_type: open
  name: dPID Resolver Data Query API
  slug: open-desci-labs-query-api
- collection_type: open
  name: dPID Resolver Data Resolve API
  slug: open-desci-labs-resolve-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.desci.com/
- group: other
  href: https://artifacts.apis.io/desci-labs/capabilities/desci-labs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/desci-labs-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/desci-labs/overlays/desci-labs-dpid-resolver-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/desci-labs-dpid-resolver-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/desci-labs/security/desci-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/desci-labs-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/desci-labs/agentic-access/desci-labs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/desci-labs-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/desci-labs/packages/desci-labs-packages.yml
  title: ''
  type: Packages
  url: packages/desci-labs-packages.yml
- group: build
  href: https://artifacts.apis.io/desci-labs/packages/desci-labs-packages.yml
  title: ''
  type: SDKs
  url: packages/desci-labs-packages.yml
- group: agent
  href: https://artifacts.apis.io/desci-labs/mcp/desci-labs-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/desci-labs-mcp.yml
- group: agent
  href: https://artifacts.apis.io/desci-labs/llms/desci-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/desci-labs-llms.txt
- group: auth
  href: https://artifacts.apis.io/desci-labs/authentication/desci-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/desci-labs-authentication.yml
- group: design
  href: https://artifacts.apis.io/desci-labs/conventions/desci-labs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/desci-labs-conventions.yml
- group: design
  href: https://artifacts.apis.io/desci-labs/conformance/desci-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/desci-labs-conformance.yml
- group: design
  href: https://artifacts.apis.io/desci-labs/lifecycle/desci-labs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/desci-labs-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.desci.com
- group: start
  href: https://artifacts.apis.io/desci-labs/sandbox/desci-labs-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/desci-labs-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/desci-labs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.desci.com
- group: docs
  title: ''
  type: APIReference
  url: https://beta.dpid.org/api-docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://desci-labs.github.io/nodes/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/desci-labs/nodes-integration-template
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/desci-labs
- group: company
  title: ''
  type: Blog
  url: https://www.desci.com/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.desci.com/find-help
- group: start
  title: ''
  type: SignUp
  url: https://nodes.desci.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.desci.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.desci.com/privacy
created: '2026-07-17'
description: DeSci Labs builds decentralized-science infrastructure for open, verifiable, and AI-native scholarly communication. Its products include DeSci Publish (DeSci Nodes) — a preprint and open-access publishing platform with rapid peer review and versioned, PID-addressed research objects; SciWeave — an AI research-discovery engine over 300M+ scientific works that ships a hosted Model Context Protocol (MCP) server; the DeSci Referee Finder for editorial reviewer matching; and the open-source dPID Resolver, an HTTP API that bridges decentralized persistent identifiers (dPIDs) to IPFS content and the Ceramic network. Developers integrate via the @desci-labs/nodes-lib client library and the public dPID Resolver API. Backed by hv-capital.
image: https://avatars.githubusercontent.com/desci-labs
layout: provider
mcp_servers:
- description: Claude connector for research paper search and AI-powered answers grounded in SciWeave's index of 300M+ scientific works; all tools are read-only and return verifiable DOIs.
  name: SciWeave MCP Server
  slug: sciweave-mcp-server
modified: '2026-07-18'
name: DeSci Labs
nav: Providers
network: true
overview: 'DeSci Labs publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Data API, Query API, and Resolve API. Tagged areas include Company, Ai Enterprise Software, Research Infrastructure, Decentralized Science, and Scholarly Communication.


  DeSci Labs'' developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, engineering blog, support, and 19 more developer resources.'
random_paper: 23
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 44.6
    developer_ergonomics: 73.2
    discoverability: 65.0
    operational_transparency: 21.1
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/desci-labs/desci-labs-2026-07-25T211750.png
security:
- kind: authentication
  name: Desci Labs Authentication
  slug: desci-labs-authentication
  summary_line: none/apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Desci Labs Domain Security
  slug: desci-labs-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: Query and page through research objects
  slug: desci-labs-query-research-objects
- name: Resolve a dPID to a research object
  slug: desci-labs-resolve-dpid
slug: desci-labs
tags:
- Company
- Ai Enterprise Software
- Research Infrastructure
- Decentralized Science
- Scholarly Communication
- Persistent Identifiers
- Open Access
- AI Research Tools
- IPFS
- MCP
website: https://www.desci.com/
---
