---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for b/cited platform providing citation metrics and plans.
  name: b/cited API
  slug: b-cited-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/bcited-ai/plans/bcited-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bcited-ai-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/bcited-ai/security/bcited-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bcited-ai-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/bcited-ai/llms/bcited-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bcited-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/bcited-ai/well-known/bcited-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bcited-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/bcited-ai/well-known/bcited-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bcited-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bcited-ai/hosts/bcited-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bcited-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bcited-ai/vendors/bcited-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bcited-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bcited.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bcited.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bcited.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://bcited.ai/blog
- group: auth
  href: https://artifacts.apis.io/bcited-ai/security/bcited-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bcited-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bcited-ai/security/bcited-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bcited-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bcited.ai/
created: '2026-11-02'
description: b/cited tracks how AI answer engines like ChatGPT, Claude, and Perplexity cite websites, providing SEO‑focused citation metrics, dashboards, and actionable briefs. Built by Clinton Munkres of the Boringhaus portfolio, it offers free scans, paid plans, and a public leaderboard of tools, operating independently of AI providers. The service reads Google Search Console data read‑only to generate citation scores without training models or selling data.
image: https://bcited.ai/opengraph-image?7aab954b1485c88a
layout: provider
modified: '2026-11-02'
name: b/cited
nav: Providers
network: true
overview: 'b/cited is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, SEO, Citations, Analytics, and Platform.


  b/cited''s developer surface includes pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Bcited Ai Plans Pricing
  plan_count: 4
  slug: bcited-ai-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bcited Ai Domain Security
  slug: bcited-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bcited Ai Vulnerability Disclosure
  slug: bcited-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bcited-ai
tags:
- Artificial Intelligence
- SEO
- Citations
- Analytics
- Platform
website: https://bcited.ai/
---
