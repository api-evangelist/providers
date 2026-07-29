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
- acting_count: 5
  human_in_the_loop: 0
  name: Circlecis Agentic Access
  operation_count: 9
  slug: circlecis-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 8
apis:
- description: The CircleCI Runner API is used for the management and execution of self-hosted runner jobs.
  name: CircleCI Self-Hosted Runner API
  slug: runner-api
- description: Real-time event notifications for pipeline, workflow, and job lifecycle events delivered via HTTP callbacks.
  name: CircleCI Webhooks
  slug: webhooks
- description: Operations for organization contexts.
  name: CircleCI Context API
  slug: circlecis-context-api
- description: Job inspection and cancellation.
  name: CircleCI Job API
  slug: circlecis-job-api
- description: Pipeline trigger and inspection.
  name: CircleCI Pipeline API
  slug: circlecis-pipeline-api
- description: Project-scoped operations.
  name: CircleCI Project API
  slug: circlecis-project-api
- description: Current user information.
  name: CircleCI User API
  slug: circlecis-user-api
- description: Workflow inspection and cancellation.
  name: CircleCI Workflow API
  slug: circlecis-workflow-api
artifact_total: 17
collections:
- collection_type: open
  name: CircleCI REST API V2
  slug: open-circlecis
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/circlecis-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/circlecis-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/circlecis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/circlecis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/circlecis-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://circleci.com/blog/feed.xml
created: '2025-01-08'
description: CircleCI is a continuous integration and delivery platform that automates software building, testing, and deployment. This repository is an alias of the primary `circleci` index and is preserved so historical references and links continue to resolve. The full set of REST, runner, webhook, and orbs APIs is profiled in the `circleci` repository at https://github.com/api-evangelist/circleci.
finops:
- name: Circlecis Finops
  service_category: API
  slug: circlecis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/circlecis.png
layout: provider
modified: '2026-05-19'
name: CircleCI
nav: Providers
network: true
overview: 'CircleCI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Context API, Job API, Pipeline API, and 3 more. Tagged areas include CI/CD, Continuous Deployment, Continuous Integration, DevOps, and Pipelines.


  CircleCI''s developer surface includes authentication, engineering blog, and 4 more developer resources.'
plans:
- name: Circlecis Plans Pricing
  plan_count: 3
  slug: circlecis-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Circlecis Rate Limits
  slug: circlecis-rate-limits
score:
  band: thin
  composite: 37.3
  delta: -1.8
  facets:
    commercial_clarity: 47.4
    contract_quality: 58.5
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/circlecis/refs/heads/main/screenshots/circlecis-2026-06-20T174349.png
security:
- kind: authentication
  name: Circlecis Authentication
  slug: circlecis-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Circlecis Domain Security
  slug: circlecis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Circlecis Vulnerability Disclosure
  slug: circlecis-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Circlecis Trust Center
  slug: circlecis-trust-center
  summary_line: SOC 2, FedRAMP, GDPR, CSA STAR
slug: circlecis
tags:
- CI/CD
- Continuous Deployment
- Continuous Integration
- DevOps
- Pipelines
- Workflows
---
