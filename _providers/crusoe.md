---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 61.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 198
  human_in_the_loop: 4
  name: Crusoe Agentic Access
  operation_count: 464
  slug: crusoe-agentic-access
  summary_line: 464 operations · 198 acting · 4 human-in-the-loop
api_count: 3
apis:
- description: REST API exposing all publicly available Crusoe Cloud endpoints — compute (VMs, instance groups, instance templates, images, custom images), storage (disks, snapshots, S3 buckets and keys), networking
  name: Crusoe Cloud API Gateway
  slug: crusoe-cloud-api-gateway
- description: OpenAI-compatible inference API from the Crusoe Intelligence Foundry. Send chat/completions and embeddings requests to Crusoe-hosted open models (DeepSeek, Llama, Gemma, GLM, Kimi, Nemotron and others
  name: Crusoe Managed Inference API
  slug: crusoe-managed-inference-api
- description: First-party, read-only Model Context Protocol server published by Crusoe as the npm package @crusoeai/cloud-mcp and as a downloadable Claude Desktop extension bundle. Runs over stdio, inherits credent
  name: Crusoe Cloud MCP Server
  slug: crusoe-cloud-mcp-server
artifact_total: 10
asyncapis:
- description: ''
  name: Crusoe Webhooks
  slug: crusoe-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.crusoe.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.crusoe.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crusoecloud.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.crusoecloud.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.crusoecloud.com/quickstart/overview
- group: operate
  title: ''
  type: Support
  url: https://docs.crusoecloud.com/resources/support
- group: company
  title: ''
  type: Blog
  url: https://www.crusoe.ai/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crusoecloud
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crusoe.ai/cloud/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.crusoecloud.com/signup
- group: start
  title: ''
  type: Login
  url: https://console.crusoecloud.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.crusoe.ai/#terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.crusoe.ai/#cloud-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crusoecloud.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/crusoe-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.crusoecloud.com/resources/deprecation_notices
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crusoe-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://www.crusoe.ai/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crusoe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/crusoe-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.crusoe.ai/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crusoe-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/crusoe-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/crusoe-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crusoe-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crusoe-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crusoe-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crusoe-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/crusoe-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/crusoe-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/crusoe-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/crusoe-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crusoe-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/crusoe-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crusoe-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crusoe-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/crusoe-cloud-api-gateway-v1-overlay.yaml
- group: operate
  title: ''
  type: SLA
  url: https://legal.crusoe.ai/#service-level-agreements
created: '2026-08-04'
description: Crusoe is a vertically integrated "AI factory" company that designs, builds, and operates energy-first AI infrastructure, and sells it as Crusoe Cloud — a GPU cloud for training, fine-tuning, and inference. The public developer surface is the Crusoe Cloud API Gateway, a REST API at api.cloud.crusoe.ai covering virtual machines, instance groups and templates, block storage disks and snapshots, S3-compatible object storage, custom images, a container registry, VPC networking and load balancers, InfiniBand partitions and NVLink domains, Crusoe Managed Kubernetes and Slurm clusters, capacity reservations, IAM role bindings, SCIM/SSO, quotas, audit logs, usage and billing. Alongside it, the Intelligence Foundry exposes an OpenAI-compatible Managed Inference API for serverless inference, serverless fine-tuning, and self-serve deployments of open models. Crusoe also ships a first-party CLI, a Terraform provider, a Go API client, and a read-only Crusoe Cloud MCP server for AI assistants.
  Founded 2018, headquartered in Denver, Colorado.
image: https://www.crusoe.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: crusoe-mcp.yml
  slug: crusoe-mcpyml
modified: '2026-08-04'
name: Crusoe
nav: Providers
network: true
overview: 'Crusoe publishes 1 API on the [APIs.io](https://apis.io/) network: Cloud API Gateway. Tagged areas include ai-infrastructure, cloud-computing, gpu-compute, machine-learning, and inference.


  The Crusoe catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Crusoe''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
random_paper: 92
score:
  band: strong
  composite: 58.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 55.8
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 63.2
  previous_composite: 58.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 48.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Crusoe Authentication
  slug: crusoe-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Crusoe Domain Security
  slug: crusoe-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Crusoe Vulnerability Disclosure
  slug: crusoe-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Crusoe Trust Center
  slug: crusoe-trust-center
  summary_line: SOC 2 Type II, SOC 2 Type I, ISO 27001, ISO 42001, GDPR
slug: crusoe
tags:
- ai-infrastructure
- cloud-computing
- gpu-compute
- machine-learning
- inference
- kubernetes
- object-storage
- infrastructure-as-a-service
- energy
- mcp
website: https://www.crusoe.ai/
---
