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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Loki Agentic Access
  operation_count: 27
  slug: loki-agentic-access
  summary_line: 27 operations · 8 acting
api_count: 5
apis:
- description: The Config API from Loki — 1 operation(s) for config.
  name: Loki Config API
  slug: loki-config-api
- description: The Loki API from Loki — 17 operation(s) for loki.
  name: Loki Loki API
  slug: loki-loki-api
- description: The Metrics API from Loki — 1 operation(s) for metrics.
  name: Loki Metrics API
  slug: loki-metrics-api
- description: The Otlp API from Loki — 1 operation(s) for otlp.
  name: Loki Otlp API
  slug: loki-otlp-api
- description: The Ready API from Loki — 1 operation(s) for ready.
  name: Loki Ready API
  slug: loki-ready-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: AgenticAccess
  url: agentic-access/loki-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/loki-trust-center.yml
- group: auth
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
- name: Loki Finops
  service_category: API
  slug: loki-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loki.png
layout: provider
modified: '2026-05-19'
name: Loki
nav: Providers
network: true
overview: 'Loki publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Config API, Loki API, Metrics API, and 2 more. Tagged areas include Logging, Observability, Open-Source, and Grafana.


  Loki''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Loki Plans Pricing
  plan_count: 3
  slug: loki-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Loki Rate Limits
  slug: loki-rate-limits
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 37.4
    developer_ergonomics: 11.9
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 65.0
  previous_composite: 28.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loki/refs/heads/main/screenshots/loki-2026-06-20T184708.png
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
- Open-Source
- Grafana
website: https://grafana.com/oss/loki/
---
