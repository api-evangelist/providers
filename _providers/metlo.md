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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Metlo API provides API security capabilities as documented.
  name: Metlo API
  slug: metlo-api
artifact_total: 3
common:
- group: build
  href: https://artifacts.apis.io/metlo/cli/metlo-cli.yml
  title: ''
  type: CLI
  url: cli/metlo-cli.yml
- group: start
  href: https://artifacts.apis.io/metlo/sandbox/metlo-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/metlo-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/metlo/authentication/metlo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/metlo-authentication.yml
- group: agent
  href: https://artifacts.apis.io/metlo/llms/metlo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/metlo-llms.txt
- group: other
  href: https://artifacts.apis.io/metlo/a2a/metlo-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/metlo-a2a.yml
- group: agent
  href: https://artifacts.apis.io/metlo/well-known/metlo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/metlo-well-known.yml
- group: other
  href: https://artifacts.apis.io/metlo/hosts/metlo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/metlo-hosts.yml
- group: other
  href: https://artifacts.apis.io/metlo/vendors/metlo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/metlo-vendors.yml
- group: build
  href: https://artifacts.apis.io/metlo/packages/metlo-packages.yml
  title: ''
  type: SDKs
  url: packages/metlo-packages.yml
- group: build
  href: https://artifacts.apis.io/metlo/packages/metlo-packages.yml
  title: ''
  type: Packages
  url: packages/metlo-packages.yml
- group: auth
  href: https://artifacts.apis.io/metlo/security/metlo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/metlo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://metlo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.metlo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metlo.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.metlo.com/intro/getting-started.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metlo-labs
- group: start
  title: ''
  type: SignUp
  url: https://app.metlo.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metlo.com/terms
coverage:
  checked: '2026-10-20'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.metlo.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Metlo provides an API security platform that automatically discovers, monitors, and protects APIs in real time. It offers developers and security teams visibility into API traffic, detects anomalies, and enforces policies without requiring code changes. Metlo’s solution integrates with CI/CD pipelines, supports OpenAPI specifications, and provides detailed dashboards and alerts to help organizations secure their API surface. The company focuses on simplifying API security for modern cloud-native environments, enabling rapid detection of threats and compliance with industry standards. Metlo also offers a free tier and enterprise plans, extensive documentation, and SDKs for multiple languages.
layout: provider
modified: '2026-10-20'
name: Metlo
nav: Providers
network: true
overview: 'Metlo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Security, Cloud-Native, Real-Time Monitoring, OpenAPI, and CI/CD Integration.


  Metlo''s developer surface includes CLI, sandbox, authentication, documentation, getting-started guide, signup flow, and 12 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 48.8
    discoverability: 69.6
    operational_transparency: 2.6
  previous_composite: 25.3
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/metlo/metlo-2026-11-03T135542.png
security:
- kind: authentication
  name: Metlo Authentication
  slug: metlo-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Metlo Domain Security
  slug: metlo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: metlo
tags:
- API Security
- Cloud-Native
- Real-Time Monitoring
- OpenAPI
- CI/CD Integration
website: https://metlo.com/
---
