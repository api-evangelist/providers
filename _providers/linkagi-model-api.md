---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.linktoagi.com
  baseurl_source: declared
  description: Messages-shaped route advertised by the service. The route reaches authentication without a key; authenticated native compatibility has not been verified in the latest evidence set.
  name: LinkAGI Model API Anthropic-style route API
  slug: linkagi-model-api-anthropic-style-route-api
- baseURL: https://api.linktoagi.com
  baseurl_source: declared
  description: Inspect the models visible to the current token group.
  name: LinkAGI Model API Discovery API
  slug: linkagi-model-api-discovery-api
- baseURL: https://api.linktoagi.com
  baseurl_source: declared
  description: generateContent-shaped route advertised by the service. The route reaches authentication without a key; authenticated native compatibility has not been verified in the latest evidence set.
  name: LinkAGI Model API Gemini-style route API
  slug: linkagi-model-api-gemini-style-route-api
- baseURL: https://api.linktoagi.com
  baseurl_source: declared
  description: OpenAI-compatible Chat Completions and Responses routes.
  name: LinkAGI Model API OpenAI compatible API
  slug: linkagi-model-api-openai-compatible-api
- baseURL: https://api.linktoagi.com
  baseurl_source: declared
  description: Unauthenticated service status and live pricing metadata.
  name: LinkAGI Model API Public metadata API
  slug: linkagi-model-api-public-metadata-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LinkAGI Anthropic-style route API
  slug: open-linkagi-model-api-anthropic-style-route-api
- collection_type: open
  name: LinkAGI Discovery API
  slug: open-linkagi-model-api-discovery-api
- collection_type: open
  name: LinkAGI Gemini-style route API
  slug: open-linkagi-model-api-gemini-style-route-api
- collection_type: open
  name: LinkAGI OpenAI compatible API
  slug: open-linkagi-model-api-openai-compatible-api
- collection_type: open
  name: LinkAGI Public metadata API
  slug: open-linkagi-model-api-public-metadata-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/linkagi-model-api-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkagi-model-api-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linkagi-model-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linkagi-model-api-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.linktoagi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.linktoagi.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.linktoagi.com/codex-api.html
- group: operate
  title: ''
  type: Support
  url: https://docs.linktoagi.com/about.html#support
- group: company
  title: ''
  type: Blog
  url: https://docs.linktoagi.com/articles/
- group: company
  title: ''
  type: BlogRSS
  url: https://docs.linktoagi.com/feed.xml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/16871233/linkagi-api-starter
- group: commercial
  title: ''
  type: Pricing
  url: https://api.linktoagi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://api.linktoagi.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.linktoagi.com/user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api.linktoagi.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.linktoagi.com/status.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/lhs-1-s-team/linkagi-api/collection/8nl8r40/linkagi-api
- group: other
  title: ''
  type: APIsJSON
  url: https://docs.linktoagi.com/apis.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linkagi-model-api-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/linkagi-model-api-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/linkagi-model-api-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/linkagi-model-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/linkagi-model-api-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/linkagi-model-api-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/linkagi-model-api-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: 'LinkAGI is a Chinese third-party AI API relay (中转站) that fronts a pool of upstream model accounts behind a single host, api.linktoagi.com, and re-exposes them on three imitated vendor protocols: OpenAI-compatible Chat Completions and Responses, an Anthropic Messages-shaped route, and a Gemini generateContent-shaped route. It is sold to developers running Codex, Claude Code, Gemini CLI and desktop chat clients who want a CNY, prepaid, pay-as-you-go base-URL swap instead of a foreign card and a vendor account. A token belongs to a group (号池) that decides which models it can address and at what billing ratio; the live model and price table is published unauthenticated at /api/pricing. The service runs the open-source New API gateway and publishes a first-party OpenAPI 3.1, APIs.json, llms.txt and Postman collection, plus an unusually candid evidence boundary that marks its Anthropic and Gemini compatibility as advertised but unverified.'
image: https://api.linktoagi.com/favicon.svg
layout: provider
modified: '2026-08-09'
name: LinkAGI Model API
nav: Providers
network: true
overview: 'LinkAGI Model API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Anthropic-style route API, Discovery API, Gemini-style route API, and 2 more. Tagged areas include Artificial Intelligence, LLM, AI API Gateway, Relay, and OpenAI-Compatible.


  LinkAGI Model API''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, GitHub presence, pricing, and 19 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 58.4
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 36.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linkagi-model-api/refs/heads/main/screenshots/linkagi-model-api-2026-08-17T081030.png
security:
- kind: authentication
  name: Linkagi Model Api Authentication
  slug: linkagi-model-api-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Linkagi Model Api Domain Security
  slug: linkagi-model-api-domain-security
  summary_line: TLSv1.3
slug: linkagi-model-api
tags:
- Artificial Intelligence
- LLM
- AI API Gateway
- Relay
- OpenAI-Compatible
- Anthropic Compatible
- Gemini-compatible
- Developer Tools
- CLI coding agents
- Model Routing
- China
website: https://api.linktoagi.com/
---
