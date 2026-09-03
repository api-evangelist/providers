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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-02'
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
- baseURL: https://circleci.com/api/v2
  baseurl_source: spec
  description: Operations for organization contexts.
  name: CircleCI Context API
  slug: circlecis-context-api
- baseURL: https://circleci.com/api/v2
  baseurl_source: spec
  description: Job inspection and cancellation.
  name: CircleCI Job API
  slug: circlecis-job-api
- baseURL: https://circleci.com/api/v2
  baseurl_source: spec
  description: Pipeline trigger and inspection.
  name: CircleCI Pipeline API
  slug: circlecis-pipeline-api
- baseURL: https://circleci.com/api/v2
  baseurl_source: spec
  description: Project-scoped operations.
  name: CircleCI Project API
  slug: circlecis-project-api
- baseURL: https://circleci.com/api/v2
  baseurl_source: spec
  description: Current user information.
  name: CircleCI User API
  slug: circlecis-user-api
- baseURL: https://circleci.com/api/v2
  baseurl_source: spec
  description: Workflow inspection and cancellation.
  name: CircleCI Workflow API
  slug: circlecis-workflow-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CircleCI REST API V2 Context API
  slug: open-circlecis-context-api
- collection_type: open
  name: CircleCI REST API V2 Context Job API
  slug: open-circlecis-job-api
- collection_type: open
  name: CircleCI REST API V2 Context Pipeline API
  slug: open-circlecis-pipeline-api
- collection_type: open
  name: CircleCI REST API V2 Context Project API
  slug: open-circlecis-project-api
- collection_type: open
  name: CircleCI REST API V2 Context User API
  slug: open-circlecis-user-api
- collection_type: open
  name: CircleCI REST API V2 Context Workflow API
  slug: open-circlecis-workflow-api
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
random_paper: 0
rate_limits:
- limit_count: 5
  name: Circlecis Rate Limits
  slug: circlecis-rate-limits
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 23.8
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 31.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
