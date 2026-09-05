---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 35
  human_in_the_loop: 35
  name: Novelai Agentic Access
  operation_count: 52
  slug: novelai-agentic-access
  summary_line: 52 operations · 35 acting · 35 human-in-the-loop
api_count: 1
apis:
- description: NovelAI API provides programmatic access to AI image generation and text generation capabilities.
  name: NovelAI API
  slug: novelai
- baseURL: https://api.novelai.net
  baseurl_source: spec
  description: The /ai/ API from NovelAI — 9 operation(s) for /ai/.
  name: NovelAI /ai/ API
  slug: novelai-ai-api
- baseURL: https://api.novelai.net
  baseurl_source: spec
  description: The /ai/module/ API from NovelAI — 3 operation(s) for /ai/module/.
  name: NovelAI /ai/module/ API
  slug: novelai-ai-module-api
- baseURL: https://api.novelai.net
  baseurl_source: spec
  description: The / API from NovelAI — 1 operation(s) for /.
  name: NovelAI / API
  slug: novelai-default-api
- baseURL: https://api.novelai.net
  baseurl_source: spec
  description: The /user/ API from NovelAI — 28 operation(s) for /user/.
  name: NovelAI /user/ API
  slug: novelai-user-api
- baseURL: https://api.novelai.net
  baseurl_source: spec
  description: The /user/subscription/ API from NovelAI — 2 operation(s) for /user/subscription/.
  name: NovelAI /user/subscription/ API
  slug: novelai-user-subscription-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NovelAI Primary /ai/ /ai/ /ai/ API
  slug: open-novelai-ai-api
- collection_type: open
  name: NovelAI Primary /ai/ /ai/ /ai/module/ API
  slug: open-novelai-ai-module-api
- collection_type: open
  name: NovelAI Primary /ai/ /ai/ / API
  slug: open-novelai-default-api
- collection_type: open
  name: NovelAI Primary /ai/ /ai/ /user/ API
  slug: open-novelai-user-api
- collection_type: open
  name: NovelAI Primary /ai/ /ai/ /user/subscription/ API
  slug: open-novelai-user-subscription-api
- collection_type: open
  name: NovelAI Primary API
  slug: open-novelai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/novelai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/novelai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/novelai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/novelai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NovelAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/novelaitechnologies
- group: company
  title: ''
  type: Website
  url: https://novelai.net/
created: '2024-07-02'
description: NovelAI is a monthly subscription service for AI-assisted image generation, storytelling, or simply a LLM powered sandbox for your imagination.
finops:
- name: Novelai Finops
  service_category: API
  slug: novelai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/novelai.png
layout: provider
modified: '2026-04-28'
name: NovelAI
nav: Providers
network: true
overview: 'NovelAI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including /ai/ API, /ai/module/ API, / API, and 2 more. Tagged areas include Artificial Intelligence, Image-Generation, LLM, and Storytelling.


  NovelAI''s developer surface includes authentication and 6 more developer resources.'
plans:
- name: Novelai Plans Pricing
  plan_count: 3
  slug: novelai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Novelai Rate Limits
  slug: novelai-rate-limits
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 46.1
    developer_ergonomics: 21.4
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 24.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/novelai/refs/heads/main/screenshots/novelai-2026-06-20T190437.png
security:
- kind: authentication
  name: Novelai Authentication
  slug: novelai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Novelai Domain Security
  slug: novelai-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Novelai Vulnerability Disclosure
  slug: novelai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: novelai
tags:
- Artificial Intelligence
- Image-Generation
- LLM
- Storytelling
website: https://novelai.net/
---
