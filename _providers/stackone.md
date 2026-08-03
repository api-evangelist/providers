---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Stackone Agentic Access
  operation_count: 78
  slug: stackone-agentic-access
  summary_line: 78 operations · 23 acting
api_count: 33
apis:
- description: StackOne Unified HRIS API provides a single, standardized interface to interact with multiple HR information system providers, normalizing data models for employee data, shifts, time-off, documents, a
  name: StackOne Unified HRIS API
  slug: hris-api
- description: StackOne Unified ATS API standardizes recruitment workflows across applicant tracking system providers, providing consistent data models for candidates, job postings, applications, and hiring pipeline
  name: StackOne Unified ATS API
  slug: ats-api
- description: StackOne Unified CRM API provides a standardized interface for managing customer contacts, accounts, and opportunities across multiple CRM platforms, ensuring a consistent view of customer data.
  name: StackOne Unified CRM API
  slug: crm-api
- description: StackOne Unified LMS API standardizes learning management across platforms, streamlining course delivery, user progress tracking, content management, and assignments with consistent data models across
  name: StackOne Unified LMS API
  slug: lms-api
- description: StackOne Unified IAM API provides a standardized interface for identity and access management across providers, with comprehensive user management, role and permission mapping, group management, and r
  name: StackOne Unified IAM API
  slug: iam-api
- description: StackOne Unified Documents API provides a standardized interface for file and knowledge management across platforms like Google Drive, SharePoint, Dropbox, and Box, with consistent data models for dri
  name: StackOne Unified Documents API
  slug: documents-api
- description: StackOne Unified Marketing API standardizes campaign management across platforms, streamlining messages (SMS, Email, Push), campaigns, templates, and more with consistent endpoints across marketing au
  name: StackOne Unified Marketing API
  slug: marketing-api
- description: StackOne Unified Ticketing API standardizes support workflows across helpdesk platforms, with consistent data models for ticket management, comments, and status tracking.
  name: StackOne Unified Ticketing API
  slug: ticketing-api
- description: StackOne Unified Messaging API standardizes communication workflows across platforms, with consistent data models for conversations, message delivery, and participant management.
  name: StackOne Unified Messaging API
  slug: messaging-api
- description: StackOne Unified Screening API standardizes candidate verification across platforms, streamlining background checks, assessments, and screening workflows with consistent data models.
  name: StackOne Unified Screening API
  slug: screening-api
- description: StackOne Platform API serves as the control plane for managing accounts, executing actions, controlling integrations, discovering connectors, monitoring and debugging via logs, and proxy requests acro
  name: StackOne Platform API
  slug: platform-api
- description: The Accounts API from StackOne — 5 operation(s) for accounts.
  name: StackOne Accounts API
  slug: stackone-accounts-api
- description: The Applications API from StackOne — 4 operation(s) for applications.
  name: StackOne Applications API
  slug: stackone-applications-api
- description: The Campaigns API from StackOne — 2 operation(s) for campaigns.
  name: StackOne Campaigns API
  slug: stackone-campaigns-api
- description: The Candidates API from StackOne — 4 operation(s) for candidates.
  name: StackOne Candidates API
  slug: stackone-candidates-api
- description: The Companies API from StackOne — 2 operation(s) for companies.
  name: StackOne Companies API
  slug: stackone-companies-api
- description: The Connect Sessions API from StackOne — 2 operation(s) for connect sessions.
  name: StackOne Connect Sessions API
  slug: stackone-connect-sessions-api
- description: The Contacts API from StackOne — 2 operation(s) for contacts.
  name: StackOne Contacts API
  slug: stackone-contacts-api
- description: The Departments API from StackOne — 2 operation(s) for departments.
  name: StackOne Departments API
  slug: stackone-departments-api
- description: The Employees API from StackOne — 4 operation(s) for employees.
  name: StackOne Employees API
  slug: stackone-employees-api
- description: The Employments API from StackOne — 2 operation(s) for employments.
  name: StackOne Employments API
  slug: stackone-employments-api
- description: The Interview Stages API from StackOne — 2 operation(s) for interview stages.
  name: StackOne Interview Stages API
  slug: stackone-interview-stages-api
- description: The Interviews API from StackOne — 2 operation(s) for interviews.
  name: StackOne Interviews API
  slug: stackone-interviews-api
- description: The Job Postings API from StackOne — 2 operation(s) for job postings.
  name: StackOne Job Postings API
  slug: stackone-job-postings-api
- description: The Jobs API from StackOne — 2 operation(s) for jobs.
  name: StackOne Jobs API
  slug: stackone-jobs-api
- description: The Lists API from StackOne — 2 operation(s) for lists.
  name: StackOne Lists API
  slug: stackone-lists-api
- description: The Locations API from StackOne — 4 operation(s) for locations.
  name: StackOne Locations API
  slug: stackone-locations-api
- description: The Offers API from StackOne — 2 operation(s) for offers.
  name: StackOne Offers API
  slug: stackone-offers-api
- description: The Proxy API from StackOne — 1 operation(s) for proxy.
  name: StackOne Proxy API
  slug: stackone-proxy-api
- description: The Rejected Reasons API from StackOne — 2 operation(s) for rejected reasons.
  name: StackOne Rejected Reasons API
  slug: stackone-rejected-reasons-api
- description: The Templates API from StackOne — 6 operation(s) for templates.
  name: StackOne Templates API
  slug: stackone-templates-api
- description: The Time Off API from StackOne — 2 operation(s) for time off.
  name: StackOne Time Off API
  slug: stackone-time-off-api
- description: The Users API from StackOne — 2 operation(s) for users.
  name: StackOne Users API
  slug: stackone-users-api
artifact_total: 251
collections:
- collection_type: postman
  name: Marketing Accounts API
  slug: postman-stackone-accounts-api
- collection_type: postman
  name: Marketing Accounts Applications API
  slug: postman-stackone-applications-api
- collection_type: postman
  name: Marketing Accounts Campaigns API
  slug: postman-stackone-campaigns-api
- collection_type: postman
  name: Marketing Accounts Candidates API
  slug: postman-stackone-candidates-api
- collection_type: postman
  name: Marketing Accounts Companies API
  slug: postman-stackone-companies-api
- collection_type: postman
  name: Marketing Accounts Connect Sessions API
  slug: postman-stackone-connect-sessions-api
- collection_type: postman
  name: Marketing Accounts Contacts API
  slug: postman-stackone-contacts-api
- collection_type: postman
  name: Marketing Accounts Departments API
  slug: postman-stackone-departments-api
- collection_type: postman
  name: Marketing Accounts Employees API
  slug: postman-stackone-employees-api
- collection_type: postman
  name: Marketing Accounts Employments API
  slug: postman-stackone-employments-api
- collection_type: postman
  name: Marketing Accounts Interview Stages API
  slug: postman-stackone-interview-stages-api
- collection_type: postman
  name: Marketing Accounts Interviews API
  slug: postman-stackone-interviews-api
- collection_type: postman
  name: Marketing Accounts Job Postings API
  slug: postman-stackone-job-postings-api
- collection_type: postman
  name: Marketing Accounts Jobs API
  slug: postman-stackone-jobs-api
- collection_type: postman
  name: Marketing Accounts Lists API
  slug: postman-stackone-lists-api
- collection_type: postman
  name: Marketing Accounts Locations API
  slug: postman-stackone-locations-api
- collection_type: postman
  name: Marketing Accounts Offers API
  slug: postman-stackone-offers-api
- collection_type: postman
  name: Marketing Accounts Proxy API
  slug: postman-stackone-proxy-api
- collection_type: postman
  name: Marketing Accounts Rejected Reasons API
  slug: postman-stackone-rejected-reasons-api
- collection_type: postman
  name: Marketing Accounts Templates API
  slug: postman-stackone-templates-api
- collection_type: postman
  name: Marketing Accounts Time Off API
  slug: postman-stackone-time-off-api
- collection_type: postman
  name: Marketing Accounts Users API
  slug: postman-stackone-users-api
- collection_type: open
  name: Marketing
  slug: open-stackone
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/stackone/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stackone-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/stackone-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stackone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stackone-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StackOneHQ
- group: company
  title: ''
  type: Website
  url: https://www.stackone.com/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.stackone.com/case-studies
- group: company
  title: ''
  type: Blog
  url: https://www.stackone.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.stackone.com/changelog
- group: other
  title: ''
  type: Events
  url: https://www.stackone.com/events
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stackone.com/guides/stackone-basics
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stackone.com/agents/guides/getting-started
- group: company
  title: ''
  type: About
  url: https://www.stackone.com/company
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stackone.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stackone.com/
- group: start
  title: ''
  type: Login
  url: https://app.stackone.com/
- group: company
  title: ''
  type: Partners
  url: https://www.stackone.com/partners
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stackonehq/
- group: other
  title: ''
  type: X
  url: https://x.com/StackOneHQ
- group: build
  title: ''
  type: SDKs
  url: https://docs.stackone.com/guides/stackone-api-sdks
- group: build
  title: ''
  type: SDKTypeScript
  url: https://github.com/StackOneHQ/stackone-client-typescript
- group: build
  title: ''
  type: SDKPython
  url: https://github.com/StackOneHQ/stackone-ai-python
- group: build
  title: ''
  type: SDKNode
  url: https://github.com/StackOneHQ/stackone-ai-node
- group: build
  title: ''
  type: SDKRuby
  url: https://github.com/StackOneHQ/stackone-client-ruby
- group: build
  title: ''
  type: SDKJava
  url: https://github.com/StackOneHQ/stackone-client-java
- group: build
  title: ''
  type: SDKPHP
  url: https://github.com/stackoneHQ/stackone-client-php
- group: build
  title: ''
  type: SDKCSharp
  url: https://github.com/StackOneHQ/stackone-client-csharp
- group: build
  title: ''
  type: SDKPackage
  url: https://www.npmjs.com/package/@stackone/stackone-client-ts
- group: build
  title: ''
  type: SDKPackage
  url: https://rubygems.org/gems/stackone_client
- group: build
  title: ''
  type: SDKPackage
  url: https://packagist.org/packages/stackone/client-sdk
- group: build
  title: ''
  type: PostmanCollection
  url: https://github.com/StackOneHQ/stackone-client-postman
- group: agent
  title: ''
  type: MCPServers
  url: https://docs.stackone.com/mcp/quickstart
- group: other
  title: ''
  type: A2AProtocol
  url: https://docs.stackone.com/a2a/introduction
- group: build
  title: ''
  type: AIToolset
  url: https://docs.stackone.com/agents/typescript/introduction
- group: docs
  title: ''
  type: OpenAPI
  url: https://docs.stackone.com/agents/guides/openapi-tools
- group: build
  title: ''
  type: IntegrationHub
  url: https://hub.stackone.com/about
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.stackone.com/llms.txt
created: '2025-06-05'
description: StackOne is an AI-powered embedded integration platform as a service (iPaaS) designed to simplify and accelerate how SaaS vendors and AI agents connect with enterprise software. It combines a proprietary LLM-based agent with a real-time execution engine to automate and manage integrations no need for manual API wiring or data syncing.
examples:
- key_count: 4
  name: Stackone List Employees Example
  slug: stackone-list-employees-example
features:
- name: Unified APIs
- name: Platform APIs
- name: Integration Hub
- name: Authentication Links
- name: API Keys
- name: Request Logs
- name: Webhooks
- name: Manage Integrations
- name: Manage Projects
- name: Manage Organizations
- name: Custom Unified Fields
- name: Liberaries
- name: SDKs
- name: Advanced Parameters
- name: Pagination
- name: StackOne Identifiers
- name: Rate Limiting
- name: OpenAPI Tools
- name: Tool Filtering
- name: Artificial Intelligence
- name: RAG
- name: SLA Guaranteed Integrations
- name: Native Webhooks
- name: Synthetic Webhooks
- name: Authentication UI
- name: Multi-Region
- name: Hybrid Deployment
- name: No PII Stored
- name: MCP Server
- name: A2A Protocol
- name: Actions API
- name: Connector Builder
- name: Proxy Requests
- name: Sandbox Environments
finops:
- name: Stackone Finops
  service_category: Integration Platform
  slug: stackone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stackone.png
json_schemas:
- name: Account
  property_count: 11
  slug: stackone-account
- name: AccountAddress
  property_count: 7
  slug: stackone-accountaddress
- name: AccountResult
  property_count: 2
  slug: stackone-accountresult
- name: AccountsPaginated
  property_count: 3
  slug: stackone-accountspaginated
- name: Answer
  property_count: 3
  slug: stackone-answer
- name: AnswerEnum
  property_count: 2
  slug: stackone-answerenum
- name: Application
  property_count: 16
  slug: stackone-application
- name: ApplicationAttachment
  property_count: 4
  slug: stackone-applicationattachment
- name: ApplicationCandidate
  property_count: 3
  slug: stackone-applicationcandidate
- name: ApplicationResult
  property_count: 2
  slug: stackone-applicationresult
- name: ApplicationsPaginated
  property_count: 3
  slug: stackone-applicationspaginated
- name: ApplicationStatusEnum
  property_count: 2
  slug: stackone-applicationstatusenum
- name: AtsCreateApplicationRequestDto
  property_count: 7
  slug: stackone-atscreateapplicationrequestdto
- name: AtsCreateCandidateRequestDto
  property_count: 8
  slug: stackone-atscreatecandidaterequestdto
- name: AtsCreateNotesRequestDto
  property_count: 2
  slug: stackone-atscreatenotesrequestdto
- name: AtsCreateOfferRequestDto
  property_count: 6
  slug: stackone-atscreateofferrequestdto
- name: ATSLocation
  property_count: 2
  slug: stackone-atslocation
- name: ATSLocationResult
  property_count: 2
  slug: stackone-atslocationresult
- name: ATSLocationsPaginated
  property_count: 3
  slug: stackone-atslocationspaginated
- name: AtsUpdateApplicationRequestDto
  property_count: 7
  slug: stackone-atsupdateapplicationrequestdto
- name: AtsUpdateCandidatesRequestDto
  property_count: 8
  slug: stackone-atsupdatecandidatesrequestdto
- name: AttachmentType
  property_count: 2
  slug: stackone-attachmenttype
- name: Campaign
  property_count: 12
  slug: stackone-campaign
- name: CampaignResult
  property_count: 2
  slug: stackone-campaignresult
- name: CampaignsPaginated
  property_count: 3
  slug: stackone-campaignspaginated
- name: StackOne Candidate
  property_count: 10
  slug: stackone-candidate
- name: CandidateEmail
  property_count: 2
  slug: stackone-candidateemail
- name: CandidateResult
  property_count: 2
  slug: stackone-candidateresult
- name: CandidatesPaginated
  property_count: 3
  slug: stackone-candidatespaginated
- name: CompaniesPaginated
  property_count: 3
  slug: stackone-companiespaginated
- name: Company
  property_count: 5
  slug: stackone-company
- name: CompanyResult
  property_count: 2
  slug: stackone-companyresult
- name: Compensation
  property_count: 8
  slug: stackone-compensation
- name: ConnectSession
  property_count: 9
  slug: stackone-connectsession
- name: ConnectSessionAuthenticate
  property_count: 1
  slug: stackone-connectsessionauthenticate
- name: ConnectSessionCreate
  property_count: 7
  slug: stackone-connectsessioncreate
- name: ConnectSessionToken
  property_count: 10
  slug: stackone-connectsessiontoken
- name: Contact
  property_count: 10
  slug: stackone-contact
- name: ContactResult
  property_count: 2
  slug: stackone-contactresult
- name: ContactsPaginated
  property_count: 3
  slug: stackone-contactspaginated
- name: Content
  property_count: 2
  slug: stackone-content
- name: CountryCodeEnum
  property_count: 2
  slug: stackone-countrycodeenum
- name: CreateCandidateNoteResult
  property_count: 3
  slug: stackone-createcandidatenoteresult
- name: CreateEmployeeResult
  property_count: 3
  slug: stackone-createemployeeresult
- name: CreateOfferResult
  property_count: 3
  slug: stackone-createofferresult
- name: CreateResult
  property_count: 3
  slug: stackone-createresult
- name: CreateTemplateResult
  property_count: 3
  slug: stackone-createtemplateresult
- name: CreateTimeOffResult
  property_count: 3
  slug: stackone-createtimeoffresult
- name: CrmCreateContactRequestDto
  property_count: 7
  slug: stackone-crmcreatecontactrequestdto
- name: Department
  property_count: 2
  slug: stackone-department
- name: DepartmentResult
  property_count: 2
  slug: stackone-departmentresult
- name: DepartmentsPaginated
  property_count: 3
  slug: stackone-departmentspaginated
- name: EmailMessageContents
  property_count: 5
  slug: stackone-emailmessagecontents
- name: EmailMessages
  property_count: 4
  slug: stackone-emailmessages
- name: StackOne Employee
  property_count: 13
  slug: stackone-employee
- name: EmployeeCustomFields
  property_count: 7
  slug: stackone-employeecustomfields
- name: EmployeeCustomFieldTypeEnum
  property_count: 2
  slug: stackone-employeecustomfieldtypeenum
- name: EmployeeResult
  property_count: 2
  slug: stackone-employeeresult
- name: EmployeesPaginated
  property_count: 3
  slug: stackone-employeespaginated
- name: Employment
  property_count: 12
  slug: stackone-employment
- name: EmploymentResult
  property_count: 2
  slug: stackone-employmentresult
- name: EmploymentScheduleTypeEnum
  property_count: 2
  slug: stackone-employmentscheduletypeenum
- name: EmploymentsPaginated
  property_count: 3
  slug: stackone-employmentspaginated
- name: EmploymentStatusEnum
  property_count: 2
  slug: stackone-employmentstatusenum
- name: EmploymentTypeEnum
  property_count: 2
  slug: stackone-employmenttypeenum
- name: EthnicityEnum
  property_count: 2
  slug: stackone-ethnicityenum
- name: GenderEnum
  property_count: 2
  slug: stackone-genderenum
- name: HiringTeam
  property_count: 5
  slug: stackone-hiringteam
- name: HrisCreateEmployeeRequestDto
  property_count: 31
  slug: stackone-hriscreateemployeerequestdto
- name: HrisCreateTimeOffRequestDto
  property_count: 6
  slug: stackone-hriscreatetimeoffrequestdto
- name: HRISLocation
  property_count: 13
  slug: stackone-hrislocation
- name: HRISLocationResult
  property_count: 2
  slug: stackone-hrislocationresult
- name: HrisLocationsCreateRequestDto
  property_count: 8
  slug: stackone-hrislocationscreaterequestdto
- name: HRISLocationsPaginated
  property_count: 3
  slug: stackone-hrislocationspaginated
- name: Image
  property_count: 2
  slug: stackone-image
- name: Interview
  property_count: 13
  slug: stackone-interview
- name: Interviewer
  property_count: 5
  slug: stackone-interviewer
- name: InterviewPart
  property_count: 6
  slug: stackone-interviewpart
- name: InterviewsPaginated
  property_count: 3
  slug: stackone-interviewspaginated
- name: InterviewsResult
  property_count: 2
  slug: stackone-interviewsresult
- name: InterviewStage
  property_count: 5
  slug: stackone-interviewstage
- name: InterviewStageResult
  property_count: 2
  slug: stackone-interviewstageresult
- name: InterviewStagesPaginated
  property_count: 3
  slug: stackone-interviewstagespaginated
- name: InterviewStatusEnum
  property_count: 2
  slug: stackone-interviewstatusenum
- name: ISO3166_2SubDivisionEnum
  property_count: 2
  slug: stackone-iso3166-2subdivisionenum
- name: Job
  property_count: 11
  slug: stackone-job
- name: JobPosting
  property_count: 15
  slug: stackone-jobposting
- name: JobPostingResult
  property_count: 2
  slug: stackone-jobpostingresult
- name: JobPostingsPaginated
  property_count: 3
  slug: stackone-jobpostingspaginated
- name: JobResult
  property_count: 2
  slug: stackone-jobresult
- name: JobsPaginated
  property_count: 3
  slug: stackone-jobspaginated
- name: JobStatusEnum
  property_count: 2
  slug: stackone-jobstatusenum
- name: LinkedAccount
  property_count: 9
  slug: stackone-linkedaccount
- name: LinkedAccountMeta
  property_count: 3
  slug: stackone-linkedaccountmeta
- name: List
  property_count: 6
  slug: stackone-list
- name: ListResult
  property_count: 2
  slug: stackone-listresult
- name: ListsPaginated
  property_count: 3
  slug: stackone-listspaginated
- name: ListTypeEnum
  property_count: 2
  slug: stackone-listtypeenum
- name: Location
  property_count: 2
  slug: stackone-location
- name: LocationTypeEnum
  property_count: 2
  slug: stackone-locationtypeenum
- name: MaritalStatusEnum
  property_count: 2
  slug: stackone-maritalstatusenum
- name: MarketingCreateEmailTemplateRequestDto
  property_count: 4
  slug: stackone-marketingcreateemailtemplaterequestdto
- name: MarketingCreatePushTemplateRequestDto
  property_count: 4
  slug: stackone-marketingcreatepushtemplaterequestdto
- name: MarketingCreateTemplateRequestDto
  property_count: 4
  slug: stackone-marketingcreatetemplaterequestdto
- name: Message
  property_count: 4
  slug: stackone-message
- name: MessageTypeEnum
  property_count: 2
  slug: stackone-messagetypeenum
- name: Note
  property_count: 6
  slug: stackone-note
- name: NoteResult
  property_count: 2
  slug: stackone-noteresult
- name: NotesPaginated
  property_count: 3
  slug: stackone-notespaginated
- name: NotesVisibilityEnum
  property_count: 2
  slug: stackone-notesvisibilityenum
- name: Offer
  property_count: 9
  slug: stackone-offer
- name: OfferHistory
  property_count: 5
  slug: stackone-offerhistory
- name: OffersPaginated
  property_count: 3
  slug: stackone-offerspaginated
- name: OffersResult
  property_count: 2
  slug: stackone-offersresult
- name: OfferStatusEnum
  property_count: 2
  slug: stackone-offerstatusenum
- name: PayFrequencyEnum
  property_count: 2
  slug: stackone-payfrequencyenum
- name: PayPeriodEnum
  property_count: 2
  slug: stackone-payperiodenum
- name: ProxyRequestBody
  property_count: 5
  slug: stackone-proxyrequestbody
- name: PushMessageContents
  property_count: 1
  slug: stackone-pushmessagecontents
- name: PushMessages
  property_count: 4
  slug: stackone-pushmessages
- name: Questionnaire
  property_count: 2
  slug: stackone-questionnaire
- name: RejectedReason
  property_count: 3
  slug: stackone-rejectedreason
- name: RejectedReasonResult
  property_count: 2
  slug: stackone-rejectedreasonresult
- name: RejectedReasonsPaginated
  property_count: 3
  slug: stackone-rejectedreasonspaginated
- name: RejectedReasonTypeEnum
  property_count: 2
  slug: stackone-rejectedreasontypeenum
- name: SmsMessageContents
  property_count: 2
  slug: stackone-smsmessagecontents
- name: SocialLink
  property_count: 2
  slug: stackone-sociallink
- name: Template
  property_count: 5
  slug: stackone-template
- name: TemplateResult
  property_count: 2
  slug: stackone-templateresult
- name: TemplatesPaginated
  property_count: 3
  slug: stackone-templatespaginated
- name: TimeOff
  property_count: 9
  slug: stackone-timeoff
- name: TimeOffPaginated
  property_count: 3
  slug: stackone-timeoffpaginated
- name: TimeOffResult
  property_count: 2
  slug: stackone-timeoffresult
- name: TimeOffStatusEnum
  property_count: 2
  slug: stackone-timeoffstatusenum
- name: TimeOffTypeEnum
  property_count: 2
  slug: stackone-timeofftypeenum
- name: UpdateResult
  property_count: 3
  slug: stackone-updateresult
- name: User
  property_count: 6
  slug: stackone-user
- name: UserResult
  property_count: 2
  slug: stackone-userresult
- name: UsersPaginated
  property_count: 3
  slug: stackone-userspaginated
json_structures:
- name: Stackone Employee Structure
  property_count: 0
  slug: stackone-employee-structure
- name: Stackone Structure
  property_count: 0
  slug: stackone-structure
jsonld:
- class_count: 11
  name: Stackone Context
  property_count: 5
  slug: stackone-context
layout: provider
modified: '2026-05-19'
name: StackOne
nav: Providers
network: true
overview: 'StackOne publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Applications API, Campaigns API, and 19 more. Tagged areas include Integrations and iPaaS.


  The StackOne catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  StackOne''s developer surface includes authentication, engineering blog, changelog, documentation, getting-started guide, pricing, and 32 more developer resources.'
plans:
- name: Stackone Plans Pricing
  plan_count: 3
  slug: stackone-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Stackone Rate Limits
  slug: stackone-rate-limits
rules:
- name: StackOne API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stackone-jsonschema-spectral-rules
- name: StackOne API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: stackone-rules
score:
  band: strong
  composite: 60.4
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 64.3
    developer_ergonomics: 43.5
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 60.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stackone/refs/heads/main/screenshots/stackone-2026-06-20T194449.png
security:
- kind: authentication
  name: Stackone Authentication
  slug: stackone-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stackone Domain Security
  slug: stackone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stackone Trust Center
  slug: stackone-trust-center
  summary_line: SOC 2, ISO 27001
slug: stackone
tags:
- Integrations
- iPaaS
use_cases:
- name: AI Agents
- name: People Tech
- name: Recruitment
- name: Learning
- name: Assessment & Background Check
- name: Global Employment
- name: Benefits
- name: Fintech
- name: Security & Compliance
website: https://www.stackone.com/
---
