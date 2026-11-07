---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
api_count: 1
apis:
- description: API documented at help.insia.ai but no machine‑readable contract discovered.
  name: INSIA API
  slug: insia-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.insia.ai/security
- group: agent
  href: https://artifacts.apis.io/insia/llms/insia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/insia-llms.txt
- group: auth
  href: https://artifacts.apis.io/insia/well-known/insia-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/insia-help-security.txt
- group: agent
  href: https://artifacts.apis.io/insia/well-known/insia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/insia-well-known.yml
- group: other
  href: https://artifacts.apis.io/insia/hosts/insia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/insia-hosts.yml
- group: other
  href: https://artifacts.apis.io/insia/vendors/insia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/insia-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.insia.ai/en/
- group: auth
  title: ''
  type: Security
  url: https://www.insia.ai/security
- group: start
  title: ''
  type: GettingStarted
  url: https://help.insia.ai/en/articles/6636579-getting-started-user-setup
- group: auth
  href: https://artifacts.apis.io/insia/security/insia-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/insia-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/insia/security/insia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/insia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://insia.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.insia.ai/about
- group: commercial
  title: ''
  type: Pricing
  url: https://www.insia.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.insia.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.insia.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.insia.ai/privacy-policy
created: '2026-10-20'
description: INSIA provides decision intelligence solutions for manufacturers and business teams, enabling early detection of operational issues through data integration, analytics, and automated insights delivered via WhatsApp, email, and Teams. Their platform offers pre‑built KPIs, benchmarks, and playbooks to help users understand problems, assess impact, and take actionable steps, improving efficiency and profitability across supply chains.
image: https://www.insia.ai/og/default.png
layout: provider
modified: '2026-10-20'
name: INSIA
nav: Providers
network: true
overview: 'INSIA is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Decision Intelligence, Manufacturing, Data Analytics, and Software-as-a-Service.


  INSIA''s developer surface includes support, getting-started guide, documentation, pricing, engineering blog, and 12 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 64.3
    operational_transparency: 5.3
  previous_composite: 23.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/insia/insia-2026-11-03T133822.png
security:
- kind: domain-security
  name: Insia Domain Security
  slug: insia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Insia Trust Center
  slug: insia-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: insia
tags:
- Company
- Decision Intelligence
- Manufacturing
- Data Analytics
- Software-as-a-Service
website: https://insia.ai/
---
