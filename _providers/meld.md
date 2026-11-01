---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 67.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Meld Agentic Access
  operation_count: 9
  slug: meld-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api-sb.meld.io
  baseurl_source: spec
  description: The Headless API from Meld.io — 4 operation(s) for headless.
  name: Meld.io Headless API
  slug: meld-headless-api
- baseURL: https://api-sb.meld.io
  baseurl_source: spec
  description: The Retail Ramp API from Meld.io — 5 operation(s) for retail ramp.
  name: Meld.io Retail Ramp API
  slug: meld-retail-ramp-api
artifact_total: 8
asyncapis:
- description: ''
  name: Meld Webhooks
  slug: meld-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/meld/agentic-access/meld-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/meld-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/meld/rules/meld-rules.yml
  title: ''
  type: Spectral
  url: rules/meld-rules.yml
- group: design
  href: https://artifacts.apis.io/meld/json-ld/meld-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/meld-context.jsonld
- group: design
  href: https://artifacts.apis.io/meld/vocabulary/meld-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/meld-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/meld/asyncapi/meld-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/meld-webhooks.yml
- group: design
  href: https://artifacts.apis.io/meld/data-model/meld-data-model.yml
  title: ''
  type: DataModel
  url: data-model/meld-data-model.yml
- group: design
  href: https://artifacts.apis.io/meld/conventions/meld-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/meld-conventions.yml
- group: design
  href: https://artifacts.apis.io/meld/conventions/meld-conventions.yml
  title: ''
  type: Conventions
  url: conventions/meld-conventions.yml
- group: start
  href: https://artifacts.apis.io/meld/sandbox/meld-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/meld-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/meld/authentication/meld-authentication.yml
  title: ''
  type: Authentication
  url: authentication/meld-authentication.yml
- group: design
  href: https://artifacts.apis.io/meld/lifecycle/meld-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/meld-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/meld/errors/meld-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/meld-problem-types.yml
- group: design
  href: https://artifacts.apis.io/meld/conformance/meld-conformance.yml
  title: ''
  type: Conformance
  url: conformance/meld-conformance.yml
- group: agent
  href: https://artifacts.apis.io/meld/llms/meld-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/meld-llms.txt
- group: other
  href: https://artifacts.apis.io/meld/a2a/meld-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/meld-a2a.yml
- group: agent
  href: https://artifacts.apis.io/meld/well-known/meld-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/meld-well-known.yml
- group: other
  href: https://artifacts.apis.io/meld/hosts/meld-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meld-hosts.yml
- group: other
  href: https://artifacts.apis.io/meld/vendors/meld-vendors.yml
  title: ''
  type: Vendors
  url: vendors/meld-vendors.yml
- group: auth
  href: https://artifacts.apis.io/meld/security/meld-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meld-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.meld.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.meld.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.meld.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.meld.io/docs/meld-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.meld.io/docs/meld-api/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.meld.io/contact?type=general
- group: company
  title: ''
  type: Blog
  url: https://www.meld.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meld.io/policy/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meld.io/policy/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meld.io/partner-application
created: '2026-10-21'
description: Meld.io provides a modern data integration platform that enables businesses to connect, transform, and orchestrate data flows across a wide variety of sources and destinations. The platform offers real-time streaming, batch processing, and powerful transformation capabilities, all accessible via a robust RESTful API. Meld.io focuses on security, scalability, and ease of use, allowing developers to build data pipelines quickly while maintaining compliance with industry standards. With extensive documentation, SDKs, and support, Meld.io aims to simplify complex data integration challenges for enterprises of all sizes.
image: https://meld.io/images/meld-icon-wordmark.png
jsonld:
- class_count: 118
  name: Meld Context
  property_count: 219
  slug: meld-context
layout: provider
modified: '2026-10-21'
name: Meld.io
nav: Providers
network: true
overview: 'Meld.io publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Headless API and Retail Ramp API. Tagged areas include Data Integration, FinTech, API Platform, Stablecoin, and Digital Assets.


  The Meld.io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Meld.io''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 22 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Meld.io API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: meld-rules
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 43.8
    catalog_earned_first_party: 0.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 67.7
    developer_ergonomics: 64.3
    discoverability: 48.2
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: unknown
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
  name: Meld Authentication
  slug: meld-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Meld Domain Security
  slug: meld-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: meld
tags:
- Data Integration
- FinTech
- API Platform
- Stablecoin
- Digital Assets
- Enterprise
website: https://www.meld.io/
---
