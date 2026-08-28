---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.3
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mosaicml-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mosaicml-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.databricks.com/research/mosaic
- group: company
  title: ''
  type: LegacyWebsite
  url: https://www.mosaicml.com
- group: other
  title: ''
  type: Product
  url: https://www.databricks.com/product/machine-learning/mosaic-ai-model-training
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mosaicml.com/en/latest/
- group: build
  title: ''
  type: SDKs
  url: https://docs.mosaicml.com/projects/mcli/en/latest/
- group: learn
  title: ''
  type: PretrainingAPI
  url: https://docs.mosaicml.com/projects/mcli/en/latest/training/pretraining_api.html
- group: other
  title: ''
  type: FinetuningAPI
  url: https://docs.mosaicml.com/projects/mcli/en/latest/finetuning/finetuning_api.html
- group: other
  title: ''
  type: Composer
  url: https://docs.mosaicml.com/projects/composer/en/stable/
- group: other
  title: ''
  type: Streaming
  url: https://docs.mosaicml.com/projects/streaming/en/stable/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mosaicml
- group: agent
  title: ''
  type: LLMFoundry
  url: https://github.com/mosaicml/llm-foundry
- group: other
  title: ''
  type: ComposerRepo
  url: https://github.com/mosaicml/composer
- group: other
  title: ''
  type: StreamingRepo
  url: https://github.com/mosaicml/streaming
- group: build
  title: ''
  type: Examples
  url: https://github.com/mosaicml/examples
- group: company
  title: ''
  type: Blog
  url: https://www.databricks.com/blog/category/ai/databricks-ai
- group: other
  title: ''
  type: Acquisition
  url: https://www.databricks.com/blog/2023/06/26/databricks-acquires-mosaicml-leading-generative-ai-platform.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.databricks.com/product/pricing
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/DbrxMosaicAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/databricks
created: '2026-05-25'
description: MosaicML was a San Francisco-based foundation model training company founded in 2021 by Naveen Rao and Hanlin Tang to make large-scale model training faster and cheaper through algorithmic and systems efficiency. Databricks acquired MosaicML in July 2023 for approximately $1.3 billion and folded the team and platform into Databricks Mosaic AI Research. The MosaicML training platform is now delivered as Databricks Mosaic AI Training (pretraining and finetuning), and the original mosaicml.com domain redirects to the Databricks Mosaic Research microsite. MosaicML's surviving open-source artifacts include Composer (a PyTorch training library with built-in speedup recipes), Streaming (a cloud-native dataset format for efficient distributed training), LLM Foundry (the training code behind Databricks' DBRX foundation model), the Diffusion training stack, and the MCLI command line and Python SDK that orchestrate Pretraining and Finetuning jobs against the managed training service. The
  Mosaic AI Training service itself is accessed exclusively through the MCLI command line, the mosaicml-cli Python SDK, and Databricks workspace integrations — there is no publicly published REST OpenAPI surface for the training control plane. Commercial access requires a Databricks account; pricing is consumption-based via Databricks DBU billing rather than an independent MosaicML pricing page.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mosaicml.png
layout: provider
modified: '2026-05-25'
name: MosaicML
nav: Providers
network: true
overview: 'MosaicML is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Foundation Models, Model Training, Pretraining, and Fine-Tuning.


  MosaicML''s developer surface includes documentation, GitHub presence, code examples, engineering blog, pricing, and 16 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 12.8
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mosaicml/refs/heads/main/screenshots/mosaicml-2026-06-20T185818.png
security:
- kind: domain-security
  name: Mosaicml Domain Security
  slug: mosaicml-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mosaicml Vulnerability Disclosure
  slug: mosaicml-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mosaicml
tags:
- Artificial Intelligence
- Foundation Models
- Model Training
- Pretraining
- Fine-Tuning
- LLM
- Generative AI
- PyTorch
- Distributed Training
- GPU
- Databricks
- DBRX
- Composer
- Streaming
- LLM Foundry
website: https://www.databricks.com/research/mosaic
---
