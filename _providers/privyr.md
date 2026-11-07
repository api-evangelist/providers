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
- group: commercial
  href: https://artifacts.apis.io/privyr/plans/privyr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/privyr-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/privyr/hosts/privyr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/privyr-hosts.yml
- group: other
  href: https://artifacts.apis.io/privyr/vendors/privyr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/privyr-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.privyr.com/knowledge-base/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.privyr.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.privyr.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://www.privyr.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.privyr.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.privyr.com/categories/intro/
- group: docs
  title: ''
  type: Documentation
  url: https://help.privyr.com/
- group: auth
  href: https://artifacts.apis.io/privyr/security/privyr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/privyr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.privyr.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.privyr.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: 'Privyr is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by crane-venture-partners) and added to the network as a stub for full-pipeline profiling.'
image: https://d1z8p0imlkk5pt.cloudfront.net/static/img/privyr-logo-preview.1088fa1e0fb0.jpg
layout: provider
modified: '2026-10-24'
name: Privyr
nav: Providers
network: true
overview: 'Privyr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include CRM, Lead Management, WhatsApp Automation, Marketing Agencies, and Real Estate.


  Privyr''s developer surface includes pricing, engineering blog, getting-started guide, documentation, and 8 more developer resources.'
plans:
- name: Privyr Plans Pricing
  plan_count: 4
  slug: privyr-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 39.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/privyr/privyr-2026-11-03T141504.png
security:
- kind: domain-security
  name: Privyr Domain Security
  slug: privyr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: privyr
tags:
- CRM
- Lead Management
- WhatsApp Automation
- Marketing Agencies
- Real Estate
- Mobile App
website: https://www.privyr.com/
---
