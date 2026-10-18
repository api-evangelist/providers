---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Unified API platform offering REST and GraphQL endpoints with authentication and rate limiting.
  name: EchoAPI Platform
  slug: echoapi-platform
- baseURL: https://httpbin.org
  baseurl_source: declared
  description: The Anything API from EchoAPI — 1 operation(s) for anything.
  name: EchoAPI Anything API
  slug: echoapi-anything-api
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/echoapi/refs/heads/main/plans/echoapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/echoapi-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/echoapi/refs/heads/main/rules/echoapi-rules.yml
  title: ''
  type: Spectral
  url: rules/echoapi-rules.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/echoapi/refs/heads/main/cli/echoapi-cli.yml
  title: ''
  type: CLI
  url: cli/echoapi-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/echoapi/refs/heads/main/changelog/echoapi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/echoapi-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/echoapi/refs/heads/main/authentication/echoapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/echoapi-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/echoapi/refs/heads/main/conformance/echoapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/echoapi-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/echoapi/refs/heads/main/hosts/echoapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/echoapi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/echoapi/refs/heads/main/vendors/echoapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/echoapi-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/echoapi-Team
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.echoapi.com/wiki/docs/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/echoapi/refs/heads/main/security/echoapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/echoapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.echoapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.echoapi.com/wiki/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.echoapi.com/wiki/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.echoapi.com/wiki/docs/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://www.echoapi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.echoapi.com/price
- group: start
  title: ''
  type: SignUp
  url: https://workspace.echoapi.com/user/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.echoapi.com/wiki/docs/termsofservice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.echoapi.com/wiki/docs/privacypolicy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.echoapi.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: EchoAPI provides a unified API platform that enables developers to integrate multiple services through a single, consistent interface. It offers robust authentication, rate limiting, and comprehensive documentation, allowing seamless connectivity to various data sources and functionalities. The platform is designed for scalability, security, and ease of use, supporting both RESTful and GraphQL endpoints, and includes SDKs for popular programming languages. EchoAPI aims to simplify API consumption and accelerate development cycles for businesses of all sizes.
image: https://assets.echoapi.com/assets/new_banner.png
layout: provider
modified: '2026-10-16'
name: EchoAPI
nav: Providers
network: true
overview: 'EchoAPI is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Anything API, and 1 more. Tagged areas include Company, API Platform, Integration, Developer Tools, and AI-powered.


  The EchoAPI catalog on APIs.io includes 1 Spectral governance ruleset.


  EchoAPI''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, engineering blog, and 13 more developer resources.'
plans:
- name: Echoapi Plans Pricing
  plan_count: 7
  slug: echoapi-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: EchoAPI API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: echoapi-rules
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 48.5
    catalog_earned_first_party: 12.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 10.7
    developer_ergonomics: 50.0
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Echoapi Authentication
  slug: echoapi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Echoapi Domain Security
  slug: echoapi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: echoapi
tags:
- Company
- API Platform
- Integration
- Developer Tools
- AI-powered
- Documentation
website: https://www.echoapi.com/
---
