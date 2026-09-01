---
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The REST control-plane API behind Synadia Cloud and the self-hosted Synadia Control Plane. 245 operations across 158 paths manage systems, accounts, teams, NATS users, JetStream streams, consumers, ke
  name: Synadia Control Plane / Synadia Cloud API
  slug: synadia-communications-control-plane
- description: A first-class RESTful HTTP interface to NATS, hosted by Synadia Cloud at api.ngs.global. 30 operations expose the NATS key-value store and its management surface, the object store and its management s
  name: Synadia Cloud NATS HTTP Gateway
  slug: synadia-communications-http-gateway
artifact_total: 10
asyncapis:
- description: ''
  name: Synadia Communications Event Surface
  slug: synadia-communications-event-surface
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/synadia-io/control-plane-sdk-go/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.synadia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.synadia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.synadia.com/
- group: docs
  title: ''
  type: APIReference
  url: https://cloud.synadia.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.synadia.com/cloud/walkthrough
- group: operate
  title: ''
  type: Support
  url: https://www.synadia.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.synadia.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/synadia-io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.synadia.com/cloud/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.synadia.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.synadia.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.synadia.com/legal/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/synadia-communications-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/synadia-communications-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/synadia-communications-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/synadia-communications-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/synadia-communications-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/synadia-communications-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/synadia-communications-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/synadia-communications-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/synadia-communications-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/synadia-communications-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/synadia-communications-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/synadia-communications-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/synadia-communications-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/synadia-communications-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synadia-communications-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/synadia-communications-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/synadia-communications-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/synadia-communications-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/synadia-communications-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/synadia-communications-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/synadia-communications-sandbox.yml
created: '2026-08-29'
description: 'Synadia Communications, Inc. is the creator and primary maintainer of NATS.io, the CNCF connectivity and messaging system, and sells the commercial platform built on it. Its products are Synadia Cloud (fully managed, globally distributed NATS with a REST control-plane API and an HTTP Gateway that exposes NATS key-value, object store, publish, request and subscribe over plain HTTP), Synadia Platform / Control Plane (self-hosted management, security and observability for NATS deployments on Kubernetes or Docker), Synadia Connect (managed connectors bridging NATS to external data systems), Synadia Insights (NATS monitoring and 143 automated audit checks), and Synadia Protect (a policy-enforcing security gateway for NATS traffic). The company positions NATS as the connectivity fabric for agentic AI, edge and distributed systems, and publishes an unusually complete machine-readable surface for agents: an llms.txt site index, Markdown twins of every page, an RFC 9727 API catalog,
  and a registry of provider-authored Agent Skills.'
image: https://www.synadia.com/images/og-image-default.webp
layout: provider
mcp_servers:
- description: 'Synadia ships NO Model Context Protocol server. This is a derived candidate only. Every NATS MCP server found in the search is third-party and unaffiliated - sinadarbouy/mcp-nats, JaredCluff/nuntius, '
  name: Synadia Communications MCP surface
  slug: synadia-communications-mcp-surface
modified: '2026-08-29'
name: Synadia Communications
nav: Providers
network: true
overview: 'Synadia Communications publishes 2 APIs on the [APIs.io](https://apis.io/) network: Synadia Control Plane / Synadia Cloud API and Synadia Cloud NATS HTTP Gateway. Tagged areas include Company, Messaging, Event Streaming, NATS, and Distributed Systems.


  The Synadia Communications catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Synadia Communications'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Synadia Communications Plans Pricing
  plan_count: 4
  slug: synadia-communications-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Synadia Communications Rate Limits
  slug: synadia-communications-rate-limits
score:
  band: strong
  composite: 62.9
  coverage:
    artifact_dirs: 21
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 55.2
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 62.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Synadia Communications Authentication
  slug: synadia-communications-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Synadia Communications Domain Security
  slug: synadia-communications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Synadia Communications Vulnerability Disclosure
  slug: synadia-communications-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Synadia Communications Trust Center
  slug: synadia-communications-trust-center
  summary_line: SOC 2
slug: synadia-communications
tags:
- Company
- Messaging
- Event Streaming
- NATS
- Distributed Systems
- Edge Computing
- Publish Subscribe
- Key-Value Store
- Object Storage
- Infrastructure
- Agentic AI
- Open-Source
website: https://www.synadia.com/
---
