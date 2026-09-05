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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Jitsu Agentic Access
  operation_count: 4
  slug: jitsu-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- baseURL: https://use.jitsu.com
  baseurl_source: declared
  description: The Batch API from Jitsu — 2 operation(s) for batch.
  name: Jitsu Batch API
  slug: jitsu-batch-api
- baseURL: https://use.jitsu.com
  baseurl_source: declared
  description: The Ingestion API from Jitsu — 2 operation(s) for ingestion.
  name: Jitsu Ingestion API
  slug: jitsu-ingestion-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jitsu Event Ingestion Batch API
  slug: open-jitsu-batch-api
- collection_type: open
  name: Jitsu Event Batch Ingestion API
  slug: open-jitsu-ingestion-api
- collection_type: open
  name: Jitsu Event Ingestion API
  slug: open-jitsu
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jitsu-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/jitsu-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jitsu-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jitsu-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jitsucom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jitsu-com
- group: company
  title: ''
  type: Website
  url: https://jitsu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://jitsu.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/jitsu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jitsu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/jitsu-finops.yml
created: '2026-06-21'
description: Jitsu is an open-source, real-time event data pipeline and customer data platform (a Segment alternative). It collects events from websites, apps, and servers and streams them to data warehouses and other destinations. Jitsu is available as MIT-licensed self-hosted software (github.com/jitsucom/jitsu) and as a managed Jitsu Cloud (use.jitsu.com); both expose the same HTTP event ingestion API authenticated with a Write Key.
finops:
- name: Jitsu Finops
  service_category: Analytics
  slug: jitsu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jitsu.png
layout: provider
modified: '2026-06-21'
name: Jitsu
nav: Providers
network: true
overview: 'Jitsu publishes 2 APIs on the [APIs.io](https://apis.io/) network: Batch API and Ingestion API. Tagged areas include Event Data, CDP, Data Pipeline, Analytics, and Open-Source.


  Jitsu''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Jitsu Plans Pricing
  plan_count: 4
  slug: jitsu-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Jitsu Rate Limits
  slug: jitsu-rate-limits
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jitsu/refs/heads/main/screenshots/jitsu-2026-07-25T223202.png
security:
- kind: authentication
  name: Jitsu Authentication
  slug: jitsu-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Jitsu Domain Security
  slug: jitsu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Jitsu Trust Center
  slug: jitsu-trust-center
  summary_line: SOC 2, GDPR
slug: jitsu
tags:
- Event Data
- CDP
- Data Pipeline
- Analytics
- Open-Source
- Ingestion
website: https://jitsu.com/
---
