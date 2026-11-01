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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/connexity/hosts/connexity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connexity-hosts.yml
- group: other
  href: https://artifacts.apis.io/connexity/vendors/connexity-vendors.yml
  title: ''
  type: Vendors
  url: vendors/connexity-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.connexity.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://publisher.connexity.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.connexity.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Connexity
- group: auth
  href: https://artifacts.apis.io/connexity/security/connexity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connexity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.connexity.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://account.connexity.com/mcp
  - status: 401
    url: https://merchant.connexity.com/mcp
  - status: 200
    url: https://www.connexity.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Connexity provides a suite of digital marketing and data-driven advertising solutions that help online retailers and brands acquire, engage, and retain customers. Leveraging a robust network of affiliate partners and sophisticated analytics, Connexity enables performance-based campaigns, audience targeting, and real-time reporting. The platform integrates with e-commerce sites, search engines, and social media to optimize ad spend and drive measurable ROI. Founded in 2004, the company continues to innovate in the affiliate marketing space, offering APIs for product feeds, transaction tracking, and partner management.
layout: provider
modified: '2026-10-21'
name: Connexity
nav: Providers
network: true
overview: 'Connexity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Advertising, Affiliate, and DataAnalytics.


  Connexity''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Connexity Domain Security
  slug: connexity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: connexity
tags:
- Company
- Marketing
- Advertising
- Affiliate
- DataAnalytics
website: https://www.connexity.com/
---
