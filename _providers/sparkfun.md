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
  href: https://artifacts.apis.io/sparkfun/hosts/sparkfun-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sparkfun-hosts.yml
- group: other
  href: https://artifacts.apis.io/sparkfun/vendors/sparkfun-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sparkfun-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sparkfun.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sparkfun.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.sparkfun.com/customer/account/login/referer/aHR0cHM6Ly93d3cuc3BhcmtmdW4uY29tLw~~/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sparkfun
- group: auth
  href: https://artifacts.apis.io/sparkfun/security/sparkfun-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sparkfun-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sparkfun.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.sparkfun.com/documentation
- group: operate
  title: ''
  type: Support
  url: https://www.sparkfun.com/support
- group: operate
  title: ''
  type: Community
  url: https://community.sparkfun.com/
- group: company
  title: ''
  type: News
  url: https://news.sparkfun.com/
coverage:
  checked: '2026-10-27'
  detail: SparkFun documentation pages are rendered via JavaScript and no machine‑readable OpenAPI or other contract could be retrieved.
  evidence:
  - status: 200
    url: https://www.sparkfun.com/documentation
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: SparkFun Electronics is a global retailer and distributor of electronic components, development boards, sensors, and accessories for makers, hobbyists, and engineers. They provide extensive product documentation, tutorials, and community support, enabling users to prototype and build electronic projects. The company also offers educational resources and a vibrant community forum for sharing ideas and troubleshooting.
layout: provider
modified: '2026-10-27'
name: SparkFun Electronics
nav: Providers
network: true
overview: 'SparkFun Electronics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Electronics, Retail, Maker, Education, and Community.


  SparkFun Electronics'' developer surface includes documentation, support, product news, and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 46.4
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sparkfun Domain Security
  slug: sparkfun-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sparkfun
tags:
- Electronics
- Retail
- Maker
- Education
- Community
website: https://www.sparkfun.com/
---
