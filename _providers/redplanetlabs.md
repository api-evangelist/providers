---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: In-cluster HTTP+JSON RPC surface exposed by Rama Supervisors (default port 2000) for appending to depots, querying PStates by navigation path, and invoking query topologies. POST-only; no application-
  name: Rama REST API
  slug: rama-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://redplanetlabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://redplanetlabs.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://redplanetlabs.com/docs/~/rest.html
- group: start
  title: ''
  type: GettingStarted
  url: https://redplanetlabs.com/docs/~/tutorial1.html
- group: commercial
  title: ''
  type: Pricing
  url: https://redplanetlabs.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.redplanetlabs.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.redplanetlabs.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/redplanetlabs
- group: build
  title: ''
  type: SDKs
  url: packages/redplanetlabs-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/redplanetlabs-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/redplanetlabs-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/redplanetlabs-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/redplanetlabs-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/redplanetlabs-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/redplanetlabs-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/redplanetlabs-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/redplanetlabs-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/redplanetlabs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/redplanetlabs-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/redplanetlabs-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redplanetlabs-domain-security.yml
- group: start
  title: ''
  type: SignUp
  url: https://redplanetlabs.com/download
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/redplanetlabs
created: '2026-07-17'
description: Red Planet Labs builds Rama, a unified backend platform for the JVM (Java/Clojure) that consolidates databases, queues, workers, and infrastructure into a single programming model — aiming to reduce backend complexity by up to 100x while providing ACID semantics, reactive queries, fine-grained change detection, and linear scalability. Rama exposes a REST API (an in-cluster HTTP+JSON RPC surface for depot appends, PState queries, and query-topology invokes), ships a `rama` operations CLI, publishes Maven client libraries under the com.rpl groupId, open-sources the Specter data-navigation library, and provides first-party Agent Skills for authoring Rama backends. Surfaced as a portfolio company of Kindred Ventures and enriched into the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/redplanetlabs.png
layout: provider
mcp_servers:
- description: ''
  name: Redplanetlabs MCP Server
  slug: redplanetlabs-mcp-server
modified: '2026-08-08'
name: Redplanetlabs
nav: Providers
network: true
overview: 'Redplanetlabs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Backend Platform, Database, Distributed Systems, and JVM.


  Redplanetlabs'' developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, CLI, authentication, and 17 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 25.7
  provenance:
    conformance: derived
    mcp: derived
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/redplanetlabs/refs/heads/main/screenshots/redplanetlabs-2026-09-02T153157.png
security:
- kind: authentication
  name: Redplanetlabs Authentication
  slug: redplanetlabs-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Redplanetlabs Domain Security
  slug: redplanetlabs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: redplanetlabs
tags:
- Company
- Backend Platform
- Database
- Distributed Systems
- JVM
- Developer Tools
- Clojure
website: https://redplanetlabs.com/
---
