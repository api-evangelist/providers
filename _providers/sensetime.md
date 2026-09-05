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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The SenseNova LLM API service platform exposes SenseTime's large multimodal foundation models (chat completions, embeddings, image and video generation, and fine-tuning) over an HTTP API, authenticate
  name: SenseNova LLM API
  slug: sensenova-llm-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sensetime-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sensetime.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.sensenova.cn/en
- group: docs
  title: ''
  type: Documentation
  url: https://platform.sensenova.cn/en/docs
- group: start
  title: ''
  type: Login
  url: https://platform.sensenova.cn/en/console
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sensenova.cn/en/token-plan
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenSenseNova
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sensetime-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sensetime-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sensetime-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/sensetime-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sensetime-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sensetime-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sensetime-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sensetime-llms.txt
created: '2026-07-17'
description: SenseTime (商汤科技) is a Shanghai-headquartered artificial-intelligence company building foundation models, AI compute infrastructure, and vision AI. Its developer-facing surface is the SenseNova LLM API service platform, which exposes large multimodal models (SenseNova U-series, SenseNova 6.x) for text, image, and video understanding, reasoning, and generation via an HTTP API. Developers authenticate with an Access Key ID / Secret Access Key pair (with OAuth2/OIDC available through SenseCore signin), call chat-completions, embeddings, and fine-tuning endpoints, and integrate with an official Python client library and CLI. SenseTime also operates SenseCore AI infrastructure, SenseFoundry vision AI, and native applications. This profile was surfaced as a Tiger Global portfolio company and enriched from public developer sources.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sensetime.png
layout: provider
modified: '2026-07-21'
name: SenseTime
nav: Providers
network: true
overview: 'SenseTime publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Foundation Models, and Large Language Models.


  SenseTime''s developer surface includes documentation, pricing, authentication, CLI, and 11 more developer resources.'
random_paper: 7
scopes:
- name: Sensetime Scopes
  scope_count: 3
  slug: sensetime-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 20.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sensetime/refs/heads/main/screenshots/sensetime-2026-09-02T154906.png
security:
- kind: authentication
  name: Sensetime Authentication
  slug: sensetime-authentication
  summary_line: apiKey/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Sensetime Domain Security
  slug: sensetime-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sensetime
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Foundation Models
- Large Language Models
- Generative AI
- Computer-Vision
- LLM API
website: https://www.sensetime.com
---
