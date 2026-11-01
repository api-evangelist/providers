---
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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Elicitly AI provides AI platform APIs for language model integration, data annotation, and workflow automation as described in the documentation.
  name: Elicitly AI API
  slug: elicitly-ai-api
artifact_total: 5
common:
- group: operate
  href: https://artifacts.apis.io/elicitly-ai/rate-limits/elicitly-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/elicitly-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/elicitly-ai/plans/elicitly-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elicitly-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/elicitly-ai/changelog/elicitly-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/elicitly-ai-changelog.yml
- group: agent
  href: https://artifacts.apis.io/elicitly-ai/llms/elicitly-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elicitly-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/elicitly-ai/well-known/elicitly-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/elicitly-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/elicitly-ai/well-known/elicitly-ai-elicitly-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/elicitly-ai-elicitly-security.txt
- group: agent
  href: https://artifacts.apis.io/elicitly-ai/well-known/elicitly-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elicitly-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/elicitly-ai/hosts/elicitly-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/elicitly-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/elicitly-ai/vendors/elicitly-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/elicitly-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.elicitly.ai/security/
- group: start
  title: ''
  type: Login
  url: https://app.elicitly.ai/signin
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.elicitly.ai/docs/changelog/
- group: auth
  href: https://artifacts.apis.io/elicitly-ai/security/elicitly-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/elicitly-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/elicitly-ai/security/elicitly-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elicitly-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://elicitly.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.elicitly.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.elicitly.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://elicitly.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://elicitly.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://elicitly.ai/privacy
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.elicitly.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Elicitly AI is an emerging artificial intelligence platform that provides developers with advanced language model integration, data annotation tools, and AI-driven workflow automation. The company focuses on simplifying AI adoption for enterprises by offering scalable APIs, comprehensive documentation, and robust security features. Elicitly AI aims to empower businesses to build intelligent applications faster, reduce operational overhead, and unlock new insights from their data through cutting‑edge machine learning capabilities.
image: https://www.elicitly.ai/og.png
layout: provider
modified: '2026-10-30'
name: elicitly-ai
nav: Providers
network: true
overview: 'elicitly-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Platform, API, and Automation.


  elicitly-ai''s developer surface includes changelog, documentation, pricing, and 17 more developer resources.'
plans:
- name: Elicitly Ai Plans Pricing
  plan_count: 3
  slug: elicitly-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Elicitly Ai Rate Limits
  slug: elicitly-ai-rate-limits
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 52.0
    catalog_earned_first_party: 20.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 47.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Elicitly Ai Domain Security
  slug: elicitly-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Elicitly Ai Vulnerability Disclosure
  slug: elicitly-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: elicitly-ai
tags:
- Company
- AI
- Platform
- API
- Automation
website: https://elicitly.ai/
---
