---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/ai-advisors-ai/plans/ai-advisors-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ai-advisors-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/ai-advisors-ai/llms/ai-advisors-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai-advisors-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/ai-advisors-ai/hosts/ai-advisors-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-advisors-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/ai-advisors-ai/vendors/ai-advisors-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai-advisors-ai-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AI-Advisors
- group: auth
  href: https://artifacts.apis.io/ai-advisors-ai/security/ai-advisors-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-advisors-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai-advisors.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ai-advisors.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ai-advisors.ai/pricing
- group: company
  title: ''
  type: About
  url: https://www.ai-advisors.ai/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ai-advisors.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ai-advisors.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.ai-advisors.ai/support
- group: company
  title: ''
  type: Blog
  url: https://www.ai-advisors.ai/blog
- group: company
  title: ''
  type: Blog
  url: https://www.ai-advisors.ai/blog
coverage:
  checked: '2026-11-01'
  detail: The provider’s website and docs are public HTML but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files were found.
  evidence:
  - status: 200
    url: https://www.ai-advisors.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AI Advisors provides an AI marketing SaaS platform that helps mid‑market B2B teams track, optimize, and grow brand visibility across AI search engines such as ChatGPT, Gemini, Perplexity, Claude, and Grok. Founded by Kevin O'Connell, the platform offers modules like AI Analytics, Answer Engine Insights, and AI Ads, delivering actionable intelligence for marketers to lead in AI search. It integrates with tools like Google Ads, WordPress, and Slack, and offers a suite of AI‑driven marketing tools and a public llms.txt generator.
image: https://www.ai-advisors.ai/opengraph-image?7c7ec71b3623fd8a
layout: provider
modified: '2026-11-01'
name: AI Advisors
nav: Providers
network: true
overview: 'AI Advisors is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketing, Software-as-a-Service, Analytics, and Advertising.


  AI Advisors'' developer surface includes documentation, pricing, support, engineering blog, and 11 more developer resources.'
plans:
- name: Ai Advisors Ai Plans Pricing
  plan_count: 3
  slug: ai-advisors-ai-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ai Advisors Ai Domain Security
  slug: ai-advisors-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ai-advisors-ai
tags:
- Artificial Intelligence
- Marketing
- Software-as-a-Service
- Analytics
- Advertising
- Company
website: https://ai-advisors.ai/
---
