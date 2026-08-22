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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 134
  human_in_the_loop: 9
  name: Snyk Agentic Access
  operation_count: 277
  slug: snyk-agentic-access
  summary_line: 277 operations · 134 acting · 9 human-in-the-loop
api_count: 48
apis:
- description: Manages Snyk Apps, the OAuth2-based extensibility surface that lets third-party applications act on behalf of Snyk users, organizations, and groups.
  name: Snyk REST API - Apps (OAuth)
  slug: rest-apps
- description: The original Snyk REST API. Still in use for project import, monitor, test, and certain reporting endpoints not yet ported to the dated REST API. Subject to end-of-life migration; new integrations sho
  name: Snyk V1 API (Legacy)
  slug: v1
- description: The AccessRequests API from Snyk — 1 operation(s) for accessrequests.
  name: Snyk AccessRequests API
  slug: snyk-accessrequests-api
- description: The AiBom API from Snyk — 4 operation(s) for aibom.
  name: Snyk AiBom API
  slug: snyk-aibom-api
- description: The Apps API from Snyk — 20 operation(s) for apps.
  name: Snyk Apps API
  slug: snyk-apps-api
- description: The Asset API from Snyk — 6 operation(s) for asset.
  name: Snyk Asset API
  slug: snyk-asset-api
- description: The Audit Logs API from Snyk — 2 operation(s) for audit logs.
  name: Snyk Audit Logs API
  slug: snyk-audit-logs-api
- description: The BrokerConnections API from Snyk — 7 operation(s) for brokerconnections.
  name: Snyk BrokerConnections API
  slug: snyk-brokerconnections-api
- description: The BrokerContexts API from Snyk — 5 operation(s) for brokercontexts.
  name: Snyk BrokerContexts API
  slug: snyk-brokercontexts-api
- description: The BrokerDeployments API from Snyk — 3 operation(s) for brokerdeployments.
  name: Snyk BrokerDeployments API
  slug: snyk-brokerdeployments-api
- description: The Catalog Resource API from Snyk — 1 operation(s) for catalog resource.
  name: Snyk Catalog Resource API
  slug: snyk-catalog-resource-api
- description: The Cloud API from Snyk — 6 operation(s) for cloud.
  name: Snyk Cloud API
  slug: snyk-cloud-api
- description: The Collection API from Snyk — 3 operation(s) for collection.
  name: Snyk Collection API
  slug: snyk-collection-api
- description: The ContainerImage API from Snyk — 3 operation(s) for containerimage.
  name: Snyk ContainerImage API
  slug: snyk-containerimage-api
- description: The ContainerRegistryImportPolicy API from Snyk — 3 operation(s) for containerregistryimportpolicy.
  name: Snyk ContainerRegistryImportPolicy API
  slug: snyk-containerregistryimportpolicy-api
- description: The Custom Base Images API from Snyk — 2 operation(s) for custom base images.
  name: Snyk Custom Base Images API
  slug: snyk-custom-base-images-api
- description: The DeploymentCredentials API from Snyk — 2 operation(s) for deploymentcredentials.
  name: Snyk DeploymentCredentials API
  slug: snyk-deploymentcredentials-api
- description: The Export API from Snyk — 6 operation(s) for export.
  name: Snyk Export API
  slug: snyk-export-api
- description: The Findings API from Snyk — 1 operation(s) for findings.
  name: Snyk Findings API
  slug: snyk-findings-api
- description: The Group API from Snyk — 1 operation(s) for group.
  name: Snyk Group API
  slug: snyk-group-api
- description: The Groups API from Snyk — 7 operation(s) for groups.
  name: Snyk Groups API
  slug: snyk-groups-api
- description: The IacSettings API from Snyk — 2 operation(s) for iacsettings.
  name: Snyk IacSettings API
  slug: snyk-iacsettings-api
- description: The Integrations API from Snyk — 3 operation(s) for integrations.
  name: Snyk Integrations API
  slug: snyk-integrations-api
- description: The Inventory Assets API from Snyk — 30 operation(s) for inventory assets.
  name: Snyk Inventory Assets API
  slug: snyk-inventory-assets-api
- description: The Invites API from Snyk — 2 operation(s) for invites.
  name: Snyk Invites API
  slug: snyk-invites-api
- description: The Issues API from Snyk — 6 operation(s) for issues.
  name: Snyk Issues API
  slug: snyk-issues-api
- description: The LanguagesSettings API from Snyk — 2 operation(s) for languagessettings.
  name: Snyk LanguagesSettings API
  slug: snyk-languagessettings-api
- description: The Learn assignment API from Snyk — 2 operation(s) for learn assignment.
  name: Snyk Learn assignment API
  slug: snyk-learn-assignment-api
- description: The Learn progress API from Snyk — 2 operation(s) for learn progress.
  name: Snyk Learn progress API
  slug: snyk-learn-progress-api
- description: The OpenAPI specification for this service.
  name: Snyk OpenAPI API
  slug: snyk-openapi-api
- description: The OpenSourceSettings API from Snyk — 4 operation(s) for opensourcesettings.
  name: Snyk OpenSourceSettings API
  slug: snyk-opensourcesettings-api
- description: The Orgs API from Snyk — 5 operation(s) for orgs.
  name: Snyk Orgs API
  slug: snyk-orgs-api
- description: The Package API from Snyk — 1 operation(s) for package.
  name: Snyk Package API
  slug: snyk-package-api
- description: The Package Version API from Snyk — 1 operation(s) for package version.
  name: Snyk Package Version API
  slug: snyk-package-version-api
- description: The PersonalAccessToken API from Snyk — 2 operation(s) for personalaccesstoken.
  name: Snyk PersonalAccessToken API
  slug: snyk-personalaccesstoken-api
- description: The Policies API from Snyk — 5 operation(s) for policies.
  name: Snyk Policies API
  slug: snyk-policies-api
- description: The Projects API from Snyk — 2 operation(s) for projects.
  name: Snyk Projects API
  slug: snyk-projects-api
- description: The Pull Request Templates API from Snyk — 1 operation(s) for pull request templates.
  name: Snyk Pull Request Templates API
  slug: snyk-pull-request-templates-api
- description: The SastSettings API from Snyk — 1 operation(s) for sastsettings.
  name: Snyk SastSettings API
  slug: snyk-sastsettings-api
- description: The SBOM API from Snyk — 4 operation(s) for sbom.
  name: Snyk SBOM API
  slug: snyk-sbom-api
- description: The ServiceAccounts API from Snyk — 6 operation(s) for serviceaccounts.
  name: Snyk ServiceAccounts API
  slug: snyk-serviceaccounts-api
- description: The Slack API from Snyk — 2 operation(s) for slack.
  name: Snyk Slack API
  slug: snyk-slack-api
- description: The SlackSettings API from Snyk — 3 operation(s) for slacksettings.
  name: Snyk SlackSettings API
  slug: snyk-slacksettings-api
- description: The Targets API from Snyk — 2 operation(s) for targets.
  name: Snyk Targets API
  slug: snyk-targets-api
- description: The TenantRole API from Snyk — 2 operation(s) for tenantrole.
  name: Snyk TenantRole API
  slug: snyk-tenantrole-api
- description: The Tenants API from Snyk — 4 operation(s) for tenants.
  name: Snyk Tenants API
  slug: snyk-tenants-api
- description: The Tests API from Snyk — 3 operation(s) for tests.
  name: Snyk Tests API
  slug: snyk-tests-api
- description: The Users API from Snyk — 3 operation(s) for users.
  name: Snyk Users API
  slug: snyk-users-api
artifact_total: 105
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Snyk AccessRequests API
  slug: open-snyk-accessrequests-api
- collection_type: open
  name: Snyk AccessRequests AiBom API
  slug: open-snyk-aibom-api
- collection_type: open
  name: Snyk AccessRequests Apps API
  slug: open-snyk-apps-api
- collection_type: open
  name: Snyk AccessRequests Asset API
  slug: open-snyk-asset-api
- collection_type: open
  name: Snyk AccessRequests Audit Logs API
  slug: open-snyk-audit-logs-api
- collection_type: open
  name: Snyk AccessRequests BrokerConnections API
  slug: open-snyk-brokerconnections-api
- collection_type: open
  name: Snyk AccessRequests BrokerContexts API
  slug: open-snyk-brokercontexts-api
- collection_type: open
  name: Snyk AccessRequests BrokerDeployments API
  slug: open-snyk-brokerdeployments-api
- collection_type: open
  name: Snyk AccessRequests Catalog Resource API
  slug: open-snyk-catalog-resource-api
- collection_type: open
  name: Snyk AccessRequests Cloud API
  slug: open-snyk-cloud-api
- collection_type: open
  name: Snyk AccessRequests Collection API
  slug: open-snyk-collection-api
- collection_type: open
  name: Snyk AccessRequests ContainerImage API
  slug: open-snyk-containerimage-api
- collection_type: open
  name: Snyk AccessRequests ContainerRegistryImportPolicy API
  slug: open-snyk-containerregistryimportpolicy-api
- collection_type: open
  name: Snyk AccessRequests Custom Base Images API
  slug: open-snyk-custom-base-images-api
- collection_type: open
  name: Snyk AccessRequests DeploymentCredentials API
  slug: open-snyk-deploymentcredentials-api
- collection_type: open
  name: Snyk AccessRequests Export API
  slug: open-snyk-export-api
- collection_type: open
  name: Snyk AccessRequests Findings API
  slug: open-snyk-findings-api
- collection_type: open
  name: Snyk AccessRequests Group API
  slug: open-snyk-group-api
- collection_type: open
  name: Snyk AccessRequests Groups API
  slug: open-snyk-groups-api
- collection_type: open
  name: Snyk AccessRequests IacSettings API
  slug: open-snyk-iacsettings-api
- collection_type: open
  name: Snyk AccessRequests Integrations API
  slug: open-snyk-integrations-api
- collection_type: open
  name: Snyk AccessRequests Inventory Assets API
  slug: open-snyk-inventory-assets-api
- collection_type: open
  name: Snyk AccessRequests Invites API
  slug: open-snyk-invites-api
- collection_type: open
  name: Snyk AccessRequests Issues API
  slug: open-snyk-issues-api
- collection_type: open
  name: Snyk AccessRequests LanguagesSettings API
  slug: open-snyk-languagessettings-api
- collection_type: open
  name: Snyk AccessRequests Learn assignment API
  slug: open-snyk-learn-assignment-api
- collection_type: open
  name: Snyk AccessRequests Learn progress API
  slug: open-snyk-learn-progress-api
- collection_type: open
  name: Snyk AccessRequests OpenAPI API
  slug: open-snyk-openapi-api
- collection_type: open
  name: Snyk AccessRequests OpenSourceSettings API
  slug: open-snyk-opensourcesettings-api
- collection_type: open
  name: Snyk AccessRequests Orgs API
  slug: open-snyk-orgs-api
- collection_type: open
  name: Snyk AccessRequests Package API
  slug: open-snyk-package-api
- collection_type: open
  name: Snyk AccessRequests Package Version API
  slug: open-snyk-package-version-api
- collection_type: open
  name: Snyk AccessRequests PersonalAccessToken API
  slug: open-snyk-personalaccesstoken-api
- collection_type: open
  name: Snyk AccessRequests Policies API
  slug: open-snyk-policies-api
- collection_type: open
  name: Snyk AccessRequests Projects API
  slug: open-snyk-projects-api
- collection_type: open
  name: Snyk AccessRequests Pull Request Templates API
  slug: open-snyk-pull-request-templates-api
- collection_type: open
  name: Snyk API
  slug: open-snyk-rest
- collection_type: open
  name: Snyk AccessRequests SastSettings API
  slug: open-snyk-sastsettings-api
- collection_type: open
  name: Snyk AccessRequests SBOM API
  slug: open-snyk-sbom-api
- collection_type: open
  name: Snyk AccessRequests ServiceAccounts API
  slug: open-snyk-serviceaccounts-api
- collection_type: open
  name: Snyk AccessRequests Slack API
  slug: open-snyk-slack-api
- collection_type: open
  name: Snyk AccessRequests SlackSettings API
  slug: open-snyk-slacksettings-api
- collection_type: open
  name: Snyk AccessRequests Targets API
  slug: open-snyk-targets-api
- collection_type: open
  name: Snyk AccessRequests TenantRole API
  slug: open-snyk-tenantrole-api
- collection_type: open
  name: Snyk AccessRequests Tenants API
  slug: open-snyk-tenants-api
- collection_type: open
  name: Snyk AccessRequests Tests API
  slug: open-snyk-tests-api
- collection_type: open
  name: Snyk AccessRequests Users API
  slug: open-snyk-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/snyk-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/snyk-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/snyk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snyk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/snyk-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snyk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/snyk
- group: company
  title: ''
  type: Website
  url: https://snyk.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snyk.io/snyk-api
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.snyk.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/snyk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/snyk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/snyk-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.snyk.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://snyk.io/blog/feed/
created: '2026-05-08'
description: Snyk is a developer-first security platform covering code, open-source dependencies, container images, and infrastructure-as-code. The Snyk REST API and V1 API expose groups, organizations, projects, issues, targets, integrations, audit logs, SBOMs, container images, custom base images, webhooks, and exports for application-security teams.
finops:
- name: Snyk Finops
  service_category: Application Security
  slug: snyk-finops
graphqls:
- description: Snyk is a developer security platform for finding and fixing vulnerabilities in code, dependencies, containers, and IaC. The API covers project scanning, vulnerability data, dependency graphs, license
  name: Snyk GraphQL API
  slug: snyk-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snyk.png
layout: provider
modified: '2026-05-19'
name: Snyk
nav: Providers
network: true
overview: 'Snyk publishes 46 APIs on the [APIs.io](https://apis.io/) network, including AccessRequests API, AiBom API, Apps API, and 43 more. Tagged areas include Security, DevSecOps, Vulnerability Management, Application Security, and SCA.


  Snyk''s developer surface includes authentication, documentation, API reference, engineering blog, and 11 more developer resources.'
plans:
- name: Snyk Plans Pricing
  plan_count: 4
  slug: snyk-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Snyk Rate Limits
  slug: snyk-rate-limits
score:
  band: thin
  composite: 34.2
  delta: -0.9
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 63.0
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 46
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snyk/refs/heads/main/screenshots/snyk-2026-06-20T194114.png
security:
- kind: authentication
  name: Snyk Authentication
  slug: snyk-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Snyk Domain Security
  slug: snyk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Snyk Vulnerability Disclosure
  slug: snyk-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Snyk Trust Center
  slug: snyk-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: snyk
tags:
- Security
- DevSecOps
- Vulnerability Management
- Application Security
- SCA
- SAST
- Container Security
- IaC
website: https://snyk.io/
---
