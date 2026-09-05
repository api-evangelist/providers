---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Open Liberty Agentic Access
  operation_count: 11
  slug: open-liberty-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- baseURL: https://localhost:9443
  baseurl_source: spec
  description: Server configuration management via Admin REST Connector.
  name: Open Liberty Configuration API
  slug: open-liberty-configuration-api
- baseURL: https://localhost:9443
  baseurl_source: spec
  description: MicroProfile Health check endpoints.
  name: Open Liberty Health API
  slug: open-liberty-health-api
- baseURL: https://localhost:9443
  baseurl_source: spec
  description: MicroProfile Metrics endpoints.
  name: Open Liberty Metrics API
  slug: open-liberty-metrics-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Open Liberty Admin REST API
  slug: open-open-liberty-admin
- collection_type: open
  name: Open Liberty Admin REST Configuration API
  slug: open-open-liberty-configuration-api
- collection_type: open
  name: Open Liberty Admin REST Configuration Health API
  slug: open-open-liberty-health-api
- collection_type: open
  name: Open Liberty Admin REST Configuration Metrics API
  slug: open-open-liberty-metrics-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-liberty-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-liberty-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/open-liberty-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://openliberty.io/
- group: docs
  title: ''
  type: Documentation
  url: https://openliberty.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://openliberty.io/start/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenLiberty
- group: company
  title: ''
  type: Blog
  url: https://openliberty.io/blog/
created: '2026-03-26'
description: Open Liberty is a lightweight, open source Java application server from IBM for building cloud-native microservices and applications with full support for Jakarta EE and MicroProfile.
finops:
- name: Open Liberty Finops
  service_category: API
  slug: open-liberty-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-liberty.png
json_schemas:
- name: Open Liberty Server Configuration
  property_count: 1
  slug: server-config
layout: provider
modified: '2026-05-19'
name: Open Liberty
nav: Providers
network: true
overview: 'Open Liberty publishes 3 APIs on the [APIs.io](https://apis.io/) network: Configuration API, Health API, and Metrics API. Tagged areas include Application Server, Cloud-Native, IBM, Jakarta EE, and Java.


  The Open Liberty catalog on APIs.io includes 1 Spectral governance ruleset.


  Open Liberty''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 4 more developer resources.'
plans:
- name: Open Liberty Plans Pricing
  plan_count: 3
  slug: open-liberty-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Open Liberty Rate Limits
  slug: open-liberty-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Open Liberty API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: open-liberty-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 45.3
    catalog_earned_first_party: 0.0
    catalog_gap: 69.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 51.2
    developer_ergonomics: 35.7
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-liberty/refs/heads/main/screenshots/open-liberty-2026-06-20T190837.png
security:
- kind: authentication
  name: Open Liberty Authentication
  slug: open-liberty-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Open Liberty Domain Security
  slug: open-liberty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: open-liberty
tags:
- Application Server
- Cloud-Native
- IBM
- Jakarta EE
- Java
- MicroProfile
- Microservices
website: https://openliberty.io/
---
