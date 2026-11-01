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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 16.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/amilia/plans/amilia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amilia-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/amilia/llms/amilia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amilia-llms.txt
- group: auth
  href: https://artifacts.apis.io/amilia/well-known/amilia-university-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amilia-university-security.txt
- group: auth
  href: https://artifacts.apis.io/amilia/well-known/amilia-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amilia-help-security.txt
- group: agent
  href: https://artifacts.apis.io/amilia/well-known/amilia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amilia-well-known.yml
- group: other
  href: https://artifacts.apis.io/amilia/hosts/amilia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amilia-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.amilia.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amilia.com/legal/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.amilia.com/newsroom
- group: start
  title: ''
  type: Login
  url: https://www.amilia.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://help.amilia.com/en/articles/3566537-subscription-setup-legacy-version
- group: auth
  href: https://artifacts.apis.io/amilia/security/amilia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amilia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amilia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.amilia.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.amilia.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.amilia.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.amilia.com/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.amilia.com
- group: company
  title: ''
  type: About
  url: https://www.amilia.com/about
coverage:
  checked: '2026-10-27'
  detail: Amilia provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.amilia.com/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: Amilia provides online registration, membership management, and facility rental software for recreation and community organizations. Their platform supports multi‑location programs, payments, AI‑enhanced features, and integrates with accounting systems, helping nonprofits, schools, and parks manage members, events, and facilities efficiently.
image: https://s3.ca-central-1.amazonaws.com/amiliacraftcmsmtl/media/images/opengraph/Amilia-opengraph-website-2022.jpg
layout: provider
modified: '2026-10-27'
name: Amilia
nav: Providers
network: true
overview: 'Amilia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software, Membership, Recreation, and Facilities.


  Amilia''s developer surface includes getting-started guide, documentation, engineering blog, pricing, support, and 14 more developer resources.'
plans:
- name: Amilia Plans Pricing
  plan_count: 3
  slug: amilia-plans-pricing
random_paper: 21
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amilia Domain Security
  slug: amilia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amilia
tags:
- Company
- Software
- Membership
- Recreation
- Facilities
- Payments
website: https://amilia.com/
---
