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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crowdwise/refs/heads/main/hosts/crowdwise-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crowdwise-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crowdwise/refs/heads/main/vendors/crowdwise-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crowdwise-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crowdwise.org/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crowdwise.org/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://crowdwise.org/login
- group: company
  title: ''
  type: Blog
  url: https://crowdwise.org/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crowdwise/refs/heads/main/security/crowdwise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crowdwise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crowdwise.org/
coverage:
  checked: '2026-10-11'
  detail: No machine‑readable API specification was found on crowdwise.org or its API host.
  evidence:
  - status: 200
    url: https://crowdwise.org/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Crowdwise is an online education and community platform focused on equity crowdfunding. It offers courses, eBooks, videos, blog posts, and tools to help investors understand and participate in startup investing. The site provides a collaborative environment with resources such as portfolio trackers, ROI calculators, and a members‑only forum, aiming to empower both novice and experienced investors in the equity crowdfunding space.
image: https://crowdwise.org/wp-content/uploads/2019/06/YouTube-Channel-Banner.png
layout: provider
modified: '2026-10-11'
name: Crowdwise
nav: Providers
network: true
overview: 'Crowdwise is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EquityCrowdfunding, Education, Community, and Tools.


  Crowdwise''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crowdwise Domain Security
  slug: crowdwise-domain-security
  summary_line: TLSv1.3 · DMARC
slug: crowdwise
tags:
- Company
- EquityCrowdfunding
- Education
- Community
- Tools
website: https://crowdwise.org/
---
