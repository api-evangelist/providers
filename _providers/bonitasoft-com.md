---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 204
  human_in_the_loop: 6
  name: Bonitasoft Com Agentic Access
  operation_count: 448
  slug: bonitasoft-com-agentic-access
  summary_line: 448 operations · 204 acting · 6 human-in-the-loop
api_count: 2
apis:
- description: API for Bonita platform as documented
  name: Bonita API
  slug: bonita-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Activity
  name: Bonitasoft Activity API
  slug: bonitasoft-com-activity-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ActivityVariable
  name: Bonitasoft Activity Variable API
  slug: bonitasoft-com-activityvariable-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Actor
  name: Bonitasoft Actor API
  slug: bonitasoft-com-actor-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ActorMember
  name: Bonitasoft Actor Member API
  slug: bonitasoft-com-actormember-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Manage applications. This enables you to build a consistent functional applicative environment for users to interact with business processes and business data from one place.
  name: Bonitasoft Application API
  slug: bonitasoft-com-application-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: 'Manage the set of menus in an application. This set of menus enables a user to navigate to the application pages. There are two types of menu item: A top-level item appears in the navigation bar of th'
  name: Bonitasoft Application Menu API
  slug: bonitasoft-com-applicationmenu-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: An application page is a custom page that has been associated with an application. Use this resource to manage application pages and define the paths used to access them. This list of pages will be us
  name: Bonitasoft Application Page API
  slug: bonitasoft-com-applicationpage-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ArchivedActivity
  name: Bonitasoft Archived Activity API
  slug: bonitasoft-com-archivedactivity-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ArchivedActivityVariable
  name: Bonitasoft Archived Activity Variable API
  slug: bonitasoft-com-archivedactivityvariable-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ArchivedConnectorInstance
  name: Bonitasoft Archived Connector Instance API
  slug: bonitasoft-com-archivedconnectorinstance-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Archived version of the Failure leading a BPM entity instance to a failed state. This Web REST API is available in **Enterprise editions only**, since version 10.3 (2025.1).
  name: Bonitasoft Archived Failure API
  slug: bonitasoft-com-archivedfailure-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ArchivedFlowNode
  name: Bonitasoft Archived Flow Node API
  slug: bonitasoft-com-archivedflownode-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ArchivedHumanTask
  name: Bonitasoft Archived Human Task API
  slug: bonitasoft-com-archivedhumantask-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ArchivedManualTask
  name: Bonitasoft Archived Manual Task API
  slug: bonitasoft-com-archivedmanualtask-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ArchivedProcessInstance
  name: Bonitasoft Archived Process Instance API
  slug: bonitasoft-com-archivedprocessinstance-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ArchivedProcessInstanceComment
  name: Bonitasoft Archived Process Instance Comment API
  slug: bonitasoft-com-archivedprocessinstancecomment-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ArchivedProcessInstanceDocument
  name: Bonitasoft Archived Process Instance Document API
  slug: bonitasoft-com-archivedprocessinstancedocument-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ArchivedProcessInstanceVariable
  name: Bonitasoft Archived Process Instance Variable API
  slug: bonitasoft-com-archivedprocessinstancevariable-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ArchivedTask
  name: Bonitasoft Archived Task API
  slug: bonitasoft-com-archivedtask-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ArchivedUserTask
  name: Bonitasoft Archived User Task API
  slug: bonitasoft-com-archivedusertask-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Authentication
  name: Bonitasoft Authentication API
  slug: bonitasoft-com-authentication-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: 'Show status or install or update the Business Data Model. Installing or updating a BDM needs to be done in two successive steps: 1. Upload a BDM file 2. Install/Update the previously uploaded file **T'
  name: Bonitasoft BDM API
  slug: bonitasoft-com-bdm-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: BDM Access control is available to protect the BDM. You can use this API to get the access control status (lastUpdatedBy, lastUpdateDate...).
  name: Bonitasoft BDM Access Control API
  slug: bonitasoft-com-bdmaccesscontrol-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: BDM Rest APIs allow to create / update / delete / import in bulk Bonita Business Data.
  name: Bonitasoft Business Data Operations API
  slug: bonitasoft-com-business-data-operations-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: BDM Rest APIs allow to query Bonita Business Data.
  name: Bonitasoft Business Data Query API
  slug: bonitasoft-com-businessdataquery-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ConnectorFailure
  name: Bonitasoft Connector Failure API
  slug: bonitasoft-com-connectorfailure-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ConnectorInstance
  name: Bonitasoft Connector Instance API
  slug: bonitasoft-com-connectorinstance-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: CustomUser
  name: Bonitasoft Custom User API
  slug: bonitasoft-com-customuser-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: CustomUserDefinition
  name: Bonitasoft Custom User Definition API
  slug: bonitasoft-com-customuserdefinition-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: CustomUserValue
  name: Bonitasoft Custom User Value API
  slug: bonitasoft-com-customuservalue-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Delegate human tasks from one user (the delegator) to another (the delegate) for a bounded period and a whitelist of processes. Delegation grants the delegate visibility and execution rights on the de
  name: Bonitasoft Delegation API
  slug: bonitasoft-com-delegation-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Diagram
  name: Bonitasoft Diagram API
  slug: bonitasoft-com-diagram-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Failure leading a BPM entity instance to a failed state This Web REST API is available in **Enterprise editions only**, since version 10.3 (2025.1).
  name: Bonitasoft Failure API
  slug: bonitasoft-com-failure-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: FlowNode
  name: Bonitasoft Flow Node API
  slug: bonitasoft-com-flownode-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Supports any type of files, used to upload a file before submitting a process or task form with a document in its contract.
  name: Bonitasoft Form File Upload API
  slug: bonitasoft-com-formfileupload-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: The FormMapping API from Bonitasoft — 2 operation(s) for formmapping.
  name: Bonitasoft Form Mapping API
  slug: bonitasoft-com-formmapping-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: The group a user belongs to. Groups have a hierarchy (subgroups can be created inside a group).
  name: Bonitasoft Group API
  slug: bonitasoft-com-group-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: HumanTask
  name: Bonitasoft Human Task API
  slug: bonitasoft-com-humantask-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: I18nlocale
  name: Bonitasoft I18nlocale API
  slug: bonitasoft-com-i18nlocale-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: I18nTranslation
  name: Bonitasoft I18ntranslation API
  slug: bonitasoft-com-i18ntranslation-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Handle the platform information. This Web REST API is available since version 10.2 (2024.3). Most of the information returned is only for Subscription editions.
  name: Bonitasoft Information API
  slug: bonitasoft-com-information-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Handle the license information. This requires a platform session. Log in using the platform login service. This Web REST API is available in **Enterprise editions only**, since version 7.11.
  name: Bonitasoft License API
  slug: bonitasoft-com-license-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: 'Access log entries recorded by the Bonita Engine during execution. Logs capture actions performed on the platform such as process deployments, task executions, or configuration changes. This Web REST '
  name: Bonitasoft Log API
  slug: bonitasoft-com-log-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: The Maintenance API from Bonitasoft — 1 operation(s) for maintenance.
  name: Bonitasoft Maintenance API
  slug: bonitasoft-com-maintenance-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ManualTask
  name: Bonitasoft Manual Task API
  slug: bonitasoft-com-manualtask-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Manage membership of users. There is a membership when a user belongs to a group and a role. Use this resource to add, search, and delete memberships.
  name: Bonitasoft Membership API
  slug: bonitasoft-com-membership-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Message
  name: Bonitasoft Message API
  slug: bonitasoft-com-message-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: The Organization API from Bonitasoft — 2 operation(s) for organization.
  name: Bonitasoft Organization API
  slug: bonitasoft-com-organization-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Use the page resource to access custom pages, UI Designer pages, layouts or forms and REST API extensions.
  name: Bonitasoft Page API
  slug: bonitasoft-com-page-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: The Platform API resources require a platform session. In order to get one, log in as the platform administrator using the platform login service.
  name: Bonitasoft Platform API
  slug: bonitasoft-com-platform-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Platform Authentication
  name: Bonitasoft Platform Authentication API
  slug: bonitasoft-com-platformauthentication-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Deploy and manage process definitions. In addition, you can instantiate a process, which will create a new process instance (case).
  name: Bonitasoft Process API
  slug: bonitasoft-com-process-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ProcessConnectorDependency
  name: Bonitasoft Process Connector Dependency API
  slug: bonitasoft-com-processconnectordependency-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ProcessInfo
  name: Bonitasoft Process Info API
  slug: bonitasoft-com-processinfo-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ProcessInstance
  name: Bonitasoft Process Instance API
  slug: bonitasoft-com-processinstance-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ProcessInstanceComment
  name: Bonitasoft Process Instance Comment API
  slug: bonitasoft-com-processinstancecomment-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ProcessInstanceDocument
  name: Bonitasoft Process Instance Document API
  slug: bonitasoft-com-processinstancedocument-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ProcessInstanceInfo
  name: Bonitasoft Process Instance Info API
  slug: bonitasoft-com-processinstanceinfo-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ProcessInstanceVariable
  name: Bonitasoft Process Instance Variable API
  slug: bonitasoft-com-processinstancevariable-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ProcessParameter
  name: Bonitasoft Process Parameter API
  slug: bonitasoft-com-processparameter-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ProcessResolutionProblem
  name: Bonitasoft Process Resolution Problem API
  slug: bonitasoft-com-processresolutionproblem-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ProcessSupervisor
  name: Bonitasoft Process Supervisor API
  slug: bonitasoft-com-processsupervisor-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ProfessionalContactData
  name: Bonitasoft Professional Contact Data API
  slug: bonitasoft-com-professionalcontactdata-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Profile
  name: Bonitasoft Profile API
  slug: bonitasoft-com-profile-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ProfileEntry
  name: Bonitasoft Profile Entry API
  slug: bonitasoft-com-profileentry-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: ProfileMember
  name: Bonitasoft Profile Member API
  slug: bonitasoft-com-profilemember-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Role
  name: Bonitasoft Role API
  slug: bonitasoft-com-role-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Session
  name: Bonitasoft Session API
  slug: bonitasoft-com-session-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: The Signal API from Bonitasoft — 1 operation(s) for signal.
  name: Bonitasoft Signal API
  slug: bonitasoft-com-signal-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Task
  name: Bonitasoft Task API
  slug: bonitasoft-com-task-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Theme
  name: Bonitasoft Theme API
  slug: bonitasoft-com-theme-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: TimerEventTrigger
  name: Bonitasoft Timer Event Trigger API
  slug: bonitasoft-com-timereventtrigger-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: The Upload API from Bonitasoft — 7 operation(s) for upload.
  name: Bonitasoft Upload API
  slug: bonitasoft-com-upload-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: User
  name: Bonitasoft User API
  slug: bonitasoft-com-user-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: UserTask
  name: Bonitasoft User Task API
  slug: bonitasoft-com-usertask-api
- baseURL: http://localhost:8080/bonita
  baseurl_source: spec
  description: Configure how Bonita automatically deletes obsolete business data. A retention rule applies to a specific business object type and defines when its instances become eligible for deletion based on a re
  name: Bonitasoft Data Retention API
  slug: bonitasoft-com-data-retention-api
artifact_total: 87
common:
- group: agent
  href: https://artifacts.apis.io/bonitasoft-com/agentic-access/bonitasoft-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bonitasoft-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bonitasoft-com/plans/bonitasoft-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bonitasoft-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bonitasoft-com/rules/bonitasoft-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bonitasoft-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bonitasoft-com/json-ld/bonitasoft-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bonitasoft-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bonitasoft-com/vocabulary/bonitasoft-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bonitasoft-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bonitasoft-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bonitasoft-com/data-model/bonitasoft-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bonitasoft-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/bonitasoft-com/errors/bonitasoft-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bonitasoft-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bonitasoft-com/conformance/bonitasoft-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bonitasoft-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/bonitasoft-com/hosts/bonitasoft-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bonitasoft-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bonitasoft-com/vendors/bonitasoft-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bonitasoft-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ofelia.com/legal-notice
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ofelia.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.ofelia.com/press
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.ofelia.com/bonita/latest/
- group: company
  title: ''
  type: Blog
  url: https://www.ofelia.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ofelia.com/fr/cas-d-usage-bonita-employee-onboarding-automation
- group: auth
  href: https://artifacts.apis.io/bonitasoft-com/authentication/bonitasoft-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bonitasoft-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bonitasoft-com/security/bonitasoft-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bonitasoft-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ofelia.com/
coverage:
  checked: '2026-10-29'
  detail: Documentation pages exist but no machine‑readable OpenAPI spec is hosted on a provider‑owned domain.
  evidence:
  - status: 200
    url: https://documentation.ofelia.com/bonita/latest/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Ofelia (formerly Bonitasoft) is a governed AI orchestration platform for enterprise operations, helping enterprises scale AI execution from simple tasks to cross‑team coordination with control, visibility and governance. The platform offers workflow automation, task coordination, and AI model management, targeting large organizations seeking to integrate AI safely and efficiently.
image: https://cdn.prod.website-files.com/69babab287a7d4136d9c544a/69babbfcdec6f9319562e4b1_Opengraph.png
jsonld:
- class_count: 120
  name: Bonitasoft Com Context
  property_count: 252
  slug: bonitasoft-com-context
layout: provider
modified: '2026-10-29'
name: Bonitasoft
nav: Providers
network: true
overview: 'Bonitasoft publishes 77 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activity API, Activity Variable API, Actor API, and 74 more. Tagged areas include AI, Orchestration, Enterprise, Automation, and Platform.


  The Bonitasoft catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bonitasoft''s developer surface includes pricing, documentation, engineering blog, getting-started guide, authentication, and 15 more developer resources.'
plans:
- name: Bonitasoft Com Plans Pricing
  plan_count: 2
  slug: bonitasoft-com-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Bonitasoft API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 2
  slug: bonitasoft-com-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 56.8
    catalog_earned_first_party: 8.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 52.9
    developer_ergonomics: 37.5
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 76
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bonitasoft Com Authentication
  slug: bonitasoft-com-authentication
  summary_line: apiKey/http/unknown · 4 schemes
- kind: domain-security
  name: Bonitasoft Com Domain Security
  slug: bonitasoft-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: bonitasoft-com-create-and-instanciate-process
  slug: bonitasoft-com-create-and-instanciate-process
- name: bonitasoft-com-create-and-retrieve-process-instance
  slug: bonitasoft-com-create-and-retrieve-process-instance
- name: bonitasoft-com-create-business-data
  slug: bonitasoft-com-create-business-data
- name: bonitasoft-com-get-business-data
  slug: bonitasoft-com-get-business-data
slug: bonitasoft-com
tags:
- AI
- Orchestration
- Enterprise
- Automation
- Platform
- Company
website: https://www.ofelia.com/
---
