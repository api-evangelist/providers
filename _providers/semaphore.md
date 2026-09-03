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
  band: agent-ready
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
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 35
  human_in_the_loop: 3
  name: Semaphore Agentic Access
  operation_count: 59
  slug: semaphore-agentic-access
  summary_line: 59 operations · 35 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://{organization}.semaphoreci.com/api/v1alpha
  baseurl_source: declared
  description: Dashboard management
  name: Semaphore Dashboards API
  slug: semaphore-dashboards-api
- baseURL: https://{organization}.semaphoreci.com/api/v1alpha
  baseurl_source: declared
  description: Deployment target management
  name: Semaphore DeploymentTargets API
  slug: semaphore-deploymenttargets-api
- baseURL: https://{organization}.semaphoreci.com/api/v1alpha
  baseurl_source: declared
  description: Notification management
  name: Semaphore Notifications API
  slug: semaphore-notifications-api
- baseURL: https://{organization}.semaphoreci.com/api/v1alpha
  baseurl_source: declared
  description: Pipeline management
  name: Semaphore Pipelines API
  slug: semaphore-pipelines-api
- baseURL: https://{organization}.semaphoreci.com/api/v1alpha
  baseurl_source: declared
  description: Project management
  name: Semaphore Projects API
  slug: semaphore-projects-api
- baseURL: https://{organization}.semaphoreci.com/api/v1alpha
  baseurl_source: declared
  description: Project-level secrets
  name: Semaphore ProjectSecrets API
  slug: semaphore-projectsecrets-api
- baseURL: https://{organization}.semaphoreci.com/api/v1alpha
  baseurl_source: declared
  description: Organization-level secrets
  name: Semaphore Secrets API
  slug: semaphore-secrets-api
- baseURL: https://{organization}.semaphoreci.com/api/v1alpha
  baseurl_source: declared
  description: Self-hosted agent management
  name: Semaphore SelfHostedAgents API
  slug: semaphore-selfhostedagents-api
- baseURL: https://{organization}.semaphoreci.com/api/v1alpha
  baseurl_source: declared
  description: Self-hosted agent type management
  name: Semaphore SelfHostedAgentTypes API
  slug: semaphore-selfhostedagenttypes-api
- baseURL: https://{organization}.semaphoreci.com/api/v1alpha
  baseurl_source: declared
  description: Task management
  name: Semaphore Tasks API
  slug: semaphore-tasks-api
- baseURL: https://{organization}.semaphoreci.com/api/v1alpha
  baseurl_source: declared
  description: Workflow management
  name: Semaphore Workflows API
  slug: semaphore-workflows-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Semaphore Public Dashboards API
  slug: open-semaphore-dashboards-api
- collection_type: open
  name: Semaphore Public Dashboards DeploymentTargets API
  slug: open-semaphore-deploymenttargets-api
- collection_type: open
  name: Semaphore Public Dashboards Notifications API
  slug: open-semaphore-notifications-api
- collection_type: open
  name: Semaphore Public Dashboards Pipelines API
  slug: open-semaphore-pipelines-api
- collection_type: open
  name: Semaphore Public Dashboards Projects API
  slug: open-semaphore-projects-api
- collection_type: open
  name: Semaphore Public Dashboards ProjectSecrets API
  slug: open-semaphore-projectsecrets-api
- collection_type: open
  name: Semaphore Public Dashboards Secrets API
  slug: open-semaphore-secrets-api
- collection_type: open
  name: Semaphore Public Dashboards SelfHostedAgents API
  slug: open-semaphore-selfhostedagents-api
- collection_type: open
  name: Semaphore Public Dashboards SelfHostedAgentTypes API
  slug: open-semaphore-selfhostedagenttypes-api
- collection_type: open
  name: Semaphore Public Dashboards Tasks API
  slug: open-semaphore-tasks-api
- collection_type: open
  name: Semaphore Public Dashboards Workflows API
  slug: open-semaphore-workflows-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/semaphore-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/semaphore-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/semaphore-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/semaphore-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/semaphore-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://semaphore.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.semaphore.io
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/semaphoreci
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/semaphore-software
- group: company
  title: ''
  type: Blog
  url: https://semaphore.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://semaphore.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.semaphore.io
- group: other
  title: ''
  type: X
  url: https://twitter.com/semaphoreci
- group: commercial
  title: ''
  type: Plans
  url: plans/semaphore-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/semaphore-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/semaphore-finops.yml
created: '2026-06-12'
description: Semaphore is a cloud-based CI/CD platform designed for high-performance engineering teams, providing fast and reliable continuous integration and continuous delivery pipelines. The platform offers a comprehensive REST API that enables programmatic management of pipelines, workflows, jobs, secrets, projects, and deployment targets for software delivery automation. Semaphore supports OAS 3.0-compliant API definitions with Swagger documentation, covering resources such as artifacts, test results, self-hosted agents, and build insights. Teams can use the API to integrate with external tools, build custom interfaces, trigger promotions, and automate their entire software delivery lifecycle.
finops:
- name: Semaphore Finops
  service_category: ''
  slug: semaphore-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/semaphore.png
jsonld:
- class_count: 18
  name: Semaphore Context
  property_count: 18
  slug: semaphore-context
layout: provider
modified: '2026-06-12'
name: Semaphore
nav: Providers
network: true
overview: 'Semaphore publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Dashboards API, DeploymentTargets API, Notifications API, and 8 more. Tagged areas include CI/CD, Continuous Integration, Continuous Delivery, Pipelines, and Workflows.


  The Semaphore catalog on APIs.io includes 1 JSON-LD context.


  Semaphore''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Semaphore Plans Pricing
  plan_count: 4
  slug: semaphore-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 6
  name: Semaphore Rate Limits
  slug: semaphore-rate-limits
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 12
    catalog_gap: 35.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 15.2
    contract_quality: 65.3
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 15.2
    operational_transparency: 52.6
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/semaphore/refs/heads/main/screenshots/semaphore-2026-06-20T193644.png
security:
- kind: authentication
  name: Semaphore Authentication
  slug: semaphore-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Semaphore Domain Security
  slug: semaphore-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Semaphore Vulnerability Disclosure
  slug: semaphore-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Semaphore Trust Center
  slug: semaphore-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: semaphore
tags:
- CI/CD
- Continuous Integration
- Continuous Delivery
- Pipelines
- Workflows
- DevOps
- Build Automation
- Software Delivery
- Deployment
- Artifacts
website: https://semaphore.io
---
