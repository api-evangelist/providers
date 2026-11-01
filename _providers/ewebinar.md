---
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.7
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/ewebinar/plans/ewebinar-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ewebinar-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/ewebinar/well-known/ewebinar-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ewebinar-well-known.yml
- group: other
  href: https://artifacts.apis.io/ewebinar/hosts/ewebinar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ewebinar-hosts.yml
- group: other
  href: https://artifacts.apis.io/ewebinar/vendors/ewebinar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ewebinar-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://ewebinar.com/integrations/webhooks
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ewebinar.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ewebinar.com/terms
- group: operate
  title: ''
  type: Support
  url: https://ewebinar.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ewebinar.com/privacy
- group: start
  title: ''
  type: Login
  url: https://app.ewebinar.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ewebinar.com/help/category/developer
- group: start
  title: ''
  type: GettingStarted
  url: https://ewebinar.com/help/category/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ewebinar
- group: auth
  href: https://artifacts.apis.io/ewebinar/security/ewebinar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ewebinar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ewebinar.com/
- group: company
  title: ''
  type: Blog
  url: https://ewebinar.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ewebinar.com/pricing
coverage:
  checked: '2026-10-28'
  detail: Documentation site https://docs.ewebinar.com returns HTML without any OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.ewebinar.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: eWebinar provides on‑demand webinar software that turns pre‑recorded videos into interactive, live‑style webinars with chat, Q&A, and polls. The platform lets teams deliver demos, onboarding, training, and product walkthroughs without requiring a live presenter, extending reach to any audience at any time. Features include customizable branding, analytics, and integration with marketing tools, helping businesses scale their video communication and engagement.
image: https://ewebinar.com/_image/w=1200,f=jpeg/cms-assets/375631bbe0d2d420/eWebinar%20Player.png
layout: provider
modified: '2026-10-28'
name: eWebinar
nav: Providers
network: true
overview: 'eWebinar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Webinar, Video, OnDemand, and SaaS.


  eWebinar''s developer surface includes support, getting-started guide, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Ewebinar Plans Pricing
  plan_count: 4
  slug: ewebinar-plans-pricing
random_paper: 5
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 13.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ewebinar Domain Security
  slug: ewebinar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ewebinar
tags:
- Company
- Webinar
- Video
- OnDemand
- SaaS
website: https://ewebinar.com/
---
