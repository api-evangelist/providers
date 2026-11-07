---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: GetXAPI provides Twitter/X data access via REST API.
  name: GetXAPI
  slug: getxapi
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/getxapi/plans/getxapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getxapi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/getxapi/vocabulary/getxapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/getxapi-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/getxapi/conventions/getxapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/getxapi-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://www.getxapi.com/privacy-and-data-handling
- group: auth
  href: https://artifacts.apis.io/getxapi/authentication/getxapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getxapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/getxapi/conformance/getxapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getxapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/getxapi/llms/getxapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getxapi-llms.txt
- group: other
  href: https://artifacts.apis.io/getxapi/a2a/getxapi-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/getxapi-a2a.yml
- group: auth
  href: https://artifacts.apis.io/getxapi/well-known/getxapi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getxapi-security.txt
- group: auth
  href: https://artifacts.apis.io/getxapi/well-known/getxapi-getxapi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getxapi-getxapi-security.txt
- group: agent
  href: https://artifacts.apis.io/getxapi/well-known/getxapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getxapi-well-known.yml
- group: other
  href: https://artifacts.apis.io/getxapi/hosts/getxapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getxapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/getxapi/vendors/getxapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getxapi-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getxapi.com/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://www.getxapi.com/status
- group: company
  title: ''
  type: Newsroom
  url: https://www.getxapi.com/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.getxapi.com/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.getxapi.com\
- group: auth
  href: https://artifacts.apis.io/getxapi/security/getxapi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/getxapi-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/getxapi/security/getxapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getxapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getxapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getxapi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getxapi.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.getxapi.com/signup
- group: operate
  title: ''
  type: Support
  url: https://www.getxapi.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.getxapi.com/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getxapi
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getxapi.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getxapi.com/privacy-and-data-handling
created: '2026-10-17'
description: GetXAPI provides affordable access to Twitter (X) data through a suite of tools and APIs. It offers low‑cost pricing ($0.05 per 1K Tweets) and features such as ID conversion, shadowban checking, fake follower detection, thread reading, and webhook support. The platform includes documentation, pricing tables, a blog, and an MCP server for monitoring. It targets developers and businesses needing scalable Twitter data without official API constraints.
image: https://www.getxapi.com/og/home.png
layout: provider
modified: '2026-10-17'
name: GetXAPI
nav: Providers
network: true
overview: 'GetXAPI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Twitter, Tools, and Documentation.


  GetXAPI''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 22 more developer resources.'
plans:
- name: Getxapi Plans Pricing
  plan_count: 1
  slug: getxapi-plans-pricing
random_paper: 10
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 41.3
    catalog_earned_first_party: 8.0
    catalog_gap: 73.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 36.8
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 34.5
    discoverability: 65.2
    operational_transparency: 23.7
  previous_composite: 38.0
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/getxapi/getxapi-2026-11-03T132815.png
security:
- kind: authentication
  name: Getxapi Authentication
  slug: getxapi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Getxapi Domain Security
  slug: getxapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Getxapi Vulnerability Disclosure
  slug: getxapi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: getxapi
tags:
- Company
- Twitter
- Tools
- Documentation
website: https://www.getxapi.com/
---
