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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Desci Labs Agentic Access
  operation_count: 12
  slug: desci-labs-agentic-access
  summary_line: 12 operations · 1 acting
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
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/desci-labs-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/desci-labs-dpid-resolver-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/desci-labs-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/desci-labs-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/desci-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/desci-labs-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/desci-labs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/desci-labs-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/desci-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/desci-labs-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/desci-labs-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/desci-labs-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.desci.com
- group: start
  title: ''
  type: Sandbox
  url: sandbox/desci-labs-sandbox.yml
- group: agent
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
overview: 'DeSci Labs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Data API, Query API, and Resolve API. Tagged areas include Company, Ai Enterprise Software, Research Infrastructure, Decentralized Science, and Scholarly Communication.


  DeSci Labs'' developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, engineering blog, support, and 18 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 46.8
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 46.5
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
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/desci-labs/refs/heads/main/screenshots/desci-labs-2026-07-25T211750.png
security:
- kind: authentication
  name: Desci Labs Authentication
  slug: desci-labs-authentication
  summary_line: none/apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Desci Labs Domain Security
  slug: desci-labs-domain-security
  summary_line: TLSv1.3
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
website: https://desci-labs.github.io/nodes/
---
