---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Barndoor Agentic Access
  operation_count: 26
  slug: barndoor-agentic-access
  summary_line: 26 operations · 13 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: Python SDK for the Barndoor AI Platform. Wraps the Platform REST API, handles Auth0 PKCE login (`loginInteractive()`), discovers governed MCP tools, brokers OAuth connections to backend SaaS, and expo
  name: Barndoor Python SDK
  slug: python-sdk
- description: TypeScript SDK for the Barndoor AI Platform. Browser- and Node-friendly client for Auth0 PKCE login, governed MCP tool discovery, OAuth connection initiation, and proxying MCP / SSE requests through B
  name: Barndoor TypeScript SDK
  slug: typescript-sdk
- description: Go SDK for the Barndoor AI Platform. Server-side client for registering agents, managing MCP servers and policies, brokering OAuth connections, and proxying MCP requests from Go services.
  name: Barndoor Go SDK
  slug: go-sdk
- description: The official Rust SDK for the Model Context Protocol. Maintained under the Barndoor AI GitHub organization; provides primitives to build MCP clients and servers in Rust.
  name: Official MCP Rust SDK
  slug: official-mcp-rust-sdk
- description: Rust SDK for Cerbos, the policy-decision-point used by Barndoor for attribute-based access control. Lets Rust services request policy decisions from a Cerbos PDP.
  name: Cerbos Rust SDK
  slug: cerbos-sdk-rust
- description: Rust test suite that validates remote MCP servers against the MCP authorization specification - RFC 9728 (Protected Resource Metadata), RFC 8414 (Authorization Server Metadata), RFC 7591 (Dynamic Clie
  name: MCP OAuth Compliance Suite
  slug: mcp-auth-compliance
- description: Reference Python demo application showing how to plug Barndoor-governed MCP tools into a Crew AI multi-agent workflow.
  name: Barndoor + Crew AI Example
  slug: crew-ai-example
- description: Manage AI agent registrations
  name: Barndoor Agents API
  slug: barndoor-agents-api
- description: Manage OAuth connections to MCP servers
  name: Barndoor Connections API
  slug: barndoor-connections-api
- description: Proxy requests to MCP servers
  name: Barndoor MCP Proxy API
  slug: barndoor-mcp-proxy-api
- description: Manage access control policies for agents and servers
  name: Barndoor Policies API
  slug: barndoor-policies-api
- description: The Policy API from Barndoor — 1 operation(s) for policy.
  name: Barndoor Policy API
  slug: barndoor-policy-api
- description: Manage MCP server instances
  name: Barndoor Servers API
  slug: barndoor-servers-api
artifact_total: 149
collections:
- collection_type: postman
  name: Barndoor Platform Agents API
  slug: postman-barndoor-agents-api
- collection_type: postman
  name: Barndoor Platform Agents Connections API
  slug: postman-barndoor-connections-api
- collection_type: postman
  name: Barndoor Platform Agents MCP Proxy API
  slug: postman-barndoor-mcp-proxy-api
- collection_type: postman
  name: Barndoor Platform Agents Policies API
  slug: postman-barndoor-policies-api
- collection_type: postman
  name: Barndoor Platform Agents Policy API
  slug: postman-barndoor-policy-api
- collection_type: postman
  name: Barndoor Platform Agents Servers API
  slug: postman-barndoor-servers-api
- collection_type: open
  name: Barndoor Platform API
  slug: open-barndoor
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/barndoor-ai/barndoor-python-sdk/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/barndoor-ai/barndoor-python-sdk/blob/main/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/barndoor-ai/barndoor-python-sdk/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/barndoor-ai/barndoor-python-sdk/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/barndoor/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/barndoor-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/barndoor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/barndoor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/barndoor-authentication.yml
- group: company
  title: ''
  type: Blog
  url: http://barndoor.ai/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/barndoor-ai
- group: company
  title: ''
  type: Website
  url: https://barndoor.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.barndoor.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.barndoor.ai/api-reference/introduction
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/barndoor-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: https://docs.barndoor.ai/api-reference/introduction
- group: build
  title: ''
  type: SDKs
  url: https://docs.barndoor.ai/sdks/introduction
- group: start
  title: ''
  type: Portal
  url: https://app.barndoor.ai/
- group: start
  title: ''
  type: Signup
  url: https://app.barndoor.ai/auth/signup/trial
- group: auth
  title: ''
  type: TokensManagement
  url: https://app.barndoor.ai/settings/tokens
- group: commercial
  title: ''
  type: Pricing
  url: https://barndoor.ai/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/barndoor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/barndoor-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/barndoor-finops.yml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/barndoor-ai
- group: auth
  title: ''
  type: Security
  url: https://barndoor.ai/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.barndoor.ai
- group: company
  title: ''
  type: About
  url: https://barndoor.ai/about-us/
- group: agent
  title: ''
  type: MCPCatalog
  url: https://docs.barndoor.ai/mcp-servers/servers
- group: other
  title: ''
  type: IPAllowlist
  url: https://docs.barndoor.ai/how-tos/ip-whitelisting
- group: other
  title: ''
  type: LogExport
  url: https://docs.barndoor.ai/how-tos/log-export
- group: design
  title: ''
  type: SpectralRules
  url: rules/barndoor-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/barndoor-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/barndoor-context.jsonld
- group: auth
  title: ''
  type: Compliance
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.barndoor.ai/llms.txt
created: '2026-03-16'
description: Barndoor AI is the control plane for agentic AI, providing secure access and governance for AI agents and Model Context Protocol (MCP) servers. Founded in 2024 by Oren Michels (founder of Mashery), Barndoor enables enterprise IT, security, and developer teams to register agents, govern MCP server access through policy, broker OAuth connections to backend SaaS, and proxy MCP traffic with runtime policy enforcement and full audit trails. The Barndoor Platform REST API manages servers, connections, policies, agents, and MCP / SSE request proxying. Python, TypeScript, and Go SDKs are published on GitHub alongside Rust SDKs (Cerbos, official MCP, MCP OAuth compliance suite) and a Crew AI example. Deployment options include SaaS (trial), private cloud, and on-premises (Enterprise).
examples:
- key_count: 3
  name: Barndoor Agent Counts Example
  slug: barndoor-agent-counts-example
- key_count: 11
  name: Barndoor Agent Directory Base Example
  slug: barndoor-agent-directory-base-example
- key_count: 5
  name: Barndoor Agent Example
  slug: barndoor-agent-example
- key_count: 1
  name: Barndoor Agent Payload Example
  slug: barndoor-agent-payload-example
- key_count: 7
  name: Barndoor Agent Response Example
  slug: barndoor-agent-response-example
- key_count: 1
  name: Barndoor Clone Policy Example
  slug: barndoor-clone-policy-example
- key_count: 1
  name: Barndoor Connection Initiation Response Example
  slug: barndoor-connection-initiation-response-example
- key_count: 1
  name: Barndoor Connection Status Response Example
  slug: barndoor-connection-status-response-example
- key_count: 2
  name: Barndoor Create Server Example
  slug: barndoor-create-server-example
- key_count: 1
  name: Barndoor Delete Connection Example
  slug: barndoor-delete-connection-example
- key_count: 1
  name: Barndoor Delete Server Example
  slug: barndoor-delete-server-example
- key_count: 1
  name: Barndoor Disable Restriction Example
  slug: barndoor-disable-restriction-example
- key_count: 1
  name: Barndoor Enable Restriction Example
  slug: barndoor-enable-restriction-example
- key_count: 3
  name: Barndoor Error Example
  slug: barndoor-error-example
- key_count: 3
  name: Barndoor Filter Category Example
  slug: barndoor-filter-category-example
- key_count: 2
  name: Barndoor Filter Option Example
  slug: barndoor-filter-option-example
- key_count: 1
  name: Barndoor Get Agent Counts Example
  slug: barndoor-get-agent-counts-example
- key_count: 1
  name: Barndoor Get Agent Example
  slug: barndoor-get-agent-example
- key_count: 1
  name: Barndoor Get Connection Status Example
  slug: barndoor-get-connection-status-example
- key_count: 1
  name: Barndoor Get Filter Definitions Example
  slug: barndoor-get-filter-definitions-example
- key_count: 1
  name: Barndoor Get Policies Summary Example
  slug: barndoor-get-policies-summary-example
- key_count: 1
  name: Barndoor Get Policy Example
  slug: barndoor-get-policy-example
- key_count: 1
  name: Barndoor Get Server Example
  slug: barndoor-get-server-example
- key_count: 2
  name: Barndoor Initiate Connection Example
  slug: barndoor-initiate-connection-example
- key_count: 1
  name: Barndoor List Agents Example
  slug: barndoor-list-agents-example
- key_count: 1
  name: Barndoor List Policies Example
  slug: barndoor-list-policies-example
- key_count: 1
  name: Barndoor List Policy Revisions Example
  slug: barndoor-list-policy-revisions-example
- key_count: 1
  name: Barndoor List Servers Example
  slug: barndoor-list-servers-example
- key_count: 6
  name: Barndoor Pagination Meta Example
  slug: barndoor-pagination-meta-example
- key_count: 14
  name: Barndoor Policy Detail Example
  slug: barndoor-policy-detail-example
- key_count: 7
  name: Barndoor Policy Revision Summary Example
  slug: barndoor-policy-revision-summary-example
- key_count: 1
  name: Barndoor Policy Rule Condition Example
  slug: barndoor-policy-rule-condition-example
- key_count: 5
  name: Barndoor Policy Rule Example
  slug: barndoor-policy-rule-example
- key_count: 13
  name: Barndoor Policy Summary Example
  slug: barndoor-policy-summary-example
- key_count: 2
  name: Barndoor Proxy Mcp Request Example
  slug: barndoor-proxy-mcp-request-example
- key_count: 2
  name: Barndoor Proxy Sserequest Example
  slug: barndoor-proxy-sserequest-example
- key_count: 1
  name: Barndoor Publish Cerbos Policy Example
  slug: barndoor-publish-cerbos-policy-example
- key_count: 2
  name: Barndoor Register Agent Example
  slug: barndoor-register-agent-example
- key_count: 6
  name: Barndoor Server Create Request Example
  slug: barndoor-server-create-request-example
- key_count: 3
  name: Barndoor Server Create Response Example
  slug: barndoor-server-create-response-example
- key_count: 5
  name: Barndoor Server Summary Example
  slug: barndoor-server-summary-example
- key_count: 5
  name: Barndoor Server Update Request Example
  slug: barndoor-server-update-request-example
- key_count: 1
  name: Barndoor Unregister Agent Example
  slug: barndoor-unregister-agent-example
- key_count: 7
  name: Barndoor Update Policy Example
  slug: barndoor-update-policy-example
- key_count: 2
  name: Barndoor Update Server Example
  slug: barndoor-update-server-example
- key_count: 2
  name: Barndoor Validate Policy Example
  slug: barndoor-validate-policy-example
- key_count: 4
  name: Barndoor Validate Policy Request Example
  slug: barndoor-validate-policy-request-example
- key_count: 3
  name: Barndoor Validate Policy Response Example
  slug: barndoor-validate-policy-response-example
features:
- description: Secure access control and policy enforcement for Model Context Protocol servers.
  name: MCP Governance
- description: Continuous governance applied at the moment AI agents act, not just at login.
  name: Runtime Policy Enforcement
- description: Precise, scoped access for agents - not broad human-level permissions.
  name: Right-Sized Permissions
- description: Dynamically surface only policy-compliant MCP tools, optimizing the context window.
  name: Context Filtering
- description: Register internal and external agents, group them, and track activity.
  name: AI Agent Registry
- description: Initiate and manage OAuth 2.0 connections from agents to backend SaaS.
  name: OAuth Connection Brokering
- description: Streaming proxy that injects credentials and enforces policy on every MCP and SSE request.
  name: MCP / SSE Proxying
- description: Create, clone, version, validate, and apply Cerbos-based RBAC and ABAC policies.
  name: Policy Authoring (RBAC/ABAC)
- description: Complete audit trails for every AI action, applied policy, and outcome.
  name: Audit Dashboards and Activity Logs
- description: Stream audit events as gzipped JSON Lines to S3 / GCS / MinIO / SeaweedFS buckets.
  name: Audit Log Export
- description: Centralized visibility into unauthorized AI apps and agents in the environment.
  name: Shadow AI Discovery
- description: Connect to existing enterprise IdPs (Keycloak-based) for SSO and identity.
  name: Identity Provider Integration
- description: Five dedicated outbound IPs for whitelisting Barndoor traffic at MCP servers.
  name: Static Egress IPs
- description: SaaS, private cloud, and on-premises deployment options for sensitive environments.
  name: Private and On-Prem Deployment
finops:
- name: Barndoor Finops
  service_category: AI Governance / Control Plane
  slug: barndoor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/barndoor.png
json_schemas:
- name: AgentCounts
  property_count: 3
  slug: barndoor-agent-counts
- name: AgentDirectoryBase
  property_count: 11
  slug: barndoor-agent-directory-base
- name: AgentPayload
  property_count: 1
  slug: barndoor-agent-payload
- name: AgentResponse
  property_count: 7
  slug: barndoor-agent-response
- name: Agent
  property_count: 5
  slug: barndoor-agent
- name: ConnectionInitiationResponse
  property_count: 1
  slug: barndoor-connection-initiation-response
- name: ConnectionStatusResponse
  property_count: 1
  slug: barndoor-connection-status-response
- name: Error
  property_count: 3
  slug: barndoor-error
- name: FilterCategory
  property_count: 3
  slug: barndoor-filter-category
- name: FilterOption
  property_count: 2
  slug: barndoor-filter-option
- name: PaginationMeta
  property_count: 6
  slug: barndoor-pagination-meta
- name: PolicyDetail
  property_count: 14
  slug: barndoor-policy-detail
- name: PolicyRevisionSummary
  property_count: 7
  slug: barndoor-policy-revision-summary
- name: PolicyRuleCondition
  property_count: 1
  slug: barndoor-policy-rule-condition
- name: PolicyRule
  property_count: 5
  slug: barndoor-policy-rule
- name: PolicySummary
  property_count: 13
  slug: barndoor-policy-summary
- name: ServerCreateRequest
  property_count: 6
  slug: barndoor-server-create-request
- name: ServerCreateResponse
  property_count: 3
  slug: barndoor-server-create-response
- name: ServerDetail
  property_count: 0
  slug: barndoor-server-detail
- name: ServerSummary
  property_count: 5
  slug: barndoor-server-summary
- name: ServerUpdateRequest
  property_count: 5
  slug: barndoor-server-update-request
- name: UpdatePolicy
  property_count: 7
  slug: barndoor-update-policy
- name: ValidatePolicyRequest
  property_count: 4
  slug: barndoor-validate-policy-request
- name: ValidatePolicyResponse
  property_count: 3
  slug: barndoor-validate-policy-response
json_structures:
- name: Barndoor Agent Counts Structure
  property_count: 3
  slug: barndoor-agent-counts-structure
- name: Barndoor Agent Directory Base Structure
  property_count: 10
  slug: barndoor-agent-directory-base-structure
- name: Barndoor Agent Payload Structure
  property_count: 1
  slug: barndoor-agent-payload-structure
- name: Barndoor Agent Response Structure
  property_count: 7
  slug: barndoor-agent-response-structure
- name: Barndoor Agent Structure
  property_count: 5
  slug: barndoor-agent-structure
- name: Barndoor Connection Initiation Response Structure
  property_count: 1
  slug: barndoor-connection-initiation-response-structure
- name: Barndoor Connection Status Response Structure
  property_count: 1
  slug: barndoor-connection-status-response-structure
- name: Barndoor Error Structure
  property_count: 3
  slug: barndoor-error-structure
- name: Barndoor Filter Category Structure
  property_count: 3
  slug: barndoor-filter-category-structure
- name: Barndoor Filter Option Structure
  property_count: 2
  slug: barndoor-filter-option-structure
- name: Barndoor Pagination Meta Structure
  property_count: 6
  slug: barndoor-pagination-meta-structure
- name: Barndoor Policy Detail Structure
  property_count: 13
  slug: barndoor-policy-detail-structure
- name: Barndoor Policy Revision Summary Structure
  property_count: 7
  slug: barndoor-policy-revision-summary-structure
- name: Barndoor Policy Rule Condition Structure
  property_count: 1
  slug: barndoor-policy-rule-condition-structure
- name: Barndoor Policy Rule Structure
  property_count: 5
  slug: barndoor-policy-rule-structure
- name: Barndoor Policy Summary Structure
  property_count: 12
  slug: barndoor-policy-summary-structure
- name: Barndoor Server Create Request Structure
  property_count: 6
  slug: barndoor-server-create-request-structure
- name: Barndoor Server Create Response Structure
  property_count: 3
  slug: barndoor-server-create-response-structure
- name: Barndoor Server Detail Structure
  property_count: 0
  slug: barndoor-server-detail-structure
- name: Barndoor Server Summary Structure
  property_count: 5
  slug: barndoor-server-summary-structure
- name: Barndoor Server Update Request Structure
  property_count: 5
  slug: barndoor-server-update-request-structure
- name: Barndoor Update Policy Structure
  property_count: 6
  slug: barndoor-update-policy-structure
- name: Barndoor Validate Policy Request Structure
  property_count: 4
  slug: barndoor-validate-policy-request-structure
- name: Barndoor Validate Policy Response Structure
  property_count: 3
  slug: barndoor-validate-policy-response-structure
jsonld:
- class_count: 3
  name: Barndoor Context
  property_count: 14
  slug: barndoor-context
layout: provider
modified: '2026-05-19'
name: Barndoor
nav: Providers
network: true
overview: 'Barndoor publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Connections API, MCP Proxy API, and 3 more. Tagged areas include AI Agents, AI Governance, Agentic AI, MCP, and Model Context Protocol.


  The Barndoor catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Barndoor''s developer surface includes authentication, engineering blog, documentation, API reference, developer portal, signup flow, pricing, and 28 more developer resources.'
plans:
- name: Barndoor Plans Pricing
  plan_count: 4
  slug: barndoor-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 6
  name: Barndoor Rate Limits
  slug: barndoor-rate-limits
rules:
- name: Barndoor API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: barndoor-jsonschema-spectral-rules
- name: Barndoor API Rules
  rule_count: 21
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 10
  slug: barndoor-spectral-rules
score:
  band: strong
  composite: 63.2
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 67.8
    developer_ergonomics: 47.8
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 63.2
  previous_composite: 63.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 42.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/barndoor/refs/heads/main/screenshots/barndoor-2026-06-20T173002.png
security:
- kind: authentication
  name: Barndoor Authentication
  slug: barndoor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Barndoor Domain Security
  slug: barndoor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Barndoor Vulnerability Disclosure
  slug: barndoor-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: barndoor
solutions:
- description: Centralize AI governance, manage shadow AI, and enforce real-time access controls at scale.
  name: IT & Security Teams
- description: Deploy agents safely without custom security logic, with end-to-end policy across dev, staging, and prod.
  name: Developers
tags:
- AI Agents
- AI Governance
- Agentic AI
- MCP
- Model Context Protocol
- Policy Enforcement
- OAuth
- Identity
- Security
- Audit
- Control Plane
use_cases:
- description: Apply access policies and governance to AI agents across the organization.
  name: Enterprise AI Governance
- description: Centrally register, secure, and manage MCP server deployments for AI agents.
  name: MCP Server Management
- description: Coordinate multi-agent workflows with security and accountability controls.
  name: Agentic Workflow Orchestration
- description: Prevent unauthorized AI agent actions and limit data exfiltration.
  name: AI Security and Data Exfiltration Prevention
- description: Surface unauthorized AI apps and agents already running in the environment.
  name: Shadow AI Discovery
- description: Build agents safely with end-to-end policy enforcement via SDKs.
  name: Developer Tooling for Governed Agents
- description: Govern agents that work across Microsoft 365 (Excel, Outlook, Teams, OneDrive).
  name: Microsoft 365 Agent Governance
website: https://barndoor.ai/
---
