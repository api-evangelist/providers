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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/craigslist/security/craigslist-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/craigslist-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/craigslist/well-known/craigslist-sfbay-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/craigslist-sfbay-security.txt
- group: auth
  href: https://artifacts.apis.io/craigslist/well-known/craigslist-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/craigslist-security.txt
- group: auth
  href: https://artifacts.apis.io/craigslist/well-known/craigslist-post-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/craigslist-post-security.txt
- group: auth
  href: https://artifacts.apis.io/craigslist/well-known/craigslist-geo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/craigslist-geo-security.txt
- group: auth
  href: https://artifacts.apis.io/craigslist/well-known/craigslist-forums-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/craigslist-forums-security.txt
- group: auth
  href: https://artifacts.apis.io/craigslist/well-known/craigslist-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/craigslist-api-security.txt
- group: auth
  href: https://artifacts.apis.io/craigslist/well-known/craigslist-accounts-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/craigslist-accounts-security.txt
- group: agent
  href: https://artifacts.apis.io/craigslist/well-known/craigslist-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/craigslist-well-known.yml
- group: other
  href: https://artifacts.apis.io/craigslist/hosts/craigslist-hosts.yml
  title: ''
  type: Hosts
  url: hosts/craigslist-hosts.yml
- group: build
  href: https://artifacts.apis.io/craigslist/packages/craigslist-packages.yml
  title: ''
  type: SDKs
  url: packages/craigslist-packages.yml
- group: build
  href: https://artifacts.apis.io/craigslist/packages/craigslist-packages.yml
  title: ''
  type: Packages
  url: packages/craigslist-packages.yml
- group: start
  title: ''
  type: Login
  url: https://accounts.craigslist.org/login/home
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.craigslist.org/about/whats-new
- group: company
  title: ''
  type: Blog
  url: http://blog.craigslist.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/craigslist
- group: auth
  href: https://artifacts.apis.io/craigslist/security/craigslist-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/craigslist-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/craigslist/security/craigslist-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/craigslist-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.craigslist.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.craigslist.org/about
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.craigslist.org/about/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.craigslist.org/about/terms.of.use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.craigslist.org/about/privacy.policy
coverage:
  checked: '2026-10-11'
  detail: Craigslist provides no public API specification; attempts to fetch OpenAPI at known endpoints returned 404.
  evidence:
  - status: 404
    url: https://api.craigslist.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Craigslist is a classified advertisements website founded in 1995, offering sections for jobs, housing, for‑sale items, services, community, and events across many U.S. cities and international locations. It operates as a simple, user‑generated platform without a formal public API, relying on web interfaces and RSS feeds for data access.
layout: provider
modified: '2026-10-11'
name: Craigslist
nav: Providers
network: true
overview: 'Craigslist is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Classifieds, Marketplace, Job, and Housing.


  Craigslist''s developer surface includes changelog, engineering blog, documentation, and 20 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 44.6
    operational_transparency: 21.1
  previous_composite: 20.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/craigslist/craigslist-2026-11-03T125513.png
security:
- kind: domain-security
  name: Craigslist Domain Security
  slug: craigslist-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Craigslist Vulnerability Disclosure
  slug: craigslist-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: craigslist
tags:
- Company
- Classifieds
- Marketplace
- Job
- Housing
- Community
website: https://www.craigslist.org
---
