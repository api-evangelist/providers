---
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
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 56
  human_in_the_loop: 9
  name: Agntcy Agentic Access
  operation_count: 106
  slug: agntcy-agentic-access
  summary_line: 106 operations · 56 acting · 9 human-in-the-loop
api_count: 4
apis:
- description: Distributed announce and discovery of multi-agent systems. gRPC-first, with services for storage (content-addressed by CID), routing over a DHT, structured search, signing and verification, domain nam
  name: Agent Directory (DIR)
  slug: agent-directory-dir
- description: Agents are AI workflows that can be configured and/or executed on this server. This means that a client of this server can start a Run on any of the Agents supported by this server. Each agent may sup
  name: AGNTCY Agents API
  slug: agntcy-agents-api
- description: AppService manages apps.
  name: AGNTCY App Service API
  slug: agntcy-appservice-api
- description: AuthService manages auth.
  name: AGNTCY Auth Service API
  slug: agntcy-authservice-api
- description: BadgeService manages badges.
  name: AGNTCY Badge Service API
  slug: agntcy-badgeservice-api
- description: The Classes and Objects API from AGNTCY — 4 operation(s) for classes and objects.
  name: AGNTCY Classes and Objects API
  slug: agntcy-classes-and-objects-api
- description: DeviceService manages device.
  name: AGNTCY Device Service API
  slug: agntcy-deviceservice-api
- description: IdService is the service that provides ID operations.
  name: AGNTCY ID Service API
  slug: agntcy-idservice-api
- description: IssuerService is the service that provides ISSUER node operations.
  name: AGNTCY Issuer Service API
  slug: agntcy-issuerservice-api
- description: The JSON Schema API from AGNTCY — 4 operation(s) for json schema.
  name: AGNTCY JSON Schema API
  slug: agntcy-json-schema-api
- description: PolicyService manages policy.
  name: AGNTCY Policy Service API
  slug: agntcy-policyservice-api
- description: The Sample Data API from AGNTCY — 4 operation(s) for sample data.
  name: AGNTCY Sample Data API
  slug: agntcy-sample-data-api
- description: The Schema API from AGNTCY — 8 operation(s) for schema.
  name: AGNTCY Schema API
  slug: agntcy-schema-api
- description: SettingsService manages settings.
  name: AGNTCY Settings Service API
  slug: agntcy-settingsservice-api
- description: A Run represents an execution of an agent. The output of a Run can be a final result or an interrupt. Result from a run can be retrieved by polling or by blocking and waiting for the result. See `Run`
  name: AGNTCY Stateless Runs API
  slug: agntcy-stateless-runs-api
- description: The Taxonomy API from AGNTCY — 3 operation(s) for taxonomy.
  name: AGNTCY Taxonomy API
  slug: agntcy-taxonomy-api
- description: Thread Runs are runs created on a thread. A Thread Run can be created on a thread **only** if there is no run in the `pending` status on the same thread, i.e. if the thread is in the state `idle` Note
  name: AGNTCY Thread Runs API
  slug: agntcy-thread-runs-api
- description: If supported by the involved agents, Run can be grouped in Threads. When a run is executed on a thread is called Thread Run. At the end of a Thread Run, the server keeps a thread state associated to t
  name: AGNTCY Threads API
  slug: agntcy-threads-api
- description: The Translation API from AGNTCY — 4 operation(s) for translation.
  name: AGNTCY Translation API
  slug: agntcy-translation-api
- description: The Validation API from AGNTCY — 4 operation(s) for validation.
  name: AGNTCY Validation API
  slug: agntcy-validation-api
- description: VC is the service that provides VC operations.
  name: AGNTCY Vc Service API
  slug: agntcy-vcservice-api
artifact_total: 37
asyncapis:
- description: ''
  name: Agntcy Events
  slug: agntcy-events
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/agntcy-oasf-schema-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/agntcy-identity-service-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/agntcy-identity-node-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agntcy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agntcy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agntcy-authentication.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: start
  title: ''
  type: Portal
  url: https://agntcy.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agntcy.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agntcy.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agntcy
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/agntcy/dir-mcp
- group: company
  title: ''
  type: Website
  url: https://outshift.cisco.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agntcy-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/agntcy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/agntcy-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agntcy-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/agntcy-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/agntcy-acp-overlay.yaml
- group: other
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agntcy-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agntcy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agntcy-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/agntcy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/agntcy/dir/blob/main/SECURITY.md
- group: start
  title: ''
  type: Sandbox
  url: sandbox/agntcy-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://schema.oasf.outshift.com/doc
- group: design
  title: ''
  type: Conventions
  url: conventions/agntcy-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/agntcy-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/agntcy-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://agntcy.org/changelog
- group: build
  title: ''
  type: CLI
  url: cli/agntcy-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agntcy-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agntcy-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agntcy-plans-pricing.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/agntcy-oasf-record.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agntcy.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://dir.agntcy.org/latest/dir/dir-quickstart/
- group: operate
  title: ''
  type: Support
  url: https://github.com/orgs/agntcy/discussions
- group: operate
  title: ''
  type: Community
  url: https://join.slack.com/t/agntcy/shared_invite/zt-3xozr6nzq-i6LXv2P8l2kVW4_Prnny2w
- group: company
  title: ''
  type: Blog
  url: https://agntcy.org/articles
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lfprojects.org/policies/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lfprojects.org/policies/privacy-policy/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/agntcy
- group: other
  title: ''
  type: Governance
  url: https://github.com/agntcy/governance
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: learn
  title: ''
  type: Video
  url: https://www.youtube.com/playlist?list=PL49BrgsjXg5qVeRVqlX9O74W02q3c8fow
created: '2026-08-19'
description: 'AGNTCY is the open collective for agent interoperability, initiated by Outshift — Cisco''s incubation group — and governed under the Linux Foundation (LF Projects, LLC), developed in the open across 52 public repositories. It publishes specifications rather than a product API: OASF (Open Agentic Schema Framework) for describing agents with a versioned record schema and skill/domain taxonomies, the Agent Directory (DIR) for announcing and discovering multi-agent systems over gRPC, SLIM (Secure Low-Latency Interactive Messaging) as a transport, the Agent Connect Protocol (ACP) as a REST interface for invoking remote agents, and an Identity layer that issues and verifies W3C Verifiable Credential badges for agents, MCP servers and tools. One AGNTCY-operated API exists — the OASF Schema Server at schema.oasf.outshift.com, unauthenticated and callable by anyone; everything else is a specification you implement or software you deploy yourself. It ships SDKs in Python, JavaScript,
  Go, Rust and .NET, a local-stdio MCP server for the Agent Directory, and SLIMRPC transports for the A2A SDKs in five languages. Everything is Apache-2.0; there is no pricing, no paid tier and no commercial plan.'
image: https://agntcy.org/logo/preview-thumbnail-new.png
json_schemas:
- name: Agntcy Identity Badge Claims.Jsonschema
  property_count: 0
  slug: agntcy-identity-badge-claims.jsonschema
- name: Agntcy Identity Credential Content.Jsonschema
  property_count: 0
  slug: agntcy-identity-credential-content.jsonschema
- name: Agntcy Oasf Dictionary
  property_count: 0
  slug: agntcy-oasf-dictionary
- name: Agntcy Oasf Locator
  property_count: 0
  slug: agntcy-oasf-locator
- name: Agntcy Oasf Record
  property_count: 0
  slug: agntcy-oasf-record
- name: ClientConfig
  property_count: 16
  slug: agntcy-slim-client-config.schema
- name: ServerConfig
  property_count: 11
  slug: agntcy-slim-server-config.schema
layout: provider
mcp_servers:
- description: ''
  name: AGNTCY MCP Server
  slug: agntcy-mcp-server
- description: ''
  name: AGNTCY MCP Server
  slug: agntcy-mcp-server-2
modified: '2026-08-19'
name: AGNTCY
nav: Providers
network: true
overview: 'AGNTCY publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Agents API, App Service API, Auth Service API, and 17 more. Tagged areas include AI Agents, Interoperability, Specification, Open-Source, and Agent Discovery.


  The AGNTCY catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AGNTCY''s developer surface includes authentication, developer portal, documentation, API reference, sandbox, developer console, changelog, and 42 more developer resources.'
plans:
- name: Agntcy Plans Pricing
  plan_count: 0
  slug: agntcy-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Agntcy Rate Limits
  slug: agntcy-rate-limits
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 24
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 61.4
    developer_ergonomics: 80.4
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 20
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Agntcy Authentication
  slug: agntcy-authentication
  summary_line: apiKey/http/openIdConnect/mutualTLS/none · 2 schemes
- kind: domain-security
  name: Agntcy Domain Security
  slug: agntcy-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Agntcy Vulnerability Disclosure
  slug: agntcy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agntcy
tags:
- AI Agents
- Interoperability
- Specification
- Open-Source
- Agent Discovery
- Identity
- Agent Directory
- MCP
- A2A
- OpenAPI
- gRPC
- Protocol Buffers
- Verifiable Credentials
- Schema
- Taxonomy
- Messaging
- Observability
- Linux Foundation
website: https://outshift.cisco.com/
---
