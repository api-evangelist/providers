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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Panorama Agentic Access
  operation_count: 7
  slug: panorama-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 3
apis:
- description: Panorama XML/REST API for centralized network security management across Palo Alto Networks firewalls.
  name: Panorama API
  slug: panorama
- description: The Panorama API API from Panorama — 1 operation(s) for panorama api.
  name: Panorama Panorama API API
  slug: panorama-panorama-api-api
- description: The Restapi API from Panorama — 3 operation(s) for restapi.
  name: Panorama Restapi API
  slug: panorama-restapi-api
artifact_total: 10
collections:
- collection_type: open
  name: Panorama API
  slug: open-panorama
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/panorama-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/panorama-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/panorama-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/panorama-ed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/panorama-education
- group: company
  title: ''
  type: Website
  url: https://www.paloaltonetworks.com/network-security/panorama
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paloaltonetworks.com/panorama
created: '2026-03-16'
description: Panorama is a centralized network security management platform by Palo Alto Networks that provides centralized policy management, device configuration, and logging across Palo Alto Networks firewalls and Prisma Access.
finops:
- name: Panorama Finops
  service_category: API
  slug: panorama-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/panorama.png
layout: provider
modified: '2026-04-28'
name: Panorama
nav: Providers
network: true
overview: 'Panorama publishes 2 APIs on the [APIs.io](https://apis.io/) network: Panorama API API and Restapi API. Tagged areas include Firewall Management, Network Security, and Palo Alto Networks.


  Panorama''s developer surface includes authentication, documentation, and 5 more developer resources.'
plans:
- name: Panorama Plans Pricing
  plan_count: 3
  slug: panorama-plans-pricing
random_paper: 87
rate_limits:
- limit_count: 5
  name: Panorama Rate Limits
  slug: panorama-rate-limits
score:
  band: thin
  composite: 34.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.4
    developer_ergonomics: 19.6
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/panorama/refs/heads/main/screenshots/panorama-2026-06-20T191341.png
security:
- kind: authentication
  name: Panorama Authentication
  slug: panorama-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Panorama Domain Security
  slug: panorama-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: panorama
tags:
- Firewall Management
- Network Security
- Palo Alto Networks
website: https://www.paloaltonetworks.com/network-security/panorama
---
