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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/noveum-ai/plans/noveum-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/noveum-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/noveum-ai/llms/noveum-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/noveum-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/noveum-ai/well-known/noveum-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/noveum-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/noveum-ai/hosts/noveum-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/noveum-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://noveum.ai/en/legal/terms
- group: start
  title: ''
  type: SignUp
  url: https://noveum.ai/auth/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://noveum.ai/en/legal/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.noveum.ai/en
- group: operate
  title: ''
  type: ChangeLog
  url: https://noveum.ai/en/changelog
- group: auth
  href: https://artifacts.apis.io/noveum-ai/security/noveum-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/noveum-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://noveum.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://noveum.ai/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://noveum.ai/en/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://noveum.ai/en/docs/getting-started/quick-setup
- group: commercial
  title: ''
  type: Pricing
  url: https://noveum.ai/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://noveum.ai/en/blog
- group: operate
  title: ''
  type: Support
  url: https://noveum.ai/en/contact
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://noveum.ai/en/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Noveum.ai provides a closed-loop AI agent evaluation platform that captures, evaluates, and acts on evidence from production AI agents. It offers trace ingestion, scoring, debugging, and recommendation tools across chat, workflow, and voice agents, supporting enterprise on‑prem and cloud deployments with security compliance such as SOC 2 Type II and GDPR.
image: https://noveum.ai/api/og/card?f=home&l=en
layout: provider
modified: '2026-10-30'
name: noveum-ai
nav: Providers
network: true
overview: 'noveum-ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Evaluation, Observability, and Enterprise.


  noveum-ai''s developer surface includes signup flow, changelog, documentation, API reference, getting-started guide, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Noveum Ai Plans Pricing
  plan_count: 6
  slug: noveum-ai-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.6
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 55.4
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 32.4
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/noveum-ai/noveum-ai-2026-11-03T140337.png
security:
- kind: domain-security
  name: Noveum Ai Domain Security
  slug: noveum-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: noveum-ai
tags:
- Company
- Artificial Intelligence
- Evaluation
- Observability
- Enterprise
website: https://noveum.ai/
---
