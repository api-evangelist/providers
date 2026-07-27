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
  band: agent-native
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 66.3
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Jenkins Agentic Access
  operation_count: 8
  slug: jenkins-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 4
apis:
- description: Connected build agents.
  name: Jenkins Computer API
  slug: jenkins-computer-api
- description: Jenkins jobs and their builds.
  name: Jenkins Jobs API
  slug: jenkins-jobs-api
- description: The build queue.
  name: Jenkins Queue API
  slug: jenkins-queue-api
- description: Information about the Jenkins instance.
  name: Jenkins Server API
  slug: jenkins-server-api
arazzos:
- description: Enumerate the jobs on an instance, drill into one job, and read the detail of its most recent build.
  name: Jenkins Discover Jobs and Inspect the Latest Build
  slug: jenkins-inspect-job-latest-build-workflow
- description: Read instance mode and executor count, check agents are online, and measure queue depth.
  name: Jenkins Instance Health and Capacity Check
  slug: jenkins-instance-health-check-workflow
- description: Trigger a parameterless job, watch it leave the queue, and poll the build until it finishes.
  name: Jenkins Trigger a Build and Await the Result
  slug: jenkins-trigger-build-and-await-result-workflow
- description: Submit build parameters to a parameterized job, confirm it queued, and poll until it finishes.
  name: Jenkins Trigger a Parameterized Build and Await the Result
  slug: jenkins-trigger-parameterized-build-workflow
artifact_total: 17
collections:
- collection_type: open
  name: Jenkins Remote Access API
  slug: open-jenkins
common:
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jenkins-trigger-build-and-await-result-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jenkins-trigger-parameterized-build-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jenkins-inspect-job-latest-build-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jenkins-instance-health-check-workflow.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jenkins-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jenkins-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jenkins-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jenkins-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/jenkins-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jenkins-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/jenkins-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jenkins-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jenkins-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/jenkins-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/jenkins-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jenkins-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jenkins-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/jenkins-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/jenkins-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jenkins-data-model.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jenkinsio
- group: company
  title: ''
  type: Website
  url: https://www.jenkins.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.jenkins.io/doc/pipeline/tour/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://www.jenkins.io/doc/
- group: other
  title: ''
  type: Installation
  url: https://www.jenkins.io/doc/book/installing/
- group: build
  title: ''
  type: Plugins
  url: https://plugins.jenkins.io/
- group: learn
  title: ''
  type: Tutorials
  url: https://www.jenkins.io/doc/tutorials/
- group: company
  title: ''
  type: Blog
  url: https://www.jenkins.io/node/
- group: operate
  title: ''
  type: Community
  url: https://www.jenkins.io/participate/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jenkinsci
- group: auth
  title: ''
  type: SecurityAdvisories
  url: https://www.jenkins.io/security/advisories/
- group: other
  title: ''
  type: Governance
  url: https://www.jenkins.io/project/governance/
- group: operate
  title: ''
  type: RoadMap
  url: https://www.jenkins.io/project/roadmap/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jenkins.io/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jenkins.io/project/conduct/
created: '2024-01-01'
description: Jenkins is the leading open source automation server that enables developers to reliably build, test, and deploy software. Jenkins exposes a machine-consumable Remote Access API for nearly every resource it manages, available in XML (with XPath filtering), JSON (with JSONP), and a Python-compatible variant, and supports HTTP Basic auth with API tokens for scripted clients.
finops:
- name: Jenkins Finops
  service_category: API
  slug: jenkins-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jenkins.png
layout: provider
mcp_servers:
- description: ''
  name: jenkins-mcp.yml
  slug: jenkins-mcpyml
modified: '2026-06-20'
name: Jenkins
nav: Providers
network: true
overview: 'Jenkins publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Computer API, Jobs API, Queue API, and 1 more. Tagged areas include Automation, Build Server, CI/CD, Continuous Delivery, and Continuous Integration.


  Jenkins'' developer surface includes authentication, changelog, CLI, getting-started guide, documentation, engineering blog, and 29 more developer resources.'
plans:
- name: Jenkins Plans Pricing
  plan_count: 3
  slug: jenkins-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Jenkins Rate Limits
  slug: jenkins-rate-limits
score:
  band: developing
  composite: 51.6
  delta: 2.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.3
    developer_ergonomics: 52.2
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 49.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jenkins/refs/heads/main/screenshots/jenkins-2026-06-20T183720.png
security:
- kind: authentication
  name: Jenkins Authentication
  slug: jenkins-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Jenkins Domain Security
  slug: jenkins-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jenkins Vulnerability Disclosure
  slug: jenkins-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jenkins
tags:
- Automation
- Build Server
- CI/CD
- Continuous Delivery
- Continuous Integration
- DevOps
- Open Source
- Remote Access API
website: https://www.jenkins.io/
---
