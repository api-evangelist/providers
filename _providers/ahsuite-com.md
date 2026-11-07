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
- description: Ahsuite API (no public contract discovered)
  name: Ahsuite API
  slug: ahsuite-api
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/ahsuite-com/vendors/ahsuite-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ahsuite-com-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/ahsuite-com/plans/ahsuite-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ahsuite-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/ahsuite-com/security/ahsuite-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ahsuite-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/ahsuite-com/llms/ahsuite-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ahsuite-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/ahsuite-com/well-known/ahsuite-com-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ahsuite-com-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/ahsuite-com/well-known/ahsuite-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ahsuite-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ahsuite-com/hosts/ahsuite-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ahsuite-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ahsuite.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ahsuite.com/privacy
- group: start
  title: ''
  type: Login
  url: https://ahsuite.com/login
- group: company
  title: ''
  type: Blog
  url: https://blog.ahsuite.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ahsuite.com/
- group: auth
  href: https://artifacts.apis.io/ahsuite-com/security/ahsuite-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ahsuite-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ahsuite-com/security/ahsuite-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ahsuite-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ahsuite.com/
coverage:
  checked: '2026-11-01'
  detail: Docs site returns a 403 when accessed via simple HTTP, indicating bot protection that prevents machine reading.
  evidence:
  - status: 403
    url: https://docs.ahsuite.com/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Ahsuite provides client portal software that enables businesses to embed videos, dashboards, and various applications directly into a secure portal. Features include file management with e‑signatures, password sharing, work journals, task management, and integrated AI chat via Claude. Tailored solutions serve accountants, agencies, freelancers, financial advisors, law firms, and small businesses, offering white‑label options and extensive customization.
image: https://d1ea3bsweroqag.cloudfront.net/images/ahsuite-og-v3.png
layout: provider
modified: '2026-11-01'
name: Ahsuite
nav: Providers
network: true
overview: 'Ahsuite is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Client Portal, Software-as-a-Service, Collaboration, AI Integration, and Accounting.


  Ahsuite''s developer surface includes engineering blog, documentation, and 13 more developer resources.'
plans:
- name: Ahsuite Com Plans Pricing
  plan_count: 10
  slug: ahsuite-com-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 24.2
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ahsuite Com Domain Security
  slug: ahsuite-com-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Ahsuite Com Vulnerability Disclosure
  slug: ahsuite-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: ahsuite-com
tags:
- Client Portal
- Software-as-a-Service
- Collaboration
- AI Integration
- Accounting
website: https://ahsuite.com/
---
