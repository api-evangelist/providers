---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 7
  human_in_the_loop: 0
  name: Akamai Technologies Agentic Access
  operation_count: 7
  slug: akamai-technologies-agentic-access
  summary_line: 7 operations · 7 acting
api_count: 4
apis:
- description: The Akamai Technologies API provides access to platform services and data for enterprise integration and automation.
  name: Akamai Technologies API
  slug: akamai-technologies-api
- description: Remove cached objects from the edge.
  name: Akamai Technologies Deletions API
  slug: akamai-technologies-deletions-api
- description: Mark cached objects as stale, forcing revalidation on next request.
  name: Akamai Technologies Invalidations API
  slug: akamai-technologies-invalidations-api
- description: Inspect rate-limit and object-limit status.
  name: Akamai Technologies Status API
  slug: akamai-technologies-status-api
artifact_total: 11
collections:
- collection_type: open
  name: Akamai Fast Purge (CCU v3) API
  slug: open-akamai-technologies
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/akamai-technologies-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/akamai-technologies-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/akamai-technologies-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/akamai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/akamai-technologies
- group: company
  title: ''
  type: Website
  url: https://www.akamai.com
created: '2026-04-19'
description: Akamai Technologies is a major US corporation and Fortune 1000 company. The Akamai Technologies API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Akamai Technologies Finops
  service_category: CDN + Edge + Cloud
  slug: akamai-technologies-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/akamai-technologies.png
layout: provider
modified: '2026-04-19'
name: Akamai Technologies
nav: Providers
network: true
overview: 'Akamai Technologies publishes 3 APIs on the [APIs.io](https://apis.io/) network: Deletions API, Invalidations API, and Status API. Tagged areas include CDN, Security, and Cloud.


  Akamai Technologies'' developer surface includes authentication and 5 more developer resources.'
plans:
- name: Akamai Technologies Plans Pricing
  plan_count: 4
  slug: akamai-technologies-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 3
  name: Akamai Technologies Rate Limits
  slug: akamai-technologies-rate-limits
score:
  band: thin
  composite: 35.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.4
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/akamai-technologies/refs/heads/main/screenshots/akamai-technologies-2026-06-20T171446.png
security:
- kind: authentication
  name: Akamai Technologies Authentication
  slug: akamai-technologies-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Akamai Technologies Domain Security
  slug: akamai-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: akamai-technologies
tags:
- CDN
- Security
- Cloud
website: https://www.akamai.com
---
