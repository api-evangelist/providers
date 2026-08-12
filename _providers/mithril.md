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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 22
  human_in_the_loop: 2
  name: Mithril Agentic Access
  operation_count: 54
  slug: mithril-agentic-access
  summary_line: 54 operations · 22 acting · 2 human-in-the-loop
api_count: 14
apis:
- description: The API Keys API from Mithril — 2 operation(s) for api keys.
  name: Mithril API Keys API
  slug: mithril-api-keys-api
- description: The image versions API from Mithril — 2 operation(s) for image versions.
  name: Mithril image versions API
  slug: mithril-image-versions-api
- description: The instance types API from Mithril — 2 operation(s) for instance types.
  name: Mithril instance types API
  slug: mithril-instance-types-api
- description: The instances API from Mithril — 5 operation(s) for instances.
  name: Mithril instances API
  slug: mithril-instances-api
- description: The kubernetes clusters API from Mithril — 2 operation(s) for kubernetes clusters.
  name: Mithril kubernetes clusters API
  slug: mithril-kubernetes-clusters-api
- description: The lifecycle scripts API from Mithril — 3 operation(s) for lifecycle scripts.
  name: Mithril lifecycle scripts API
  slug: mithril-lifecycle-scripts-api
- description: The pricing API from Mithril — 2 operation(s) for pricing.
  name: Mithril pricing API
  slug: mithril-pricing-api
- description: The profile API from Mithril — 2 operation(s) for profile.
  name: Mithril profile API
  slug: mithril-profile-api
- description: The projects API from Mithril — 1 operation(s) for projects.
  name: Mithril projects API
  slug: mithril-projects-api
- description: The quotas API from Mithril — 1 operation(s) for quotas.
  name: Mithril quotas API
  slug: mithril-quotas-api
- description: The reservations API from Mithril — 10 operation(s) for reservations.
  name: Mithril reservations API
  slug: mithril-reservations-api
- description: The spot API from Mithril — 5 operation(s) for spot.
  name: Mithril spot API
  slug: mithril-spot-api
- description: The SSH Keys API from Mithril — 2 operation(s) for ssh keys.
  name: Mithril SSH Keys API
  slug: mithril-ssh-keys-api
- description: The volumes API from Mithril — 2 operation(s) for volumes.
  name: Mithril volumes API
  slug: mithril-volumes-api
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://mithril.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mithril.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mithril.ai/compute-api/api-overview-and-quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mithril.ai/compute-api/compute-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mithril.ai/getting-started/welcome-to-mithril
- group: start
  title: ''
  type: SignUp
  url: https://login.mithril.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.mithril.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://mithril.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://mithril.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://mithril.ai/contact-sales
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.mithril.ai/security-and-trust/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.mithril.ai/security-and-trust/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mithril.ai
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mithril-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mithril-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/mithril-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mithril-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/mithril-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mithril-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mithril-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mithril-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/mithril-compute-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/mithril-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.mlfoundry.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/mithril-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mithril-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mithril-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mithril-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mithril-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mithril-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.mithril.ai/security-and-trust/reporting-security-concerns
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mithril-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mithril-agentic-access.yml
created: '2026-07-17'
description: Mithril is an AI omnicloud compute platform, operated by Foundry Technologies, that aggregates GPU, CPU, and storage capacity across multiple cloud providers behind a single interface with transparent, market-based pricing. Developers reserve NVIDIA A100/H100/H200 GPUs on flexible reservations or burst onto interruptible spot capacity via price-limited bids, attach WEKA/NVMe persistent storage, run Kubernetes clusters, and drive it all through the v2 Compute REST API, the `ml` CLI, and a Python batch/inference SDK. Used for training, fine-tuning, inference, and batch workloads; SOC 2 Type II certified. Backed by Lightspeed, Multicoin Capital, and Redpoint.
image: https://app.mithril.ai/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: mithril-mcp.yml
  slug: mithril-mcpyml
modified: '2026-07-20'
name: Mithril
nav: Providers
network: true
overview: 'Mithril publishes 14 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, image versions API, instance types API, and 11 more. Tagged areas include Company, GPU Cloud, AI Infrastructure, Machine Learning, and Cloud Computing.


  Mithril''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 27 more developer resources.'
random_paper: 65
score:
  band: strong
  composite: 56.7
  delta: -0.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.7
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 42.1
  previous_composite: 57.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mithril/refs/heads/main/screenshots/mithril-2026-08-07T183809.png
security:
- kind: authentication
  name: Mithril Authentication
  slug: mithril-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mithril Domain Security
  slug: mithril-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mithril Vulnerability Disclosure
  slug: mithril-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Mithril Trust Center
  slug: mithril-trust-center
  summary_line: SOC 2 Type II (availability, security, confidentiality)
slug: mithril
tags:
- Company
- GPU Cloud
- AI Infrastructure
- Machine Learning
- Cloud Computing
- Compute
- Spot Instances
- Kubernetes
- GPU
website: https://mithril.ai
---
