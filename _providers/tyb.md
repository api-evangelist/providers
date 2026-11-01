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
- group: agent
  href: https://artifacts.apis.io/tyb/llms/tyb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tyb-llms.txt
- group: other
  href: https://artifacts.apis.io/tyb/hosts/tyb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tyb-hosts.yml
- group: other
  href: https://artifacts.apis.io/tyb/vendors/tyb-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tyb-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.tyb.xyz/login
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tyb.xyz/
- group: auth
  href: https://artifacts.apis.io/tyb/security/tyb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tyb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tyb.xyz/
- group: company
  title: ''
  type: Blog
  url: https://www.tyb.xyz/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tyb.xyz/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tyb.xyz/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: Provider docs pages are JavaScript‑rendered and no machine‑readable API spec was found.
  evidence:
  - status: error
    url: https://app.tyb.xyz/fan/developer
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: TYB is a community rewards platform where brand engagement pays off. It enables fans to earn rewards for creating content, social ambassadorship, purchases, and active participation. Brands leverage TYB to boost loyalty, gather user‑generated content, and drive sales through gamified experiences, fostering a vibrant ecosystem of creators and consumers.
image: https://cdn.prod.website-files.com/6847283f7bcb9c223f50faf8/685a2551b78d0dc4985659c6_Share%20Image%20-%20Fan.png
layout: provider
modified: '2026-10-29'
name: TYB
nav: Providers
network: true
overview: 'TYB is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Rewards, Community, Engagement, and Platform.


  TYB''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
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
  name: Tyb Domain Security
  slug: tyb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tyb
tags:
- Company
- Rewards
- Community
- Engagement
- Platform
website: https://www.tyb.xyz/
---
