---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/ai-translators-com/llms/ai-translators-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai-translators-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ai-translators-com/mcp/ai-translators-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ai-translators-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/ai-translators-com/hosts/ai-translators-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-translators-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ai-translators-com/vendors/ai-translators-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai-translators-com-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ai-translators.com/sk/blog
- group: auth
  href: https://artifacts.apis.io/ai-translators-com/security/ai-translators-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-translators-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai-translators.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ai-translators.com/en/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.ai-translators.com/en/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ai-translators.com/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ai-translators.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ai-translators.com/en/gdpr
- group: operate
  title: ''
  type: Support
  url: https://www.ai-translators.com/en/help
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ai-translators.com/en/api-docs
- group: start
  title: ''
  type: SignUp
  url: https://www.ai-translators.com/en/pricing
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are rendered via JavaScript and no machine-readable API spec was found.
  evidence:
  - status: 200
    url: https://www.ai-translators.com/en
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AI-Translators.com provides a professional AI-powered translation platform offering text, document, website, photo, and video translation services in over 100 languages. The service emphasizes privacy, does not store user data for training, and offers a free tier with limits plus paid plans. It supports real-time conversation mode and integrates with various tools, aiming to break language barriers worldwide.
image: https://www.ai-translators.com/logo_badge.png
layout: provider
mcp_servers:
- description: Remote MCP server at ai-translators.com.
  name: AI-Translators.com MCP Server
  slug: ai-translators-com-mcp-yml
modified: '2026-11-01'
name: AI-Translators.com
nav: Providers
network: true
overview: 'AI-Translators.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Translation, Machine Learning, Software-as-a-Service, and Language Technology.


  AI-Translators.com''s developer surface includes engineering blog, documentation, API reference, pricing, support, getting-started guide, signup flow, and 8 more developer resources.'
plans:
- name: Ai Translators Com Plans Pricing
  plan_count: 0
  slug: ai-translators-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Ai Translators Com Rate Limits
  slug: ai-translators-com-rate-limits
scopes:
- name: Ai Translators Com Scopes
  scope_count: 0
  slug: ai-translators-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 21.9
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ai Translators Com Authentication
  slug: ai-translators-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ai Translators Com Domain Security
  slug: ai-translators-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ai-translators-com
tags:
- Artificial Intelligence
- Translation
- Machine Learning
- Software-as-a-Service
- Language Technology
website: https://ai-translators.com/
---
