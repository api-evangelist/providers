---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Dropwizard Agentic Access
  operation_count: 7
  slug: dropwizard-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: JVM diagnostic endpoints.
  name: Dropwizard Diagnostics API
  slug: dropwizard-diagnostics-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: Health check and liveness endpoints.
  name: Dropwizard Health API
  slug: dropwizard-health-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: Application metrics endpoints.
  name: Dropwizard Metrics API
  slug: dropwizard-metrics-api
- baseURL: http://localhost:8081
  baseurl_source: spec
  description: Administrative task execution endpoints.
  name: Dropwizard Tasks API
  slug: dropwizard-tasks-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dropwizard Admin API
  slug: open-dropwizard-admin
- collection_type: open
  name: Dropwizard Admin Diagnostics API
  slug: open-dropwizard-diagnostics-api
- collection_type: open
  name: Dropwizard Admin Diagnostics Health API
  slug: open-dropwizard-health-api
- collection_type: open
  name: Dropwizard Admin Diagnostics Metrics API
  slug: open-dropwizard-metrics-api
- collection_type: open
  name: Dropwizard Admin Diagnostics Tasks API
  slug: open-dropwizard-tasks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dropwizard-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dropwizard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dropwizard.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dropwizard.io/en/stable/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dropwizard.io/en/stable/getting-started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dropwizard
created: '2026-03-26'
description: Dropwizard is a Java framework for developing ops-friendly, high-performance RESTful web services, pulling together stable, mature libraries from the Java ecosystem into a simple, lightweight package.
finops:
- name: Dropwizard Finops
  service_category: API
  slug: dropwizard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dropwizard.png
json_schemas:
- name: Dropwizard Configuration
  property_count: 4
  slug: dropwizard-config
layout: provider
modified: '2026-05-19'
name: Dropwizard
nav: Providers
network: true
overview: 'Dropwizard publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Diagnostics API, Health API, Metrics API, and 1 more. Tagged areas include API Development, Frameworks, Java, Microservices, and REST.


  The Dropwizard catalog on APIs.io includes 1 Spectral governance ruleset.


  Dropwizard''s developer surface includes documentation, getting-started guide, and 4 more developer resources.'
plans:
- name: Dropwizard Plans Pricing
  plan_count: 3
  slug: dropwizard-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Dropwizard Rate Limits
  slug: dropwizard-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Dropwizard API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dropwizard-jsonschema-spectral-rules
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 50.3
    catalog_earned_first_party: 0.0
    catalog_gap: 64.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 47.3
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 27.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dropwizard/refs/heads/main/screenshots/dropwizard-2026-06-20T180247.png
security:
- kind: domain-security
  name: Dropwizard Domain Security
  slug: dropwizard-domain-security
  summary_line: TLSv1.3
slug: dropwizard
tags:
- API Development
- Frameworks
- Java
- Microservices
- REST
- Web Services
website: https://www.dropwizard.io/
---
