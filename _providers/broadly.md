---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/broadly/plans/broadly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/broadly-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/broadly/llms/broadly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/broadly-llms.txt
- group: other
  href: https://artifacts.apis.io/broadly/hosts/broadly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/broadly-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://broadly.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://broadly.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://broadly.com/pricing-ai-workforce
- group: start
  title: ''
  type: Login
  url: https://broadly.com/login
- group: company
  title: ''
  type: Blog
  url: https://broadly.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/broadly
- group: auth
  href: https://artifacts.apis.io/broadly/security/broadly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/broadly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://broadly.com
coverage:
  checked: '2026-10-22'
  detail: Broadly's developer documentation is rendered via JavaScript and no machine‑readable OpenAPI spec is publicly accessible.
  evidence:
  - status: 200
    url: https://broadly.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Broadly provides an AI‑powered customer engagement platform for local service businesses. The platform combines tools for attracting customers, generating and managing online reviews, handling messaging across SMS, email, and social channels, and enabling self‑service appointment scheduling. It is designed for businesses such as HVAC, plumbing, dental, legal, and other service providers that rely on local search visibility and customer relationships.
image: https://broadly.com/api/media/file/Broadly%20-%20featured%20image%20-%20standard.webp?prefix=media
layout: provider
modified: '2026-10-22'
name: Broadly
nav: Providers
network: true
overview: 'Broadly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Workforce, Reputation Management, Local SEO, CRM, and Messaging.


  Broadly''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Broadly Plans Pricing
  plan_count: 1
  slug: broadly-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Broadly Domain Security
  slug: broadly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: broadly
tags:
- AI Workforce
- Reputation Management
- Local SEO
- CRM
- Messaging
- Appointment Scheduling
- Marketing Automation
- Home Services
website: https://broadly.com
---
