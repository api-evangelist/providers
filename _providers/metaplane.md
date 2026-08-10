---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Metaplane Agentic Access
  operation_count: 22
  slug: metaplane-agentic-access
  summary_line: 22 operations · 16 acting
api_count: 5
apis:
- description: Metaplane is a data observability platform providing automated anomaly detection and data quality monitoring.
  name: Metaplane
  slug: metaplane
- description: The Connections API from Metaplane — 4 operation(s) for connections.
  name: Metaplane Connections API
  slug: metaplane-connections-api
- description: The Datapoints API from Metaplane — 1 operation(s) for datapoints.
  name: Metaplane Datapoints API
  slug: metaplane-datapoints-api
- description: The Monitors API from Metaplane — 10 operation(s) for monitors.
  name: Metaplane Monitors API
  slug: metaplane-monitors-api
- description: The Tags API from Metaplane — 7 operation(s) for tags.
  name: Metaplane Tags API
  slug: metaplane-tags-api
artifact_total: 13
collections:
- collection_type: open
  name: Metaplane API
  slug: open-metaplane
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metaplane-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/metaplane-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metaplane-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metaplane-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metaplane
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/metaplane
- group: company
  title: ''
  type: Website
  url: https://www.metaplane.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metaplane.dev
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.metaplane.dev/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.metaplane.dev/blog/rss.xml
created: '2026-03-27'
description: Metaplane is a data observability platform providing automated anomaly detection and data quality monitoring.
finops:
- name: Metaplane Finops
  service_category: API
  slug: metaplane-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metaplane.png
layout: provider
modified: '2026-03-27'
name: Metaplane
nav: Providers
network: true
overview: 'Metaplane publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Connections API, Datapoints API, Monitors API, and 1 more. Tagged areas include AIOps and Data Observability.


  Metaplane''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Metaplane Plans Pricing
  plan_count: 3
  slug: metaplane-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Metaplane Rate Limits
  slug: metaplane-rate-limits
score:
  band: thin
  composite: 36.8
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 54.3
    developer_ergonomics: 21.7
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metaplane/refs/heads/main/screenshots/metaplane-2026-06-20T185251.png
security:
- kind: authentication
  name: Metaplane Authentication
  slug: metaplane-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Metaplane Domain Security
  slug: metaplane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Metaplane Trust Center
  slug: metaplane-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: metaplane
tags:
- AIOps
- Data Observability
website: https://www.metaplane.dev
---
