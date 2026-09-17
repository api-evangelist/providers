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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.0
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 12
  human_in_the_loop: 6
  name: Atlassian Compass Agentic Access
  operation_count: 13
  slug: atlassian-compass-agentic-access
  summary_line: 13 operations · 12 acting · 6 human-in-the-loop
api_count: 2
apis:
- description: 'The Compass GraphQL API enables programmatic management of software components, scorecards, metrics, relationships, custom fields, and event ingestion within the Compass developer experience platform '
  name: Atlassian Compass GraphQL API
  slug: atlassian-compass-graphql-api
- baseURL: https://api.atlassian.com/graphql
  baseurl_source: declared
  description: Ingest events into a Compass event source
  name: Atlassian Compass Events API
  slug: atlassian-compass-events-api
- baseURL: https://api.atlassian.com/graphql
  baseurl_source: declared
  description: Ingest metric values
  name: Atlassian Compass Metrics API
  slug: atlassian-compass-metrics-api
- baseURL: https://api.atlassian.com/graphql
  baseurl_source: declared
  description: The attachment-rest-controller API from Atlassian Compass — 2 operation(s) for attachment-rest-controller.
  name: Atlassian Compass Attachment Rest Controller API
  slug: atlassian-compass-attachment-rest-controller-api
- baseURL: https://api.atlassian.com/graphql
  baseurl_source: declared
  description: The entitlement-rest-controller API from Atlassian Compass — 1 operation(s) for entitlement-rest-controller.
  name: Atlassian Compass Entitlement Rest Controller API
  slug: atlassian-compass-entitlement-rest-controller-api
- baseURL: https://api.atlassian.com/graphql
  baseurl_source: declared
  description: The incoming-webhooks-rest-controller API from Atlassian Compass — 1 operation(s) for incoming-webhooks-rest-controller.
  name: Atlassian Compass Incoming Webhooks Rest Controller API
  slug: atlassian-compass-incoming-webhooks-rest-controller-api
- baseURL: https://api.atlassian.com/graphql
  baseurl_source: declared
  description: This resource represents package dependencies. Use this resource to associate package dependencies with a component.
  name: Atlassian Compass Package Dependencies API
  slug: atlassian-compass-package-dependencies-api
artifact_total: 42
asyncapis:
- description: ''
  name: Atlassian Compass Webhooks
  slug: atlassian-compass-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Atlassian Compass REST Events API
  slug: open-atlassian-compass-events-api
- collection_type: open
  name: Atlassian Compass REST Events Metrics API
  slug: open-atlassian-compass-metrics-api
- collection_type: open
  name: Atlassian Compass REST API
  slug: open-atlassian-compass
common:
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/openapi/atlassian-compass-compass-rest-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/atlassian-compass-compass-rest-api-openapi.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/overlays/atlassian-compass-compass-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/atlassian-compass-compass-rest-api-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/packages/atlassian-compass-packages.yml
  title: ''
  type: Packages
  url: packages/atlassian-compass-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/packages/atlassian-compass-packages.yml
  title: ''
  type: SDKs
  url: packages/atlassian-compass-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/cli/atlassian-compass-cli.yml
  title: ''
  type: CLI
  url: cli/atlassian-compass-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/mcp/atlassian-compass-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atlassian-compass-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/mcp/atlassian-compass-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/atlassian-compass-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/llms/atlassian-compass-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlassian-compass-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/well-known/atlassian-compass-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atlassian-compass-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/well-known/atlassian-compass-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/atlassian-compass-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/security/atlassian-compass-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/atlassian-compass-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/security/atlassian-compass-trust-center.yml
  title: ''
  type: Compliance
  url: security/atlassian-compass-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/conformance/atlassian-compass-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atlassian-compass-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/conventions/atlassian-compass-conventions.yml
  title: ''
  type: Conventions
  url: conventions/atlassian-compass-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/errors/atlassian-compass-error-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/atlassian-compass-error-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/data-model/atlassian-compass-data-model.yml
  title: ''
  type: DataModel
  url: data-model/atlassian-compass-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/asyncapi/atlassian-compass-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/atlassian-compass-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/lifecycle/atlassian-compass-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/atlassian-compass-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/lifecycle/atlassian-compass-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/atlassian-compass-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/changelog/atlassian-compass-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/atlassian-compass-changelog.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/rate-limits/atlassian-compass-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/atlassian-compass-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/plans/atlassian-compass-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/atlassian-compass-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/finops/atlassian-compass-finops.yml
  title: ''
  type: FinOps
  url: finops/atlassian-compass-finops.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.atlassian.com/cloud/compass/rest/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.atlassian.com/roadmap/cloud
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/atlassian-labs/compass-examples
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/agentic-access/atlassian-compass-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/atlassian-compass-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/security/atlassian-compass-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/atlassian-compass-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/security/atlassian-compass-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/atlassian-compass-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/security/atlassian-compass-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlassian-compass-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/authentication/atlassian-compass-authentication.yml
  title: ''
  type: Authentication
  url: authentication/atlassian-compass-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/scopes/atlassian-compass-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/atlassian-compass-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.atlassian.com/software/compass
- group: start
  title: ''
  type: Portal
  url: https://developer.atlassian.com/cloud/compass/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.atlassian.com/cloud/compass/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.atlassian.com/cloud/compass/integrations/get-started-integrating-with-Compass/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.atlassian.com/cloud/compass/integrations/get-started-integrating-with-Compass/
- group: start
  title: ''
  type: Signup
  url: https://www.atlassian.com/software/compass
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atlassian
- group: operate
  title: ''
  type: StatusPage
  url: https://status.atlassian.com/
- group: operate
  title: ''
  type: Support
  url: https://support.atlassian.com/
- group: operate
  title: ''
  type: Community
  url: https://community.atlassian.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlassian.com/legal/cloud-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlassian.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atlassian.com/software/compass/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.atlassian.com/blog/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.atlassian.com/cloud/compass/changelog/
created: '2026-03-16'
description: Atlassian Compass is a developer experience platform that helps engineering teams understand, manage, and improve the health of their software components and services. It provides a centralized catalog of software components with scorecards, metrics, dependency tracking, and event ingestion to improve developer productivity and software quality. Compass exposes a GraphQL API for querying and mutating component data and a REST Operations API for integrations.
features:
- description: Central catalog of all software components with metadata, ownership, and lifecycle tracking across teams.
  name: Component Catalog
- description: Configurable scorecards that evaluate components against engineering standards and best practices to measure health.
  name: Scorecards
- description: Ingest build, deployment, incident, and vulnerability events from CI/CD pipelines and monitoring tools via webhooks and REST.
  name: Event Ingestion
- description: Track relationships and dependencies between software components to understand blast radius and system topology.
  name: Dependency Tracking
- description: Extend component metadata with custom text, number, boolean, and user fields to capture team-specific data.
  name: Custom Fields
- description: Build custom Compass apps using the Atlassian Forge platform with the GraphQL toolkit for deep platform integration.
  name: Forge Integration
finops:
- name: Atlassian Compass Finops
  service_category: API
  slug: atlassian-compass-finops
graphqls:
- description: 'The Compass GraphQL API enables programmatic management of software components, scorecards, metrics, relationships, custom fields, and event ingestion within the Compass developer experience platform '
  name: Atlassian Compass GraphQL API
  slug: atlassian-compass-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/atlassian-compass.png
integrations:
- description: Native integration with Jira for linking components to project tracking and incident management workflows.
  name: Jira
- description: Connect Bitbucket repositories to Compass components for automated code health and deployment event tracking.
  name: Bitbucket
- description: Integrate GitHub repositories and GitHub Actions CI/CD pipelines with Compass component events.
  name: GitHub
- description: Ingest PagerDuty incident events into Compass for on-call and incident tracking scorecard criteria.
  name: PagerDuty
- description: Connect Datadog monitoring data and deployment events to Compass component metrics.
  name: Datadog
- description: Manage Compass resources via the Atlassian Operations Terraform provider for infrastructure-as-code workflows.
  name: Terraform
layout: provider
mcp_servers:
- description: The official Atlassian Model Context Protocol server. It is a cloud-hosted bridge between an Atlassian Cloud site and an MCP client, and Atlassian's own README lists Compass among the supported produc
  name: Atlassian Rovo MCP Server
  slug: atlassian-rovo-mcp-server
modified: '2026-09-06'
name: Atlassian Compass
nav: Providers
network: true
overview: 'Atlassian Compass publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Events API, Metrics API, Attachment Rest Controller API, and 3 more. Tagged areas include Atlassian, Component Management, Developer Experience, Software Catalog, and GraphQL.


  The Atlassian Compass catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Atlassian Compass'' developer surface includes CLI, changelog, API reference, authentication, developer portal, documentation, getting-started guide, and 41 more developer resources.'
plans:
- name: Atlassian Compass Plans Pricing
  plan_count: 3
  slug: atlassian-compass-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Atlassian Compass Rate Limits
  slug: atlassian-compass-rate-limits
scopes:
- name: Atlassian Compass Scopes
  scope_count: 4
  slug: atlassian-compass-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 69.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 94.7
    contract_governance: 18.2
    contract_quality: 60.7
    developer_ergonomics: 73.2
    discoverability: 68.5
    operational_transparency: 97.4
  previous_composite: 70.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/screenshots/atlassian-compass-2026-06-20T172526.png
security:
- kind: authentication
  name: Atlassian Compass Authentication
  slug: atlassian-compass-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Atlassian Compass Domain Security
  slug: atlassian-compass-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Atlassian Compass Vulnerability Disclosure
  slug: atlassian-compass-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Atlassian Compass Trust Center
  slug: atlassian-compass-trust-center
  summary_line: FedRAMP
slug: atlassian-compass
solutions:
- description: Provide engineering teams with a centralized platform to understand, manage, and improve the health of their software systems.
  name: Developer Experience Platform
- description: Enable platform engineering teams to enforce standards, track compliance, and improve developer productivity at scale.
  name: Platform Engineering
tags:
- Atlassian
- Component Management
- Developer Experience
- Software Catalog
- GraphQL
use_cases:
- description: Register and track all microservices, libraries, and software components with ownership and lifecycle metadata.
  name: Software Catalog Management
- description: Create scorecards to measure and improve engineering standards like on-call coverage, documentation, and security posture.
  name: Engineering Health Monitoring
- description: Ingest deployment and incident events to track DORA metrics including deployment frequency and change failure rate.
  name: DORA Metrics Tracking
- description: Map dependencies between services to identify coupling, blast radius, and architectural debt.
  name: Dependency Mapping
- description: Integrate Compass with internal developer portals and CI/CD pipelines for automated component registration and event tracking.
  name: Developer Portal Integration
website: https://www.atlassian.com/software/compass
---
