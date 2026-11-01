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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Loki Agentic Access
  operation_count: 27
  slug: loki-agentic-access
  summary_line: 27 operations · 7 acting
api_count: 5
apis:
- baseURL: http://localhost:3100
  baseurl_source: spec
  description: The Config API from Loki — 1 operation(s) for config.
  name: Loki Config API
  slug: loki-config-api
- baseURL: http://localhost:3100
  baseurl_source: spec
  description: The Loki API from Loki — 17 operation(s) for loki.
  name: Loki API
  slug: loki-loki-api
- baseURL: http://localhost:3100
  baseurl_source: spec
  description: The Metrics API from Loki — 1 operation(s) for metrics.
  name: Loki Metrics API
  slug: loki-metrics-api
- baseURL: http://localhost:3100
  baseurl_source: spec
  description: The Otlp API from Loki — 1 operation(s) for otlp.
  name: Loki Otlp API
  slug: loki-otlp-api
- baseURL: http://localhost:3100
  baseurl_source: spec
  description: The Ready API from Loki — 1 operation(s) for ready.
  name: Loki Ready API
  slug: loki-ready-api
artifact_total: 17
collections:
- collection_type: open
  name: Loki HTTP Config API
  slug: open-loki-config-api
- collection_type: open
  name: HTTP Config Loki API
  slug: open-loki-loki-api
- collection_type: open
  name: Loki HTTP Config Metrics API
  slug: open-loki-metrics-api
- collection_type: open
  name: Loki HTTP Config Otlp API
  slug: open-loki-otlp-api
- collection_type: open
  name: Loki HTTP Config Ready API
  slug: open-loki-ready-api
- collection_type: open
  name: Loki HTTP API
  slug: open-loki
common:
- group: commercial
  href: https://artifacts.apis.io/loki/plans/loki-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/loki-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/loki/rate-limits/loki-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/loki-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/loki/finops/loki-finops.yml
  title: ''
  type: FinOps
  url: finops/loki-finops.yml
- group: other
  href: https://artifacts.apis.io/loki/capabilities/loki-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/loki-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/grafana/loki/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/grafana/loki/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/grafana/loki/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/grafana/loki/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/grafana/loki/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/loki/agentic-access/loki-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/loki-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/loki/security/loki-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/loki-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/loki/security/loki-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loki-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://grafana.com/oss/loki/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/loki/latest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/grafana
- group: company
  title: ''
  type: Blog
  url: https://grafana.com/blog/index.xml
created: '2026-03-25'
description: Loki is an open source log aggregation system from Grafana Labs designed to store and query logs efficiently using labels instead of full-text indexing.
finops:
- has_sources: false
  method: generated
  name: Loki Finops
  primary_unit: request
  service_category: API
  slug: loki-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loki.png
layout: provider
modified: '2026-09-16'
name: Loki
nav: Providers
network: true
overview: 'Loki is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Config API, Metrics API, and 3 more. Tagged areas include Logging, Observability, Open Source, and Grafana.


  Loki''s developer surface includes documentation, engineering blog, and 14 more developer resources.'
plans:
- name: Loki Plans Pricing
  plan_count: 3
  slug: loki-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Loki Rate Limits
  slug: loki-rate-limits
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 33.7
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 28.9
  previous_composite: 21.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/loki/loki-2026-06-20T184708.png
security:
- kind: domain-security
  name: Loki Domain Security
  slug: loki-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Loki Trust Center
  slug: loki-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FedRAMP, GDPR, CSA STAR
slug: loki
tags:
- Logging
- Observability
- Open Source
- Grafana
website: https://grafana.com/oss/loki/
---
