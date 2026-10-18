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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/viant-technology/refs/heads/main/vendors/viant-technology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/viant-technology-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/viant-technology/refs/heads/main/well-known/viant-technology-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/viant-technology-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/viant-technology/refs/heads/main/well-known/viant-technology-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/viant-technology-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/viant-technology/refs/heads/main/hosts/viant-technology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/viant-technology-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.viantinc.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.viantinc.com/
- group: auth
  title: ''
  type: Security
  url: https://www.viantinc.com/company/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.viantinc.com/privacy-center/
- group: company
  title: ''
  type: Newsroom
  url: https://www.viantinc.com/company/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.viantinc.com/company/team/
- group: company
  title: ''
  type: Blog
  url: https://www.viantinc.com/insights/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://help.viantinc.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/viant-technology/refs/heads/main/security/viant-technology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/viant-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.viantinc.com
coverage:
  checked: '2026-10-14'
  detail: API endpoints require authentication, returning 401 for OpenAPI and GraphQL discovery.
  evidence:
  - status: 401
    url: https://api.viantinc.com/graphql
  reason: partner-login
  state: gated
created: '2026-10-14'
description: Viant Technology provides a digital advertising technology platform that combines data-driven audience targeting, programmatic buying, and AI-powered optimization. Their solutions include a Demand Side Platform (DSP), identity resolution, household ID technology, and a data platform for omnichannel marketing across TV, audio, display, and mobile. The company serves advertisers and agencies seeking to reach consumers efficiently through advanced analytics and machine learning.
image: https://s49695.pcdn.co/wp-content/uploads/2024/04/Image-of-a-woman-on-Connected-TV-Home-Preview-Image-Hard-Light-Optimized.jpg
layout: provider
modified: '2026-10-14'
name: Viant Technology
nav: Providers
network: true
overview: 'Viant Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Marketing, Technology, DSP, and Artificial Intelligence.


  Viant Technology''s developer surface includes support, engineering blog, documentation, and 11 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 51.8
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Viant Technology Domain Security
  slug: viant-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: viant-technology
tags:
- Advertising
- Marketing
- Technology
- DSP
- Artificial Intelligence
website: https://www.viantinc.com
---
