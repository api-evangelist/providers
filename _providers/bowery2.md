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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bowery2/refs/heads/main/hosts/bowery2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bowery2-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bowery2/refs/heads/main/vendors/bowery2-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bowery2-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boweryvaluation.com/terms-conditions
- group: start
  title: ''
  type: Sandbox
  url: https://www.boweryvaluation.com/testing-folder/sandbox
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boweryvaluation.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.boweryvaluation.com/press
- group: company
  title: ''
  type: Blog
  url: https://www.boweryvaluation.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boweryvaluation
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bowery2/refs/heads/main/security/bowery2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bowery2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boweryvaluation.com
coverage:
  checked: '2026-10-03'
  detail: The portal page renders via JavaScript and provides no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://portal.boweryvaluation.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Bowery Valuation (Bowery2) provides cloud‑based commercial appraisal software and a mobile app that enable real‑estate appraisers to produce high‑quality appraisal reports faster and more consistently. Founded in 2015 and headquartered in New York, the company serves top financial institutions and lenders with advanced CRE technology, proprietary databases, and integrated public‑record data. Their platform accelerates valuation workflows, improves accuracy, and reduces costs for clients across the United States.
image: https://cdn.prod.website-files.com/5cc9fe0737d849c4f294ae53/5d420360f65670868b8351d7_banner_illustration_svg.svg
layout: provider
modified: '2026-10-03'
name: Bowery2
nav: Providers
network: true
overview: 'Bowery2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Appraisal, Software, and Artificial Intelligence.


  Bowery2''s developer surface includes sandbox, engineering blog, and 8 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bowery2 Domain Security
  slug: bowery2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bowery2
tags:
- Company
- Real Estate
- Appraisal
- Software
- Artificial Intelligence
website: https://www.boweryvaluation.com
---
