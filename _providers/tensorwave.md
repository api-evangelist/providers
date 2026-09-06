---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://gpt-oss.cray-lm.com
  baseurl_source: declared
  description: Queue-backed batch inference and worker coordination.
  name: TensorWave Generate API
  slug: tensorwave-generate-api
- baseURL: https://gpt-oss.cray-lm.com
  baseurl_source: declared
  description: Health checks, service logs and metrics.
  name: TensorWave Health API
  slug: tensorwave-health-api
- baseURL: https://gpt-oss.cray-lm.com
  baseurl_source: declared
  description: OpenAI-compatible inference endpoints proxied to vLLM.
  name: TensorWave Open AI API
  slug: tensorwave-openai-api
- baseURL: https://gpt-oss.cray-lm.com
  baseurl_source: declared
  description: Slurm scheduler status and job control.
  name: TensorWave Slurm API
  slug: tensorwave-slurm-api
- baseURL: https://gpt-oss.cray-lm.com
  baseurl_source: declared
  description: Megatron-LM training jobs, chunked dataset upload, checkpoints and Hugging Face publishing.
  name: TensorWave Training API
  slug: tensorwave-training-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ScalarLM Generate API
  slug: open-tensorwave-generate-api
- collection_type: open
  name: ScalarLM Health API
  slug: open-tensorwave-health-api
- collection_type: open
  name: ScalarLM Open AI API
  slug: open-tensorwave-openai-api
- collection_type: open
  name: ScalarLM Slurm API
  slug: open-tensorwave-slurm-api
- collection_type: open
  name: ScalarLM Training API
  slug: open-tensorwave-training-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tensorwave-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/tensorwavecloud/ScalarLM/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/tensorwavecloud/ScalarLM/releases
- group: agent
  title: ''
  type: AgentSkill
  url: skills/tensorwave-batch-inference.md
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tensorwave-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tensorwave-scalarlm-overlay.yaml
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
overview: 'TensorWave publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Generate API, Health API, Open AI API, and 2 more. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Cloud Computing, and GPU.


  TensorWave''s developer surface includes documentation, getting-started guide, support, engineering blog, CLI, changelog, and 23 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 48.3
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 47.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tensorwave/refs/heads/main/screenshots/tensorwave-2026-08-17T082314.png
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
- Machine-Learning
- Cloud Computing
- GPU
- Infrastructure
- Inference
- Model Training
- High Performance Computing
- Data Centers
website: https://tensorwave.com/
---
