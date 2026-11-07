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
    mcp_server: documented
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Bynor AI platform as described in the documentation.
  name: Bynor AI API
  slug: bynor-ai-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/bynor-ai/plans/bynor-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bynor-ai-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://bynor.ai/privacy-e-cookie-policy
- group: agent
  href: https://artifacts.apis.io/bynor-ai/llms/bynor-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bynor-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/bynor-ai/well-known/bynor-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bynor-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/bynor-ai/well-known/bynor-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bynor-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bynor-ai/hosts/bynor-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bynor-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bynor-ai/vendors/bynor-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bynor-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bynor.ai/terms.html
- group: start
  title: ''
  type: SignUp
  url: https://bynor.ai/guide/sign-up-and-free-trial.html
- group: commercial
  title: ''
  type: Pricing
  url: https://bynor.ai/en/pricing.html
- group: company
  title: ''
  type: Blog
  url: https://bynor.ai/Blog
- group: auth
  href: https://artifacts.apis.io/bynor-ai/security/bynor-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bynor-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bynor-ai/security/bynor-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bynor-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bynor.ai/
coverage:
  checked: '2026-11-03'
  detail: Documentation pages are JavaScript-rendered and provide no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://bynor.ai/guide/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Bynor provides an AI‑powered operating system for social media, enabling users to create, publish, analyze, and grow content across platforms. The platform unifies conversations, data, and automation in a single place, helping brands and creators streamline their social workflows and gain insights.
image: https://bynor.ai/og-home-cielo.jpg
layout: provider
modified: '2026-11-03'
name: Bynor
nav: Providers
network: true
overview: 'Bynor is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Social Media, Automation, and Analytics.


  Bynor''s developer surface includes signup flow, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Bynor Ai Plans Pricing
  plan_count: 2
  slug: bynor-ai-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bynor Ai Domain Security
  slug: bynor-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bynor Ai Vulnerability Disclosure
  slug: bynor-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bynor-ai
tags:
- Company
- Artificial Intelligence
- Social Media
- Automation
- Analytics
website: https://bynor.ai/
---
