---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 27.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: ScalarLM is the open-source (CC0-1.0) unified LLM training and inference stack maintained and sponsored by TensorWave. A single deployment exposes an OpenAI-compatible inference endpoint backed by vLL
  name: ScalarLM API
  slug: scalarlm
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/tensorwave-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://tensorwave.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tensorwave.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensorwave.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tensorwave.com/welcome-to-tensorwave/bare-metal-quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.tensorwave.com/support/filing-support-tickets
- group: company
  title: ''
  type: Blog
  url: https://tensorwave.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tensorwavecloud
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tensorwave.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tensorwave.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://security.tensorwave.com/
- group: auth
  title: ''
  type: Security
  url: https://security.tensorwave.com/
- group: operate
  title: ''
  type: Contact
  url: https://tensorwave.com/connect
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tensorwave-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/tensorwave-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tensorwave-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tensorwave-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tensorwave-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tensorwave-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tensorwave-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tensorwave-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tensorwave-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tensorwave-vulnerability-disclosure.yml
created: '2026-08-02'
description: TensorWave is a Las Vegas-headquartered AI cloud provider that builds and operates bare-metal GPU infrastructure exclusively on AMD Instinct accelerators (MI300X, MI325X, MI355X and MI455X) with AMD's open ROCm software stack. The company sells dedicated GPU nodes, high-speed network storage, and managed Slurm and Kubernetes clusters for AI model training, fine-tuning and inference, with observability, job scheduling, alerting and expert support layered on top. Access to the compute platform itself is delivered over SSH, Slurm and Kubernetes rather than a public REST control-plane API. TensorWave's public API surface is ScalarLM, the CC0-licensed unified training-and-inference stack it maintains and sponsors alongside RelationalAI, which exposes an OpenAI-compatible inference endpoint backed by vLLM together with a Megatron-LM training surface from a single deployment.
image: https://cdn.builder.io/api/v1/image/assets%2Ff941d509b8ea45f8972dd215996c7055%2Fdb1d4443bf134999962dbc3ab17eb3e6
layout: provider
modified: '2026-08-02'
name: TensorWave
nav: Providers
network: true
overview: 'TensorWave publishes 1 API on the [APIs.io](https://apis.io/) network: ScalarLM API. Tagged areas include Company, Artificial Intelligence, Machine Learning, Cloud Computing, and GPU.


  TensorWave''s developer surface includes documentation, getting-started guide, support, engineering blog, CLI, changelog, and 17 more developer resources.'
random_paper: 85
score:
  band: developing
  composite: 45.4
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 52.7
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 31.6
  previous_composite: 45.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Tensorwave Authentication
  slug: tensorwave-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tensorwave Domain Security
  slug: tensorwave-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tensorwave Vulnerability Disclosure
  slug: tensorwave-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Tensorwave Trust Center
  slug: tensorwave-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: tensorwave
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Cloud Computing
- GPU
- Infrastructure
- Inference
- Model Training
- High Performance Computing
- Data Centers
website: https://tensorwave.com/
---
