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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/councilbox/hosts/councilbox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/councilbox-hosts.yml
- group: build
  href: https://artifacts.apis.io/councilbox/packages/councilbox-packages.yml
  title: ''
  type: SDKs
  url: packages/councilbox-packages.yml
- group: build
  href: https://artifacts.apis.io/councilbox/packages/councilbox-packages.yml
  title: ''
  type: Packages
  url: packages/councilbox-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.councilbox.com/en/legal-notice-2/
- group: operate
  title: ''
  type: Support
  url: https://www.councilbox.com/en/help/meetings-and-assemblies-manuals/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.councilbox.com/en/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.councilbox.com/en/news/
- group: company
  title: ''
  type: Blog
  url: https://www.councilbox.com/Blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/councilbox
- group: auth
  href: https://artifacts.apis.io/councilbox/security/councilbox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/councilbox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.councilbox.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.councilbox.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Councilbox provides a cloud-based platform that enables local governments and community organizations to engage citizens, collect feedback, and manage public services through a suite of APIs. The solution focuses on transparency, collaboration, and data-driven decision making, offering endpoints for surveys, event management, service requests, and analytics. Backed by Adara Venture Partners, Councilbox aims to modernize civic tech and improve public sector efficiency.
image: https://www.councilbox.com/wp-content/uploads/2026/08/Councilbox-OVAC-Firma-digital-corp.jpg
layout: provider
modified: '2026-10-21'
name: Councilbox
nav: Providers
network: true
overview: 'Councilbox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CivicTech, APIPlatform, CommunityEngagement, and CloudServices.


  Councilbox''s developer surface includes support, engineering blog, and 9 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
  name: Councilbox Domain Security
  slug: councilbox-domain-security
  summary_line: TLSv1.3 · DMARC
slug: councilbox
tags:
- Company
- CivicTech
- APIPlatform
- CommunityEngagement
- CloudServices
website: https://www.councilbox.com/
---
