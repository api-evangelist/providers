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
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/donordrive/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/donordrive/well-known/donordrive-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/donordrive-status-security.txt
- group: agent
  href: https://artifacts.apis.io/donordrive/well-known/donordrive-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/donordrive-well-known.yml
- group: other
  href: https://artifacts.apis.io/donordrive/hosts/donordrive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/donordrive-hosts.yml
- group: other
  href: https://artifacts.apis.io/donordrive/vendors/donordrive-vendors.yml
  title: ''
  type: Vendors
  url: vendors/donordrive-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.donordrive.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DonorDrive
- group: auth
  href: https://artifacts.apis.io/donordrive/security/donordrive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/donordrive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://donordrive.com/
- group: docs
  title: ''
  type: Documentation
  url: https://donordrive.com/resources/
- group: company
  title: ''
  type: AboutUs
  url: https://donordrive.com/about/
- group: company
  title: ''
  type: News
  url: https://donordrive.com/about/news/
coverage:
  checked: '2026-10-27'
  detail: Documentation pages exist but no OpenAPI/GraphQL/AsyncAPI spec was found.
  evidence:
  - status: 200
    url: https://donordrive.com/resources/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: DonorDrive provides a fundraising platform that helps nonprofits and charitable organizations manage and grow donor relationships. The solution offers tools for online giving, event registration, donor management, and reporting, enabling supporters to easily contribute and organizations to track impact and engagement. With customizable campaigns, mobile-friendly donation pages, and integration capabilities, DonorDrive aims to boost stewardship and increase fundraising efficiency for nonprofits of all sizes.
image: https://www.donordrive.com/sites/default/cache/file/FAC57551-D744-02F2-1C2F797F93909A29_og-rectangle.jpg
layout: provider
modified: '2026-10-27'
name: DonorDrive
nav: Providers
network: true
overview: 'DonorDrive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fundraising, Non-Profit, Donation Platform, and Software-as-a-Service.


  DonorDrive''s developer surface includes documentation, product news, and 10 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.2
    discoverability: 49.1
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.9
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/donordrive/donordrive-2026-11-03T130935.png
security:
- kind: domain-security
  name: Donordrive Domain Security
  slug: donordrive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: donordrive
tags:
- Company
- Fundraising
- Non-Profit
- Donation Platform
- Software-as-a-Service
website: https://donordrive.com/
---
