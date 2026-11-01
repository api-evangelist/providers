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
  href: https://artifacts.apis.io/joinchief-com/hosts/joinchief-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/joinchief-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/joinchief-com/vendors/joinchief-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/joinchief-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chief.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chief.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://chief.com/press
- group: other
  title: ''
  type: Leadership
  url: https://chief.com/articles/leadership
- group: auth
  href: https://artifacts.apis.io/joinchief-com/security/joinchief-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/joinchief-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.joinchief.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.joinchief.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Chief provides a membership and community platform empowering senior women leaders with tools, network, and space to conduct business, drive change, and lead. The service fosters connections, resources, and events aimed at amplifying women's power in professional environments, offering curated content, mentorship, and collaborative opportunities across industries.
image: https://cdn.sanity.io/images/xcsyo6gw/production/c4e53c537d9269d685eb0d20fdd42ec4324fb2cb-1000x1000.png
layout: provider
modified: '2026-10-22'
name: Chief
nav: Providers
network: true
overview: Chief is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Membership, Community, WomenLeadership, and Platform.
random_paper: 11
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Joinchief Com Domain Security
  slug: joinchief-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: joinchief-com
tags:
- Company
- Membership
- Community
- WomenLeadership
- Platform
website: http://www.joinchief.com/
---
