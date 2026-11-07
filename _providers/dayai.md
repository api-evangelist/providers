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
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/dayai/plans/dayai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dayai-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://day.ai/trust
- group: agent
  href: https://artifacts.apis.io/dayai/llms/dayai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dayai-llms.txt
- group: agent
  href: https://artifacts.apis.io/dayai/well-known/dayai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dayai-well-known.yml
- group: other
  href: https://artifacts.apis.io/dayai/hosts/dayai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dayai-hosts.yml
- group: other
  href: https://artifacts.apis.io/dayai/vendors/dayai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dayai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dayai/security/dayai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dayai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dayai/security/dayai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dayai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://day.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://day.ai/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://day.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/day-ai/day-ai-sdk
- group: start
  title: ''
  type: GettingStarted
  url: https://day.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://day.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://day.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://day.ai/privacy
created: '2026-10-23'
description: Day.ai provides an AI-powered platform that helps businesses automate and optimize their daily operations through intelligent assistants, workflow automation, and data-driven insights. Leveraging large language models, the service offers natural language interfaces, task scheduling, and integration with existing enterprise tools, enabling teams to streamline processes, improve productivity, and make informed decisions based on real-time analytics. The company focuses on delivering scalable, secure, and customizable AI solutions for a wide range of industries, from finance to healthcare.
image: https://day.ai/og-image.png
layout: provider
modified: '2026-10-23'
name: Day.ai
nav: Providers
network: true
overview: 'Day.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Enterprise, Productivity, and Platform.


  Day.ai''s developer surface includes documentation, API reference, getting-started guide, pricing, and 12 more developer resources.'
plans:
- name: Dayai Plans Pricing
  plan_count: 5
  slug: dayai-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 55.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dayai/dayai-2026-11-03T130330.png
security:
- kind: domain-security
  name: Dayai Domain Security
  slug: dayai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dayai Trust Center
  slug: dayai-trust-center
  summary_line: SOC 2
slug: dayai
tags:
- Artificial Intelligence
- Automation
- Enterprise
- Productivity
- Platform
website: https://day.ai/
---
