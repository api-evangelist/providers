---
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Fastrouter Agentic Access
  operation_count: 19
  slug: fastrouter-agentic-access
  summary_line: 19 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.fastrouter.ai
  baseurl_source: declared
  description: The Audio API from Fastrouter — 2 operation(s) for audio.
  name: Fastrouter Audio API
  slug: fastrouter-audio-api
- baseURL: https://api.fastrouter.ai
  baseurl_source: declared
  description: The Batches API from Fastrouter — 2 operation(s) for batches.
  name: Fastrouter Batches API
  slug: fastrouter-batches-api
- baseURL: https://api.fastrouter.ai
  baseurl_source: declared
  description: The Embeddings API from Fastrouter — 1 operation(s) for embeddings.
  name: Fastrouter Embeddings API
  slug: fastrouter-embeddings-api
- baseURL: https://api.fastrouter.ai
  baseurl_source: declared
  description: The Files API from Fastrouter — 2 operation(s) for files.
  name: Fastrouter Files API
  slug: fastrouter-files-api
- baseURL: https://api.fastrouter.ai
  baseurl_source: declared
  description: The Generation API from Fastrouter — 1 operation(s) for generation.
  name: Fastrouter Generation API
  slug: fastrouter-generation-api
- baseURL: https://api.fastrouter.ai
  baseurl_source: declared
  description: The GetAsyncResponse API from Fastrouter — 1 operation(s) for getasyncresponse.
  name: Fastrouter Get Async Response API
  slug: fastrouter-getasyncresponse-api
- baseURL: https://api.fastrouter.ai
  baseurl_source: declared
  description: The GetPromptToAudioResponse API from Fastrouter — 1 operation(s) for getprompttoaudioresponse.
  name: Fastrouter Get Prompt To Audio Response API
  slug: fastrouter-getprompttoaudioresponse-api
- baseURL: https://api.fastrouter.ai
  baseurl_source: declared
  description: The Images API from Fastrouter — 2 operation(s) for images.
  name: Fastrouter Images API
  slug: fastrouter-images-api
- baseURL: https://api.fastrouter.ai
  baseurl_source: declared
  description: The Model API from Fastrouter — 2 operation(s) for model.
  name: Fastrouter Model API
  slug: fastrouter-model-api
- baseURL: https://api.fastrouter.ai
  baseurl_source: declared
  description: The Models API from Fastrouter — 1 operation(s) for models.
  name: Fastrouter Models API
  slug: fastrouter-models-api
- baseURL: https://api.fastrouter.ai
  baseurl_source: declared
  description: The Moderations API from Fastrouter — 1 operation(s) for moderations.
  name: Fastrouter Moderations API
  slug: fastrouter-moderations-api
- baseURL: https://api.fastrouter.ai
  baseurl_source: declared
  description: The Responses API from Fastrouter — 1 operation(s) for responses.
  name: Fastrouter Responses API
  slug: fastrouter-responses-api
- baseURL: https://api.fastrouter.ai
  baseurl_source: declared
  description: The Videos API from Fastrouter — 1 operation(s) for videos.
  name: Fastrouter Videos API
  slug: fastrouter-videos-api
- baseURL: https://api.fastrouter.ai
  baseurl_source: declared
  description: The Chat Completions API from Fastrouter — 1 operation(s) for chat completions.
  name: Fastrouter Chat Completions API
  slug: fastrouter-chat-completions-api
artifact_total: 20
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fastrouter/refs/heads/main/agentic-access/fastrouter-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fastrouter-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fastrouter/refs/heads/main/plans/fastrouter-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fastrouter-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fastrouter/refs/heads/main/rules/fastrouter-rules.yml
  title: ''
  type: Spectral
  url: rules/fastrouter-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fastrouter/refs/heads/main/data-model/fastrouter-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fastrouter-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fastrouter/refs/heads/main/cli/fastrouter-cli.yml
  title: ''
  type: CLI
  url: cli/fastrouter-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fastrouter/refs/heads/main/changelog/fastrouter-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fastrouter-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fastrouter/refs/heads/main/conformance/fastrouter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fastrouter-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fastrouter/refs/heads/main/llms/fastrouter-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fastrouter-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fastrouter/refs/heads/main/well-known/fastrouter-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fastrouter-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fastrouter/refs/heads/main/hosts/fastrouter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fastrouter-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fastrouter/refs/heads/main/vendors/fastrouter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fastrouter-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fastrouter.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fastrouter.ai/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.fastrouter.ai/product-updates/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fastrouter.ai/api-reference
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.fastrouter.ai</span
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fastrouter
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fastrouter/refs/heads/main/authentication/fastrouter-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fastrouter-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fastrouter/refs/heads/main/security/fastrouter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fastrouter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fastrouter.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fastrouter.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fastrouter.ai/explore-features/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://fastrouter.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://fastrouter.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://fastrouter.ai/sign-up
- group: operate
  title: ''
  type: Contact
  url: https://fastrouter.ai/contact
created: '2026-10-16'
description: FastRouter.ai provides a unified API gateway for large language models, enabling enterprises to route, compare, and operate across over 200 AI models via a single OpenAI‑compatible endpoint. It offers features such as automatic model selection, cost‑optimization insights, response caching, prompt management, and comprehensive analytics, helping teams build scalable, reliable AI applications while reducing latency and expense.
image: https://fastrouter.ai/opengraph-image
json_schemas:
- name: JsonObject
  property_count: 0
  slug: fastrouter-json-object
layout: provider
modified: '2026-10-16'
name: Fastrouter
nav: Providers
network: true
overview: 'Fastrouter publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audio API, Batches API, Embeddings API, and 11 more. Tagged areas include Company, Artificial Intelligence, API Gateway, LLM, and Enterprise.


  The Fastrouter catalog on APIs.io includes 1 Spectral governance ruleset.


  Fastrouter''s developer surface includes CLI, changelog, API reference, authentication, documentation, getting-started guide, pricing, and 19 more developer resources.'
plans:
- name: Fastrouter Plans Pricing
  plan_count: 4
  slug: fastrouter-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Fastrouter API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: fastrouter-rules
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 58.9
    catalog_earned_first_party: 12.0
    catalog_gap: 56.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 46.8
    developer_ergonomics: 59.5
    discoverability: 73.2
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Fastrouter Authentication
  slug: fastrouter-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fastrouter Domain Security
  slug: fastrouter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fastrouter
tags:
- Company
- Artificial Intelligence
- API Gateway
- LLM
- Enterprise
website: https://fastrouter.ai/
---
