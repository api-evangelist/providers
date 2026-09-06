---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 134
  human_in_the_loop: 15
  name: Sonatype Agentic Access
  operation_count: 265
  slug: sonatype-agentic-access
  summary_line: 265 operations · 134 acting · 15 human-in-the-loop
api_count: 1
apis:
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use the Advanced Search REST API to perform searches on Lifecycle application scan reports.
  name: Sonatype Advanced Search API
  slug: sonatype-advanced-search-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use the Application Categories REST API to manage the application categories or tags assigned to the applications in an organization.
  name: Sonatype Application Categories API
  slug: sonatype-application-categories-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to retrieve the data from an application composition report, that is generated after an evaluation.
  name: Sonatype Application Report Data API
  slug: sonatype-application-report-data-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage applications. In addition to the primary functions of create, update and delete, you can also move applications from one organization to other.
  name: Sonatype Applications API
  slug: sonatype-applications-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to access the IQ Server audit logs.
  name: Sonatype Audit Logs API
  slug: sonatype-audit-logs-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to create and delete auto policy waiver exclusions.
  name: Sonatype Auto Policy Waiver Exclusions API
  slug: sonatype-auto-policy-waiver-exclusions-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to create, modify and retrieve auto policy waivers.
  name: Sonatype Auto Policy Waivers API
  slug: sonatype-auto-policy-waivers-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage CI integration configuration. Configurations can be set at organization or application level and are merged from the organization hierarchy with lower levels taking precede
  name: Sonatype CI Configuration API
  slug: sonatype-ci-configuration-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage components that are developed in-house and are not open-source. Claiming the component stores the identity information for the component hash and avoids triggering the Comp
  name: Sonatype Claim Components API
  slug: sonatype-claim-components-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage component labels for applications, organizations and repositories. Component Labels can be used as attributes of a component at the time of creating policies. A policy viol
  name: Sonatype Component Labels API
  slug: sonatype-component-labels-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to search for components in application evaluation reports.
  name: Sonatype Component Search API
  slug: sonatype-component-search-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to retrieve a component's security vulnerability data, license data, age and popularity.
  name: Sonatype Components API
  slug: sonatype-components-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: 'Use this REST API to access the composite source control management configuration (SCM) for an application or organization. Composite source control configuration is defined as the configuration that '
  name: Sonatype Composite Source Control API
  slug: sonatype-composite-source-control-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to validate the composite source control management (SCM) configuration. Composite source control configuration is defined as the configuration that is inherited from the parent or i
  name: Sonatype Composite Source Control Validator API
  slug: sonatype-composite-source-control-validator-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage the configuration of an existing Atlassian Crowd Server that is being used to authenticate users for IQ Server.
  name: Sonatype Config Crowd API
  slug: sonatype-config-crowd-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage Jira configurations to receive notifications from Lifecycle. It is supported for Jira Cloud, Jira Server, and Jira Data Center.
  name: Sonatype Config Jira API
  slug: sonatype-config-jira-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage the configuration of an SMTP server, to receive email notifications.
  name: Sonatype Config Mail API
  slug: sonatype-config-mail-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage the OIDC configuration for IQ Server.
  name: Sonatype Config OIDC API
  slug: sonatype-config-oidc-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage the configuration of IQ Server with an existing HTTP proxy server.
  name: Sonatype Config Proxy Server API
  slug: sonatype-config-proxy-server-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage the configuration of a reverse proxy server.
  name: Sonatype Config Reverse Proxy Authentication API
  slug: sonatype-config-reverse-proxy-authentication-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage the SAML configuration for IQ Server.
  name: Sonatype Config SAML API
  slug: sonatype-config-saml-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage the configuration of IQ Server with your Source Control Management (SCM) system (e.g. GitHub).
  name: Sonatype Config Source Control API
  slug: sonatype-config-source-control-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage the configuration of a Zscaler service.
  name: Sonatype Config Zscaler API
  slug: sonatype-config-zscaler-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to configure the IQ Server system properties. We strongly recommend using this REST API instead of config.yml for versions 142 and higher.
  name: Sonatype Configuration API
  slug: sonatype-configuration-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage the configuration of Firewall for JFrog Artifactory.
  name: Sonatype Configure Artifactory Connection API
  slug: sonatype-configure-artifactory-connection-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use the CPE Matching Configuration REST API to add/set/remove cpe matching configuration to organizations and applications
  name: Sonatype CPE Matching Configuration API
  slug: sonatype-cpe-matching-configuration-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use the CycloneDX REST API to generate CycloneDX SBOMs in XML or JSON formats, containing coordinates and licenses for components found in a scan report.
  name: Sonatype CycloneDX API
  slug: sonatype-cyclonedx-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Set policies for automatic purging of obsolete application and Success Metrics reports. <p>Note that IQ Server has a preset limit of purging 5000 reports in one execution of its report purging job.
  name: Sonatype Data Retention Policies API
  slug: sonatype-data-retention-policies-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to export Sonatype Developer component priorities data, including security reachability data.
  name: Sonatype Developer Priorities API
  slug: sonatype-developer-priorities-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: This REST API returns the OpenAPI documentation for the specified IQ Server REST API.
  name: Sonatype Endpoints API
  slug: sonatype-endpoints-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to enable/disable the IQ Server features.
  name: Sonatype Feature Configuration API
  slug: sonatype-feature-configuration-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API for managing and monitoring firewall features, including metrics, repository management, quarantine operations, and namespace confusion prevention.
  name: Sonatype Firewall API
  slug: sonatype-firewall-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: GitHub App configuration operations
  name: Sonatype GitHub App Configuration API
  slug: sonatype-github-app-configuration-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to retrieve license legal metadata in raw or HTML format.
  name: Sonatype License Legal Metadata Report API
  slug: sonatype-license-legal-metadata-report-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage and customize templates for the license legal metadata generated in HTML format.
  name: Sonatype License Legal Metadata Template API
  slug: sonatype-license-legal-metadata-template-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage license overrides for components in your applicationsorganizations and repositories.
  name: Sonatype License Overrides API
  slug: sonatype-license-overrides-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to create new organizations, retrieve, edit or delete existing organizations.
  name: Sonatype Organizations API
  slug: sonatype-organizations-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to retrieve details on all existing policies in your instance of Lifecycle.
  name: Sonatype Policies API
  slug: sonatype-policies-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: 'Use this REST API to perform an application policy evaluation. Policy evaluations are executed asynchronously.<p>This is a 2-step process that involves: 1. Requesting a policy evaluation (POST) 2. Che'
  name: Sonatype Policy Evaluation API
  slug: sonatype-policy-evaluation-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to obtain the violation details, violation details across stages (cross stage), violations occurring due to transitive dependencies and all waivers applicable to a violation. Cross-s
  name: Sonatype Policy Violation Details API
  slug: sonatype-policy-violation-details-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this rest API to fetch available policy waiver reasons
  name: Sonatype Policy Waiver Reasons API
  slug: sonatype-policy-waiver-reasons-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage policy waiver requests.
  name: Sonatype Policy Waiver Requests API
  slug: sonatype-policy-waiver-requests-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to create and retrieve policy waivers.
  name: Sonatype Policy Waivers API
  slug: sonatype-policy-waivers-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage a product license.
  name: Sonatype Product License API
  slug: sonatype-product-license-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to view application scan reports, generate a list of stale waivers, view existing policy waivers on components, view quarantined components and retrieve additional metrics data.
  name: Sonatype Reports API
  slug: sonatype-reports-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage quarantined components.
  name: Sonatype Repositories API
  slug: sonatype-repositories-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage authorizations for users or user groups. You can view existing role assignments and grant or revoke user authorization on organizations, applications and repositories.
  name: Sonatype Role Memberships API
  slug: sonatype-role-memberships-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: 'Roles provide sets of permissions that grant access to the functionality in the user interface, through integrations, and when using REST APIs. Permissions are granted by assigning users or groups to '
  name: Sonatype Roles API
  slug: sonatype-roles-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to retrieve security vulnerabilities that have been overridden.
  name: Sonatype Security Vulnerability Overrides API
  slug: sonatype-security-vulnerability-overrides-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: The Solutions API from Sonatype — 1 operation(s) for solutions.
  name: Sonatype Solutions API
  slug: sonatype-solutions-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to:<ul><li>Create, update and delete source control management (SCM) configuration for the root organization, sub-organizations and applications.</li><li>Automatically assign the dev
  name: Sonatype Source Control API
  slug: sonatype-source-control-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to view the response times of a source control evaluation.
  name: Sonatype Source Control Metrics API
  slug: sonatype-source-control-metrics-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to generate SPDX SBOMs in XML or JSON formats.
  name: Sonatype SPDX API
  slug: sonatype-spdx-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to scan SBOMs for your applications.
  name: Sonatype Third-Party Analysis API
  slug: sonatype-third-party-analysis-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage user token expiration configuration.
  name: Sonatype User Token Configuration API
  slug: sonatype-user-token-configuration-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage user tokens.
  name: Sonatype User Tokens API
  slug: sonatype-user-tokens-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to manage users.
  name: Sonatype Users API
  slug: sonatype-users-api
- baseURL: https://{iq-server-host}/
  baseurl_source: declared
  description: Use this REST API to retrieve vulnerability details.
  name: Sonatype Vulnerability Details API
  slug: sonatype-vulnerability-details-api
artifact_total: 132
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search API
  slug: open-sonatype-advanced-search-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Application Categories API
  slug: open-sonatype-application-categories-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Application Report Data API
  slug: open-sonatype-application-report-data-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Applications API
  slug: open-sonatype-applications-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Audit Logs API
  slug: open-sonatype-audit-logs-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Auto Policy Waiver Exclusions API
  slug: open-sonatype-auto-policy-waiver-exclusions-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Auto Policy Waivers API
  slug: open-sonatype-auto-policy-waivers-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search CI Configuration API
  slug: open-sonatype-ci-configuration-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Claim Components API
  slug: open-sonatype-claim-components-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Component Labels API
  slug: open-sonatype-component-labels-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Component Search API
  slug: open-sonatype-component-search-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Components API
  slug: open-sonatype-components-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Composite Source Control API
  slug: open-sonatype-composite-source-control-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Composite Source Control Validator API
  slug: open-sonatype-composite-source-control-validator-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Config Crowd API
  slug: open-sonatype-config-crowd-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Config Jira API
  slug: open-sonatype-config-jira-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Config Mail API
  slug: open-sonatype-config-mail-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Config OIDC API
  slug: open-sonatype-config-oidc-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Config Proxy Server API
  slug: open-sonatype-config-proxy-server-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Config Reverse Proxy Authentication API
  slug: open-sonatype-config-reverse-proxy-authentication-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Config SAML API
  slug: open-sonatype-config-saml-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Config Source Control API
  slug: open-sonatype-config-source-control-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Config Zscaler API
  slug: open-sonatype-config-zscaler-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Configuration API
  slug: open-sonatype-configuration-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Configure Artifactory Connection API
  slug: open-sonatype-configure-artifactory-connection-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search CPE Matching Configuration API
  slug: open-sonatype-cpe-matching-configuration-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search CycloneDX API
  slug: open-sonatype-cyclonedx-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Data Retention Policies API
  slug: open-sonatype-data-retention-policies-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Developer Priorities API
  slug: open-sonatype-developer-priorities-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Endpoints API
  slug: open-sonatype-endpoints-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Feature Configuration API
  slug: open-sonatype-feature-configuration-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Firewall API
  slug: open-sonatype-firewall-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search GitHub App Configuration API
  slug: open-sonatype-github-app-configuration-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search License Legal Metadata Report API
  slug: open-sonatype-license-legal-metadata-report-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search License Legal Metadata Template API
  slug: open-sonatype-license-legal-metadata-template-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search License Overrides API
  slug: open-sonatype-license-overrides-api
- collection_type: open
  name: Sonatype Lifecycle Public REST API
  slug: open-sonatype-lifecycle
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Organizations API
  slug: open-sonatype-organizations-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Policies API
  slug: open-sonatype-policies-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Policy Evaluation API
  slug: open-sonatype-policy-evaluation-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Policy Violation Details API
  slug: open-sonatype-policy-violation-details-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Policy Waiver Reasons API
  slug: open-sonatype-policy-waiver-reasons-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Policy Waiver Requests API
  slug: open-sonatype-policy-waiver-requests-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Policy Waivers API
  slug: open-sonatype-policy-waivers-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Product License API
  slug: open-sonatype-product-license-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Reports API
  slug: open-sonatype-reports-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Repositories API
  slug: open-sonatype-repositories-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Role Memberships API
  slug: open-sonatype-role-memberships-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Roles API
  slug: open-sonatype-roles-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Security Vulnerability Overrides API
  slug: open-sonatype-security-vulnerability-overrides-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Solutions API
  slug: open-sonatype-solutions-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Source Control API
  slug: open-sonatype-source-control-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Source Control Metrics API
  slug: open-sonatype-source-control-metrics-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search SPDX API
  slug: open-sonatype-spdx-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Third-Party Analysis API
  slug: open-sonatype-third-party-analysis-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search User Token Configuration API
  slug: open-sonatype-user-token-configuration-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search User Tokens API
  slug: open-sonatype-user-tokens-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Users API
  slug: open-sonatype-users-api
- collection_type: open
  name: Sonatype Lifecycle Public REST Advanced Search Vulnerability Details API
  slug: open-sonatype-vulnerability-details-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/sonatype-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sonatype-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sonatype-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sonatype-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sonatype
- group: start
  title: ''
  type: Portal
  url: https://www.sonatype.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.sonatype.com/
- group: company
  title: ''
  type: Website
  url: https://www.sonatype.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sonatype-nexus-community
- group: company
  title: ''
  type: Blog
  url: https://www.sonatype.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.sonatype.com/en/sonatype-iq-server-2025-release-notes.html
- group: operate
  title: ''
  type: Support
  url: https://support.sonatype.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sonatype.com/products/pricing
created: '2025-02-12'
description: Sonatype provides software supply chain management solutions including Sonatype Lifecycle (IQ Server), Sonatype Repository Firewall, SBOM Manager, and Nexus Repository. The Lifecycle Public REST API provides 188 endpoints for application portfolio management, policy enforcement, vulnerability reporting, component analysis, SBOM generation, source control integration, and software composition analysis across the SDLC.
examples:
- key_count: 3
  name: Sonatype List Applications Example
  slug: sonatype-list-applications-example
- key_count: 3
  name: Sonatype Search Component Example
  slug: sonatype-search-component-example
finops:
- name: Sonatype Finops
  service_category: API
  slug: sonatype-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sonatype.png
json_schemas:
- name: Sonatype Lifecycle Application
  property_count: 6
  slug: sonatype-application
- name: Sonatype Policy Violation
  property_count: 8
  slug: sonatype-policy-violation
json_structures:
- name: Sonatype Application Structure
  property_count: 0
  slug: sonatype-application-structure
jsonld:
- class_count: 2
  name: Sonatype Context
  property_count: 12
  slug: sonatype-context
layout: provider
modified: '2026-05-19'
name: Sonatype
nav: Providers
network: true
overview: 'Sonatype publishes 58 APIs on the [APIs.io](https://apis.io/) network, including Advanced Search API, Application Categories API, Application Report Data API, and 55 more. Tagged areas include Software Supply Chain, Security, Vulnerability Management, SBOM, and Software Composition Analysis.


  The Sonatype catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sonatype''s developer surface includes authentication, developer portal, documentation, GitHub presence, engineering blog, changelog, support, and 6 more developer resources.'
plans:
- name: Sonatype Plans Pricing
  plan_count: 3
  slug: sonatype-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Sonatype Rate Limits
  slug: sonatype-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sonatype API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sonatype-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Sonatype API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: sonatype-rules
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 55.5
    catalog_earned_first_party: 0.0
    catalog_gap: 59.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 57.3
    developer_ergonomics: 45.2
    discoverability: 44.4
    governance: 13.6
    operational_transparency: 13.2
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 58
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sonatype/refs/heads/main/screenshots/sonatype-2026-06-20T194159.png
security:
- kind: authentication
  name: Sonatype Authentication
  slug: sonatype-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Sonatype Domain Security
  slug: sonatype-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sonatype
tags:
- Software Supply Chain
- Security
- Vulnerability Management
- SBOM
- Software Composition Analysis
- DevSecOps
website: https://www.sonatype.com/
---
