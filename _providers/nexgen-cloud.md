---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: 'The Hyperstack API is a REST API for deploying and managing GPU infrastructure on the Hyperstack cloud: provision virtual machines, manage snapshots and images, attach block-storage volumes, manage S3'
  name: Hyperstack API
  slug: nexgen-cloud-hyperstack-api
- description: 'The AI Studio API is a REST API for inference on Hyperstack AI Studio: list the base-model catalog with pricing, run OpenAI-compatible chat completions, generate and edit images, manage conversations '
  name: Hyperstack AI Studio API
  slug: nexgen-cloud-ai-studio-api
artifact_total: 9
asyncapis:
- description: ''
  name: Nexgen Cloud Webhooks
  slug: nexgen-cloud-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.nexgencloud.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hyperstack.cloud/docs/intro
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hyperstack.cloud/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hyperstack.cloud/docs/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hyperstack.cloud/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.hyperstack.cloud/docs/support
- group: company
  title: ''
  type: Blog
  url: https://www.hyperstack.cloud/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NexGenCloud
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hyperstack.cloud/gpu-pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.hyperstack.cloud/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hyperstack.cloud/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hyperstack.cloud/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hyperstack.cloud/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.hyperstack.cloud/docs/release-notes
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nexgen-cloud-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nexgen-cloud-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/nexgen-cloud-api-catalog.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nexgen-cloud-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/nexgen-cloud-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/nexgen-cloud-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nexgen-cloud-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nexgen-cloud-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nexgen-cloud-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nexgen-cloud-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nexgen-cloud-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nexgen-cloud-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nexgen-cloud-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nexgen-cloud-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nexgen-cloud-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/nexgen-cloud-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nexgen-cloud-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexgen-cloud-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nexgen-cloud-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nexgen-cloud-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: NexGen Cloud Limited is a UK-headquartered AI cloud and GPU infrastructure provider. Its on-demand platform, Hyperstack, sells NVIDIA GPU and CPU virtual machines, managed Kubernetes clusters, block storage volumes, S3-compatible object storage and high-speed networking across three regions (CANADA-1, NORWAY-1, US-1), billed per minute. A second product, Hyperstack AI Studio, provides an OpenAI-compatible inference API over a catalog of third-party hosted text and image models, with playgrounds, system prompts, conversations and knowledge bases. The company also sells Secure Private Cloud, a single-tenant sovereign supercluster offering. Everything Hyperstack does in the console is available through a documented REST API at infrahub-api.nexgencloud.com, with official Python, Go, JavaScript and TypeScript SDKs, a Terraform provider, a Kubernetes CSI driver, a hosted read-only documentation MCP server and a self-hosted API MCP server.
image: https://www.hyperstack.cloud/hubfs/hyperstack_2023/home/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: NexGen Cloud MCP Server
  slug: nexgen-cloud-mcp-server
modified: '2026-08-26'
name: NexGen Cloud
nav: Providers
network: true
overview: 'NexGen Cloud publishes 2 APIs on the [APIs.io](https://apis.io/) network: Hyperstack API and Hyperstack AI Studio API. Tagged areas include Company, Cloud, GPU, Artificial Intelligence, and Machine Learning.


  The NexGen Cloud catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  NexGen Cloud''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Nexgen Cloud Plans Pricing
  plan_count: 4
  slug: nexgen-cloud-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Nexgen Cloud Rate Limits
  slug: nexgen-cloud-rate-limits
score:
  band: exemplar
  composite: 68.4
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 30.3
    contract_quality: 64.7
    developer_ergonomics: 66.1
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 63.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Nexgen Cloud Authentication
  slug: nexgen-cloud-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Nexgen Cloud Domain Security
  slug: nexgen-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Nexgen Cloud Trust Center
  slug: nexgen-cloud-trust-center
  summary_line: SOC 2, ISO 27001
slug: nexgen-cloud
tags:
- Company
- Cloud
- GPU
- Artificial Intelligence
- Machine Learning
- Infrastructure
- Compute
- Kubernetes
- Storage
- Inference
- Virtual Machines
- Sovereign AI
website: https://www.nexgencloud.com/
---
