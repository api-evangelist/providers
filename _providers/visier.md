---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 184
  human_in_the_loop: 10
  name: Visier Agentic Access
  operation_count: 366
  slug: visier-agentic-access
  summary_line: 366 operations · 184 acting · 10 human-in-the-loop
api_count: 51
apis:
- description: Visier's hosted Model Context Protocol server, exposing Vee (natural-language workforce question answering) and structured data-query tools to MCP clients such as Claude Desktop and Cursor over HTTPS/
  name: Visier Query MCP Server
  slug: query-mcp
- description: Create, retrieve, update, and delete analytic objects in your analytic model. You can create, update, and delete one or more analytic objects in an API call. The supported analytic objects are <em>sub
  name: Visier Analytic Objects V2 API
  slug: visier-analyticobjectsv2-api
- description: Request an authentication token through basic authentication. With basic authentication, use your username and password to request a secure token. The response returns an ASID token that you can use i
  name: Visier Basic Authentication API
  slug: visier-basicauthentication-api
- description: Get benchmark values.
  name: Visier Benchmarks API
  slug: visier-benchmarks-api
- description: Create, retrieve, update, and delete concepts in your analytic model. You can create, update, and delete one or more concepts in an API call.
  name: Visier Concepts V2 API
  slug: visier-conceptsv2-api
- description: Manage your consolidated analytics (CA) tenants in Visier, such as retrieving the details of CA tenants, creating CA tenants, adding or deleting source tenants from CA tenants, and excluding sources f
  name: Visier Consolidated Analytics API
  slug: visier-consolidatedanalytics-api
- description: Initiate and manage jobs, included or excluded data, and data connector credentials. Administrating tenant users can manage jobs and data for their analytic tenants.
  name: Visier Data And Job Handling API
  slug: visier-dataandjobhandling-api
- description: Manage data export connectors and credentials, and run data export connector jobs. Data export connectors send Visier data to external systems, such as Databricks or Snowflake. Use these APIs to manag
  name: Visier Data Export Connectors API API
  slug: visier-dataexportconnectorsapi-api
- description: Send raw or untransformed data to Visier. After we receive the data, Visier runs business rules to transform your data into the expected format for the existing mappings. <br>**Note:** <em>This API is
  name: Visier Data Intake API
  slug: visier-dataintake-api
- description: Discover the objects that make up your Visier solution and provide detailed information on the object's schema. You can retrieve detailed information about objects in Visier by retrieving a list of al
  name: Visier Data Model API
  slug: visier-datamodel-api
- description: Query against your data in Visier to get aggregate and list data.
  name: Visier Data Query API
  slug: visier-dataquery-api
- description: Send data files to Visier. After we receive the data, Visier starts a receiving job and a processing job to process the data.
  name: Visier Data Upload API
  slug: visier-dataupload-api
- description: Export Visier data version information, such as tables, columns, and file information, in CSV format. <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way with
  name: Visier Data Version Export API
  slug: visier-dataversionexport-api
- description: Discover dimensions and members. A dimension organizes unique values of an attribute into a list or a hierarchical structure of members. The structure can be navigated to discover the members, and the
  name: Visier Dimensions API
  slug: visier-dimensions-api
- description: Create, retrieve, update, and delete dimensions in your analytic model. You can create, update, and delete one or more dimensions in an API call. <br>**Note:** <em>This API is in **alpha**. While in a
  name: Visier Dimensions V2 API
  slug: visier-dimensionsv2-api
- description: Use the Direct Data Intake API to load data directly into Visier objects. These objects can be delivered as part of Visier Blueprint, locally modified objects, or even completely custom objects. Objec
  name: Visier Direct Data Intake API
  slug: visier-directdataintake-api
- description: Manage the list of user email address domains that are allowed in your tenant. <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionali
  name: Visier Email Domains API
  slug: visier-emaildomains-api
- description: Manage the encryption keys in your Visier tenant. Administrating tenants can specify the tenant in which to manage keys using the `TargetTenantID` header. For PGP keys, see `/v1/api/pgp-keys`. <br>**N
  name: Visier Encryption Keys API
  slug: visier-encryptionkeys-api
- description: Access over 3,300 standard jobs and get complete details in 27 languages, such as alternative titles, descriptions, and skills.
  name: Visier Jobs Library API
  slug: visier-jobs-library-api
- description: Create, retrieve, update, and delete simple and derived metrics in your analytic model. A simple metric is a metric based on one or more analytic objects. A derived metric is a metric based on a simpl
  name: Visier Metrics V2 API
  slug: visier-metricsv2-api
- description: Manage the IP addresses that can call Visier APIs. <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no de
  name: Visier Network Subnets API
  slug: visier-networksubnets-api
- description: Request an authentication token through OAuth 2.0 with Open ID Connect (OIDC). With OAuth 2.0 with OIDC, use an OAuth 2.0 grant to request an authentication token. The response returns a JSON Web Toke
  name: Visier O Auth2 API
  slug: visier-oauth2-api
- description: Manage objects in your analytic model.
  name: Visier Object Configuration API
  slug: visier-objectconfiguration-api
- description: 'Manage permissions in Visier, such as retrieving the details of a permission, content package, or data access set, creating new permissions and data access sets, and updating or deleting permissions. '
  name: Visier Permissions API
  slug: visier-permissions-api
- description: Manage your personalized alerts in Visier. Alerts notify you if a metric exceeds your defined threshold. <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way w
  name: Visier Personalized Alerts API
  slug: visier-personalizedalerts-api
- description: The Pretty Good Privacy (PGP) Keys API generates key pairs and provides a public key to encrypt data that you send to Visier. PGP encryption adds an additional layer of security against data disclosur
  name: Visier PGP Keys API
  slug: visier-pgpkeys-api
- description: Manage collaboration projects in your plans, including actions such as consolidating and reopening subplans.
  name: Visier Plan Administration API
  slug: visier-planadministration-api
- description: Send data directly to your plan's scenario and optionally add or remove rows from your plan.
  name: Visier Plan Data Load API
  slug: visier-plandataload-api
- description: Retrieve details about planning events such as member promotions and row changes.
  name: Visier Plan Events API
  slug: visier-planevents-api
- description: Use this API to retrieve information about data versions that were published to production. In Visier, production is the version of Visier available to your end users.
  name: Visier Production Versions API
  slug: visier-productionversions-api
- description: Manage the profiles assigned to users, such as assigning or removing a profile from a list of users and retrieving profile details. Administrating tenant users can manage profiles at the administratin
  name: Visier Profiles API
  slug: visier-profiles-api
- description: Create projects, publish projects, and retrieve project details.
  name: Visier Projects API
  slug: visier-projects-api
- description: Manage the Visier product release versions for your tenants. <br>**Note:** <em>This API is available for Embedded Partners.</em> <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may ch
  name: Visier Release Version Configuration API
  slug: visier-releaseversionconfiguration-api
- description: 'Create, retrieve, delete, copy, and download reports. <br>**Note**: This API is available for Embedded Partners. <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaki'
  name: Visier Reporting API
  slug: visier-reporting-api
- description: Search for documents, such as analyses, in Visier. <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no de
  name: Visier Search API
  slug: visier-search-api
- description: Manage your sidecar solution's configuration. A sidecar solution is a unique solution built using the Visier platform, such as Smart Compensation. Use this API to retrieve the current settings, update
  name: Visier Sidecar Solutions API
  slug: visier-sidecarsolutions-api
- description: Access over 14,000 skills and get complete skill details in 27 languages, such as alternative titles, descriptions, and hierarchies.
  name: Visier Skills Library API
  slug: visier-skills-library-api
- description: 'Download a tenants source files. <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices '
  name: Visier Source Files Download API
  slug: visier-sourcefilesdownload-api
- description: Export and import sources in Visier. <br>**Note:** <em>This API is in **beta**. While in beta, APIs are interface-stable and implementation may change without notice. Rarely, interface changes may occ
  name: Visier Sources API
  slug: visier-sources-api
- description: Check the health and status of Visier's platform and services.
  name: Visier System Status API
  slug: visier-systemstatus-api
- description: Use row-based management for your source data in Visier. The Table Source API supports direct SQL-based data modifications, eliminating concerns about file management or override behavior. Use the API
  name: Visier Table Source API
  slug: visier-tablesource-api
- description: Create analytic tenants, retrieve tenant information, and validate metric values.
  name: Visier Tenants V1 API
  slug: visier-tenantsv1-api
- description: 'Create analytic tenants, deprovision tenants, retrieve tenant information, and update tenant information. Tenants V2 improves upon Tenants V1 in the following ways: * Programmatically assign a Home an'
  name: Visier Tenants V2 API
  slug: visier-tenantsv2-api
- description: Manage user groups in Visier, such as creating, updating, and deleting user groups in bulk.
  name: Visier User Groups V2 API
  slug: visier-usergroupsv2-api
- description: Manage users within an organization, such as assigning permissions to users and retrieving user permission assignments and application logs. <br>**Tip:** Visier recommends that administrating tenant u
  name: Visier Users V1 API
  slug: visier-usersv1-api
- description: Manage users in bulk, such as creating, updating, and deleting many users. <br>**Tip:** Visier recommends that administrating tenant users focus primarily on managing users at the administrating tenan
  name: Visier Users V2 API
  slug: visier-usersv2-api
- description: Manage users within an organization. Users V3 offers the ability to update or insert (upsert) a user.
  name: Visier Users V3 API
  slug: visier-usersv3-api
- description: 'Manage Vee v2 instructions and safeguards for a tenant. Instructions guide Vee''s behavior when responding to queries. Safeguards prevent Vee from responding to certain types of queries. <br>**Note:** '
  name: Visier Vee Configuration API
  slug: visier-veeconfiguration-api
- description: Use Vee through Visier APIs, such as asking questions, submitting feedback, and getting sample questions.
  name: Visier Vee V1 API
  slug: visier-veev1-api
- description: Use Vee through Visier APIs, such as getting sample questions. Vee V2 improves upon Vee V1 by aligning response field names with the Vee UI.
  name: Visier Vee V2 API
  slug: visier-veev2-api
- description: 'Create, manage, and retrieve webhook definitions. Use webhooks to register your own HTTPS endpoints with Visier and listen for specific events. When these events occur, Visier sends an API request to '
  name: Visier Webhooks API
  slug: visier-webhooks-api
artifact_total: 111
asyncapis:
- description: ''
  name: Visier Webhooks
  slug: visier-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Visier Analytic Model Analytic Objects V2 API
  slug: open-visier-analyticobjectsv2-api
- collection_type: open
  name: Visier Authentication Basic Authentication API
  slug: open-visier-basicauthentication-api
- collection_type: open
  name: Compensation Benchmarks API
  slug: open-visier-benchmarks-api
- collection_type: open
  name: Visier Analytic Model Concepts V2 API
  slug: open-visier-conceptsv2-api
- collection_type: open
  name: Visier Administration Consolidated Analytics API
  slug: open-visier-consolidatedanalytics-api
- collection_type: open
  name: Visier Data In Data And Job Handling API
  slug: open-visier-dataandjobhandling-api
- collection_type: open
  name: Visier Data Out Data Export Connectors API API
  slug: open-visier-dataexportconnectorsapi-api
- collection_type: open
  name: Visier Data In Data Intake API
  slug: open-visier-dataintake-api
- collection_type: open
  name: Visier Analytic Model Data Model API
  slug: open-visier-datamodel-api
- collection_type: open
  name: Visier Data Out Data Query API
  slug: open-visier-dataquery-api
- collection_type: open
  name: Visier Data In Data Upload API
  slug: open-visier-dataupload-api
- collection_type: open
  name: Visier Data Out Data Version Export API
  slug: open-visier-dataversionexport-api
- collection_type: open
  name: Compensation Benchmarks Dimensions API
  slug: open-visier-dimensions-api
- collection_type: open
  name: Visier Analytic Model Dimensions V2 API
  slug: open-visier-dimensionsv2-api
- collection_type: open
  name: Visier Data In Direct Data Intake API
  slug: open-visier-directdataintake-api
- collection_type: open
  name: Visier Administration Email Domains API
  slug: open-visier-emaildomains-api
- collection_type: open
  name: Visier Administration Encryption Keys API
  slug: open-visier-encryptionkeys-api
- collection_type: open
  name: Skills Intelligence Engine Jobs Library API
  slug: open-visier-jobs-library-api
- collection_type: open
  name: Visier Analytic Model Metrics V2 API
  slug: open-visier-metricsv2-api
- collection_type: open
  name: Visier Administration Network Subnets API
  slug: open-visier-networksubnets-api
- collection_type: open
  name: Visier Authentication O Auth2 API
  slug: open-visier-oauth2-api
- collection_type: open
  name: Visier Analytic Model Object Configuration API
  slug: open-visier-objectconfiguration-api
- collection_type: open
  name: Visier Administration Permissions API
  slug: open-visier-permissions-api
- collection_type: open
  name: Visier Analytic Model Personalized Alerts API
  slug: open-visier-personalizedalerts-api
- collection_type: open
  name: Visier Data In PGP Keys API
  slug: open-visier-pgpkeys-api
- collection_type: open
  name: Visier Planning Public Plan Administration API
  slug: open-visier-planadministration-api
- collection_type: open
  name: Visier Planning Public Plan Data Load API
  slug: open-visier-plandataload-api
- collection_type: open
  name: Visier Planning Public Plan Events API
  slug: open-visier-planevents-api
- collection_type: open
  name: Visier Administration Production Versions API
  slug: open-visier-productionversions-api
- collection_type: open
  name: Visier Administration Profiles API
  slug: open-visier-profiles-api
- collection_type: open
  name: Visier Administration Projects API
  slug: open-visier-projects-api
- collection_type: open
  name: Visier Administration Release Version Configuration API
  slug: open-visier-releaseversionconfiguration-api
- collection_type: open
  name: Visier Data Out Reporting API
  slug: open-visier-reporting-api
- collection_type: open
  name: Visier Data Out Search API
  slug: open-visier-search-api
- collection_type: open
  name: Visier Administration Sidecar Solutions API
  slug: open-visier-sidecarsolutions-api
- collection_type: open
  name: Skills Intelligence Engine Skills Library API
  slug: open-visier-skills-library-api
- collection_type: open
  name: Visier Data Out Source Files Download API
  slug: open-visier-sourcefilesdownload-api
- collection_type: open
  name: Visier Administration Sources API
  slug: open-visier-sources-api
- collection_type: open
  name: Visier Administration System Status API
  slug: open-visier-systemstatus-api
- collection_type: open
  name: Visier Data In Table Source API
  slug: open-visier-tablesource-api
- collection_type: open
  name: Visier Administration Tenants V1 API
  slug: open-visier-tenantsv1-api
- collection_type: open
  name: Visier Administration Tenants V2 API
  slug: open-visier-tenantsv2-api
- collection_type: open
  name: Visier Administration User Groups V2 API
  slug: open-visier-usergroupsv2-api
- collection_type: open
  name: Visier Administration Users V1 API
  slug: open-visier-usersv1-api
- collection_type: open
  name: Visier Administration Users V2 API
  slug: open-visier-usersv2-api
- collection_type: open
  name: Visier Administration Users V3 API
  slug: open-visier-usersv3-api
- collection_type: open
  name: Visier Administration Vee Configuration API
  slug: open-visier-veeconfiguration-api
- collection_type: open
  name: Visier Data Out Vee V1 API
  slug: open-visier-veev1-api
- collection_type: open
  name: Visier Data Out Vee V2 API
  slug: open-visier-veev2-api
- collection_type: open
  name: Visier Webhooks API
  slug: open-visier-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/visier-administration-apis-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.visier.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.visier.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.visier.com/developer/Default.htm
- group: docs
  title: ''
  type: APIReference
  url: https://docs.visier.com/developer/apis/apis.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.visier.com/developer/apis/apis-get-started-home.htm
- group: operate
  title: ''
  type: Support
  url: https://my.visier.com/csm?id=community_home
- group: company
  title: ''
  type: Blog
  url: https://www.visier.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/visier
- group: start
  title: ''
  type: SignUp
  url: https://www.visier.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.visier.com/terms-of-use-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.visier.com/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/visier-alpine?tab=collections
- group: operate
  title: ''
  type: StatusPage
  url: https://status.visier.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.visier.com/developer/apis/version-control.htm
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/visier-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.visier.com/.well-known/security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/visier-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.visier.com/trust/compliance/
- group: build
  title: ''
  type: CLI
  url: cli/visier-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/visier-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/visier-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/visier-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/visier-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/visier-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/visier-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/visier-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/visier-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/visier-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/visier-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/visier-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/visier-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/visier-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/visier-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/visier-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/visier-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/visier-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/visier-agentic-access.yml
created: '2026-08-02'
description: Visier is a workforce and people analytics platform that consolidates HR, talent, compensation, and operational data into a purpose-built people data model, then exposes that model for analysis, planning, and AI-assisted question answering. Visier publishes a broad suite of public REST APIs — Data In (Direct Data Intake, Data Upload, job handling), Data Out (Data Query, Vee, exports), Administration (tenants, users, profiles, permissions, projects), Analytic Model (data model, concepts, metrics, dimensions), Planning, Webhooks, and dataset APIs such as Compensation Benchmarks and the Skills Intelligence Engine. OpenAPI v3 definitions for every collection are published on GitHub at visier/openapi-clients, generated Python SDKs ship to PyPI, and a hosted Visier Query MCP server exposes Vee and data-query tools to MCP clients over OAuth 2.0.
image: https://www.visier.com/static/visier-og-image-289b36a6392a307b7342ffcf69bdee4c.jpg
layout: provider
mcp_servers:
- description: ''
  name: Visier Query MCP Server
  slug: visier-query-mcp-server
modified: '2026-08-02'
name: Visier
nav: Providers
network: true
overview: 'Visier publishes 50 APIs on the [APIs.io](https://apis.io/) network, including Analytic Objects V2 API, Basic Authentication API, Benchmarks API, and 47 more. Tagged areas include Company, People Analytics, Workforce Analytics, Human Resources, and HR Technology.


  The Visier catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Visier''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 32 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 2
  name: Visier Rate Limits
  slug: visier-rate-limits
scopes:
- name: Visier Scopes
  scope_count: 2
  slug: visier-scopes
  summary_line: 2 scopes · authorizationCode/password
score:
  band: strong
  composite: 57.5
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 16.7
    contract_quality: 57.2
    developer_ergonomics: 82.7
    discoverability: 57.4
    governance: 16.7
    operational_transparency: 68.4
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 50
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/visier/refs/heads/main/screenshots/visier-2026-08-17T082801.png
security:
- kind: authentication
  name: Visier Authentication
  slug: visier-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Visier Domain Security
  slug: visier-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Visier Vulnerability Disclosure
  slug: visier-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Visier Trust Center
  slug: visier-trust-center
  summary_line: SOC 2, CSA STAR Level 1
slug: visier
tags:
- Company
- People Analytics
- Workforce Analytics
- Human Resources
- HR Technology
- Workforce Planning
- Analytics
- Business Intelligence
- Compensation
- Skills
- Artificial Intelligence
- MCP
website: https://www.visier.com/
---
