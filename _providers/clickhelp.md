---
access_model:
  confidence: medium
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/clickhelp/plans/clickhelp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clickhelp-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://clickhelp.com/trust/
- group: auth
  href: https://artifacts.apis.io/clickhelp/authentication/clickhelp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clickhelp-authentication.yml
- group: agent
  href: https://artifacts.apis.io/clickhelp/llms/clickhelp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clickhelp-llms.txt
- group: agent
  href: https://artifacts.apis.io/clickhelp/well-known/clickhelp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clickhelp-well-known.yml
- group: other
  href: https://artifacts.apis.io/clickhelp/hosts/clickhelp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clickhelp-hosts.yml
- group: other
  href: https://artifacts.apis.io/clickhelp/vendors/clickhelp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clickhelp-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clickhelp.com/legal/terms-of-use/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clickhelp.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clickhelp.com/legal/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.clickhelp.com/articles/clickhelp-user-manual/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clickhelp.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/clickhelp/security/clickhelp-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clickhelp-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/clickhelp/security/clickhelp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clickhelp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clickhelp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clickhelp.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://clickhelp.com/online-documentation-tool-pricing/
- group: company
  title: ''
  type: Blog
  url: https://clickhelp.com/clickhelp-technical-writing-blog/
- group: operate
  title: ''
  type: Support
  url: https://clickhelp.com/support/
created: '2026-10-20'
description: ClickHelp provides an AI‑powered documentation platform for technical writers and teams, offering cloud‑based authoring, single‑sourcing, white‑label branding, and a robust API for integrating documentation into applications. The service includes features such as full‑text search, translation management, analytics, and customizable workflows, targeting enterprises seeking to streamline their documentation processes.
image: https://clickhelp.com/wp-content/uploads/2025/07/OG-MainPage-1.webp
layout: provider
modified: '2026-10-20'
name: ClickHelp
nav: Providers
network: true
overview: 'ClickHelp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Documentation, Artificial Intelligence, Software-as-a-Service, and Technical Writing.


  ClickHelp''s developer surface includes authentication, getting-started guide, API reference, documentation, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Clickhelp Plans Pricing
  plan_count: 3
  slug: clickhelp-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 55.4
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 34.0
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
screenshot: https://apis.io/screenshots/clickhelp/clickhelp-2026-11-03T124414.png
security:
- kind: authentication
  name: Clickhelp Authentication
  slug: clickhelp-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Clickhelp Domain Security
  slug: clickhelp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Clickhelp Trust Center
  slug: clickhelp-trust-center
  summary_line: SOC 2, GDPR
slug: clickhelp
tags:
- Company
- Documentation
- Artificial Intelligence
- Software-as-a-Service
- Technical Writing
website: https://clickhelp.com/
---
