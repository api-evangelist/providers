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
  score: 13.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Agent-native web hosting API by BorealHost.ai (Quebec, Canada).
  name: BorealHost API
  slug: borealhost-api
artifact_total: 4
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://borealhost.ai/en/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://borealhost.ai/en/legal/privacy-policy/
- group: commercial
  href: https://artifacts.apis.io/borealhost-ai/plans/borealhost-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/borealhost-ai-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/borealhost-ai/security/borealhost-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/borealhost-ai-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/borealhost-ai/llms/borealhost-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/borealhost-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/borealhost-ai/well-known/borealhost-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/borealhost-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/borealhost-ai/well-known/borealhost-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/borealhost-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/borealhost-ai/hosts/borealhost-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/borealhost-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/borealhost-ai/vendors/borealhost-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/borealhost-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://borealhost.ai/auth/login/
- group: auth
  href: https://artifacts.apis.io/borealhost-ai/security/borealhost-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/borealhost-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/borealhost-ai/security/borealhost-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/borealhost-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://borealhost.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://borealhost.ai/mcp/
- group: docs
  title: ''
  type: Documentation
  url: https://borealhost.ai/for-agents
- group: docs
  title: ''
  type: APIReference
  url: https://borealhost.ai/api/v1/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://borealhost.ai/for-agents
- group: operate
  title: ''
  type: Support
  url: https://borealhost.ai/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://borealhost.ai/pricing
created: '2026-11-02'
description: BorealHost.ai provides high‑performance WordPress hosting from Quebec, offering plans starting at $2 per month with automatic SSL, daily backups, and scalable resources. The platform includes a RESTful API for managing sites, DNS, and billing, targeting developers and agencies seeking automated web‑hosting solutions.
image: https://borealhost.ai/static/img/og-default.png
layout: provider
modified: '2026-11-02'
name: BorealHost.ai
nav: Providers
network: true
overview: 'BorealHost.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Hosting, WordPress, Quebec, and Cloud.


  BorealHost.ai''s developer surface includes documentation, API reference, getting-started guide, support, pricing, and 14 more developer resources.'
plans:
- name: Borealhost Ai Plans Pricing
  plan_count: 15
  slug: borealhost-ai-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Borealhost Ai Domain Security
  slug: borealhost-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Borealhost Ai Vulnerability Disclosure
  slug: borealhost-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: borealhost-ai
tags:
- Hosting
- WordPress
- Quebec
- Cloud
website: https://borealhost.ai/
---
