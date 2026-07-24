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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 60.6
  scored_at: '2026-07-23'
api_count: 19
apis:
- description: 'OpenAI-compatible chat completions API (POST /v1/chat/completions) and, for supporting models, an Anthropic-compatible Messages API (POST /v1/messages). Drop-in: point the official OpenAI SDKs at the '
  name: OpenRelay Inference API
  slug: openrelay-inference-api
- description: 'The signed-in user: profile, memberships, and first-time onboarding.'
  name: OpenRelay Account API
  slug: openrelay-account-api
- description: Programmatic access keys (vl_…) used to authenticate with this API.
  name: OpenRelay API Keys API
  slug: openrelay-api-keys-api
- description: 'Batch inference jobs: submit a JSONL file of requests, poll status, and download results at a discounted rate. Served by the inference endpoint (inference.openrelay.inc). Batch access is enabled per o'
  name: OpenRelay Batches API
  slug: openrelay-batches-api
- description: Prepaid balance, saved cards, deposits, and auto-recharge.
  name: OpenRelay Billing API
  slug: openrelay-billing-api
- description: 'Public catalog: GPU models, availability, pricing, templates, and locations.'
  name: OpenRelay Catalog API
  slug: openrelay-catalog-api
- description: Autoscaling inference clusters that serve a container image behind an endpoint.
  name: OpenRelay Clusters API
  slug: openrelay-clusters-api
- description: Input and result files for the Batch API (JSONL, up to 200 MB and 50,000 records). Served by the inference endpoint (inference.openrelay.inc).
  name: OpenRelay Files API
  slug: openrelay-files-api
- description: Machine-to-machine endpoints used by platform infrastructure. Not part of the public API.
  name: OpenRelay Internal API
  slug: openrelay-internal-api
- description: Organizations and their members. Most resources are scoped to an org.
  name: OpenRelay Organizations API
  slug: openrelay-organizations-api
- description: 'For GPU providers: applications, nodes, provisioning tokens, and earnings.'
  name: OpenRelay Provider API
  slug: openrelay-provider-api
- description: Private container-registry credentials for pulling images.
  name: OpenRelay Registry Credentials API
  slug: openrelay-registry-credentials-api
- description: Managed GitHub Actions runner pools.
  name: OpenRelay Runners API
  slug: openrelay-runners-api
- description: Point-in-time VM snapshots and forking new VMs from them.
  name: OpenRelay Snapshots API
  slug: openrelay-snapshots-api
- description: Org-level SSH public keys that can be attached to VMs.
  name: OpenRelay SSH Keys API
  slug: openrelay-ssh-keys-api
- description: Move resources between organizations you belong to.
  name: OpenRelay Transfers API
  slug: openrelay-transfers-api
- description: Current-period usage and cost breakdowns.
  name: OpenRelay Usage API
  slug: openrelay-usage-api
- description: 'GPU virtual machines: lifecycle, disks, SSH access, and console links.'
  name: OpenRelay VMs API
  slug: openrelay-vms-api
- description: Subscribe to platform events with signed HTTP callbacks.
  name: OpenRelay Webhooks API
  slug: openrelay-webhooks-api
artifact_total: 24
asyncapis:
- description: ''
  name: Openrelay Webhooks
  slug: openrelay-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.openrelay.inc
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openrelay.inc
- group: docs
  title: ''
  type: APIReference
  url: https://docs.openrelay.inc/docs/account/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.openrelay.inc/docs/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://app.openrelay.inc/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://openrelay.inc/pricing
- group: company
  title: ''
  type: Blog
  url: https://openrelay.inc/blog
- group: operate
  title: ''
  type: Support
  url: https://forum.openrelay.inc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenRelayInc
- group: operate
  title: ''
  type: StatusPage
  url: https://openrelay.inc/status
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/openrelay-changelog.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openrelay.inc/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openrelay.inc/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/openrelay-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openrelay-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/openrelay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/openrelay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/openrelay-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openrelay-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/openrelay-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/openrelay-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openrelay-llms.txt
- group: build
  title: ''
  type: CLI
  url: cli/openrelay-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/openrelay-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openrelay-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/openrelay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/openrelay-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/openrelay-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/openrelay-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'OpenRelay is a Y Combinator-backed distributed GPU cloud for production AI inference — "the CDN of inference." It runs a global mesh of GPUs (RTX 4090/5090, A100, H100) that teams reach through a single API: rent dedicated GPU VMs with SSH and persistent volumes, stand up autoscaling inference clusters behind an endpoint, or call hosted open models via an OpenAI-compatible (and Anthropic Messages-compatible) API. Anyone can also join as a provider and earn on idle compute. The control-plane REST API (api.openrelay.inc) manages orgs, VMs, clusters, snapshots, billing, usage, transfers, provider nodes, batches, files, and webhooks, and is fully driveable from the first-party `orl` CLI — which also ships an official MCP server for agents. Traffic reroutes across healthy nodes in milliseconds, with pricing OpenRelay claims is up to 90% cheaper than the hyperscalers.'
image: https://openrelay.inc/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: openrelay-mcp.yml
  slug: openrelay-mcpyml
modified: '2026-07-20'
name: OpenRelay
nav: Providers
network: true
overview: 'OpenRelay publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Account API, API Keys API, Batches API, and 15 more. Tagged areas include Company, GPU, Inference, AI, and Machine Learning.


  The OpenRelay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OpenRelay''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 23 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 57.8
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 61.1
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 57.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Openrelay Authentication
  slug: openrelay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openrelay Domain Security
  slug: openrelay-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Openrelay Vulnerability Disclosure
  slug: openrelay-vulnerability-disclosure
  summary_line: Hackerone
slug: openrelay
tags:
- Company
- GPU
- Inference
- AI
- Machine Learning
- Cloud Compute
- Infrastructure
- OpenAI-Compatible
- GPU Cloud
- LLM
website: https://app.openrelay.inc
---
