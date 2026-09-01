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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 30
  human_in_the_loop: 2
  name: Artifact Hub Agentic Access
  operation_count: 58
  slug: artifact-hub-agentic-access
  summary_line: 58 operations · 30 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The Artifact Hub REST API provides endpoints for searching and retrieving cloud-native packages across all supported artifact types, managing repositories, handling user authentication and sessions, m
  name: Artifact Hub API
  slug: artifact-hub-api
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
- description: The Availability checks API from Artifact Hub — 1 operation(s) for availability checks.
  name: Artifact Hub Availability checks API
  slug: artifact-hub-availability-checks-api
- description: The Integrations API from Artifact Hub — 3 operation(s) for integrations.
  name: Artifact Hub Integrations API
  slug: artifact-hub-integrations-api
artifact_total: 41
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Artifact Hub Availability checks API
  slug: open-artifact-hub-availability-checks-api
- collection_type: open
  name: Artifact Hub Integrations API
  slug: open-artifact-hub-integrations-api
- collection_type: open
  name: Artifact Hub Organizations API
  slug: open-artifact-hub-organizations-api
- collection_type: open
  name: Artifact Hub Packages API
  slug: open-artifact-hub-packages-api
- collection_type: open
  name: Artifact Hub Repositories API
  slug: open-artifact-hub-repositories-api
- collection_type: open
  name: Artifact Hub Stats API
  slug: open-artifact-hub-stats-api
- collection_type: open
  name: Artifact Hub Subscriptions API
  slug: open-artifact-hub-subscriptions-api
- collection_type: open
  name: Artifact Hub Users API
  slug: open-artifact-hub-users-api
- collection_type: open
  name: Artifact Hub Webhooks API
  slug: open-artifact-hub-webhooks-api
- collection_type: open
  name: Artifact Hub API
  slug: open-artifact-hub
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/artifacthub/hub/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/artifacthub/hub/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/artifacthub/hub/blob/master/code-of-conduct.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/artifacthub/hub/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/artifacthub/hub/blob/master/LICENSE
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
overview: 'Artifact Hub publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Organizations API, Packages API, Repositories API, and 6 more. Tagged areas include Cloud-Native, CNCF, Helm Charts, Package Registry, and Discovery.


  Artifact Hub''s developer surface includes authentication, documentation, developer portal, release notes, and 11 more developer resources.'
plans:
- name: Artifact Hub Plans Pricing
  plan_count: 3
  slug: artifact-hub-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Artifact Hub Rate Limits
  slug: artifact-hub-rate-limits
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 55.9
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Cloud-Native
- CNCF
- Helm Charts
- Package Registry
- Discovery
- Open-Source
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
