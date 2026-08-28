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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Cloudbees Agentic Access
  operation_count: 14
  slug: cloudbees-agentic-access
  summary_line: 14 operations · 5 acting
api_count: 12
apis:
- description: CloudBees CI is a hardened, enterprise distribution of Jenkins. The REST API is the Jenkins remote access API exposed at /api on every controller and on individual jobs, runs, queues and nodes. Caller
  name: CloudBees CI REST API
  slug: ci
- description: 'The CloudBees CD/RO (Continuous Delivery / Release Orchestration) REST API exposes resources for pipelines, releases, environments, applications, deployments, projects and resources. Operations cover '
  name: CloudBees CD/RO REST API
  slug: cd-ro
- description: The CloudBees Feature Management REST API (formerly Rollout) provides programmatic access to applications, environments, feature flags, experiments, target groups, audit logs, and users. Authenticatio
  name: CloudBees Feature Management REST API
  slug: feature-management
- description: CloudBees Unify is the modern, opinionated software delivery platform that unifies CI, CD, feature management, analytics, and security into a single workflow. The platform exposes APIs for managing or
  name: CloudBees Unify Platform API
  slug: unify
- description: The CloudBees CD plugin for Jenkins exposes Jenkins pipeline steps that call CloudBees CD/RO REST endpoints — triggering pipelines, running releases, deploying applications, and pulling artifacts from
  name: CloudBees CD/RO Jenkins Plugin Steps
  slug: jenkins-plugin
- description: The Computer API from CloudBees — 1 operation(s) for computer.
  name: CloudBees Computer API
  slug: cloudbees-computer-api
- description: The CreateItem API from CloudBees — 1 operation(s) for createitem.
  name: CloudBees CreateItem API
  slug: cloudbees-createitem-api
- description: The Job API from CloudBees — 7 operation(s) for job.
  name: CloudBees Job API
  slug: cloudbees-job-api
- description: The Json API from CloudBees — 1 operation(s) for json.
  name: CloudBees Json API
  slug: cloudbees-json-api
- description: The Python API from CloudBees — 1 operation(s) for python.
  name: CloudBees Python API
  slug: cloudbees-python-api
- description: The Queue API from CloudBees — 1 operation(s) for queue.
  name: CloudBees Queue API
  slug: cloudbees-queue-api
- description: The Xml API from CloudBees — 1 operation(s) for xml.
  name: CloudBees Xml API
  slug: cloudbees-xml-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer API
  slug: open-cloudbees-computer-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer CreateItem API
  slug: open-cloudbees-createitem-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer Job API
  slug: open-cloudbees-job-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer Json API
  slug: open-cloudbees-json-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer Python API
  slug: open-cloudbees-python-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer Queue API
  slug: open-cloudbees-queue-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer Xml API
  slug: open-cloudbees-xml-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible)
  slug: open-cloudbees
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudbees-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cloudbees-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudbees-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudbees-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudbees-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudbees
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudbees
- group: company
  title: ''
  type: Website
  url: https://www.cloudbees.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudbees.com/
- group: operate
  title: ''
  type: Support
  url: https://support.cloudbees.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudbees.com/privacy
- group: build
  title: ''
  type: Plugins
  url: https://docs.cloudbees.com/plugins/ci
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloudbees-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloudbees-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cloudbees.com/blog/rss.xml
created: '2025-01-08'
description: CloudBees provides software delivery automation across continuous integration, continuous deployment, release orchestration, and feature management. Their developer surface includes the CloudBees CI REST API (an extension of the Jenkins REST API), the CloudBees CD/RO REST API for release orchestration, the CloudBees Feature Management REST API (formerly Rollout) for feature flags and environments, and the CloudBees Unify Platform API for the modern unified delivery platform. APIs are generally JSON, token-authenticated, and follow REST conventions.
finops:
- name: Cloudbees Finops
  service_category: API
  slug: cloudbees-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudbees.png
jsonld:
- class_count: 0
  name: Cloudbees Context
  property_count: 11
  slug: cloudbees-context
layout: provider
modified: '2026-04-23'
name: CloudBees
nav: Providers
network: true
overview: 'CloudBees publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Computer API, CreateItem API, Job API, and 4 more. Tagged areas include CI/CD, Continuous Delivery, Continuous Integration, DevOps, and Feature Flags.


  The CloudBees catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CloudBees'' developer surface includes authentication, documentation, support, engineering blog, and 11 more developer resources.'
plans:
- name: Cloudbees Plans Pricing
  plan_count: 3
  slug: cloudbees-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Cloudbees Rate Limits
  slug: cloudbees-rate-limits
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: CloudBees API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 6
  slug: cloudbees-rules
score:
  band: developing
  composite: 40.1
  delta: 2.6
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 54.5
    contract_quality: 47.3
    developer_ergonomics: 35.7
    discoverability: 64.8
    governance: 54.5
    operational_transparency: 26.3
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudbees/refs/heads/main/screenshots/cloudbees-2026-06-20T174542.png
security:
- kind: authentication
  name: Cloudbees Authentication
  slug: cloudbees-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cloudbees Domain Security
  slug: cloudbees-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cloudbees Vulnerability Disclosure
  slug: cloudbees-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cloudbees Trust Center
  slug: cloudbees-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: cloudbees
tags:
- CI/CD
- Continuous Delivery
- Continuous Integration
- DevOps
- Feature Flags
- Feature Management
- Jenkins
- Release Orchestration
- Software Delivery
website: https://www.cloudbees.com/
---
