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
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 6
  human_in_the_loop: 2
  name: Netflix Eureka Agentic Access
  operation_count: 13
  slug: netflix-eureka-agentic-access
  summary_line: 13 operations · 6 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: Query registered applications
  name: Netflix Eureka Applications API
  slug: netflix-eureka-applications-api
- description: Manage service instances
  name: Netflix Eureka Instances API
  slug: netflix-eureka-instances-api
- description: Virtual IP address based queries
  name: Netflix Eureka VIP API
  slug: netflix-eureka-vip-api
artifact_total: 8
collections:
- collection_type: open
  name: Netflix Eureka REST API
  slug: open-eureka-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/netflix-eureka-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/Netflix/eureka
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Netflix/eureka/wiki
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Netflix
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/Netflix/eureka/wiki/Getting-Started
- group: operate
  title: ''
  type: FAQ
  url: https://github.com/Netflix/eureka/wiki/Eureka-2.0-Motivations
- group: operate
  title: ''
  type: Issues
  url: https://github.com/Netflix/eureka/issues
created: '2026-03-26'
description: Netflix Eureka is a RESTful service registry used for service discovery, load balancing, and failover of middle-tier servers in microservice and cloud-native architectures, originally built for the AWS cloud.
finops:
- name: Netflix Eureka Finops
  service_category: API
  slug: netflix-eureka-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netflix-eureka.png
layout: provider
modified: '2026-05-19'
name: Netflix Eureka
nav: Providers
network: true
overview: 'Netflix Eureka publishes 3 APIs on the [APIs.io](https://apis.io/) network: Applications API, Instances API, and VIP API. Tagged areas include Cloud Native, Failover, Java, Load Balancing, and Microservices.


  Netflix Eureka''s developer surface includes documentation, getting-started guide, FAQ, and 4 more developer resources.'
plans:
- name: Netflix Eureka Plans Pricing
  plan_count: 3
  slug: netflix-eureka-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Netflix Eureka Rate Limits
  slug: netflix-eureka-rate-limits
score:
  band: emerging
  composite: 27.9
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 50.5
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 27.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netflix-eureka/refs/heads/main/screenshots/netflix-eureka-2026-06-20T190154.png
slug: netflix-eureka
tags:
- Cloud Native
- Failover
- Java
- Load Balancing
- Microservices
- Netflix
- Service Discovery
- Service Registry
---
