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
  href: https://raw.githubusercontent.com/api-evangelist/cpa-com/refs/heads/main/hosts/cpa-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cpa-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cpa.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cpa.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cpa.com/webinars/pricing-packaging-and-finding-right-fit-your-firm
- group: company
  title: ''
  type: Newsroom
  url: https://www.cpa.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.cpa.com/team/mo-huda
- group: docs
  title: ''
  type: Documentation
  url: https://www.cpa.com/guides/building-success-sage-intacct-accountants-program
- group: company
  title: ''
  type: Blog
  url: https://www.cpa.com/blog/2026/09/21/turn-your-vision-velocity-dcpa26
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cpa.com/webinars/part-1-5-engagement-setup-and-build-insights-technology-around-prep-comp-and-review
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cpa-com/refs/heads/main/security/cpa-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cpa-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cpa.com/
coverage:
  checked: '2026-10-11'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found at https://api.cpa.com/openapi.json (404).
  evidence:
  - status: 404
    url: https://api.cpa.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: CPA.com, founded in 2001 as an affiliate of the American Institute of CPAs (AICPA), empowers accounting firms and finance teams for the digital age. It offers technology solutions, advisory services, and resources across practice areas such as audit, tax, and practice management. The company provides insights, research, webinars, and a community to help firms adopt innovative technologies and stay competitive.
image: https://www.cpa.com/sites/cpa/files/2020-09/cpa-logo-1200.jpg
layout: provider
modified: '2026-10-11'
name: CPA.com
nav: Providers
network: true
overview: 'CPA.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounting, Technology, Advisory, and Community.


  CPA.com''s developer surface includes pricing, documentation, engineering blog, getting-started guide, and 7 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cpa Com Domain Security
  slug: cpa-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cpa-com
tags:
- Company
- Accounting
- Technology
- Advisory
- Community
website: https://www.cpa.com/
---
