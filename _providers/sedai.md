---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Sedai is an AI-driven autonomous cloud optimization platform using reinforcement learning to continuously adjust resources in real-time.
  name: Sedai
  slug: sedai
artifact_total: 7
asyncapis:
- description: ''
  name: Sedai Webhooks
  slug: sedai-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sedai-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sedai
- group: company
  title: ''
  type: Website
  url: https://sedai.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sedai.io/
- group: agent
  title: ''
  type: LlmsText
  url: https://sedai.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://sedai.io/blog
- group: build
  title: ''
  type: Packages
  url: packages/sedai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sedai-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sedai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/sedai-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sedai-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SedaiEngineering
- group: commercial
  title: ''
  type: Pricing
  url: https://sedai.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.sedai.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sedai.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sedai.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://sedai.io/contact
- group: company
  title: ''
  type: Twitter
  url: https://x.com/sedai_io
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@sedaicloud
created: '2026-03-27'
description: 'Sedai is an autonomous cloud and AI optimization platform. It continuously analyzes application behavior — traffic, resource utilization, latency and errors — and then adjusts cloud configuration in real time to cut cost, improve performance and protect availability, across Kubernetes, VMs, serverless, storage, databases, GPUs and AI agent workloads on AWS, Azure and GCP. It operates in three modes: Datapilot (observe only), Copilot (human approves each change) and Autopilot (fully autonomous). Sedai exposes a tenant-scoped platform API at https://{tenant}.sedai.app reached through first-party Python and TypeScript SDKs, a Terraform provider and a Helm chart for its in-cluster Smart Agent, but publishes no OpenAPI and no public API reference on its documentation site.'
finops:
- name: Sedai Finops
  service_category: API
  slug: sedai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sedai.png
layout: provider
modified: '2026-08-29'
name: Sedai
nav: Providers
network: true
overview: 'Sedai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Optimization, FinOps, Kubernetes, Cloud Cost Management, and Autonomous Operations.


  The Sedai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sedai''s developer surface includes documentation, engineering blog, pricing, signup flow, support, YouTube channel, and 13 more developer resources.'
plans:
- name: Sedai Plans Pricing
  plan_count: 0
  slug: sedai-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Sedai Rate Limits
  slug: sedai-rate-limits
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 44.3
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sedai/refs/heads/main/screenshots/sedai-2026-06-20T193631.png
security:
- kind: authentication
  name: Sedai Authentication
  slug: sedai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sedai Domain Security
  slug: sedai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sedai
tags:
- Cloud Optimization
- FinOps
- Kubernetes
- Cloud Cost Management
- Autonomous Operations
- Observability
- Artificial Intelligence
- DevOps
website: https://sedai.io/
---
