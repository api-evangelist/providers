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
    dynamic_client_registration: true
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Parasoft provides API testing solutions documented at the developer portal.
  name: Parasoft API
  slug: parasoft-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/parasoft/well-known/parasoft-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/parasoft-well-known.yml
- group: other
  href: https://artifacts.apis.io/parasoft/hosts/parasoft-hosts.yml
  title: ''
  type: Hosts
  url: hosts/parasoft-hosts.yml
- group: other
  href: https://artifacts.apis.io/parasoft/vendors/parasoft-vendors.yml
  title: ''
  type: Vendors
  url: vendors/parasoft-vendors.yml
- group: build
  href: https://artifacts.apis.io/parasoft/packages/parasoft-packages.yml
  title: ''
  type: SDKs
  url: packages/parasoft-packages.yml
- group: build
  href: https://artifacts.apis.io/parasoft/packages/parasoft-packages.yml
  title: ''
  type: Packages
  url: packages/parasoft-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.parasoft.com/news/c-ctest-full-support-misra-c2023-tc1-day-one/
- group: auth
  href: https://artifacts.apis.io/parasoft/security/parasoft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/parasoft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.parasoft.com/
- group: company
  title: ''
  type: Blog
  url: https://www.parasoft.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://www.parasoft.com/solutions/
- group: docs
  title: ''
  type: APIReference
  url: https://www.parasoft.com/solutions/api-testing/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.parasoft.com/request-a-demo/
- group: operate
  title: ''
  type: Support
  url: https://www.parasoft.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.parasoft.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.parasoft.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parasoft
- group: company
  title: ''
  type: Website
  url: https://parasoft.com/
coverage:
  checked: '2026-10-21'
  detail: Docs are served via a JavaScript-rendered Confluence site, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.parasoft.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Parasoft provides automated software testing solutions that help development teams improve code quality, accelerate release cycles, and ensure compliance with industry standards. Their portfolio includes tools for static code analysis, unit testing, API testing, and runtime error detection across a wide range of programming languages and platforms. Parasoft serves industries such as aerospace, automotive, finance, and healthcare, offering both on-premises and cloud-based solutions to meet diverse testing needs.
layout: provider
modified: '2026-10-21'
name: Parasoft
nav: Providers
network: true
overview: 'Parasoft is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Testing, Automation, Software, and Quality.


  Parasoft''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, pricing, and 11 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 54.5
    operational_transparency: 2.6
  previous_composite: 19.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/parasoft/parasoft-2026-11-03T140933.png
security:
- kind: domain-security
  name: Parasoft Domain Security
  slug: parasoft-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: parasoft
tags:
- Company
- Testing
- Automation
- Software
- Quality
website: https://www.parasoft.com/
---
