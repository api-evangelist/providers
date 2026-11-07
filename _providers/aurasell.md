---
access_model:
  confidence: low
  label: Paid · Requires approval
  onboarding: approval
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documented at the support site, but no machine‑readable contract found.
  name: Aurasell API
  slug: aurasell-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/aurasell/plans/aurasell-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aurasell-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.aurasell.ai/
- group: agent
  href: https://artifacts.apis.io/aurasell/llms/aurasell-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aurasell-llms.txt
- group: auth
  href: https://artifacts.apis.io/aurasell/well-known/aurasell-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aurasell-status-security.txt
- group: agent
  href: https://artifacts.apis.io/aurasell/well-known/aurasell-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aurasell-well-known.yml
- group: other
  href: https://artifacts.apis.io/aurasell/hosts/aurasell-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aurasell-hosts.yml
- group: other
  href: https://artifacts.apis.io/aurasell/vendors/aurasell-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aurasell-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.aurasell.ai/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aurasell.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.aurasell.ai/changelog
- group: auth
  href: https://artifacts.apis.io/aurasell/security/aurasell-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aurasell-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/aurasell/security/aurasell-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aurasell-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aurasell.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.aurasell.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aurasell.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aurasell.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aurasell.ai/website-terms-of-use
- group: auth
  title: ''
  type: Trust
  url: https://www.aurasell.ai/trust
coverage:
  checked: 2026-09-26
  detail: Support site renders docs via JavaScript, no OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://support.aurasell.ai/changelog
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Aurasell is an AI‑native sales and go‑to‑market platform that provides a unified operating system for modern sales teams. It combines a CRM, AI‑driven prospecting, deal management, and automation tools into a single cloud service. The platform offers features such as Agent Builder for rapid GTM agent creation, AI‑native GTM OS, integrations with existing stacks, pricing plans, case studies, and a community hub. Aurasell aims to replace fragmented sales tools with an intelligent, end‑to‑end solution for operators and enterprises.
image: https://cdn.prod.website-files.com/6943823083ffa5d7dc3d96ea/697325e768adbb01d5c046a9_og-image.avif
layout: provider
modified: '2026-09-26'
name: Aurasell
nav: Providers
network: true
overview: 'Aurasell is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Sales, CRM, and Platform.


  Aurasell''s developer surface includes support, changelog, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Aurasell Plans Pricing
  plan_count: 1
  slug: aurasell-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 64.3
    operational_transparency: 26.3
  previous_composite: 27.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aurasell/aurasell-2026-10-11T100843.png
security:
- kind: domain-security
  name: Aurasell Domain Security
  slug: aurasell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aurasell Trust Center
  slug: aurasell-trust-center
  summary_line: SOC 2, ISO 27001
slug: aurasell
tags:
- Company
- Artificial Intelligence
- Sales
- CRM
- Platform
website: https://www.aurasell.ai/
---
