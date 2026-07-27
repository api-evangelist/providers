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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 30
  human_in_the_loop: 2
  name: Artifact Hub Agentic Access
  operation_count: 58
  slug: artifact-hub-agentic-access
  summary_line: 58 operations · 30 acting · 2 human-in-the-loop
api_count: 9
apis:
- description: The Artifact Hub REST API provides endpoints for searching and retrieving cloud-native packages across all supported artifact types, managing repositories, handling user authentication and sessions, m
  name: Artifact Hub API
  slug: artifact-hub-api
- description: API key management
  name: Artifact Hub API Keys API
  slug: artifact-hub-api-keys-api
- description: Organizations and memberships
  name: Artifact Hub Organizations API
  slug: artifact-hub-organizations-api
- description: Search and retrieve cloud-native packages
  name: Artifact Hub Packages API
  slug: artifact-hub-packages-api
- description: Repository management
  name: Artifact Hub Repositories API
  slug: artifact-hub-repositories-api
- description: Site-wide statistics
  name: Artifact Hub Stats API
  slug: artifact-hub-stats-api
- description: Package event subscriptions
  name: Artifact Hub Subscriptions API
  slug: artifact-hub-subscriptions-api
- description: User accounts and sessions
  name: Artifact Hub Users API
  slug: artifact-hub-users-api
- description: Webhook configuration and delivery
  name: Artifact Hub Webhooks API
  slug: artifact-hub-webhooks-api
artifact_total: 30
collections:
- collection_type: open
  name: Artifact Hub API
  slug: open-artifact-hub
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/artifact-hub-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/artifact-hub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/artifact-hub-authentication.yml
- group: docs
  title: Artifact Hub Documentation
  type: Documentation
  url: https://artifacthub.io/docs/
- group: build
  title: Artifact Hub GitHub Organization
  type: GitHubOrganization
  url: https://github.com/artifacthub
- group: build
  title: Artifact Hub Source Repository
  type: GitHubRepository
  url: https://github.com/artifacthub/hub
- group: start
  title: Artifact Hub
  type: Portal
  url: https://artifacthub.io/
- group: auth
  title: CNCF Project Page
  type: Compliance
  url: https://www.cncf.io/projects/artifact-hub/
- group: operate
  title: Release Notes
  type: ReleaseNotes
  url: https://github.com/artifacthub/hub/releases
- group: agent
  title: ''
  type: LlmsText
  url: https://artifacthub.io/llms.txt
created: '2026-03-16'
description: Artifact Hub is a CNCF incubating web-based application that enables finding, installing, and publishing cloud-native packages. Built primarily in TypeScript and Go, it addresses fragmentation in the cloud-native ecosystem by providing a single discovery experience for consumers. It supports 27+ artifact types including Helm charts, OPA policies, Falco rules, OLM operators, Tinkerbell actions, kubectl plugins, Tekton tasks, KEDA scalers, CoreDNS plugins, and more. Artifact Hub provides a searchable catalog with versioning, security reports via Trivy and Snyk, changelog tracking, and webhook notification support. Licensed under Apache 2.0 and governed by the CNCF.
features:
- description: Unified search across 27+ cloud-native artifact types including Helm charts, Kubernetes operators, OPA policies, Falco rules, and Tekton tasks from a single interface.
  name: Package Discovery
- description: Automated security scanning of Helm chart images using Trivy and Snyk, with visualized vulnerability reports and severity ratings.
  name: Security Reports
- description: Configurable webhooks for receiving notifications when new package versions are published or security issues are discovered.
  name: Webhook Notifications
- description: Publishers add and manage their Helm chart repositories, OCI registries, and other sources via the Artifact Hub API.
  name: Repository Management
- description: Interactive exploration of Helm chart values schemas and template structures directly in the browser.
  name: Schema and Template Explorer
- description: Artifact Hub can be deployed on-premise using the official Helm chart, enabling organizations to run their own private artifact registry.
  name: Self-Hosting Support
finops:
- name: Artifact Hub Finops
  service_category: API
  slug: artifact-hub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/artifact-hub.png
integrations:
- description: Native integration with Helm chart repositories including support for OCI-based chart distribution via container registries.
  name: Helm
- description: Integration with Aqua Security's Trivy for container image vulnerability scanning in Helm chart security reports.
  name: Trivy
- description: Integration with Snyk for additional container security scanning capabilities in Artifact Hub security reports.
  name: Snyk
- description: Artifact Hub is an official CNCF incubating project integrated into the Cloud Native Computing Foundation's ecosystem.
  name: CNCF Landscape
layout: provider
modified: '2026-04-19'
name: Artifact Hub
nav: Providers
network: true
overview: 'Artifact Hub publishes 8 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Organizations API, Packages API, and 5 more. Tagged areas include Cloud Native, CNCF, Helm Charts, Package Registry, and Discovery.


  Artifact Hub''s developer surface includes authentication, documentation, developer portal, release notes, and 6 more developer resources.'
plans:
- name: Artifact Hub Plans Pricing
  plan_count: 3
  slug: artifact-hub-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Artifact Hub Rate Limits
  slug: artifact-hub-rate-limits
score:
  band: thin
  composite: 43.9
  delta: 3.3
  facets:
    commercial_clarity: 47.4
    contract_quality: 47.5
    developer_ergonomics: 28.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 40.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/artifact-hub/refs/heads/main/screenshots/artifact-hub-2026-06-20T172443.png
security:
- kind: authentication
  name: Artifact Hub Authentication
  slug: artifact-hub-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Artifact Hub Domain Security
  slug: artifact-hub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: artifact-hub
tags:
- Cloud Native
- CNCF
- Helm Charts
- Package Registry
- Discovery
- Open Source
use_cases:
- description: Platform engineers discover and evaluate Helm charts across multiple repositories from a single searchable interface with version history and security report data.
  name: Helm Chart Discovery
- description: Open source maintainers publish their Helm charts, operators, and other cloud-native packages to Artifact Hub for discoverability.
  name: Package Publishing
- description: Security teams review Artifact Hub security reports to identify vulnerable container images used in Helm charts before deployment.
  name: Security Auditing
- description: Development teams configure webhooks to receive notifications when new versions of dependencies like Helm charts are published.
  name: Release Monitoring
website: https://artifacthub.io/
---
