---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Developer documentation for NewzAI API integration.
  name: newzai-ai
  slug: newzai-ai
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/newzai-ai/authentication/newzai-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/newzai-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/newzai-ai/conformance/newzai-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/newzai-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/newzai-ai/llms/newzai-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/newzai-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/newzai-ai/well-known/newzai-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/newzai-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/newzai-ai/hosts/newzai-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/newzai-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/newzai-ai/vendors/newzai-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/newzai-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/newzai-ai/security/newzai-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/newzai-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://newzai.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://newzai.ai/resources/articles/
- group: start
  title: ''
  type: GettingStarted
  url: https://newzai.ai/for-you
- group: company
  title: ''
  type: Blog
  url: https://newzai.ai/resources/blogs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://newzai.ai/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://newzai.ai/legal/privacy-policy
coverage:
  checked: '2026-10-30'
  detail: OpenAPI spec at https://api.newzai.ai/openapi.json appears to be a generic FastAPI example unrelated to NewzAI.
  evidence:
  - status: 200
    url: https://api.newzai.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: NewzAI provides an AI‑powered news aggregation platform that curates personalized news feeds, summarises articles, and offers real‑time alerts across topics like finance, sports, and technology. Users can access the service via web, Android, and iOS apps, and developers can integrate news streams into agents via the MCP. The platform emphasizes multilingual support, customizable topics, and rapid updates to keep users informed with minimal effort.
image: https://newzai.ai/logo.png
layout: provider
modified: '2026-10-30'
name: newzai-ai
nav: Providers
network: true
overview: 'newzai-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include News, Artificial Intelligence, Aggregation, Personalization, and Multilingual.


  newzai-ai''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 9 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/newzai-ai/newzai-ai-2026-11-03T140155.png
security:
- kind: authentication
  name: Newzai Ai Authentication
  slug: newzai-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Newzai Ai Domain Security
  slug: newzai-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: newzai-ai
tags:
- News
- Artificial Intelligence
- Aggregation
- Personalization
- Multilingual
website: https://newzai.ai/
---
