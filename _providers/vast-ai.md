---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 64
  human_in_the_loop: 2
  name: Vast Ai Agentic Access
  operation_count: 89
  slug: vast-ai-agentic-access
  summary_line: 89 operations · 64 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The Vast.ai REST API is the control plane for the GPU marketplace. It supports searching offers across hosts, renting and managing instances, configuring machines and templates, attaching persistent v
  name: Vast.ai REST API
  slug: rest-api
- baseURL: https://console.vast.ai/api/v0
  baseurl_source: declared
  description: The Accounts API from Vast.ai — 13 operation(s) for accounts.
  name: Vast.ai Accounts API
  slug: vast-ai-accounts-api
- baseURL: https://console.vast.ai/api/v0
  baseurl_source: declared
  description: The Billing API from Vast.ai — 4 operation(s) for billing.
  name: Vast.ai Billing API
  slug: vast-ai-billing-api
- baseURL: https://console.vast.ai/api/v0
  baseurl_source: declared
  description: The Instances API from Vast.ai — 14 operation(s) for instances.
  name: Vast.ai Instances API
  slug: vast-ai-instances-api
- baseURL: https://console.vast.ai/api/v0
  baseurl_source: declared
  description: The Machines API from Vast.ai — 10 operation(s) for machines.
  name: Vast.ai Machines API
  slug: vast-ai-machines-api
- baseURL: https://console.vast.ai/api/v0
  baseurl_source: declared
  description: The Network Volumes API from Vast.ai — 4 operation(s) for network volumes.
  name: Vast.ai Network Volumes API
  slug: vast-ai-network-volumes-api
- baseURL: https://console.vast.ai/api/v0
  baseurl_source: declared
  description: The Search API from Vast.ai — 3 operation(s) for search.
  name: Vast.ai Search API
  slug: vast-ai-search-api
- baseURL: https://console.vast.ai/api/v0
  baseurl_source: declared
  description: The Serverless API from Vast.ai — 9 operation(s) for serverless.
  name: Vast.ai Serverless API
  slug: vast-ai-serverless-api
- baseURL: https://console.vast.ai/api/v0
  baseurl_source: declared
  description: The Team API from Vast.ai — 9 operation(s) for team.
  name: Vast.ai Team API
  slug: vast-ai-team-api
- baseURL: https://console.vast.ai/api/v0
  baseurl_source: declared
  description: The Templates API from Vast.ai — 1 operation(s) for templates.
  name: Vast.ai Templates API
  slug: vast-ai-templates-api
- baseURL: https://console.vast.ai/api/v0
  baseurl_source: declared
  description: The Volumes API from Vast.ai — 4 operation(s) for volumes.
  name: Vast.ai Volumes API
  slug: vast-ai-volumes-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vast.ai Accounts API
  slug: open-vast-ai-accounts-api
- collection_type: open
  name: Vast.ai Accounts Billing API
  slug: open-vast-ai-billing-api
- collection_type: open
  name: Vast.ai Accounts Instances API
  slug: open-vast-ai-instances-api
- collection_type: open
  name: Vast.ai Accounts Machines API
  slug: open-vast-ai-machines-api
- collection_type: open
  name: Vast.ai Accounts Network Volumes API
  slug: open-vast-ai-network-volumes-api
- collection_type: open
  name: Vast.ai Accounts Search API
  slug: open-vast-ai-search-api
- collection_type: open
  name: Vast.ai Accounts Serverless API
  slug: open-vast-ai-serverless-api
- collection_type: open
  name: Vast.ai Accounts Team API
  slug: open-vast-ai-team-api
- collection_type: open
  name: Vast.ai Accounts Templates API
  slug: open-vast-ai-templates-api
- collection_type: open
  name: Vast.ai Accounts Volumes API
  slug: open-vast-ai-volumes-api
- collection_type: open
  name: Vast.ai API
  slug: open-vast-ai
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/vast-ai-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vast-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vast-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vast-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vast-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://vast.ai
- group: other
  title: ''
  type: Developer
  url: https://docs.vast.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vast.ai
- group: start
  title: ''
  type: Portal
  url: https://cloud.vast.ai
- group: start
  title: ''
  type: Signup
  url: https://cloud.vast.ai/create
- group: start
  title: ''
  type: Login
  url: https://cloud.vast.ai/login
- group: commercial
  title: ''
  type: Pricing
  url: https://vast.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://vast.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vast.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vast.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://vast.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vast-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vast-ai
- group: build
  title: ''
  type: CLI
  url: https://github.com/vast-ai/vast-cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/vast-ai/vast-sdk
- group: build
  title: ''
  type: Examples
  url: https://github.com/vast-ai/base-image
- group: other
  title: ''
  type: GPUs
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.vast.ai/llms.txt
created: '2026-05-23'
description: Vast.ai is a decentralized GPU marketplace that matches buyers with 40+ datacenters and individual hosts renting out NVIDIA GPUs at market prices. It exposes a REST API, Python SDK, and vastai CLI for searching GPU offers, renting instances, attaching persistent volumes, and running serverless workloads across 68+ GPU types including H100, H200, B200, A100, and consumer RTX cards.
features:
- description: Market-driven matching of buyers with 40+ datacenters and individual hosts across 68+ GPU types.
  name: GPU Marketplace
- description: Per-second-billed GPU rentals with guaranteed uptime, with no minimum hours.
  name: On-Demand Instances
- description: Fault-tolerant workloads priced 50%+ cheaper than on-demand with potential preemption.
  name: Interruptible Instances
- description: Up to 50% discounts on 1, 3, or 6-month commitments for stable workloads.
  name: Reserved Capacity
- description: Serverless GPU workers built on the pyworker agent for autoscaling inference.
  name: Serverless Endpoints
- description: Pre-configured instance templates for fast launching of common workloads.
  name: Templates
finops:
- name: Vast Ai Finops
  service_category: API
  slug: vast-ai-finops
graphqls:
- description: Vast.ai is a decentralized GPU marketplace for AI and ML workloads. The API covers instance rental, machine offers, container management, SSH access configuration, and billing for on-demand and spot G
  name: Vast.ai GraphQL API
  slug: vast-ai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vast-ai.png
integrations:
- description: Bring-your-own Docker image support across all rental instances.
  name: Docker
- description: Direct SSH access to rented instances for development and orchestration.
  name: SSH
layout: provider
modified: '2026-05-23'
name: Vast.ai
nav: Providers
network: true
overview: 'Vast.ai publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Billing API, Instances API, and 7 more. Tagged areas include Artificial Intelligence, Cloud, Compute, GPU, and Machine-Learning.


  Vast.ai''s developer surface includes authentication, documentation, developer portal, signup flow, pricing, engineering blog, support, and 15 more developer resources.'
plans:
- name: Vast Ai Plans Pricing
  plan_count: 1
  slug: vast-ai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Vast Ai Rate Limits
  slug: vast-ai-rate-limits
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 0.0
    contract_quality: 61.8
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vast-ai/refs/heads/main/screenshots/vast-ai-2026-06-20T200827.png
security:
- kind: authentication
  name: Vast Ai Authentication
  slug: vast-ai-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Vast Ai Domain Security
  slug: vast-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vast Ai Trust Center
  slug: vast-ai-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: vast-ai
tags:
- Artificial Intelligence
- Cloud
- Compute
- GPU
- Machine-Learning
- Marketplace
- Serverless
website: https://vast.ai
---
