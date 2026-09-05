---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    agent_skills: true
    agentic_access: derived
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
  score: 30.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Segmind Agentic Access
  operation_count: 12
  slug: segmind-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 1
apis:
- description: The Segmind AI Gateway — one REST surface in front of 200+ generative AI models for image, video, audio, 3D and text, authenticated with a single API key and metered against a prepaid credit balance.
  name: Segmind
  slug: segmind
- baseURL: https://api.segmind.com
  baseurl_source: declared
  description: Synchronous (v1) and asynchronous (v2) model inference. v2 is the current contract — submit a job, poll a lightweight status endpoint, fetch the result — and reports cost, remaining credits and timing
  name: Segmind Inference API
  slug: segmind-inference-api
- baseURL: https://api.segmind.com
  baseurl_source: declared
  description: Read the account's spendable and free credit balance. Runs no model and costs nothing, and is the documented way to verify that an API key works.
  name: Segmind Account API
  slug: segmind-account-api
- baseURL: https://workflows-api.segmind.com
  baseurl_source: declared
  description: Upload a file to Segmind Storage and get a reusable URL to pass as an image input to any model, instead of re-uploading the same file. Served from the workflows host.
  name: Segmind Storage API
  slug: segmind-storage-api
- description: Call a published PixelFlow workflow over REST. Submit to POST /workflows/v2/{slug} with the key names given to the workflow's input nodes, poll the status URL, and fetch the result — the same async co
  name: Segmind PixelFlow Workflow API
  slug: segmind-workflow-api
- description: Manage dedicated GPU endpoints programmatically — list, add, update capacity and delete. Served from a separate control-plane host and authenticated with the same API key. Add, update and delete share
  name: Segmind Dedicated Endpoints API
  slug: segmind-endpoints-api
- baseURL: https://api.segmind.com
  baseurl_source: declared
  description: DEPRECATED. Fine-tuning request management and data handling. Segmind's fine-tuning service no longer accepts new training jobs; existing fine-tuned models remain available for inference until further
  name: Segmind Fine-tuning API
  slug: segmind-fine-tuning-api
artifact_total: 21
asyncapis:
- description: ''
  name: Segmind Webhooks
  slug: segmind-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Segmind Account API
  slug: open-segmind-account-api
- collection_type: open
  name: Segmind Account Fine-tuning API
  slug: open-segmind-fine-tuning-api
- collection_type: open
  name: Segmind Account Inference API
  slug: open-segmind-inference-api
- collection_type: open
  name: Segmind Account Storage API
  slug: open-segmind-storage-api
- collection_type: open
  name: Segmind API
  slug: open-segmind
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/segmind-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.segmind.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.segmind.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.segmind.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.segmind.com/docs/serverless-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.segmind.com/docs/get-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.segmind.com/docs/get-started/support
- group: start
  title: ''
  type: SignUp
  url: https://platform.segmind.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.segmind.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.segmind.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.segmind.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.segmind.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/segmind-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/segmind-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/segmind-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/segmind-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/segmind-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/segmind-finops.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/segmind-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/segmind-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/segmind-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/segmind-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/segmind-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/segmind-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/segmind-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/segmind-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/segmind-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/segmind-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/segmind-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/segmind-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/segmind-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/segmind-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://www.segmind.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/segmind
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/segmind
- group: company
  title: ''
  type: Blog
  url: https://blog.segmind.com/feed
created: '2025-03-01'
description: Segmind is a serverless GPU inference platform that puts 200+ generative AI models — image, video, audio, 3D and LLM — behind one REST gateway with a single API key. Calls are metered per GPU-second or per generation against a prepaid credit balance, with the cost of every request reported inline on the response. The v2 asynchronous API is a submit-poll-fetch job contract built for long-running video and upscaling work, while the v1 synchronous route remains for fast models. Alongside the gateway, PixelFlow is a visual workflow builder that chains models on a canvas and publishes any workflow as its own production REST API, and dedicated endpoints run a chosen model on reserved GPUs with autoscaling. A first-party Python SDK, a browser playground, media-editing endpoints and a weekly dated changelog round out the developer surface.
finops:
- name: Segmind Finops
  service_category: API
  slug: segmind-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/segmind.png
layout: provider
modified: '2026-08-27'
name: Segmind
nav: Providers
network: true
overview: 'Segmind publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Inference API, Account API, Storage API, and 1 more. Tagged areas include Artificial Intelligence, Machine-Learning, Generative AI, Inference, and Image-Generation.


  The Segmind catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Segmind''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, pricing, changelog, and 30 more developer resources.'
plans:
- name: Segmind Plans Pricing
  plan_count: 5
  slug: segmind-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 7
  name: Segmind Rate Limits
  slug: segmind-rate-limits
scopes:
- name: Segmind Scopes
  scope_count: 0
  slug: segmind-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 66.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 57.7
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 66.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/segmind/refs/heads/main/screenshots/segmind-2026-06-20T193634.png
security:
- kind: authentication
  name: Segmind Authentication
  slug: segmind-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Segmind Domain Security
  slug: segmind-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: segmind
tags:
- Artificial Intelligence
- Machine-Learning
- Generative AI
- Inference
- Image-Generation
- Video Generation
- Text-to-Image
- Text-to-Video
- Serverless
- GPU
- Workflows
- Fine-Tuning
website: https://www.segmind.com/
---
