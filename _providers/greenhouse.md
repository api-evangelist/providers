---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 76
  human_in_the_loop: 0
  name: Greenhouse Agentic Access
  operation_count: 149
  slug: greenhouse-agentic-access
  summary_line: 149 operations · 76 acting
api_count: 7
apis:
- description: The Assessment Partner API enables assessment platforms (code testing, video interviewing, personality testing) to seamlessly integrate with the Greenhouse interview workflow.
  name: Greenhouse Assessment API
  slug: assessment
- description: The Audit Log API offers a record of important events, providing insight into who accessed or edited information in Greenhouse.
  name: Greenhouse Audit Log API
  slug: audit-log
- description: Recruiting Webhooks deliver event notifications for Greenhouse Recruiting activities such as candidate updates, application stage changes, and offers.
  name: Greenhouse Recruiting Webhooks
  slug: recruiting-webhooks
- description: Onboarding Webhooks deliver event notifications for Greenhouse Onboarding activities such as new hires and employee updates.
  name: Greenhouse Onboarding Webhooks
  slug: onboarding-webhooks
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: The Applications API from Greenhouse — 5 operation(s) for applications.
  name: Greenhouse Applications API
  slug: greenhouse-applications-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: The Candidates API from Greenhouse — 2 operation(s) for candidates.
  name: Greenhouse Candidates API
  slug: greenhouse-candidates-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: The Departments API from Greenhouse — 2 operation(s) for departments.
  name: Greenhouse Departments API
  slug: greenhouse-departments-api
- baseURL: https://boards-api.greenhouse.io/v1/boards/{board_token}
  baseurl_source: declared
  description: The Education API from Greenhouse — 3 operation(s) for education.
  name: Greenhouse Education API
  slug: greenhouse-education-api
- baseURL: https://boards-api.greenhouse.io/v1/boards/{board_token}
  baseurl_source: declared
  description: The Greenhouse Job Board API API from Greenhouse — 1 operation(s) for greenhouse job board api.
  name: Greenhouse Job Board API
  slug: greenhouse-greenhouse-job-board-api-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: The Jobs API from Greenhouse — 3 operation(s) for jobs.
  name: Greenhouse Jobs API
  slug: greenhouse-jobs-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: The Offices API from Greenhouse — 3 operation(s) for offices.
  name: Greenhouse Offices API
  slug: greenhouse-offices-api
- baseURL: https://api.greenhouse.io/v1/partner
  baseurl_source: declared
  description: The Prospects API from Greenhouse — 1 operation(s) for prospects.
  name: Greenhouse Prospects API
  slug: greenhouse-prospects-api
- baseURL: https://boards-api.greenhouse.io/v1/boards/{board_token}
  baseurl_source: declared
  description: The Sections API from Greenhouse — 2 operation(s) for sections.
  name: Greenhouse Sections API
  slug: greenhouse-sections-api
- baseURL: https://api.greenhouse.io/v1/partner
  baseurl_source: declared
  description: The Tracking API from Greenhouse — 1 operation(s) for tracking.
  name: Greenhouse Tracking API
  slug: greenhouse-tracking-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: The Users API from Greenhouse — 3 operation(s) for users.
  name: Greenhouse Users API
  slug: greenhouse-users-api
- baseURL: https://onboarding-api.greenhouse.io
  baseurl_source: declared
  description: The Graph QL API from Greenhouse — 1 operation(s) for graph ql.
  name: Greenhouse Graph QL API
  slug: greenhouse-graph-ql-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: Per-candidate timeline of activity events.
  name: Greenhouse Activity Feed API
  slug: greenhouse-activity-feed-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: Approval flows for jobs and offers.
  name: Greenhouse Approvals API
  slug: greenhouse-approvals-api
- baseURL: https://auditlog.us.greenhouse.io
  baseurl_source: declared
  description: JWT access token issuance.
  name: Greenhouse Auth API
  slug: greenhouse-auth-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: Org-defined custom fields and their options.
  name: Greenhouse Custom Fields API
  slug: greenhouse-custom-fields-api
- baseURL: https://auditlog.us.greenhouse.io
  baseurl_source: declared
  description: Audit log events.
  name: Greenhouse Events API
  slug: greenhouse-events-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: Individual openings under a Job.
  name: Greenhouse Job Openings API
  slug: greenhouse-job-openings-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: The interview/pipeline stages a job uses.
  name: Greenhouse Job stages API
  slug: greenhouse-job-stages-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: Public-facing job postings and their statuses.
  name: Greenhouse Job Posts API
  slug: greenhouse-jobposts-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: Offers extended to candidates.
  name: Greenhouse Offers API
  slug: greenhouse-offers-api
- baseURL: https://api.greenhouse.io/v1/partner
  baseurl_source: declared
  description: Read configured prospect pools and their stages.
  name: Greenhouse Prospect Pools API
  slug: greenhouse-prospectpools-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: Configured rejection reasons.
  name: Greenhouse Rejection Reasons API
  slug: greenhouse-rejectionreasons-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: Scheduled interview events on the calendar.
  name: Greenhouse Scheduled Interviews API
  slug: greenhouse-scheduledinterviews-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: Interview scorecards captured by interviewers.
  name: Greenhouse Scorecards API
  slug: greenhouse-scorecards-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: Candidate-source taxonomy (where the candidate came from).
  name: Greenhouse Sources API
  slug: greenhouse-sources-api
- baseURL: https://harvest.greenhouse.io/v1
  baseurl_source: declared
  description: Candidate tags.
  name: Greenhouse Tags API
  slug: greenhouse-tags-api
- baseURL: https://{partner_host}/{base_path}
  baseurl_source: declared
  description: Sending tests to candidates and reporting status.
  name: Greenhouse Test Delivery API
  slug: greenhouse-testdelivery-api
- baseURL: https://{partner_host}/{base_path}
  baseurl_source: declared
  description: Available tests offered by the partner.
  name: Greenhouse Tests API
  slug: greenhouse-tests-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Access Token API from Greenhouse — 1 operation(s) for access token.
  name: Greenhouse Access Token API
  slug: greenhouse-access-token-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Application Stages API from Greenhouse — 1 operation(s) for application stages.
  name: Greenhouse Application Stages API
  slug: greenhouse-application-stages-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Applied Candidate Tags API from Greenhouse — 2 operation(s) for applied candidate tags.
  name: Greenhouse Applied Candidate Tags API
  slug: greenhouse-applied-candidate-tags-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Approval Flows API from Greenhouse — 3 operation(s) for approval flows.
  name: Greenhouse Approval Flows API
  slug: greenhouse-approval-flows-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Approver Flows API from Greenhouse — 1 operation(s) for approver flows.
  name: Greenhouse Approver Flows API
  slug: greenhouse-approver-flows-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Approver Groups API from Greenhouse — 2 operation(s) for approver groups.
  name: Greenhouse Approver Groups API
  slug: greenhouse-approver-groups-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Approvers API from Greenhouse — 1 operation(s) for approvers.
  name: Greenhouse Approvers API
  slug: greenhouse-approvers-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Attachments API from Greenhouse — 2 operation(s) for attachments.
  name: Greenhouse Attachments API
  slug: greenhouse-attachments-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Bulk Requests API from Greenhouse — 4 operation(s) for bulk requests.
  name: Greenhouse Bulk Requests API
  slug: greenhouse-bulk-requests-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Candidate Attribute Types API from Greenhouse — 1 operation(s) for candidate attribute types.
  name: Greenhouse Candidate Attribute Types API
  slug: greenhouse-candidate-attribute-types-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Candidate Educations API from Greenhouse — 2 operation(s) for candidate educations.
  name: Greenhouse Candidate Educations API
  slug: greenhouse-candidate-educations-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Candidate Employments API from Greenhouse — 2 operation(s) for candidate employments.
  name: Greenhouse Candidate Employments API
  slug: greenhouse-candidate-employments-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Candidate Tags API from Greenhouse — 2 operation(s) for candidate tags.
  name: Greenhouse Candidate Tags API
  slug: greenhouse-candidate-tags-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Close Reasons API from Greenhouse — 1 operation(s) for close reasons.
  name: Greenhouse Close Reasons API
  slug: greenhouse-close-reasons-api
- baseURL: https://onboarding-api.greenhouse.io
  baseurl_source: declared
  description: The Countries API from Greenhouse — 1 operation(s) for countries.
  name: Greenhouse Countries API
  slug: greenhouse-countries-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Custom Field Departments API from Greenhouse — 2 operation(s) for custom field departments.
  name: Greenhouse Custom Field Departments API
  slug: greenhouse-custom-field-departments-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Custom Field Offices API from Greenhouse — 2 operation(s) for custom field offices.
  name: Greenhouse Custom Field Offices API
  slug: greenhouse-custom-field-offices-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Custom Field Options API from Greenhouse — 2 operation(s) for custom field options.
  name: Greenhouse Custom Field Options API
  slug: greenhouse-custom-field-options-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Default Interviewers API from Greenhouse — 1 operation(s) for default interviewers.
  name: Greenhouse Default Interviewers API
  slug: greenhouse-default-interviewers-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Demographic Answer Options API from Greenhouse — 1 operation(s) for demographic answer options.
  name: Greenhouse Demographic Answer Options API
  slug: greenhouse-demographic-answer-options-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Demographic Answers API from Greenhouse — 1 operation(s) for demographic answers.
  name: Greenhouse Demographic Answers API
  slug: greenhouse-demographic-answers-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Demographic Question Sets API from Greenhouse — 1 operation(s) for demographic question sets.
  name: Greenhouse Demographic Question Sets API
  slug: greenhouse-demographic-question-sets-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Demographic Questions API from Greenhouse — 1 operation(s) for demographic questions.
  name: Greenhouse Demographic Questions API
  slug: greenhouse-demographic-questions-api
- baseURL: https://onboarding-api.greenhouse.io
  baseurl_source: declared
  description: The Documents API from Greenhouse — 1 operation(s) for documents.
  name: Greenhouse Documents API
  slug: greenhouse-documents-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The EEOC API from Greenhouse — 1 operation(s) for eeoc.
  name: Greenhouse EEOC API
  slug: greenhouse-eeoc-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Email Templates API from Greenhouse — 1 operation(s) for email templates.
  name: Greenhouse Email Templates API
  slug: greenhouse-email-templates-api
- baseURL: https://onboarding-api.greenhouse.io
  baseurl_source: declared
  description: The Employees API from Greenhouse — 2 operation(s) for employees.
  name: Greenhouse Employees API
  slug: greenhouse-employees-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Focus Candidate Attributes API from Greenhouse — 1 operation(s) for focus candidate attributes.
  name: Greenhouse Focus Candidate Attributes API
  slug: greenhouse-focus-candidate-attributes-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Future Job Permissions API from Greenhouse — 2 operation(s) for future job permissions.
  name: Greenhouse Future Job Permissions API
  slug: greenhouse-future-job-permissions-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Interview Kits API from Greenhouse — 1 operation(s) for interview kits.
  name: Greenhouse Interview Kits API
  slug: greenhouse-interview-kits-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Interviewer Tags API from Greenhouse — 1 operation(s) for interviewer tags.
  name: Greenhouse Interviewer Tags API
  slug: greenhouse-interviewer-tags-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Interviewers API from Greenhouse — 1 operation(s) for interviewers.
  name: Greenhouse Interviewers API
  slug: greenhouse-interviewers-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Interviews API from Greenhouse — 2 operation(s) for interviews.
  name: Greenhouse Interviews API
  slug: greenhouse-interviews-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Job Board Custom Locations API from Greenhouse — 1 operation(s) for job board custom locations.
  name: Greenhouse Job Board Custom Locations API
  slug: greenhouse-job-board-custom-locations-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Job Candidate Attributes API from Greenhouse — 1 operation(s) for job candidate attributes.
  name: Greenhouse Job Candidate Attributes API
  slug: greenhouse-job-candidate-attributes-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Job Hiring Managers API from Greenhouse — 2 operation(s) for job hiring managers.
  name: Greenhouse Job Hiring Managers API
  slug: greenhouse-job-hiring-managers-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Job Interview Stages API from Greenhouse — 1 operation(s) for job interview stages.
  name: Greenhouse Job Interview Stages API
  slug: greenhouse-job-interview-stages-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Job Interviews API from Greenhouse — 1 operation(s) for job interviews.
  name: Greenhouse Job Interviews API
  slug: greenhouse-job-interviews-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Job Notes API from Greenhouse — 2 operation(s) for job notes.
  name: Greenhouse Job Notes API
  slug: greenhouse-job-notes-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Job Owners API from Greenhouse — 2 operation(s) for job owners.
  name: Greenhouse Job Owners API
  slug: greenhouse-job-owners-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Job Post Locations API from Greenhouse — 2 operation(s) for job post locations.
  name: Greenhouse Job Post Locations API
  slug: greenhouse-job-post-locations-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Job Posts API from Greenhouse — 2 operation(s) for job posts.
  name: Greenhouse Job Posts API
  slug: greenhouse-job-posts-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Notes API from Greenhouse — 1 operation(s) for notes.
  name: Greenhouse Notes API
  slug: greenhouse-notes-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Openings API from Greenhouse — 2 operation(s) for openings.
  name: Greenhouse Openings API
  slug: greenhouse-openings-api
- baseURL: https://onboarding-api.greenhouse.io
  baseurl_source: declared
  description: The Other Criteria API from Greenhouse — 1 operation(s) for other criteria.
  name: Greenhouse Other Criteria API
  slug: greenhouse-other-criteria-api
- baseURL: https://onboarding-api.greenhouse.io
  baseurl_source: declared
  description: The Pending Hires API from Greenhouse — 2 operation(s) for pending hires.
  name: Greenhouse Pending Hires API
  slug: greenhouse-pending-hires-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Prospect Details API from Greenhouse — 1 operation(s) for prospect details.
  name: Greenhouse Prospect Details API
  slug: greenhouse-prospect-details-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Prospect Pool Stages API from Greenhouse — 1 operation(s) for prospect pool stages.
  name: Greenhouse Prospect Pool Stages API
  slug: greenhouse-prospect-pool-stages-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Prospect Pools API from Greenhouse — 1 operation(s) for prospect pools.
  name: Greenhouse Prospect Pools API
  slug: greenhouse-prospect-pools-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Referrers API from Greenhouse — 1 operation(s) for referrers.
  name: Greenhouse Referrers API
  slug: greenhouse-referrers-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Rejection Details API from Greenhouse — 2 operation(s) for rejection details.
  name: Greenhouse Rejection Details API
  slug: greenhouse-rejection-details-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Rejection Reasons API from Greenhouse — 1 operation(s) for rejection reasons.
  name: Greenhouse Rejection Reasons API
  slug: greenhouse-rejection-reasons-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Scorecard Candidate Attributes API from Greenhouse — 2 operation(s) for scorecard candidate attributes.
  name: Greenhouse Scorecard Candidate Attributes API
  slug: greenhouse-scorecard-candidate-attributes-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Scorecard Question Answer Options API from Greenhouse — 1 operation(s) for scorecard question answer options.
  name: Greenhouse Scorecard Question Answer Options API
  slug: greenhouse-scorecard-question-answer-options-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Scorecard Question Answers API from Greenhouse — 2 operation(s) for scorecard question answers.
  name: Greenhouse Scorecard Question Answers API
  slug: greenhouse-scorecard-question-answers-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Scorecard Question Candidate Attributes API from Greenhouse — 1 operation(s) for scorecard question candidate attributes.
  name: Greenhouse Scorecard Question Candidate Attributes API
  slug: greenhouse-scorecard-question-candidate-attributes-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Scorecard Question Options API from Greenhouse — 1 operation(s) for scorecard question options.
  name: Greenhouse Scorecard Question Options API
  slug: greenhouse-scorecard-question-options-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Scorecard Questions API from Greenhouse — 1 operation(s) for scorecard questions.
  name: Greenhouse Scorecard Questions API
  slug: greenhouse-scorecard-questions-api
- baseURL: https://onboarding-api.greenhouse.io
  baseurl_source: declared
  description: The Signature Request Templates API from Greenhouse — 1 operation(s) for signature request templates.
  name: Greenhouse Signature Request Templates API
  slug: greenhouse-signature-request-templates-api
- baseURL: https://onboarding-api.greenhouse.io
  baseurl_source: declared
  description: The Signature Requests API from Greenhouse — 1 operation(s) for signature requests.
  name: Greenhouse Signature Requests API
  slug: greenhouse-signature-requests-api
- baseURL: https://onboarding-api.greenhouse.io
  baseurl_source: declared
  description: The Team Categories API from Greenhouse — 1 operation(s) for team categories.
  name: Greenhouse Team Categories API
  slug: greenhouse-team-categories-api
- baseURL: https://onboarding-api.greenhouse.io
  baseurl_source: declared
  description: The Teams API from Greenhouse — 3 operation(s) for teams.
  name: Greenhouse Teams API
  slug: greenhouse-teams-api
- baseURL: https://auth.greenhouse.io
  baseurl_source: declared
  description: The Token API from Greenhouse — 1 operation(s) for token.
  name: Greenhouse Token API
  slug: greenhouse-token-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Tracking Links API from Greenhouse — 1 operation(s) for tracking links.
  name: Greenhouse Tracking Links API
  slug: greenhouse-tracking-links-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The User Emails API from Greenhouse — 1 operation(s) for user emails.
  name: Greenhouse User Emails API
  slug: greenhouse-user-emails-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The User Job Permissions API from Greenhouse — 2 operation(s) for user job permissions.
  name: Greenhouse User Job Permissions API
  slug: greenhouse-user-job-permissions-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The User Roles API from Greenhouse — 1 operation(s) for user roles.
  name: Greenhouse User Roles API
  slug: greenhouse-user-roles-api
- baseURL: https://harvest.greenhouse.io
  baseurl_source: declared
  description: The Webhooks API from Greenhouse — 2 operation(s) for webhooks.
  name: Greenhouse Webhooks API
  slug: greenhouse-webhooks-api
artifact_total: 148
asyncapis:
- description: ''
  name: Greenhouse Webhooks
  slug: greenhouse-webhooks
collections:
- collection_type: open
  name: Greenhouse Harvest Applications API
  slug: open-greenhouse-applications-api
- collection_type: open
  name: Greenhouse Harvest Applications Candidates API
  slug: open-greenhouse-candidates-api
- collection_type: open
  name: Greenhouse Harvest Applications Departments API
  slug: open-greenhouse-departments-api
- collection_type: open
  name: Greenhouse Harvest Applications Education API
  slug: open-greenhouse-education-api
- collection_type: open
  name: Greenhouse Harvest Applications Graphql API
  slug: open-greenhouse-graphql-api
- collection_type: open
  name: Greenhouse Harvest Applications Greenhouse Job Board API API
  slug: open-greenhouse-greenhouse-job-board-api-api
- collection_type: open
  name: Greenhouse Harvest API
  slug: open-greenhouse-harvest
- collection_type: open
  name: Greenhouse Candidate Ingestion API
  slug: open-greenhouse-ingestion
- collection_type: open
  name: Greenhouse Job Board API
  slug: open-greenhouse-job-board
- collection_type: open
  name: Greenhouse Harvest Applications Jobs API
  slug: open-greenhouse-jobs-api
- collection_type: open
  name: Greenhouse Harvest Applications Offices API
  slug: open-greenhouse-offices-api
- collection_type: open
  name: Greenhouse Onboarding API
  slug: open-greenhouse-onboarding
- collection_type: open
  name: Greenhouse Harvest Applications Prospects API
  slug: open-greenhouse-prospects-api
- collection_type: open
  name: Greenhouse Harvest Applications Sections API
  slug: open-greenhouse-sections-api
- collection_type: open
  name: Greenhouse Harvest Applications Tracking API
  slug: open-greenhouse-tracking-api
- collection_type: open
  name: Greenhouse Harvest Applications Users API
  slug: open-greenhouse-users-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/greenhouse/overview
- group: start
  title: ''
  type: Portal
  url: https://www.greenhouse.com
- group: other
  title: ''
  type: Customers
  url: https://www.greenhouse.com/customers
- group: company
  title: ''
  type: Careers
  url: https://www.greenhouse.com/jobs
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Greenhouse
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/grnhse/greenhouse-api-docs
- group: design
  href: https://artifacts.apis.io/greenhouse/json-ld/greenhouse-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/greenhouse-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/greenhouse/rules/greenhouse-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/greenhouse-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/greenhouse/rules/greenhouse-rules.yml
  title: ''
  type: Spectral
  url: rules/greenhouse-rules.yml
- group: design
  href: https://artifacts.apis.io/greenhouse/json-ld/greenhouse-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/greenhouse-context.jsonld
- group: design
  href: https://artifacts.apis.io/greenhouse/vocabulary/greenhouse-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/greenhouse-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/greenhouse/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/greenhouse/asyncapi/greenhouse-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/greenhouse-webhooks.yml
- group: design
  href: https://artifacts.apis.io/greenhouse/data-model/greenhouse-data-model.yml
  title: ''
  type: DataModel
  url: data-model/greenhouse-data-model.yml
- group: operate
  href: https://artifacts.apis.io/greenhouse/changelog/greenhouse-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/greenhouse-changelog.yml
- group: design
  href: https://artifacts.apis.io/greenhouse/conventions/greenhouse-conventions.yml
  title: ''
  type: Conventions
  url: conventions/greenhouse-conventions.yml
- group: start
  href: https://artifacts.apis.io/greenhouse/sandbox/greenhouse-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/greenhouse-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.greenhouse.com/
- group: operate
  href: https://artifacts.apis.io/greenhouse/lifecycle/greenhouse-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/greenhouse-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/greenhouse/lifecycle/greenhouse-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/greenhouse-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/greenhouse/errors/greenhouse-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/greenhouse-problem-types.yml
- group: design
  href: https://artifacts.apis.io/greenhouse/conformance/greenhouse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/greenhouse-conformance.yml
- group: agent
  href: https://artifacts.apis.io/greenhouse/llms/greenhouse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/greenhouse-llms.txt
- group: build
  href: https://artifacts.apis.io/greenhouse/mcp/greenhouse-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/greenhouse-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/greenhouse/mcp/greenhouse-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/greenhouse-mcp.yml
- group: agent
  href: https://artifacts.apis.io/greenhouse/well-known/greenhouse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/greenhouse-well-known.yml
- group: other
  href: https://artifacts.apis.io/greenhouse/hosts/greenhouse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/greenhouse-hosts.yml
- group: build
  href: https://artifacts.apis.io/greenhouse/integrations/greenhouse-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/greenhouse-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/greenhouse/vendors/greenhouse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/greenhouse-vendors.yml
- group: build
  href: https://artifacts.apis.io/greenhouse/packages/greenhouse-packages.yml
  title: ''
  type: SDKs
  url: packages/greenhouse-packages.yml
- group: build
  href: https://artifacts.apis.io/greenhouse/packages/greenhouse-packages.yml
  title: ''
  type: Packages
  url: packages/greenhouse-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.greenhouse.com/security
- group: other
  title: ''
  type: Leadership
  url: https://www.greenhouse.com/leadership
- group: auth
  href: https://artifacts.apis.io/greenhouse/security/greenhouse-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/greenhouse-trust-center.yml
- group: commercial
  href: https://artifacts.apis.io/greenhouse/plans/greenhouse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/greenhouse-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/greenhouse/rate-limits/greenhouse-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/greenhouse-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/greenhouse/finops/greenhouse-finops.yml
  title: ''
  type: FinOps
  url: finops/greenhouse-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.greenhouse.com/blog
- group: other
  href: https://artifacts.apis.io/greenhouse/capabilities/greenhouse-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/greenhouse-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.greenhouse.com
- group: agent
  href: https://artifacts.apis.io/greenhouse/agentic-access/greenhouse-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/greenhouse-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/greenhouse/security/greenhouse-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/greenhouse-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/greenhouse/security/greenhouse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/greenhouse-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/greenhouse/authentication/greenhouse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/greenhouse-authentication.yml
- group: auth
  href: https://artifacts.apis.io/greenhouse/scopes/greenhouse-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/greenhouse-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/greenhouse-inc-
- group: docs
  title: ''
  type: Documentation
  url: https://developers.greenhouse.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/grnhse
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.greenhouse.io/
- group: docs
  title: ''
  type: APIReference
  url: https://harvestdocs.greenhouse.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://harvestdocs.greenhouse.io/docs/overview-and-philosophy
- group: operate
  title: ''
  type: Support
  url: https://support.greenhouse.io/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.greenhouse.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.greenhouse.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.greenhouse.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://harvestdocs.greenhouse.io/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.greenhouse.io/
- group: company
  title: ''
  type: Newsroom
  url: https://www.greenhouse.com/newsroom
- group: docs
  title: ''
  type: Documentation
  url: https://developers.greenhouse.io/harvest.html
- group: docs
  title: ''
  type: Documentation
  url: https://developers.greenhouse.io/job-board.html
- group: docs
  title: ''
  type: Documentation
  url: https://developers.greenhouse.io/webhooks.html
- group: docs
  title: ''
  type: Documentation
  url: https://developers.greenhouse.io/onboarding_webhooks.html
- group: docs
  title: ''
  type: Documentation
  url: https://developers.greenhouse.io/gho.html
- group: docs
  title: ''
  type: Documentation
  url: https://developers.greenhouse.io/candidate-ingestion.html
- group: docs
  title: ''
  type: Documentation
  url: https://developers.greenhouse.io/assessment.html
- group: docs
  title: ''
  type: Documentation
  url: https://developers.greenhouse.io/audit-log.html
created: '2025-01-07'
description: Greenhouse is an applicant tracking system (ATS) and recruiting software platform. It exposes a family of APIs and webhooks that let partners and customers manage candidates, jobs, applications, onboarding, audit logs, and assessment integrations.
finops:
- has_sources: true
  method: generated
  name: Greenhouse Finops
  primary_unit: ''
  service_category: Recruiting / ATS SaaS
  slug: greenhouse-finops
  template: false
graphqls:
- description: A GraphQL API for Greenhouse Onboarding. Provides queries and mutations for employees, departments, locations, custom fields, teams, and pending hires.
  name: Greenhouse GraphQL API
  slug: greenhouse-graphql
- description: The Greenhouse Onboarding (GHO) API is a single GraphQL endpoint covering employees,
  name: Greenhouse GraphQL API
  slug: greenhouse-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/greenhouse.png
json_schemas:
- name: ApplicationCreate
  property_count: 5
  slug: greenhouse-application-create
- name: Application
  property_count: 17
  slug: greenhouse-application
- name: ApplicationSubmission
  property_count: 13
  slug: greenhouse-application-submission
- name: Attachment
  property_count: 5
  slug: greenhouse-attachment
- name: Greenhouse Candidate
  property_count: 21
  slug: greenhouse-candidate
- name: Department
  property_count: 6
  slug: greenhouse-department
- name: Education
  property_count: 5
  slug: greenhouse-education
- name: Employment
  property_count: 4
  slug: greenhouse-employment
- name: HiringTeam
  property_count: 4
  slug: greenhouse-hiring-team
- name: JobCreate
  property_count: 6
  slug: greenhouse-job-create
- name: Greenhouse Job
  property_count: 15
  slug: greenhouse-job
- name: Office
  property_count: 6
  slug: greenhouse-office
- name: User
  property_count: 12
  slug: greenhouse-user
json_structures:
- name: Greenhouse Structure
  property_count: 0
  slug: greenhouse-structure
jsonld:
- class_count: 102
  name: Greenhouse Context
  property_count: 371
  slug: greenhouse-context
- class_count: 0
  name: Greenhouse Io Context
  property_count: 11
  slug: greenhouse-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.greenhouse.io over HTTP requiring OAuth; 29 tools listed.
  name: Greenhouse MCP Server
  slug: greenhouse
modified: '2026-11-05'
name: Greenhouse
nav: Providers
network: true
overview: 'Greenhouse publishes 101 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applications API, Candidates API, Departments API, and 98 more. Tagged areas include Human Resources, Greenhouse, Applicant Tracking, Recruiting, and Candidates.


  The Greenhouse catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 2 Spectral governance rulesets.


  Greenhouse''s developer surface includes developer portal, changelog, sandbox, engineering blog, authentication, documentation, API reference, and 59 more developer resources.'
plans:
- name: Greenhouse Plans Pricing
  plan_count: 3
  slug: greenhouse-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 3
  name: Greenhouse Rate Limits
  slug: greenhouse-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Greenhouse API Rules
  rule_count: 58
  severity_counts:
    error: 43
    hint: 0
    info: 2
    warn: 13
  slug: greenhouse-rules
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Greenhouse API Rules
  rule_count: 17
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 11
  slug: greenhouse-spectral-rules
scopes:
- name: Greenhouse Scopes
  scope_count: 174
  slug: greenhouse-scopes
  summary_line: 174 scopes · clientCredentials/authorizationCode
score:
  band: exemplar
  composite: 79.7
  coverage:
    artifact_dirs: 40
    catalog_earned: 84.8
    catalog_earned_first_party: 24.0
    catalog_gap: 30.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 45.3
  facets:
    access_clarity: 78.9
    contract_governance: 35.6
    contract_quality: 69.6
    developer_ergonomics: 79.8
    discoverability: 68.3
    operational_transparency: 94.7
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 28.4
      derived: 0
      marker_coverage: 0.0
      total: 97
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 52.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/greenhouse/greenhouse-2026-06-20T182356.png
security:
- kind: authentication
  name: Greenhouse Authentication
  slug: greenhouse-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Greenhouse Domain Security
  slug: greenhouse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Greenhouse Vulnerability Disclosure
  slug: greenhouse-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Greenhouse Trust Center
  slug: greenhouse-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
slug: greenhouse
tags:
- Human Resources
- Greenhouse
- Applicant Tracking
- Recruiting
- Candidates
- Job
- Onboarding
- Hiring
- Talent Acquisition
- Enterprise Saas
website: https://www.greenhouse.com
---
