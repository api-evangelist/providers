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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Lytics Agentic Access
  operation_count: 19
  slug: lytics-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 7
apis:
- description: Manage Lytics accounts and retrieve account information
  name: Lytics Accounts API
  slug: lytics-accounts-api
- description: Manage data source and destination connections
  name: Lytics Connections API
  slug: lytics-connections-api
- description: Manage data models and stream schemas
  name: Lytics Datamodels API
  slug: lytics-datamodels-api
- description: Look up unified user profiles by field value
  name: Lytics Entity API
  slug: lytics-entity-api
- description: Orchestrate and monitor background data jobs
  name: Lytics Jobs API
  slug: lytics-jobs-api
- description: Query and scan behavioral audience segments
  name: Lytics Segments API
  slug: lytics-segments-api
- description: Trigger background workflow operations
  name: Lytics Work API
  slug: lytics-work-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lytics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lytics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lytics-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.lytics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lytics.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/lytics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lytics
- group: company
  title: ''
  type: Blog
  url: https://www.lytics.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lytics.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://lytics.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://x.com/lyticsio
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lytics.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.lytics.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/lytics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lytics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lytics-finops.yml
created: '2026-06-13'
description: Lytics is a customer data platform (CDP) that provides a REST API for managing unified user profiles, behavioral segments, content affinity scoring, campaigns, and real-time personalization integrations. The platform enables marketers to ingest data from 100+ sources, build predictive audiences, and activate them across advertising networks, email providers, data warehouses, and on-site personalization tools.
examples:
- key_count: 7
  name: Lytics Collect Event Example
  slug: lytics-collect-event-example
- key_count: 1
  name: Lytics Segment Scan Request Example
  slug: lytics-segment-scan-request-example
- key_count: 5
  name: Lytics Segment Scan Response Example
  slug: lytics-segment-scan-response-example
- key_count: 11
  name: Lytics User Profile Example
  slug: lytics-user-profile-example
finops:
- name: Lytics Finops
  service_category: ''
  slug: lytics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lytics.png
json_schemas:
- name: Lytics Collect Event
  property_count: 7
  slug: lytics-collect-event
- name: Lytics Segment
  property_count: 10
  slug: lytics-segment
- name: Lytics User Profile
  property_count: 11
  slug: lytics-user-profile
jsonld:
- class_count: 8
  name: Lytics Context
  property_count: 32
  slug: lytics-context
layout: provider
modified: '2026-06-13'
name: Lytics
nav: Providers
network: true
overview: 'Lytics publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Connections API, Datamodels API, and 4 more. Tagged areas include Customer Data Platform, CDP, Personalization, Segmentation, and User Profiles.


  The Lytics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lytics'' developer surface includes authentication, documentation, engineering blog, pricing, changelog, support, and 10 more developer resources.'
plans:
- name: Lytics Plans Pricing
  plan_count: 3
  slug: lytics-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 0
  name: Lytics Rate Limits
  slug: lytics-rate-limits
rules:
- name: Lytics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lytics-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.3
  delta: -0.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.7
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lytics/refs/heads/main/screenshots/lytics-2026-06-20T184816.png
security:
- kind: authentication
  name: Lytics Authentication
  slug: lytics-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Lytics Domain Security
  slug: lytics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lytics
tags:
- Customer Data Platform
- CDP
- Personalization
- Segmentation
- User Profiles
- Behavioral Analytics
- Content Affinity
- Real-Time Data
- Marketing Automation
- Audience Activation
website: https://www.lytics.com/
---
