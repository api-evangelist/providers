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
- group: agent
  href: https://artifacts.apis.io/adaction/llms/adaction-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adaction-llms.txt
- group: other
  href: https://artifacts.apis.io/adaction/hosts/adaction-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adaction-hosts.yml
- group: other
  href: https://artifacts.apis.io/adaction/vendors/adaction-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adaction-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adaction.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.adaction.com/news
- group: company
  title: ''
  type: Blog
  url: https://www.adaction.com/blog/app-installs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdAction
- group: auth
  href: https://artifacts.apis.io/adaction/security/adaction-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adaction-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adaction.com/
coverage:
  checked: '2026-10-28'
  detail: No machine‑readable API specification was found on the provider’s website or documented hosts.
  evidence:
  - status: 200
    url: https://www.adaction.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: AdAction provides mobile app advertising, offerwall, and monetization solutions, offering products such as Qualume, AdGem Play, AdGem Rewards, and Activate360. The company serves advertisers and publishers, focusing on user acquisition, engagement, loyalty, and ecosystem growth, and is recognized in industry performance indexes.
image: https://www.adaction.com/wp-content/uploads/2022/07/Favicon_1@2x.png
layout: provider
modified: '2026-10-28'
name: AdAction
nav: Providers
network: true
overview: 'AdAction is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Mobile, Monetization, and User Acquisition.


  AdAction''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
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
  name: Adaction Domain Security
  slug: adaction-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adaction
tags:
- Company
- Advertising
- Mobile
- Monetization
- User Acquisition
website: https://adaction.com/
---
