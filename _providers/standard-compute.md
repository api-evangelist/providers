---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.stdcmpt.com/v1
  baseurl_source: declared
  description: OpenAI-compatible (and Anthropic Messages-compatible) LLM inference endpoint. Set base URL to https://api.stdcmpt.com/v1, use a Bearer API key, and set model to 'standardcompute'. Supports POST /v1/ch
  name: Standard Compute Inference API
  slug: standard-compute-inference-api
artifact_total: 6
common:
- group: docs
  title: ''
  type: Documentation
  url: https://standardcompute.com/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://standardcompute.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://standardcompute.com/support
- group: company
  title: ''
  type: Blog
  url: https://standardcompute.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://standardcompute.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://standardcompute.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://standardcompute.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://standardcompute.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://standardcompute.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://standardcompute.com/changelog
- group: auth
  title: ''
  type: Security
  url: https://standardcompute.com/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/standard-compute-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/standard-compute-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/standard-compute-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/standard-compute-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/standard-compute-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/standard-compute-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/standard-compute-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/standard-compute-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/standard-compute-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/standard-compute-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/standard-compute-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/standard-compute-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/standard-compute-domain-security.yml
created: '2026-09-02'
description: 'An independent, flat-rate LLM inference API for AI coding agents. Standard Compute runs a single OpenAI-compatible (and Anthropic Messages-compatible) inference endpoint that smart-routes each request to the best-fit model across closed frontier and efficient open models, sold as a flat monthly subscription with a stated compute budget rather than per-token billing. Integration is a base-URL swap: point any OpenAI-compatible agent at https://api.stdcmpt.com/v1, use a Bearer key, and set the model to "standardcompute". There are no per-minute 429 walls and no 5-hour or weekly windows; requests run at full speed until the monthly budget is reached, then return HTTP 402 until the period renews.'
image: https://standardcompute.com/opengraph-image.png
layout: provider
modified: '2026-09-02'
name: Standard Compute
nav: Providers
network: true
overview: 'Standard Compute publishes 1 API on the [APIs.io](https://apis.io/) network: Inference API. Tagged areas include llm api, flat-rate, subscription, ai agents, and inference.


  Standard Compute''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 18 more developer resources.'
plans:
- name: Standard Compute Plans Pricing
  plan_count: 8
  slug: standard-compute-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Standard Compute Rate Limits
  slug: standard-compute-rate-limits
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 34.7
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 46.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Standard Compute Authentication
  slug: standard-compute-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Standard Compute Domain Security
  slug: standard-compute-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Standard Compute Vulnerability Disclosure
  slug: standard-compute-vulnerability-disclosure
  summary_line: disclosure policy published
slug: standard-compute
tags:
- llm api
- flat-rate
- subscription
- ai agents
- inference
- model routing
- ai gateway
- developer tools
- coding agents
- openai-compatible
---
