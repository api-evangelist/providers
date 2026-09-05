---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    error_semantics: false
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
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Exa Agentic Access
  operation_count: 4
  slug: exa-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- description: The Exa Search API provides neural web search, contents retrieval, find similar, and grounded answers for AI agents. Multiple speed modes range from fast 250ms searches to deep research lasting tens o
  name: Exa Search API
  slug: search-api
- baseURL: https://api.exa.ai
  baseurl_source: declared
  description: The Answer API from Exa — 1 operation(s) for answer.
  name: Exa Answer API
  slug: exa-answer-api
- baseURL: https://api.exa.ai
  baseurl_source: declared
  description: The Contents API from Exa — 1 operation(s) for contents.
  name: Exa Contents API
  slug: exa-contents-api
- baseURL: https://api.exa.ai
  baseurl_source: declared
  description: The Search API from Exa — 2 operation(s) for search.
  name: Exa Search API
  slug: exa-search-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Exa Search Answer API
  slug: open-exa-answer-api
- collection_type: open
  name: Exa Search Answer Contents API
  slug: open-exa-contents-api
- collection_type: open
  name: Exa Answer Search API
  slug: open-exa-search-api
- collection_type: open
  name: Exa Search API
  slug: open-exa
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/exa-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/exa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/exa-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://exa.ai
- group: docs
  title: ''
  type: Documentation
  url: https://exa.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://exa.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/exa-labs
- group: commercial
  title: ''
  type: Pricing
  url: https://exa.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://exa.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://exa.ai/privacy-policy
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/HCShtBqbfV
- group: other
  title: ''
  type: X
  url: https://x.com/exaailabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/exa-ai
created: '2026-05-23'
description: Exa is a neural web search API designed for AI agents and applications. It combines a purpose-built web index with embedding-based retrieval to deliver highly relevant results across categories such as full web, news, companies, research, people, and financials. Exa exposes search, contents, find similar, and answer endpoints, with multiple search modes ranging from fast sub-second responses to deeper multi-step research. It also returns token-efficient highlights and summaries that reduce LLM input costs and supports structured output extraction across more than 70 million indexed companies. Exa is SOC 2 Type II certified, offers Zero Data Retention, and ships Python and JavaScript SDKs.
finops:
- name: Exa Finops
  service_category: API
  slug: exa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exa.png
layout: provider
modified: '2026-05-23'
name: Exa
nav: Providers
network: true
overview: 'Exa publishes 3 APIs on the [APIs.io](https://apis.io/) network: Answer API, Contents API, and Search API. Tagged areas include Search, Neural Search, AI Agents, LLMs, and Web Index.


  Exa''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Exa Plans Pricing
  plan_count: 1
  slug: exa-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Exa Rate Limits
  slug: exa-rate-limits
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exa/refs/heads/main/screenshots/exa-2026-06-20T180946.png
security:
- kind: authentication
  name: Exa Authentication
  slug: exa-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Exa Domain Security
  slug: exa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Exa Vulnerability Disclosure
  slug: exa-vulnerability-disclosure
  summary_line: disclosure policy published
slug: exa
tags:
- Search
- Neural Search
- AI Agents
- LLMs
- Web Index
- Retrieval
- Answers
- Contents
- Find Similar
- Research
- SOC 2
- MCP
website: https://exa.ai
---
