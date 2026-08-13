---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Marqo Agentic Access
  operation_count: 16
  slug: marqo-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 7
apis:
- description: Add, update, get, and delete documents in an index.
  name: Marqo Documents API
  slug: marqo-documents-api
- description: Generate embedding vectors using engine-loaded models.
  name: Marqo Embeddings API
  slug: marqo-embeddings-api
- description: Create, list, inspect, and delete tensor / lexical indexes.
  name: Marqo Indexes API
  slug: marqo-indexes-api
- description: Inspect, load, and eject embedding models from the engine.
  name: Marqo Models API
  slug: marqo-models-api
- description: Return documents similar to one or more reference documents.
  name: Marqo Recommendations API
  slug: marqo-recommendations-api
- description: Tensor, lexical, and hybrid search across an index.
  name: Marqo Search API
  slug: marqo-search-api
- description: Health, readiness, and engine-level metadata.
  name: Marqo Telemetry API
  slug: marqo-telemetry-api
artifact_total: 41
collections:
- collection_type: open
  name: Marqo REST API
  slug: open-marqo
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/marqo-ai/marqo/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/marqo-ai/marqo/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/marqo-ai/marqo/blob/mainline/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/marqo-ai/marqo/blob/mainline/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/marqo-ai/marqo/blob/mainline/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/marqo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marqo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/marqo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.marqo.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/marqo-ai
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/marqo-ai/marqo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/marqo-ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.marqo.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/marqo-ai/marqo#getting-started
- group: commercial
  title: ''
  type: License
  url: https://github.com/marqo-ai/marqo/blob/mainline/LICENSE
- group: company
  title: ''
  type: Blog
  url: https://www.marqo.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.marqo.ai/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/marqo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/marqo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/marqo-finops.yml
- group: build
  title: ''
  type: SDKs
  url: https://github.com/marqo-ai/py-marqo
- group: build
  title: ''
  type: SDKs
  url: https://github.com/marqo-ai/marqo-instantsearch-client
- group: build
  title: ''
  type: Tools
  url: https://github.com/marqo-ai/terraform-provider-marqo
- group: build
  title: ''
  type: Tools
  url: https://github.com/marqo-ai/marqo-base
- group: build
  title: ''
  type: Tools
  url: https://github.com/marqo-ai/ingrain_server
- group: other
  title: ''
  type: Models
  url: https://github.com/marqo-ai/marqo-ecommerce-embeddings
- group: other
  title: ''
  type: Models
  url: https://github.com/marqo-ai/marqo-FashionCLIP
- group: other
  title: ''
  type: Research
  url: https://github.com/marqo-ai/GCL
- group: build
  title: ''
  type: Examples
  url: https://github.com/marqo-ai/local-image-search-demo
- group: learn
  title: ''
  type: Course
  url: https://github.com/marqo-ai/fine-tuning-embedding-models-course
created: '2026-05-08'
description: Marqo is an open-source, multimodal vector search engine that lets developers index text and images, generate embeddings on the fly, and run tensor, lexical, and hybrid search through a single REST API. Built on Vespa for storage and retrieval and FastAPI for the HTTP surface, Marqo bundles model inference (Sentence Transformers, OpenCLIP, ONNX) inside the engine so a single `docker run` produces a working semantic search stack. The Apache 2.0 open-source engine has been marked deprecated by the maintainers as Marqo pivots to a hosted ecommerce search product, but the project remains widely forked, downloaded, and self-hosted, with active sibling repositories for the Python client, Terraform provider, InstantSearch client, ecommerce embedding models, and Generalised Contrastive Learning research.
features:
- Open-source Apache 2.0 vector search engine (project marked deprecated by maintainers; still 5,000+ stars and actively forked)
- Single `docker run` install bundling Vespa storage and embedding model inference
- Tensor, lexical, and hybrid search through a unified REST API
- Multimodal indexing of text and images with on-engine inference
- Embedding generation via Sentence Transformers, OpenCLIP, and ONNX models
- Generalised Contrastive Learning (GCL) framework for fine-tuned retrieval
- Marqo-FashionCLIP and marqo-ecommerce-embeddings open-weight models
- Recommendations, filters, and structured + unstructured fields
- FastAPI runtime exposing live `/openapi.json` and Swagger UI at `/docs`
- Compose files for inference, model management, and Triton-backed serving
- Python client (py-marqo), Terraform provider, and InstantSearch client
- Hosted Marqo Cloud surface preserves API parity for legacy users
finops:
- name: Marqo Finops
  service_category: Vector Database
  slug: marqo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marqo.png
integrations:
- description: Vespa is the underlying storage and retrieval engine that backs every Marqo index.
  name: Vespa
- description: Default text embedding model family loaded by the engine for tensor search.
  name: Sentence Transformers
- description: Multimodal text-and-image embedding family used for visual and cross-modal search.
  name: OpenCLIP
- description: Models are pulled from Hugging Face hubs at first use unless preloaded.
  name: Hugging Face
- description: '`compose-triton.yaml` ships a Triton-backed model server profile for GPU inference.'
  name: NVIDIA Triton
- description: terraform-provider-marqo manages Marqo Cloud indexes as infrastructure-as-code.
  name: Terraform
- description: marqo-instantsearch-client adapts Marqo to the InstantSearch.js front-end conventions.
  name: Algolia InstantSearch
- description: Hosted Marqo product offers one-click integration for Shopify catalogs.
  name: Shopify
- description: Hosted Marqo product offers Adobe Commerce / Magento connector.
  name: Adobe Commerce
- description: Hosted Marqo product offers Salesforce Commerce Cloud connector.
  name: Salesforce Commerce Cloud
layout: provider
modified: '2026-05-25'
name: Marqo
nav: Providers
network: true
overview: 'Marqo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Embeddings API, Indexes API, and 4 more. Tagged areas include Vector Database, Vector Search, Multimodal, Semantic Search, and Embeddings.


  Marqo''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, tooling, code examples, and 23 more developer resources.'
plans:
- name: Marqo Plans Pricing
  plan_count: 1
  slug: marqo-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 1
  name: Marqo Rate Limits
  slug: marqo-rate-limits
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 50.7
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marqo/refs/heads/main/screenshots/marqo-2026-06-20T185006.png
security:
- kind: authentication
  name: Marqo Authentication
  slug: marqo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Marqo Domain Security
  slug: marqo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: marqo
tags:
- Vector Database
- Vector Search
- Multimodal
- Semantic Search
- Embeddings
- AI
- Machine Learning
- Open Source
- Ecommerce Search
use_cases:
- description: Index text and images into a single tensor store and query with natural-language or image inputs, with embedding inference running inside the engine.
  name: Multimodal Semantic Search
- description: Power RAG pipelines by serving the nearest-neighbor retrieval layer for LLM context windows over private corpora.
  name: Retrieval-Augmented Generation
- description: Drive product search, recommendations, and merchandising-aware ranking using semantic relevance plus structured filters and boosts.
  name: Ecommerce Product Discovery
- description: Search product catalogs and image libraries using image-to-image and text-to-image similarity through OpenCLIP / Marqo-FashionCLIP.
  name: Visual Search
- description: Stand up an Apache 2.0 vector search service alongside your application stack with `docker run`, no separate embedding service required.
  name: Self-Hosted Vector Backend
website: https://www.marqo.ai/
---
