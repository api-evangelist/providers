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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Pulse Software Agentic Access
  operation_count: 29
  slug: pulse-software-agentic-access
  summary_line: 29 operations · 14 acting
api_count: 10
apis:
- description: The Pulse API is targeted towards developers looking to automate tasks in Pulse.
  name: Pulse Software
  slug: pulse-software
- description: Authentication for accessing Pulse Public API
  name: Pulse Software Authentication API
  slug: pulse-software-authentication-api
- description: API for managing CPR data in Pulse
  name: Pulse Software Corporate Planning API API
  slug: pulse-software-corporate-planning-api-api
- description: API for managing forms and records in Pulse
  name: Pulse Software Forms API API
  slug: pulse-software-forms-api-api
- description: API for managing learning info in Pulse
  name: Pulse Software Learning API API
  slug: pulse-software-learning-api-api
- description: API for managing project info in Pulse
  name: Pulse Software Project API API
  slug: pulse-software-project-api-api
- description: API for managing recruitment info in Pulse
  name: Pulse Software Recruitment API API
  slug: pulse-software-recruitment-api-api
- description: API for handling synchronisation data from and/or to Pulse including for managing sync history records
  name: Pulse Software Sync API API
  slug: pulse-software-sync-api-api
- description: API for managing user details in Pulse
  name: Pulse Software User Details API API
  slug: pulse-software-user-details-api-api
- description: API for managing user details in Pulse including additional attributes
  name: Pulse Software User Details API v2 API
  slug: pulse-software-user-details-api-v2-api
artifact_total: 17
collections:
- collection_type: open
  name: Pulse Public API
  slug: open-pulse-software
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pulse-software-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pulse-software-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pulse-software-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pulsesoftware
created: '2025-02-24'
description: The Pulse API is targeted towards developers looking to automate tasks in Pulse.
finops:
- name: Pulse Software Finops
  service_category: API
  slug: pulse-software-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pulse-software.png
layout: provider
modified: '2026-04-28'
name: Pulse Software
nav: Providers
network: true
overview: 'Pulse Software publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Corporate Planning API API, Forms API API, and 6 more. Tagged areas include Pulse, Automation, and Developer.


  Pulse Software''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Pulse Software Plans Pricing
  plan_count: 3
  slug: pulse-software-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Pulse Software Rate Limits
  slug: pulse-software-rate-limits
score:
  band: emerging
  composite: 26.9
  delta: -3.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pulse-software/refs/heads/main/screenshots/pulse-software-2026-06-20T192256.png
security:
- kind: authentication
  name: Pulse Software Authentication
  slug: pulse-software-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Pulse Software Domain Security
  slug: pulse-software-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pulse-software
tags:
- Pulse
- Automation
- Developer
---
