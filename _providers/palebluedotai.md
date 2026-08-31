---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: OpenAI-, Anthropic- and Gemini-compatible inference gateway. One API key and one base URL route requests across 131 listed models from 22 vendors, with cross-provider failover, prompt caching and per-
  name: PBD TokenRouter Inference API
  slug: pbd-tokenrouter-inference-api
- description: Administrative API for holders of a Management Key, covering API key listing/enable/disable, per-key spend quota, personal and organization wallet balances, and paginated or CSV usage-log export. Nine
  name: PBD TokenRouter Management API
  slug: pbd-tokenrouter-management-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/palebluedotai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.palebluedot.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tokenrouter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tokenrouter.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.tokenrouter.com/docs/management-api-documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tokenrouter.com/docs/tokenrouter-feature-guide/
- group: company
  title: ''
  type: Blog
  url: https://www.tokenrouter.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tokenrouter.com/models/
- group: start
  title: ''
  type: Login
  url: https://www.tokenrouter.com/console
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tokenrouter.com/docs/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tokenrouter.com/docs/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.tokenrouter.com/contact-us/
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/XX57FY8S9X
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TokenRouter-Tools
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/palebluedotai-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: security/palebluedotai-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/palebluedotai-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/palebluedotai-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/palebluedotai-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/palebluedotai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/palebluedotai-plans-pricing.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/palebluedotai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/palebluedotai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/palebluedotai-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/palebluedotai-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/palebluedotai-llms.txt
created: '2026-08-26'
description: PaleBlueDot AI is a Palo Alto, California headquartered AI compute and intelligence platform that supplies GPU infrastructure, dedicated clusters and model access at scale. Its developer-facing product is PBD TokenRouter (www.tokenrouter.com), a unified AI model gateway that fronts 131 currently listed models from 22 vendors behind a single API key and four wire formats - OpenAI Chat Completions, OpenAI Responses, Anthropic Messages and Google Gemini generateContent - alongside image, audio and video generation endpoints. TokenRouter layers cross-provider routing and failover, prompt caching, per-key spend quotas, organization-level usage analytics and a stated Zero Data Retention policy on top of those models, and publishes a documented Management API for API key, quota, wallet and usage-log administration. The TokenRouter platform is operated by Artemis Tokenrouter Inc.
image: https://www.palebluedot.ai/figma/pbd-home/logo.png
layout: provider
modified: '2026-08-26'
name: PaleBlueDot.AI
nav: Providers
network: true
overview: 'PaleBlueDot.AI publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Machine-Learning, Large Language Models, Inference, and API Gateway.


  PaleBlueDot.AI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, changelog, and 19 more developer resources.'
plans:
- name: Palebluedotai Plans Pricing
  plan_count: 2
  slug: palebluedotai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 10
  name: Palebluedotai Rate Limits
  slug: palebluedotai-rate-limits
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 40.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Palebluedotai Authentication
  slug: palebluedotai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Palebluedotai Domain Security
  slug: palebluedotai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Palebluedotai Trust Center
  slug: palebluedotai-trust-center
  summary_line: ISO/IEC 27001, SOC 2, SOC 3
slug: palebluedotai
tags:
- Artificial Intelligence
- Machine-Learning
- Large Language Models
- Inference
- API Gateway
- GPU
- Cloud Computing
- Model Routing
- Compute
- Company
website: https://www.palebluedot.ai/
---
