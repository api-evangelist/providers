---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-08-26'
api_count: 26
apis:
- description: 'Manage users, accounts, and account groups in the ThousandEyes platform using the Administrative API. This API provides the following operations to manage your organization: * `/account-groups`: Accou'
  name: ThousandEyes Administrative API
  slug: thousandeyes-administrative-api
- description: Manage your ThousandEyes OpenAPI bearer token.
  name: ThousandEyes API Token Management API
  slug: thousandeyes-api-token-management-api
- description: Manage Cloud and Enterprise Agents available to your account in ThousandEyes.
  name: ThousandEyes Agents API
  slug: thousandeyes-agents-api
- description: 'You can manage the following alert functionalities on the ThousandEyes platform using the Alerts API: * **Alerts**: Retrieve alert details. Alerts are assigned to tests through alert rules. * **Alert '
  name: ThousandEyes Alerts API
  slug: thousandeyes-alerts-api
- description: Retrieve information that ThousandEyes holds about Autonomous Systems.
  name: ThousandEyes Autonomous Systems API
  slug: thousandeyes-autonomous-systems-api
- description: 'Retrieve information about BGP monitors available to your ThousandEyes account. ThousandEyes ingests BGP routing data from dozens of global BGP collectors and automatically integrates that visibility '
  name: ThousandEyes BGP Monitors API
  slug: thousandeyes-bgp-monitors-api
- description: 'The Cloud Insights Integrations API lets you programmatically manage **AWS** and **Azure** monitoring integrations in ThousandEyes. ### What You Can Do - **List** all integrations. - **Get** details f'
  name: ThousandEyes Cloud Insights Integrations API
  slug: thousandeyes-cloud-insights-integrations-api
- description: 'Manage credentials for transaction tests using the Credentials API. The following permissions are required to access Credentials API operations: * `Settings Tests Read` for read operations. * `Setting'
  name: ThousandEyes Credentials API
  slug: thousandeyes-credentials-api
- description: Manage ThousandEyes Dashboards.
  name: ThousandEyes Dashboards API
  slug: thousandeyes-dashboards-api
- description: The Emulation API facilitates the retrieval of user-agent strings for HTTP, pageload, and transaction tests. It also enables the retrieval and addition of emulated devices for pageload and transaction
  name: ThousandEyes Emulation API
  slug: thousandeyes-emulation-api
- description: Manage ThousandEyes Endpoint Agents using this API. For more information about Endpoint Agents, see Endpoint Agents.
  name: ThousandEyes Endpoint Agents API
  slug: thousandeyes-endpoint-agents-api
- description: You can create and execute a new endpoint instant scheduled test within ThousandEyes using this API. The test parameters are specified in the `POST` data. The following applies to the Endpoint Instant
  name: ThousandEyes Endpoint Instant Scheduled Tests API
  slug: thousandeyes-endpoint-instant-scheduled-tests-api
- description: Manage labels applied to endpoint agents using this API.
  name: ThousandEyes Endpoint Agent Labels API
  slug: thousandeyes-endpoint-agent-labels-api
- description: Retrieve results for scheduled and dynamic tests on endpoint agents.
  name: ThousandEyes Endpoint Test Results API
  slug: thousandeyes-endpoint-test-results-api
- description: Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API.
  name: ThousandEyes Endpoint Tests API
  slug: thousandeyes-endpoint-tests-api
- description: Event detection occurs when ThousandEyes identifies that error signals related to a component (proxy, network node, AS, server etc) have deviated from the baselines established by events. * To determi
  name: ThousandEyes Event Detection API
  slug: thousandeyes-event-detection-api
- description: Manage connectors and operations.
  name: ThousandEyes Integrations API
  slug: thousandeyes-integrations-api
- description: 'We are happy to announce the release of the Internet Insights API set. This limited release includes endpoints that: * Make our catalog provider and Internet outage data accessible to API users. * Pro'
  name: ThousandEyes Internet Insights API
  slug: thousandeyes-internet-insights-api
- description: Creates a new test snapshot in ThousandEyes.
  name: ThousandEyes Test Snapshots API
  slug: thousandeyes-test-snapshots-api
- description: 'The ThousandEyes Tags API provides a tagging system with key/value pairs. It allows you to tag assets within the ThousandEyes platform (such as agents, tests, or dashboards) with meaningful metadata. '
  name: ThousandEyes Tags API
  slug: thousandeyes-tags-api
- description: 'Templates provide a streamlined approach to creating multiple tests (Synthetic/CEA and Endpoint), tags, alert rules, dashboards, labels (deprecated) and other assets within ThousandEyes from a single '
  name: ThousandEyes Templates API
  slug: thousandeyes-templates-api
- description: This API allows you to list, create, edit, and delete Network and Application Synthetics tests.
  name: ThousandEyes Tests API
  slug: thousandeyes-tests-api
- description: The Instant Tests API operations lets you create and run new instant tests. You will need to be an Account Admin. The response does not include the immediate test results. Use the Test Results endpoin
  name: ThousandEyes Instant Tests API
  slug: thousandeyes-instant-tests-api
- description: Get test result metrics for Network and Application Synthetics tests.
  name: ThousandEyes Test Results API
  slug: thousandeyes-test-results-api
- description: '* Traces * Connected Devices * OTel-based integrations that rely on connectors and operations, including: * Splunk Cloud Platform HEC * Splunk Enterprise HEC * Splunk Observability APM * Dynatrace Obs'
  name: ThousandEyes ThousandEyes for OpenTelemetry API
  slug: thousandeyes-opentelemetry-api
- description: 'These usage endpoints define the following operations: * **Usage**: Retrieve usage data for the specified time period (default is one month). * Users must have the `View organization usage` permission'
  name: ThousandEyes Usage API
  slug: thousandeyes-usage-api
artifact_total: 35
asyncapis:
- description: ''
  name: Thousandeyes Webhooks
  slug: thousandeyes-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thousandeyes-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thousandeyes-authentication.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/thousandeyes/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thousandeyes.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cisco.com/docs/thousandeyes/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thousandeyes
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/CiscoDevNet/ThousandEyes-MCP-Server-official
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/thousandeyes/thousandeyes-sdk-python
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- group: company
  title: ''
  type: Website
  url: https://www.thousandeyes.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cisco.com/thousandeyes/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cisco.com/docs/thousandeyes/getting-started/
- group: start
  title: ''
  type: Quickstart
  url: https://docs.thousandeyes.com/product-documentation/getting-started/getting-started-with-the-thousandeyes-api
- group: operate
  title: ''
  type: Support
  url: https://developer.cisco.com/docs/thousandeyes/developer-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.thousandeyes.com/
- group: operate
  title: ''
  type: Community
  url: https://community.cisco.com/t5/thousandeyes/bd-p/disc-thousandeyes
- group: company
  title: ''
  type: Blog
  url: https://blogs.cisco.com/tag/cisco-thousandeyes
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thousandeyes.com
- group: start
  title: ''
  type: Login
  url: https://app.thousandeyes.com/login
- group: start
  title: ''
  type: SignUp
  url: https://app.thousandeyes.com/login?fwd=%2Fsignup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cisco.com/c/en/us/products/collateral/security/cisco-thousandeyes-og.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.cisco.com/site/license/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/cisco/cisco-devnet-s-public-workspace/collection/v2ogbsf/cisco-thousandeyes-api-v7
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.cisco.com/docs/thousandeyes/thousandeyes-api-license-terms-and-support-policy/
- group: auth
  title: ''
  type: Security
  url: https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html
- group: auth
  title: ''
  type: Compliance
  url: https://trustportal.cisco.com/c/r/ctp/trust-portal.html
- group: build
  title: ''
  type: SDKs
  url: packages/thousandeyes-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/thousandeyes-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/thousandeyes-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thousandeyes-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thousandeyes-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/thousandeyes-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/thousandeyes-tool-crosswalk.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thousandeyes-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/thousandeyes-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thousandeyes-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/thousandeyes-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/thousandeyes-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/thousandeyes-trust-center.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thousandeyes-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/thousandeyes-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/thousandeyes-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/thousandeyes-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thousandeyes-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/thousandeyes-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-19'
description: ThousandEyes is Cisco's digital experience monitoring platform, acquired in 2020 and operated as part of Cisco Networking. It runs a global fleet of Cloud, Enterprise, Endpoint and Connected Device agents that measure network paths, BGP routing, DNS, application response and internet outages end to end, then exposes that telemetry through the ThousandEyes v7 REST API. The v7 API is documented on Cisco DevNet and publishes 26 downloadable OpenAPI 3.0 documents plus a unified document covering 326 operations across tests, instant tests, test results, agents, endpoint agents, alerts, event detection, dashboards, tags, templates, integrations, credentials, Internet Insights, Cloud Insights, usage and administration. Authentication is a bearer API token, with an OAuth 2.0 authorization-code and device-code flow advertised anonymously at /.well-known/oauth-authorization-server. Cisco also runs a remote MCP server at https://api.thousandeyes.com/mcp with about 51 documented tools,
  generated SDKs for Python, Java and Go, a Go CLI, a Terraform provider, a public Postman collection and a ThousandEyes for Government FedRAMP Moderate instance.
image: https://docs.thousandeyes.com/~gitbook/image?url=https%3A%2F%2F1112912342-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M4QARF6s57qxMrOHDTZ%252Favatar-1586888079651.png%3Fgeneration%3D1586888079959831%26alt%3Dmedia&width=180&height=180&sign=8b5c0248&sv=2
layout: provider
mcp_servers:
- description: ''
  name: ThousandEyes MCP Server
  slug: thousandeyes-mcp-server
modified: '2026-08-19'
name: ThousandEyes
nav: Providers
network: true
overview: 'ThousandEyes publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Administrative API, API Token Management API, Agents API, and 23 more. Tagged areas include Monitoring, Network Visibility, Digital Experience, Observability, and Networking.


  The ThousandEyes catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ThousandEyes'' developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, quickstart, support, and 41 more developer resources.'
plans:
- name: Thousandeyes Plans Pricing
  plan_count: 7
  slug: thousandeyes-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Thousandeyes Rate Limits
  slug: thousandeyes-rate-limits
scopes:
- name: Thousandeyes Scopes
  scope_count: 2
  slug: thousandeyes-scopes
  summary_line: 2 scopes · authorizationCode/deviceCode
score:
  band: exemplar
  composite: 70.2
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 16.7
    contract_quality: 63.1
    developer_ergonomics: 73.2
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 92.1
  previous_composite: 70.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 26
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Thousandeyes Authentication
  slug: thousandeyes-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Thousandeyes Domain Security
  slug: thousandeyes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Thousandeyes Vulnerability Disclosure
  slug: thousandeyes-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Thousandeyes Trust Center
  slug: thousandeyes-trust-center
  summary_line: FedRAMP Moderate
slug: thousandeyes
tags:
- Monitoring
- Network Visibility
- Digital Experience
- Observability
- Networking
- Enterprise
- Synthetic Monitoring
- BGP
- Internet Insights
- Endpoint Monitoring
- OpenTelemetry
- Cisco
website: https://www.thousandeyes.com/
---
