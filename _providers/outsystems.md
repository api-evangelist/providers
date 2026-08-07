---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 56
  human_in_the_loop: 3
  name: Outsystems Agentic Access
  operation_count: 150
  slug: outsystems-agentic-access
  summary_line: 150 operations · 56 acting · 3 human-in-the-loop
api_count: 14
apis:
- description: REST endpoints for retrieving and managing users, groups, application roles, organization roles, permissions, identity providers, OIDC clients, realms and subjects in an OutSystems Developer Cloud org
  name: OutSystems ODC User and Access Management API
  slug: user-access-management-api-v1
- description: REST endpoints for retrieving information about assets and environments deployed across the stages of an OutSystems Developer Cloud organization.
  name: OutSystems ODC Portfolio API
  slug: portfolio-api-v2
- description: Version 1 of the ODC Portfolio API, superseded by v2. REST endpoints for retrieving information about assets and environments in your organization.
  name: OutSystems ODC Portfolio API (v1)
  slug: portfolio-api-v1
- description: REST endpoints for retrieving information about assets and asset revisions held in the OutSystems Developer Cloud asset repository.
  name: OutSystems ODC Asset Repository API
  slug: asset-repository-api-v1
- description: REST endpoints to get and update global environment settings and to manage configuration for individual agents and applications.
  name: OutSystems ODC Asset Configurations API
  slug: asset-configurations-api-v1
- description: REST endpoints for managing environment (stage) configurations in ODC, covering custom domains, IP filters and private gateways.
  name: OutSystems ODC Environment Configurations API
  slug: environment-configurations-api-v1
- description: REST endpoints to start build operations for ODC assets and retrieve information about their status.
  name: OutSystems ODC Build Operations API
  slug: build-operations-api-v1
- description: REST endpoints for publishing and deploying assets across the environments (stages) in an OutSystems Developer Cloud organization, including rollback.
  name: OutSystems ODC Deployments API
  slug: deployments-api-v1
- description: REST endpoints for launching and retrieving the results of impact analysis for the deployment and deletion of an asset.
  name: OutSystems ODC Dependency Management API
  slug: dependency-management-api-v1
- description: REST endpoints to submit code analysis requests and retrieve code quality findings, application scores and analysis results — the technical-debt surface of the platform.
  name: OutSystems ODC Code Quality API
  slug: code-quality-api-v1
- description: REST endpoints for building and managing native iOS and Android mobile application packages, build versions, validation and extensibility settings.
  name: OutSystems ODC Native Mobile Build API
  slug: native-mobile-build-api-v1
- description: REST endpoints for generating and managing external libraries from high-code .NET packages so ODC apps can consume custom C# logic.
  name: OutSystems ODC External Library Generation API
  slug: external-library-generation-api-v1
- description: REST endpoints for retrieving subscription and entitlement data and usage metrics for an OutSystems Developer Cloud organization.
  name: OutSystems ODC Subscription API
  slug: subscription-api-v1
- description: Official OutSystems remote Model Context Protocol server (early alpha), exposed per tenant over streamable HTTP with OAuth Dynamic Client Registration. Tool domains cover Apps, the read-only Context S
  name: OutSystems Remote MCP Server
  slug: remote-mcp
artifact_total: 22
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/outsystems-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.outsystems.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.outsystems.com/community/
- group: docs
  title: ''
  type: Documentation
  url: https://success.outsystems.com/documentation/outsystems_developer_cloud/
- group: docs
  title: ''
  type: APIReference
  url: https://success.outsystems.com/documentation/outsystems_developer_cloud/odc_rest_apis/api_references/
- group: start
  title: ''
  type: GettingStarted
  url: https://success.outsystems.com/documentation/outsystems_developer_cloud/getting_started/
- group: operate
  title: ''
  type: Support
  url: https://success.outsystems.com/support/home/
- group: company
  title: ''
  type: Blog
  url: https://www.outsystems.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OutSystems
- group: commercial
  title: ''
  type: Pricing
  url: https://www.outsystems.com/pricing-and-editions/
- group: start
  title: ''
  type: SignUp
  url: https://www.outsystems.com/free-edition/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.outsystems.com/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.outsystems.com/legal/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/outsystems-official/outsystems-11-platform-apis
- group: operate
  title: ''
  type: StatusPage
  url: https://status.outsystems.com/
- group: auth
  title: ''
  type: Security
  url: https://www.outsystems.com/security/report-a-vulnerability
- group: auth
  title: ''
  type: Compliance
  url: https://security.outsystems.com/
- group: build
  title: ''
  type: Packages
  url: packages/outsystems-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/outsystems-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/outsystems-cli.yml
- group: design
  title: ''
  type: Components
  url: components/outsystems-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/outsystems-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/outsystems-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/outsystems-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/outsystems-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/outsystems-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/outsystems-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/outsystems-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/outsystems-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/outsystems-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/outsystems-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/outsystems-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/outsystems-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/outsystems-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/outsystems-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/outsystems-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/outsystems-agentic-access.yml
created: '2026-08-02'
description: OutSystems is an enterprise low-code and AI-assisted application development platform company, founded in 2001 and headquartered in Boston, Massachusetts with engineering in Lisbon, Portugal. Its two product lines are OutSystems 11 (O11), the self-managed/PaaS platform, and OutSystems Developer Cloud (ODC), the cloud-native successor. ODC publishes a documented set of public REST APIs covering user and access management, portfolio, asset repository, asset and environment configurations, build operations, deployments, dependency and impact analysis, code quality, native mobile builds, external library generation, and subscription/entitlement usage. All ODC REST APIs authenticate with OAuth 2.0 client-credentials via a per-tenant OIDC discovery document, use offset/limit pagination, and are rate limited per API domain. OutSystems also ships a remote MCP server (early alpha) that exposes app inspection, the Mentor OML editing session, publishing, deployments, external libraries
  and environments to AI coding agents.
image: https://www.outsystems.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: outsystems-mcp.yml
  slug: outsystems-mcpyml
modified: '2026-08-02'
name: OutSystems
nav: Providers
network: true
overview: 'OutSystems publishes 13 APIs on the [APIs.io](https://apis.io/) network, including ODC User and Access Management API, ODC Portfolio API, ODC Portfolio API (v1), and 10 more. Tagged areas include Company, Low-Code, Application Development, Platform as a Service, and DevOps.


  OutSystems'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 12
  name: Outsystems Rate Limits
  slug: outsystems-rate-limits
scopes:
- name: Outsystems Scopes
  scope_count: 0
  slug: outsystems-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 55.3
    developer_ergonomics: 71.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 86.8
  previous_composite: 62.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Outsystems Authentication
  slug: outsystems-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Outsystems Domain Security
  slug: outsystems-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Outsystems Vulnerability Disclosure
  slug: outsystems-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Outsystems Trust Center
  slug: outsystems-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018, FedRAMP, GDPR
slug: outsystems
tags:
- Company
- Low-Code
- Application Development
- Platform as a Service
- DevOps
- Deployment
- Identity and Access Management
- Artificial Intelligence
- Enterprise Software
- Mobile Development
website: https://www.outsystems.com/
---
