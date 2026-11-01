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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: SensorUp provides GraphQL and MCP APIs for emissions management, asset tracking, and industrial IoT data integration.
  name: SensorUp Solutions API
  slug: sensorup-solutions-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.sensorup.com/security/
- group: auth
  href: https://artifacts.apis.io/sensorup-inc/authentication/sensorup-inc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sensorup-inc-authentication.yml
- group: agent
  href: https://artifacts.apis.io/sensorup-inc/llms/sensorup-inc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sensorup-inc-llms.txt
- group: agent
  href: https://artifacts.apis.io/sensorup-inc/well-known/sensorup-inc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sensorup-inc-well-known.yml
- group: other
  href: https://artifacts.apis.io/sensorup-inc/hosts/sensorup-inc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sensorup-inc-hosts.yml
- group: other
  href: https://artifacts.apis.io/sensorup-inc/vendors/sensorup-inc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sensorup-inc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sensorup.com/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://www.sensorup.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sensorup.com/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.sensorup.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.sensorup.com/releases/2026-06-16
- group: company
  title: ''
  type: Blog
  url: https://www.sensorup.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sensorup.com/use-sensorup/getting-started/platform-overview
- group: docs
  title: ''
  type: Documentation
  url: https://dev.sensorup.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SensorUp
- group: auth
  href: https://artifacts.apis.io/sensorup-inc/security/sensorup-inc-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sensorup-inc-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/sensorup-inc/security/sensorup-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sensorup-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.sensorup.com
coverage:
  checked: '2026-10-23'
  detail: GraphQL API requires POST introspection which is blocked by provider documentation.
  evidence:
  - status: 200
    url: https://docs.sensorup.com/api/graphql/overview
  reason: partner-login
  state: gated
created: '2026-10-23'
description: SensorUp provides an industrial IoT platform that enables heavy industry teams to manage governed records, shape tools, and integrate sensor data across assets. The platform offers a unified data model, real‑time analytics, and secure APIs for device onboarding, data ingestion, and asset management, helping manufacturers accelerate digital transformation and operational efficiency.
image: https://www.sensorup.com/og-default.png
layout: provider
modified: '2026-10-23'
name: SensorUp Inc.
nav: Providers
network: true
overview: 'SensorUp Inc. is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Industrial, DataPlatform, and Manufacturing.


  SensorUp Inc.''s developer surface includes authentication, changelog, engineering blog, getting-started guide, documentation, and 13 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 57.1
    operational_transparency: 31.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sensorup Inc Authentication
  slug: sensorup-inc-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Sensorup Inc Domain Security
  slug: sensorup-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sensorup Inc Trust Center
  slug: sensorup-inc-trust-center
  summary_line: SOC 2, ISO 27001
slug: sensorup-inc
tags:
- Company
- IoT
- Industrial
- DataPlatform
- Manufacturing
website: http://www.sensorup.com
---
