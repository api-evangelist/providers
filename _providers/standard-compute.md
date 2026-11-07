---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.stdcmpt.com/v1
  baseurl_source: declared
  description: The Completions API from Standard Compute — 1 operation(s) for completions.
  name: Standard Compute Completions API
  slug: standard-compute-completions-api
- baseURL: https://api.stdcmpt.com/v1
  baseurl_source: declared
  description: The Healthz API from Standard Compute — 1 operation(s) for healthz.
  name: Standard Compute Healthz API
  slug: standard-compute-healthz-api
- baseURL: https://api.stdcmpt.com/v1
  baseurl_source: declared
  description: The Install.ps1 API from Standard Compute — 1 operation(s) for install.ps1.
  name: Standard Compute Install.ps1 API
  slug: standard-compute-install-ps1-api
- baseURL: https://api.stdcmpt.com/v1
  baseurl_source: declared
  description: The Install.sh API from Standard Compute — 1 operation(s) for install.sh.
  name: Standard Compute Install.sh API
  slug: standard-compute-install-sh-api
- baseURL: https://api.stdcmpt.com/v1
  baseurl_source: declared
  description: The Messages API from Standard Compute — 2 operation(s) for messages.
  name: Standard Compute Messages API
  slug: standard-compute-messages-api
- baseURL: https://api.stdcmpt.com/v1
  baseurl_source: declared
  description: The Models API from Standard Compute — 1 operation(s) for models.
  name: Standard Compute Models API
  slug: standard-compute-models-api
- baseURL: https://api.stdcmpt.com/v1
  baseurl_source: declared
  description: The Responses API from Standard Compute — 1 operation(s) for responses.
  name: Standard Compute Responses API
  slug: standard-compute-responses-api
- baseURL: https://api.stdcmpt.com/v1
  baseurl_source: declared
  description: The Chat Completions API from Standard Compute — 1 operation(s) for chat completions.
  name: Standard Compute Chat Completions API
  slug: standard-compute-chat-completions-api
artifact_total: 18
common:
- group: other
  href: https://artifacts.apis.io/standard-compute/capabilities/standard-compute-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/standard-compute-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.standardcompute.com/
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
  href: https://artifacts.apis.io/standard-compute/llms/standard-compute-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/standard-compute-llms.txt
- group: design
  href: https://artifacts.apis.io/standard-compute/lifecycle/standard-compute-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/standard-compute-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/standard-compute/plans/standard-compute-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/standard-compute-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/standard-compute/rate-limits/standard-compute-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/standard-compute-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/standard-compute/authentication/standard-compute-authentication.yml
  title: ''
  type: Authentication
  url: authentication/standard-compute-authentication.yml
- group: design
  href: https://artifacts.apis.io/standard-compute/conventions/standard-compute-conventions.yml
  title: ''
  type: Conventions
  url: conventions/standard-compute-conventions.yml
- group: design
  href: https://artifacts.apis.io/standard-compute/conformance/standard-compute-conformance.yml
  title: ''
  type: Conformance
  url: conformance/standard-compute-conformance.yml
- group: design
  href: https://artifacts.apis.io/standard-compute/errors/standard-compute-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/standard-compute-problem-types.yml
- group: design
  href: https://artifacts.apis.io/standard-compute/data-model/standard-compute-data-model.yml
  title: ''
  type: DataModel
  url: data-model/standard-compute-data-model.yml
- group: build
  href: https://artifacts.apis.io/standard-compute/packages/standard-compute-packages.yml
  title: ''
  type: Packages
  url: packages/standard-compute-packages.yml
- group: other
  href: https://artifacts.apis.io/standard-compute/overlays/standard-compute-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/standard-compute-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/standard-compute/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/standard-compute/security/standard-compute-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/standard-compute-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/standard-compute/security/standard-compute-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/standard-compute-domain-security.yml
created: '2026-09-02'
description: 'An independent, flat-rate LLM inference API for AI coding agents. Standard Compute runs a single OpenAI-compatible (and Anthropic Messages-compatible) inference endpoint that smart-routes each request to the best-fit model across closed frontier and efficient open models, sold as a flat monthly subscription with a stated compute budget rather than per-token billing. Integration is a base-URL swap: point any OpenAI-compatible agent at https://api.stdcmpt.com/v1, use a Bearer key, and set the model to "standardcompute". There are no per-minute 429 walls and no 5-hour or weekly windows; requests run at full speed until the monthly budget is reached, then return HTTP 402 until the period renews.'
finops:
- has_sources: true
  method: derived
  name: Standard Compute Finops
  primary_unit: plan per key
  service_category: ''
  slug: standard-compute-finops
  template: false
image: https://standardcompute.com/opengraph-image.png
layout: provider
modified: '2026-09-02'
name: Standard Compute
nav: Providers
network: true
overview: 'Standard Compute publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Completions API, Healthz API, Install.ps1 API, and 5 more. Tagged areas include LLM API, Flat Rate, Subscription, AI Agents, and Inference.


  The Standard Compute catalog on APIs.io includes 1 Spectral governance ruleset.


  Standard Compute''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 20 more developer resources.'
plans:
- name: Standard Compute Plans Pricing
  plan_count: 10
  slug: standard-compute-plans-pricing
- name: Standard Compute Price Estimates
  plan_count: 0
  slug: standard-compute-price-estimates
random_paper: 3
rate_limits:
- limit_count: 0
  name: Standard Compute Rate Limits
  slug: standard-compute-rate-limits
rules:
- authorship: generated
  effective_rule_count: 65
  extends:
  - spectral:oas
  name: Standard Compute API Rules
  rule_count: 24
  severity_counts:
    error: 22
    hint: 0
    info: 1
    warn: 1
  slug: standard-compute-rules
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 38.4
    developer_ergonomics: 42.3
    discoverability: 73.2
    operational_transparency: 42.1
  previous_composite: 50.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/standard-compute/standard-compute-2026-10-11T130343.png
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
  summary_line: no policy recorded
skill_count: 2
skills:
- name: standard-compute-estimate-before-spending
  slug: standard-compute-estimate-before-spending
- name: standard-compute-switch-agent-provider
  slug: standard-compute-switch-agent-provider
slug: standard-compute
tags:
- LLM API
- Flat Rate
- Subscription
- AI Agents
- Inference
- Model Routing
- AI Gateway
- Developer Tools
- Coding Agents
- OpenAI-Compatible
website: https://www.standardcompute.com/
---
