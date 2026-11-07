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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/contextli-com/plans/contextli-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contextli-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/contextli-com/llms/contextli-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contextli-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/contextli-com/well-known/contextli-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/contextli-com-security.txt
- group: agent
  href: https://artifacts.apis.io/contextli-com/well-known/contextli-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contextli-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/contextli-com/hosts/contextli-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contextli-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/contextli-com/vendors/contextli-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contextli-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contextli.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.contextli.com
- group: auth
  title: ''
  type: Security
  url: https://contextli.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contextli.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://contextli.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://help.contextli.com/collections/getting-started
- group: company
  title: ''
  type: Blog
  url: https://contextli.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.contextli.com/
- group: auth
  href: https://artifacts.apis.io/contextli-com/security/contextli-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/contextli-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/contextli-com/security/contextli-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contextli-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contextli.com/
coverage:
  checked: '2026-11-04'
  detail: Docs are rendered via JavaScript and no machine‑readable OpenAPI or other contract could be retrieved.
  evidence:
  - status: 200
    url: https://help.contextli.com/collections/getting-started
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Contextli provides AI-powered, context‑aware speech‑to‑text dictation for professionals. It automatically formats spoken content for apps like Email, Slack, and LinkedIn while respecting user privacy. The service supports multiple languages and offers a secure, cloud‑based solution for hands‑free productivity.
image: https://contextli.com/og-image.png
layout: provider
modified: '2026-11-04'
name: Contextli
nav: Providers
network: true
overview: 'Contextli is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Speech-to-Text, Productivity, Artificial Intelligence, Voice Dictation, and Tool Integration.


  Contextli''s developer surface includes support, pricing, getting-started guide, engineering blog, documentation, and 12 more developer resources.'
plans:
- name: Contextli Com Plans Pricing
  plan_count: 3
  slug: contextli-com-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 55.4
    operational_transparency: 10.5
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
  name: Contextli Com Domain Security
  slug: contextli-com-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Contextli Com Vulnerability Disclosure
  slug: contextli-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: contextli-com
tags:
- Speech-to-Text
- Productivity
- Artificial Intelligence
- Voice Dictation
- Tool Integration
website: https://contextli.com/
---
