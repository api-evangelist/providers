---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public API providing access to creator data, campaign management, analytics and payments.
  name: Upfluence API
  slug: upfluence-api
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/upfluence/changelog/upfluence-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/upfluence-changelog.yml
- group: agent
  href: https://artifacts.apis.io/upfluence/llms/upfluence-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/upfluence-llms.txt
- group: auth
  href: https://artifacts.apis.io/upfluence/well-known/upfluence-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/upfluence-help-security.txt
- group: agent
  href: https://artifacts.apis.io/upfluence/well-known/upfluence-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/upfluence-well-known.yml
- group: other
  href: https://artifacts.apis.io/upfluence/hosts/upfluence-hosts.yml
  title: ''
  type: Hosts
  url: hosts/upfluence-hosts.yml
- group: other
  href: https://artifacts.apis.io/upfluence/vendors/upfluence-vendors.yml
  title: ''
  type: Vendors
  url: vendors/upfluence-vendors.yml
- group: build
  href: https://artifacts.apis.io/upfluence/packages/upfluence-packages.yml
  title: ''
  type: SDKs
  url: packages/upfluence-packages.yml
- group: build
  href: https://artifacts.apis.io/upfluence/packages/upfluence-packages.yml
  title: ''
  type: Packages
  url: packages/upfluence-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upfluence
- group: auth
  href: https://artifacts.apis.io/upfluence/security/upfluence-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/upfluence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://upfluence.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.upfluence.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.upfluence.co
- group: docs
  title: ''
  type: APIReference
  url: https://www.upfluence.com/influencer-marketing-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.upfluence.com/get-started/
- group: operate
  title: ''
  type: Support
  url: https://help.upfluence.co/
- group: company
  title: ''
  type: Blog
  url: https://www.upfluence.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.upfluence.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upfluence.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://creators.upfluence.com/sign-up
coverage:
  checked: '2026-10-27'
  detail: The Upfluence documentation provides API details in markdown but no publicly accessible OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.upfluence.co
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Upfluence provides an influencer marketing platform that connects brands with creators. Their solution includes a robust API and MCP (Marketing Collaboration Platform) enabling programmatic access to creator data, campaign management, analytics, and payment processing. Powered by Jaice AI, Upfluence offers tools for discovery, vetting, outreach, and performance measurement, supporting e‑commerce, agencies, affiliate programs, and user‑generated content initiatives.
image: https://www.upfluence.com/wp-content/uploads/2024/09/Illu-Hero-4.png
layout: provider
modified: '2026-10-27'
name: Upfluence
nav: Providers
network: true
overview: 'Upfluence is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, InfluencerMarketing, API, MCP, and SaaS.


  Upfluence''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 13 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Upfluence Domain Security
  slug: upfluence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upfluence
tags:
- Company
- InfluencerMarketing
- API
- MCP
- SaaS
- CreatorEconomy
website: https://upfluence.com/
---
