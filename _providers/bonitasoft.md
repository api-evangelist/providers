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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-02'
api_count: 2
apis:
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Activity
  name: Bonitasoft Activity API
  slug: bonitasoft-activity-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ActivityVariable
  name: Bonitasoft Activity Variable API
  slug: bonitasoft-activityvariable-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Actor
  name: Bonitasoft Actor API
  slug: bonitasoft-actor-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ActorMember
  name: Bonitasoft Actor Member API
  slug: bonitasoft-actormember-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Manage applications. This enables you to build a consistent functional applicative environment for users to interact with business processes and business data from one place.
  name: Bonitasoft Application API
  slug: bonitasoft-application-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: 'Manage the set of menus in an application. This set of menus enables a user to navigate to the application pages. There are two types of menu item: A top-level item appears in the navigation bar of th'
  name: Bonitasoft Application Menu API
  slug: bonitasoft-applicationmenu-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: An application page is a custom page that has been associated with an application. Use this resource to manage application pages and define the paths used to access them. This list of pages will be us
  name: Bonitasoft Application Page API
  slug: bonitasoft-applicationpage-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ArchivedActivity
  name: Bonitasoft Archived Activity API
  slug: bonitasoft-archivedactivity-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ArchivedActivityVariable
  name: Bonitasoft Archived Activity Variable API
  slug: bonitasoft-archivedactivityvariable-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ArchivedConnectorInstance
  name: Bonitasoft Archived Connector Instance API
  slug: bonitasoft-archivedconnectorinstance-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Archived version of the Failure leading a BPM entity instance to a failed state. This Web REST API is available in **Enterprise editions only**, since version 10.3 (2025.1).
  name: Bonitasoft Archived Failure API
  slug: bonitasoft-archivedfailure-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ArchivedFlowNode
  name: Bonitasoft Archived Flow Node API
  slug: bonitasoft-archivedflownode-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ArchivedHumanTask
  name: Bonitasoft Archived Human Task API
  slug: bonitasoft-archivedhumantask-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ArchivedManualTask
  name: Bonitasoft Archived Manual Task API
  slug: bonitasoft-archivedmanualtask-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ArchivedProcessInstance
  name: Bonitasoft Archived Process Instance API
  slug: bonitasoft-archivedprocessinstance-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ArchivedProcessInstanceComment
  name: Bonitasoft Archived Process Instance Comment API
  slug: bonitasoft-archivedprocessinstancecomment-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ArchivedProcessInstanceDocument
  name: Bonitasoft Archived Process Instance Document API
  slug: bonitasoft-archivedprocessinstancedocument-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ArchivedProcessInstanceVariable
  name: Bonitasoft Archived Process Instance Variable API
  slug: bonitasoft-archivedprocessinstancevariable-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ArchivedTask
  name: Bonitasoft Archived Task API
  slug: bonitasoft-archivedtask-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ArchivedUserTask
  name: Bonitasoft Archived User Task API
  slug: bonitasoft-archivedusertask-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Authentication
  name: Bonitasoft Authentication API
  slug: bonitasoft-authentication-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: 'Show status or install or update the Business Data Model. Installing or updating a BDM needs to be done in two successive steps: 1. Upload a BDM file 2. Install/Update the previously uploaded file **T'
  name: Bonitasoft BDM API
  slug: bonitasoft-bdm-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: BDM Access control is available to protect the BDM. You can use this API to get the access control status (lastUpdatedBy, lastUpdateDate...).
  name: Bonitasoft BDM Access Control API
  slug: bonitasoft-bdmaccesscontrol-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: BDM Rest APIs allow to create / update / delete / import in bulk Bonita Business Data.
  name: Bonitasoft Business Data Operations API
  slug: bonitasoft-business-data-operations-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: BDM Rest APIs allow to query Bonita Business Data.
  name: Bonitasoft Business Data Query API
  slug: bonitasoft-businessdataquery-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ConnectorFailure
  name: Bonitasoft Connector Failure API
  slug: bonitasoft-connectorfailure-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ConnectorInstance
  name: Bonitasoft Connector Instance API
  slug: bonitasoft-connectorinstance-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: CustomUser
  name: Bonitasoft Custom User API
  slug: bonitasoft-customuser-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: CustomUserDefinition
  name: Bonitasoft Custom User Definition API
  slug: bonitasoft-customuserdefinition-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: CustomUserValue
  name: Bonitasoft Custom User Value API
  slug: bonitasoft-customuservalue-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Configure how Bonita automatically deletes obsolete business data. A retention rule applies to a specific business object type and defines when its instances become eligible for deletion based on a re
  name: Bonitasoft Data Retention API
  slug: bonitasoft-dataretention-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Delegate human tasks from one user (the delegator) to another (the delegate) for a bounded period and a whitelist of processes. Delegation grants the delegate visibility and execution rights on the de
  name: Bonitasoft Delegation API
  slug: bonitasoft-delegation-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Diagram
  name: Bonitasoft Diagram API
  slug: bonitasoft-diagram-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Failure leading a BPM entity instance to a failed state This Web REST API is available in **Enterprise editions only**, since version 10.3 (2025.1).
  name: Bonitasoft Failure API
  slug: bonitasoft-failure-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: FlowNode
  name: Bonitasoft Flow Node API
  slug: bonitasoft-flownode-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Supports any type of files, used to upload a file before submitting a process or task form with a document in its contract.
  name: Bonitasoft Form File Upload API
  slug: bonitasoft-formfileupload-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: The FormMapping API from Bonitasoft — 2 operation(s) for formmapping.
  name: Bonitasoft Form Mapping API
  slug: bonitasoft-formmapping-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: The group a user belongs to. Groups have a hierarchy (subgroups can be created inside a group).
  name: Bonitasoft Group API
  slug: bonitasoft-group-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: HumanTask
  name: Bonitasoft Human Task API
  slug: bonitasoft-humantask-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: I18nlocale
  name: Bonitasoft I18nlocale API
  slug: bonitasoft-i18nlocale-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: I18nTranslation
  name: Bonitasoft I18ntranslation API
  slug: bonitasoft-i18ntranslation-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Handle the platform information. This Web REST API is available since version 10.2 (2024.3). Most of the information returned is only for Subscription editions.
  name: Bonitasoft Information API
  slug: bonitasoft-information-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Handle the license information. This requires a platform session. Log in using the platform login service. This Web REST API is available in **Enterprise editions only**, since version 7.11.
  name: Bonitasoft License API
  slug: bonitasoft-license-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: 'Access log entries recorded by the Bonita Engine during execution. Logs capture actions performed on the platform such as process deployments, task executions, or configuration changes. This Web REST '
  name: Bonitasoft Log API
  slug: bonitasoft-log-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: The Maintenance API from Bonitasoft — 1 operation(s) for maintenance.
  name: Bonitasoft Maintenance API
  slug: bonitasoft-maintenance-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ManualTask
  name: Bonitasoft Manual Task API
  slug: bonitasoft-manualtask-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Manage membership of users. There is a membership when a user belongs to a group and a role. Use this resource to add, search, and delete memberships.
  name: Bonitasoft Membership API
  slug: bonitasoft-membership-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Message
  name: Bonitasoft Message API
  slug: bonitasoft-message-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: The Organization API from Bonitasoft — 2 operation(s) for organization.
  name: Bonitasoft Organization API
  slug: bonitasoft-organization-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Use the page resource to access custom pages, UI Designer pages, layouts or forms and REST API extensions.
  name: Bonitasoft Page API
  slug: bonitasoft-page-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: The Platform API resources require a platform session. In order to get one, log in as the platform administrator using the platform login service.
  name: Bonitasoft Platform API
  slug: bonitasoft-platform-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Platform Authentication
  name: Bonitasoft Platform Authentication API
  slug: bonitasoft-platformauthentication-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Deploy and manage process definitions. In addition, you can instantiate a process, which will create a new process instance (case).
  name: Bonitasoft Process API
  slug: bonitasoft-process-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ProcessConnectorDependency
  name: Bonitasoft Process Connector Dependency API
  slug: bonitasoft-processconnectordependency-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ProcessInfo
  name: Bonitasoft Process Info API
  slug: bonitasoft-processinfo-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ProcessInstance
  name: Bonitasoft Process Instance API
  slug: bonitasoft-processinstance-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ProcessInstanceComment
  name: Bonitasoft Process Instance Comment API
  slug: bonitasoft-processinstancecomment-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ProcessInstanceDocument
  name: Bonitasoft Process Instance Document API
  slug: bonitasoft-processinstancedocument-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ProcessInstanceInfo
  name: Bonitasoft Process Instance Info API
  slug: bonitasoft-processinstanceinfo-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ProcessInstanceVariable
  name: Bonitasoft Process Instance Variable API
  slug: bonitasoft-processinstancevariable-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ProcessParameter
  name: Bonitasoft Process Parameter API
  slug: bonitasoft-processparameter-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ProcessResolutionProblem
  name: Bonitasoft Process Resolution Problem API
  slug: bonitasoft-processresolutionproblem-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ProcessSupervisor
  name: Bonitasoft Process Supervisor API
  slug: bonitasoft-processsupervisor-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ProfessionalContactData
  name: Bonitasoft Professional Contact Data API
  slug: bonitasoft-professionalcontactdata-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Profile
  name: Bonitasoft Profile API
  slug: bonitasoft-profile-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ProfileEntry
  name: Bonitasoft Profile Entry API
  slug: bonitasoft-profileentry-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: ProfileMember
  name: Bonitasoft Profile Member API
  slug: bonitasoft-profilemember-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Role
  name: Bonitasoft Role API
  slug: bonitasoft-role-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Session
  name: Bonitasoft Session API
  slug: bonitasoft-session-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: The Signal API from Bonitasoft — 1 operation(s) for signal.
  name: Bonitasoft Signal API
  slug: bonitasoft-signal-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Task
  name: Bonitasoft Task API
  slug: bonitasoft-task-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: Theme
  name: Bonitasoft Theme API
  slug: bonitasoft-theme-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: TimerEventTrigger
  name: Bonitasoft Timer Event Trigger API
  slug: bonitasoft-timereventtrigger-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: The Upload API from Bonitasoft — 7 operation(s) for upload.
  name: Bonitasoft Upload API
  slug: bonitasoft-upload-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: User
  name: Bonitasoft User API
  slug: bonitasoft-user-api
- baseURL: https://{subscription}.bonitacloud.com/bonita
  baseurl_source: declared
  description: UserTask
  name: Bonitasoft User Task API
  slug: bonitasoft-usertask-api
artifact_total: 82
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/bonitasoft/bonita-openapi/blob/master/LICENSE
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bonitasoft-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bonitasoft-bonita-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.ofelia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.ofelia.com/bonita/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.ofelia.com/bonita/latest/api/api-index
- group: docs
  title: ''
  type: APIReference
  url: https://api-documentation.ofelia.com/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.ofelia.com/bonita/latest/getting-started/getting-started-index
- group: operate
  title: ''
  type: Support
  url: https://community.ofelia.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ofelia.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bonitasoft
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ofelia.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.ofelia.com/downloads
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ofelia.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ofelia.com/personal-data-protection-policy
- group: build
  title: ''
  type: Postman
  url: https://api-documentation.ofelia.com/latest/postman.json
- group: operate
  title: ''
  type: ChangeLog
  url: https://documentation.ofelia.com/bonita/latest/release-notes
- group: build
  title: ''
  type: Packages
  url: packages/bonitasoft-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bonitasoft-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bonitasoft-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bonitasoft-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/bonitasoft-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bonitasoft-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bonitasoft-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bonitasoft-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bonitasoft-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bonitasoft-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://documentation.ofelia.com/bonita/latest/contributing/vulnerability-reporting-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.ofelia.com/about
- group: build
  title: ''
  type: CLI
  url: cli/bonitasoft-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bonitasoft-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bonitasoft-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/bonitasoft-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bonitasoft-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bonitasoft-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bonitasoft-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bonitasoft-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-17'
description: Bonitasoft is the French open-source company behind Bonita, a business process management and process automation platform used to model BPMN processes, build living applications, and orchestrate work across an organization. Bonita ships as Bonita Studio, Bonita Fabric (Process Designer, BPA Studio, UI Builder), Bonita Work Hub and the Bonita Runtime, in a free Community Edition and a commercial Enterprise Edition, plus a managed Bonita Cloud offering. Every Bonita feature reachable over HTTP is described by a single first-party OpenAPI 3.0.2 document — the Bonita Web REST API, 153 paths and 224 operations across BPM, identity, application, BDM and platform resources — published as an open-source repository, a versioned release asset and a live ReDoc reference. In June 2026 the company rebranded to Ofelia and moved its web, documentation and community properties from bonitasoft.com to ofelia.com, adding a governed agentic AI orchestration line (Ofelia Assistant, Ofelia Workflow,
  Ofelia Agentic) alongside the Bonita BPM platform.
image: https://cdn.prod.website-files.com/69babab287a7d4136d9c544a/69babbfcdec6f9319562e4b1_Opengraph.png
layout: provider
mcp_servers:
- description: ''
  name: Bonitasoft MCP Server
  slug: bonitasoft-mcp-server
modified: '2026-08-17'
name: Bonitasoft
nav: Providers
network: true
overview: 'Bonitasoft publishes 76 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Activity Variable API, Actor API, and 73 more. Tagged areas include Company, Software-as-a-Service, Business Process Management, Process Automation, and Workflows.


  Bonitasoft''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Bonitasoft Plans Pricing
  plan_count: 4
  slug: bonitasoft-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Bonitasoft Rate Limits
  slug: bonitasoft-rate-limits
score:
  band: strong
  composite: 61.7
  coverage:
    artifact_dirs: 23
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 51.4
    developer_ergonomics: 85.1
    discoverability: 63.0
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 61.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 76
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bonitasoft/refs/heads/main/screenshots/bonitasoft-2026-09-02T144932.png
security:
- kind: authentication
  name: Bonitasoft Authentication
  slug: bonitasoft-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Bonitasoft Domain Security
  slug: bonitasoft-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bonitasoft Vulnerability Disclosure
  slug: bonitasoft-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: bonitasoft
tags:
- Company
- Software-as-a-Service
- Business Process Management
- Process Automation
- Workflows
- BPMN
- Low-Code
- Open-Source
- Orchestration
- Agentic AI
- Case Management
- Java
website: https://www.ofelia.com/
---
