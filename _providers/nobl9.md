---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.7
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: REST API for retrieving service level objective status, error budget consumption, and reliability metrics programmatically. Authentication uses a Nobl9 access token.
  name: Nobl9 SLO Status API
  slug: slo-api
- description: REST API for creating and managing SLO annotations to contextualize reliability data with deployments, incidents, and operational events.
  name: Nobl9 Annotations API
  slug: annotations-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Blog
  url: https://www.nobl9.com/resources
- group: company
  title: ''
  type: BlogRSS
  url: https://www.nobl9.com/resources/rss.xml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nobl9/refs/heads/main/security/nobl9-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nobl9-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nobl9inc
- group: company
  title: ''
  type: Website
  url: https://www.nobl9.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nobl9.com
- group: docs
  title: ''
  type: API Documentation
  url: https://docs.nobl9.com/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nobl9.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.nobl9.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nobl9
- group: build
  title: ''
  type: GitHub SDK
  url: https://github.com/nobl9/nobl9-go
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.nobl9.com/llms.txt
created: '2026-05-11'
description: Nobl9 is a service-level objective (SLO) management platform that helps engineering and SRE teams define, measure, and act on reliability targets across cloud and observability tools. The platform aggregates data from Datadog, Prometheus, New Relic, Splunk, AWS CloudWatch, and other sources to compute error budgets and surface reliability insights. Nobl9 exposes a suite of REST APIs for managing SLOs, annotations, budget adjustments, audit logs, and reports using access token authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nobl9.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.nobl9.com over HTTP.
  name: Nobl9 MCP Server
  slug: nobl9
modified: '2026-10-06'
name: Nobl9
nav: Providers
network: true
overview: 'Nobl9 is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Reliability, SLO, SRE, Observability, and Error Budgets.


  Nobl9''s developer surface includes engineering blog, documentation, pricing, signup flow, and 8 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 75.0
    operational_transparency: 2.6
  previous_composite: 17.7
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/nobl9/refs/heads/main/screenshots/nobl9-2026-06-20T190350.png
security:
- kind: domain-security
  name: Nobl9 Domain Security
  slug: nobl9-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nobl9
tags:
- Reliability
- SLO
- SRE
- Observability
- Error Budgets
website: https://www.nobl9.com
---
