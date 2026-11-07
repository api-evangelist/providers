---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 21.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Access DiscoLike datasets for business discovery, firmographic data, and contact enrichment.
  name: DiscoLike API
  slug: discolike-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/discolike-com/plans/discolike-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/discolike-com-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/discolike-com/cli/discolike-com-cli.yml
  title: ''
  type: CLI
  url: cli/discolike-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/discolike-com/authentication/discolike-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/discolike-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/discolike-com/conformance/discolike-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/discolike-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/discolike-com/llms/discolike-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/discolike-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/discolike-com/well-known/discolike-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/discolike-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/discolike-com/hosts/discolike-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/discolike-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/discolike-com/vendors/discolike-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/discolike-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/discolike-com/packages/discolike-com-packages.yml
  title: ''
  type: SDKs
  url: packages/discolike-com-packages.yml
- group: build
  href: https://artifacts.apis.io/discolike-com/packages/discolike-com-packages.yml
  title: ''
  type: Packages
  url: packages/discolike-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://discolike.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://discolike.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://discolike.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://discolike.com/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/discolike
- group: company
  title: ''
  type: Blog
  url: https://discolike.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.discolike.com/sdk/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.discolike.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.discolike.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/discolike-com/security/discolike-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/discolike-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://discolike.com/
created: '2026-11-05'
description: DiscoLike provides a platform for discovering and analyzing market competitors. It aggregates company data, financials, and API endpoints to help businesses gain insights into their competitive landscape. Users can explore detailed profiles, compare metrics, and stay updated with the latest market movements through an intuitive dashboard and robust API services.
image: https://discolike.com/images/og-image-default.jpg
layout: provider
modified: '2026-11-05'
name: DiscoLike
nav: Providers
network: true
overview: 'DiscoLike is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Market Intelligence, Data Aggregation, API Platform, and Competitive Analysis.


  DiscoLike''s developer surface includes CLI, authentication, pricing, engineering blog, getting-started guide, documentation, API reference, and 14 more developer resources.'
plans:
- name: Discolike Com Plans Pricing
  plan_count: 5
  slug: discolike-com-plans-pricing
random_paper: 19
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Discolike Com Authentication
  slug: discolike-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Discolike Com Domain Security
  slug: discolike-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: discolike-com
tags:
- Company
- Market Intelligence
- Data Aggregation
- API Platform
- Competitive Analysis
website: https://discolike.com/
---
