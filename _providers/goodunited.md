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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/goodunited/plans/goodunited-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/goodunited-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/goodunited/conformance/goodunited-conformance.yml
  title: ''
  type: Conformance
  url: conformance/goodunited-conformance.yml
- group: other
  href: https://artifacts.apis.io/goodunited/hosts/goodunited-hosts.yml
  title: ''
  type: Hosts
  url: hosts/goodunited-hosts.yml
- group: other
  href: https://artifacts.apis.io/goodunited/vendors/goodunited-vendors.yml
  title: ''
  type: Vendors
  url: vendors/goodunited-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goodunited.io/legal/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://www.goodunited.io/journeys/signup-for-future-actions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goodunited.io/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.goodunited.io/about/news
- group: company
  title: ''
  type: Blog
  url: https://www.goodunited.io/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goodunited
- group: auth
  href: https://artifacts.apis.io/goodunited/security/goodunited-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goodunited-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goodunited.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.goodunited.io/solutions
- group: docs
  title: ''
  type: Documentation
  url: https://www.goodunited.io/results
- group: docs
  title: ''
  type: Documentation
  url: https://www.goodunited.io/resources
- group: start
  title: ''
  type: GettingStarted
  url: https://www.goodunited.io/book-a-demo
coverage:
  checked: '2026-10-27'
  detail: The provider's documentation pages are HTML without any published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.goodunited.io/solutions
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: GoodUnited helps nonprofit organizations turn anonymous social media followers into named donors through direct messaging. Their platform enables organizations to engage supporters, increase donations, and collect valuable data without additional staff, leveraging social media outreach and personalized communication.
image: https://cdn.prod.website-files.com/6398ccdfe4646107149f2b55/69843f34956e58f5694009f8_GU-OG.png
layout: provider
modified: '2026-10-27'
name: GoodUnited
nav: Providers
network: true
overview: 'GoodUnited is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Non-Profit, Social Media, Fundraising, and Donor Engagement.


  GoodUnited''s developer surface includes signup flow, engineering blog, documentation, getting-started guide, and 12 more developer resources.'
plans:
- name: Goodunited Plans Pricing
  plan_count: 50
  slug: goodunited-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 48.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 49.1
    operational_transparency: 2.6
  previous_composite: 26.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/goodunited/goodunited-2026-11-03T132931.png
security:
- kind: domain-security
  name: Goodunited Domain Security
  slug: goodunited-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goodunited
tags:
- Company
- Non-Profit
- Social Media
- Fundraising
- Donor Engagement
website: https://goodunited.io/
---
