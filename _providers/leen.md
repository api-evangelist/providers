---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Leen Webhooks
  slug: leen-webhooks
common:
- group: design
  href: https://artifacts.apis.io/leen/asyncapi/leen-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/leen-webhooks.yml
- group: design
  href: https://artifacts.apis.io/leen/conventions/leen-conventions.yml
  title: ''
  type: Conventions
  url: conventions/leen-conventions.yml
- group: auth
  href: https://artifacts.apis.io/leen/authentication/leen-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leen-authentication.yml
- group: agent
  href: https://artifacts.apis.io/leen/llms/leen-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leen-llms.txt
- group: other
  href: https://artifacts.apis.io/leen/a2a/leen-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/leen-a2a.yml
- group: agent
  href: https://artifacts.apis.io/leen/well-known/leen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/leen-well-known.yml
- group: other
  href: https://artifacts.apis.io/leen/hosts/leen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/leen-hosts.yml
- group: other
  href: https://artifacts.apis.io/leen/vendors/leen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/leen-vendors.yml
- group: build
  href: https://artifacts.apis.io/leen/packages/leen-packages.yml
  title: ''
  type: SDKs
  url: packages/leen-packages.yml
- group: build
  href: https://artifacts.apis.io/leen/packages/leen-packages.yml
  title: ''
  type: Packages
  url: packages/leen-packages.yml
- group: auth
  href: https://artifacts.apis.io/leen/security/leen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.leen.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leen.dev/intro/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.leen.dev/intro/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://www.leen.dev/demo
- group: company
  title: ''
  type: Blog
  url: https://www.leen.dev/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://www.leen.dev/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leen.dev/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leen.dev/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/leen/workspace
created: '2026-10-21'
description: Leen provides a unified API and data fabric for security operations, aggregating data from various security tools into a single, normalized model. It supports vulnerability management, reporting, AI-driven SOC automation, cyber insurance, and automated GRC, helping organizations streamline security data integration and reduce complexity across their security stack.
image: https://cdn.prod.website-files.com/65beeed38aea1cf4d02d2653/66034c942335eb51805fc6d0_7.png
layout: provider
modified: '2026-10-21'
name: Leen
nav: Providers
network: true
overview: 'Leen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Data Fabric, Integration, and Automation.


  The Leen catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Leen''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, and 15 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 36.9
    discoverability: 46.4
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 36.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/leen/leen-2026-11-03T134802.png
security:
- kind: authentication
  name: Leen Authentication
  slug: leen-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Leen Domain Security
  slug: leen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: leen
tags:
- Security
- Data Fabric
- Integration
- Automation
website: https://www.leen.dev/
---
