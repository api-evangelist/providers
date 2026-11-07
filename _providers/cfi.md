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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/cfi/well-known/cfi-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cfi-status-security.txt
- group: start
  title: ''
  type: Login
  url: https://learn.corporatefinanceinstitute.com/auth/login
- group: commercial
  href: https://artifacts.apis.io/cfi/plans/cfi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cfi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cfi/changelog/cfi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cfi-changelog.yml
- group: agent
  href: https://artifacts.apis.io/cfi/well-known/cfi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cfi-well-known.yml
- group: other
  href: https://artifacts.apis.io/cfi/hosts/cfi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cfi-hosts.yml
- group: other
  href: https://artifacts.apis.io/cfi/vendors/cfi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cfi-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.corporatefinanceinstitute.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corporatefinanceinstitute.com/about-cfi/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://corporatefinanceinstitute.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://corporatefinanceinstitute.com/resources/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://corporatefinanceinstitute.com/resources/management/generative-ai-webinar/
- group: operate
  title: ''
  type: ChangeLog
  url: https://corporatefinanceinstitute.com/whats-new/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.corporatefinanceinstitute.com/article/1091-getting-started-with-cfi
- group: docs
  title: ''
  type: Documentation
  url: https://help.corporatefinanceinstitute.com/
- group: auth
  href: https://artifacts.apis.io/cfi/security/cfi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cfi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://corporatefinanceinstitute.com
coverage:
  checked: '2026-10-25'
  detail: The provider's website serves HTML with a browser upgrade notice and no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 404
    url: https://corporatefinanceinstitute.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Corporate Finance Institute (CFI) provides online finance education, certifications, and training programs for individuals and teams. It offers courses in financial modeling, valuation, FP&A, and AI for finance, serving professionals seeking to advance their careers. CFI’s platform includes a resource library, career maps, and enterprise solutions for organizations, positioning itself as a leading provider of finance skills and certifications worldwide.
image: https://cdn.corporatefinanceinstitute.com/assets/Corporate-Finance-Institute-Default-Social.jpg
layout: provider
modified: '2026-10-25'
name: CFI
nav: Providers
network: true
overview: 'CFI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Finance, Certification, and E-Learning.


  CFI''s developer surface includes changelog, pricing, getting-started guide, documentation, and 13 more developer resources.'
plans:
- name: Cfi Plans Pricing
  plan_count: 7
  slug: cfi-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 50.0
    operational_transparency: 26.3
  previous_composite: 24.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cfi/cfi-2026-11-03T123744.png
security:
- kind: domain-security
  name: Cfi Domain Security
  slug: cfi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cfi
tags:
- Company
- Education
- Finance
- Certification
- E-Learning
website: https://corporatefinanceinstitute.com
---
