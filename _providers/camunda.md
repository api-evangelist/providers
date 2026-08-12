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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Camunda Agentic Access
  operation_count: 23
  slug: camunda-agentic-access
  summary_line: 23 operations · 19 acting
api_count: 10
apis:
- description: The Cluster API from Camunda — 1 operation(s) for cluster.
  name: Camunda Cluster API
  slug: camunda-cluster-api
- description: The Decisions API from Camunda — 2 operation(s) for decisions.
  name: Camunda Decisions API
  slug: camunda-decisions-api
- description: The Deployments API from Camunda — 2 operation(s) for deployments.
  name: Camunda Deployments API
  slug: camunda-deployments-api
- description: The Incidents API from Camunda — 2 operation(s) for incidents.
  name: Camunda Incidents API
  slug: camunda-incidents-api
- description: The Jobs API from Camunda — 4 operation(s) for jobs.
  name: Camunda Jobs API
  slug: camunda-jobs-api
- description: The Messages API from Camunda — 1 operation(s) for messages.
  name: Camunda Messages API
  slug: camunda-messages-api
- description: The Process Definitions API from Camunda — 3 operation(s) for process definitions.
  name: Camunda Process Definitions API
  slug: camunda-process-definitions-api
- description: The Process Instances API from Camunda — 3 operation(s) for process instances.
  name: Camunda Process Instances API
  slug: camunda-process-instances-api
- description: The Signals API from Camunda — 1 operation(s) for signals.
  name: Camunda Signals API
  slug: camunda-signals-api
- description: The User Tasks API from Camunda — 3 operation(s) for user tasks.
  name: Camunda User Tasks API
  slug: camunda-user-tasks-api
artifact_total: 19
collections:
- collection_type: open
  name: Camunda 8 REST API
  slug: open-camunda-8-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/camunda-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/camunda-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/camunda-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/camunda-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/camunda-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/camunda
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/camunda
- group: company
  title: ''
  type: Website
  url: https://camunda.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.camunda.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.camunda.io/docs/apis-tools/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.camunda.io/docs/guides/
- group: company
  title: ''
  type: Blog
  url: https://camunda.com/blog/
- group: operate
  title: ''
  type: Community
  url: https://forum.camunda.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://camunda.com/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://camunda.com/legal/terms/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.camunda.io/llms.txt
created: '2026-03-16'
description: Camunda is a process orchestration platform that enables organizations to design, automate, and improve business processes using BPMN (Business Process Model and Notation). Camunda provides a complete solution for workflow automation, decision automation, and process monitoring.
finops:
- name: Camunda Finops
  service_category: API
  slug: camunda-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/camunda.png
layout: provider
modified: '2026-05-19'
name: Camunda
nav: Providers
network: true
overview: 'Camunda publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Cluster API, Decisions API, Deployments API, and 7 more. Tagged areas include BPMN, Business Process Management, Process Automation, and Workflow.


  Camunda''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 11 more developer resources.'
plans:
- name: Camunda Plans Pricing
  plan_count: 3
  slug: camunda-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 5
  name: Camunda Rate Limits
  slug: camunda-rate-limits
score:
  band: thin
  composite: 40.1
  delta: -7.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 56.0
    developer_ergonomics: 45.7
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/camunda/refs/heads/main/screenshots/camunda-2026-06-20T173920.png
security:
- kind: authentication
  name: Camunda Authentication
  slug: camunda-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Camunda Domain Security
  slug: camunda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Camunda Vulnerability Disclosure
  slug: camunda-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Camunda Trust Center
  slug: camunda-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, GDPR
slug: camunda
tags:
- BPMN
- Business Process Management
- Process Automation
- Workflow
website: https://camunda.com/
---
