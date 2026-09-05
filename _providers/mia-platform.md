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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Mia-Platform is an Internal Developer Platform that harmonizes infrastructure, applications, and data for intelligent engineering at scale, enabling teams to build and deploy cloud-native applications
  name: Mia-Platform
  slug: mia-platform
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mia-platform-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mia-platform
- group: company
  title: ''
  type: Website
  url: https://mia-platform.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mia-platform.eu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mia-platform
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/mia-platform/console-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.mia-platform.eu/llms.txt
- group: company
  title: ''
  type: BlogRSS
  url: https://mia-platform.eu/blog/feed/
created: '2025-08-19'
description: Mia-Platform is an Internal Developer Platform (IDP) that harmonizes infrastructure, applications, and data for intelligent engineering at scale. It provides an API-first platform for building and managing microservices and cloud-native applications.
finops:
- name: Mia Platform Finops
  service_category: API
  slug: mia-platform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mia-platform.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Mia-Platform
nav: Providers
network: true
overview: 'Mia-Platform publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud-Native, Developer Platform, DevOps, IDP, and Microservices.


  Mia-Platform''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Mia Platform Plans Pricing
  plan_count: 3
  slug: mia-platform-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Mia Platform Rate Limits
  slug: mia-platform-rate-limits
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mia-platform/refs/heads/main/screenshots/mia-platform-2026-06-20T185328.png
security:
- kind: domain-security
  name: Mia Platform Domain Security
  slug: mia-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mia-platform
tags:
- Cloud-Native
- Developer Platform
- DevOps
- IDP
- Microservices
website: https://mia-platform.eu/
---
