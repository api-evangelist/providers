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
  href: https://artifacts.apis.io/bdow/llms/bdow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bdow-llms.txt
- group: auth
  href: https://artifacts.apis.io/bdow/well-known/bdow-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bdow-help-security.txt
- group: agent
  href: https://artifacts.apis.io/bdow/well-known/bdow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bdow-well-known.yml
- group: other
  href: https://artifacts.apis.io/bdow/hosts/bdow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bdow-hosts.yml
- group: other
  href: https://artifacts.apis.io/bdow/vendors/bdow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bdow-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://bdow.com/stories/whats-new/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.bdow.com/en/articles/9114583-getting-started-with-shortcuts
- group: docs
  title: ''
  type: APIReference
  url: https://api.bdow.com/docs
- group: auth
  href: https://artifacts.apis.io/bdow/security/bdow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bdow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bdow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bdow.com/features
- group: commercial
  title: ''
  type: Pricing
  url: https://bdow.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://bdow.com/stories
- group: start
  title: ''
  type: SignUp
  url: https://bdow.com/register
- group: operate
  title: ''
  type: HelpCenter
  url: https://bdow.com/how-it-works
coverage:
  checked: '2026-10-26'
  detail: The provider's website (https://bdow.com) offers no developer documentation or API specifications.
  evidence:
  - status: 200
    url: https://bdow.com
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: BDOW! is a lead generation and email capture platform that provides tools for creating forms, pop‑ups, and landing pages to grow website visitor lists. The service offers customizable templates, A/B testing, analytics, and integrations with marketing and CRM systems. It targets marketers, small businesses, and agencies looking to increase conversions and capture leads directly from their sites.
image: https://static.showit.co/1200/5Cu-MFw2S9yf-YaWgDTHjw/237372/homepage-bdow-social.jpg
layout: provider
modified: '2026-10-26'
name: BDOW!
nav: Providers
network: true
overview: 'BDOW! is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  BDOW!''s developer surface includes changelog, getting-started guide, API reference, documentation, pricing, engineering blog, signup flow, and 8 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 39.3
    operational_transparency: 26.3
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
  name: Bdow Domain Security
  slug: bdow-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bdow
tags:
- Company
website: https://bdow.com/
---
