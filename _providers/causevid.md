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
  href: https://artifacts.apis.io/causevid/hosts/causevid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/causevid-hosts.yml
- group: auth
  href: https://artifacts.apis.io/causevid/security/causevid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/causevid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://causevid.com/
- group: company
  title: ''
  type: Blog
  url: https://causevid.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://causevid.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://causevid.com/how-it-works
- group: company
  title: ''
  type: About
  url: https://causevid.com/why-causevid
coverage:
  checked: '2026-10-27'
  detail: CauseVid does not provide a public developer program or API documentation.
  evidence:
  - status: 200
    url: https://causevid.com/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: CauseVid provides a platform for nonprofits to create, send, and track personalized video messages that engage donors and tell the story of their cause. Their service enables organizations of any size to produce custom video content easily, integrate with fundraising workflows, and measure impact through analytics, helping donors feel appreciated and increasing donation rates.
layout: provider
modified: '2026-10-27'
name: CauseVid
nav: Providers
network: true
overview: 'CauseVid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Nonprofit, Video, Fundraising, Marketing, and SaaS.


  CauseVid''s developer surface includes engineering blog, pricing, getting-started guide, and 4 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Causevid Domain Security
  slug: causevid-domain-security
  summary_line: DNSSEC · DMARC
slug: causevid
tags:
- Nonprofit
- Video
- Fundraising
- Marketing
- SaaS
website: https://causevid.com/
---
