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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Evolutionaryscale Agentic Access
  operation_count: 11
  slug: evolutionaryscale-agentic-access
  summary_line: 11 operations · 11 acting
api_count: 7
apis:
- description: Official Python SDK packaging ESM3 and ESM Cambrian model loaders, the `ESMProtein` multi-track data model, generation/sampling configurations, structure tokenization utilities, and a `forge.client()`
  name: EvolutionaryScale ESM Python SDK
  slug: esm-python-sdk
- description: Sequence-only tokenization and representation extraction.
  name: EvolutionaryScale Embeddings API
  slug: evolutionaryscale-embeddings-api
- description: Tokenize ESMProtein objects into ESMProteinTensor inputs (and back).
  name: EvolutionaryScale Encoding API
  slug: evolutionaryscale-encoding-api
- description: Generate proteins across sequence, structure, and function tracks.
  name: EvolutionaryScale Generation API
  slug: evolutionaryscale-generation-api
- description: Fetch multiple sequence alignments used by structure predictors.
  name: EvolutionaryScale MSA API
  slug: evolutionaryscale-msa-api
- description: Low-level forward passes with logits and sampling control.
  name: EvolutionaryScale Sampling API
  slug: evolutionaryscale-sampling-api
- description: Predict protein backbone coordinates from sequence and back.
  name: EvolutionaryScale Structure API
  slug: evolutionaryscale-structure-api
artifact_total: 25
collections:
- collection_type: open
  name: EvolutionaryScale Forge ESM3 API
  slug: open-evolutionaryscale-forge-esm3-api
- collection_type: open
  name: EvolutionaryScale Forge ESM Cambrian API
  slug: open-evolutionaryscale-forge-esmc-api
- collection_type: open
  name: EvolutionaryScale Forge Folding API
  slug: open-evolutionaryscale-forge-folding-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/evolutionaryscale-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evolutionaryscale-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/evolutionaryscale-authentication.yml
created: '2026-05-24'
description: EvolutionaryScale is a New York-based biology foundation model lab spun out of Meta AI's ESM team that develops AI to deepen scientific understanding of biology. Its flagship ESM3 model is a multimodal generative protein language model that reasons jointly across sequence, structure, and function, scaling to 98B parameters trained on 771B tokens from 2.78B natural proteins. The companion ESM Cambrian (ESM C) family provides protein representation learning at 300M–6B parameters as a performant ESM2 replacement. Models are accessible via the hosted Forge inference API (forge.evolutionaryscale.ai), an open-source Python SDK (`pip install esm`), open weights on Hugging Face, and AWS Marketplace (SageMaker, NVIDIA BioNeMo and NIM). EvolutionaryScale was integrated into the Biohub organization in 2025; the ESM SDK now lives at github.com/Biohub/esm.
examples:
- key_count: 2
  name: Evolutionaryscale Forge Esmc Logits Example
  slug: evolutionaryscale-forge-esmc-logits-example
- key_count: 2
  name: Evolutionaryscale Forge Fold Example
  slug: evolutionaryscale-forge-fold-example
- key_count: 2
  name: Evolutionaryscale Forge Generate Example
  slug: evolutionaryscale-forge-generate-example
finops:
- name: Evolutionaryscale Finops
  service_category: AI and Machine Learning
  slug: evolutionaryscale-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/evolutionaryscale.png
json_schemas:
- name: EvolutionaryScale ESMProtein
  property_count: 7
  slug: evolutionaryscale-esm-protein
- name: EvolutionaryScale GenerationConfig
  property_count: 7
  slug: evolutionaryscale-generation-config
- name: EvolutionaryScale LogitsOutput
  property_count: 3
  slug: evolutionaryscale-logits-output
jsonld:
- class_count: 0
  name: Evolutionaryscale Context
  property_count: 5
  slug: evolutionaryscale-context
layout: provider
modified: '2026-05-24'
name: EvolutionaryScale
nav: Providers
network: true
overview: 'EvolutionaryScale publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Embeddings API, Encoding API, Generation API, and 3 more. Tagged areas include AI, Artificial Intelligence, Biology, Bioinformatics, and Computational Biology.


  The EvolutionaryScale catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  EvolutionaryScale''s developer surface includes authentication and 2 more developer resources.'
plans:
- name: Evolutionaryscale Plans Pricing
  plan_count: 4
  slug: evolutionaryscale-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 7
  name: Evolutionaryscale Rate Limits
  slug: evolutionaryscale-rate-limits
rules:
- name: EvolutionaryScale API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: evolutionaryscale-jsonschema-spectral-rules
- name: EvolutionaryScale API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: evolutionaryscale-rules
score:
  band: developing
  composite: 45.3
  delta: -1.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 68.1
    developer_ergonomics: 10.9
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 31.6
  previous_composite: 46.8
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evolutionaryscale/refs/heads/main/screenshots/evolutionaryscale-2026-06-20T180917.png
security:
- kind: authentication
  name: Evolutionaryscale Authentication
  slug: evolutionaryscale-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Evolutionaryscale Domain Security
  slug: evolutionaryscale-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: evolutionaryscale
tags:
- AI
- Artificial Intelligence
- Biology
- Bioinformatics
- Computational Biology
- Drug Discovery
- ESM
- ESM3
- ESM Cambrian
- Foundation Models
- Generative Biology
- Life Sciences
- Machine Learning
- Protein Design
- Protein Folding
- Protein Language Models
- Proteins
- Representation Learning
- Structure Prediction
---
