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
  href: https://raw.githubusercontent.com/api-evangelist/icpsr/refs/heads/main/hosts/icpsr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/icpsr-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/icpsr/refs/heads/main/vendors/icpsr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/icpsr-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.icpsr.umich.edu/sites/icpsr/about/policies/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.icpsr.umich.edu/sites/icpsr/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/icpsr/refs/heads/main/security/icpsr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/icpsr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.icpsr.umich.edu
- group: docs
  title: ''
  type: Documentation
  url: https://www.icpsr.umich.edu/sites/icpsr/help
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.icpsr.umich.edu
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: The Inter-university Consortium for Political and Social Research (ICPSR) at the University of Michigan provides a curated archive of social science data, offering tools for data discovery, access, and management. It supports researchers, educators, and policymakers with datasets spanning health, politics, economics, and more, and provides documentation, help guides, and membership resources.
image: https://wpvip.icpsr.umich.edu/icpsr/wp-content/uploads/sites/11/2026_Small-widget2.png
layout: provider
modified: '2026-10-13'
name: ICPSR
nav: Providers
network: true
overview: 'ICPSR is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Research, SocialScience, and Archives.


  ICPSR''s developer surface includes documentation and 6 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Icpsr Domain Security
  slug: icpsr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: icpsr
tags:
- Company
- Data
- Research
- SocialScience
- Archives
website: https://www.icpsr.umich.edu
---
