---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 62
  human_in_the_loop: 24
  name: Gloat Agentic Access
  operation_count: 130
  slug: gloat-agentic-access
  summary_line: 130 operations · 62 acting · 24 human-in-the-loop
api_count: 8
apis:
- description: Tenant-scoped REST API to sync users, jobs, candidacies, projects, learning items, and the Skills Foundation job architecture into Gloat, plus RBAC authorization and company settings.
  name: Gloat Customer API
  slug: gloat-customer-api-2
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Access Rules API from Gloat — 2 operation(s) for access rules.
  name: Gloat Access Rules API
  slug: gloat-access-rules-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Admin console access API from Gloat — 1 operation(s) for admin console access.
  name: Gloat Admin console access API
  slug: gloat-admin-console-access-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Analytics API from Gloat — 2 operation(s) for analytics.
  name: Gloat Analytics API
  slug: gloat-analytics-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: API keys management endpoints for creating, updating, and managing API keys. These endpoints require the external_api_token_management permission.
  name: Gloat API keys API
  slug: gloat-api-keys-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Applications API from Gloat — 5 operation(s) for applications.
  name: Gloat Applications API
  slug: gloat-applications-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The auth-settings API from Gloat — 3 operation(s) for auth-settings.
  name: Gloat Auth Settings API
  slug: gloat-auth-settings-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: Candidacies operations
  name: Gloat Candidacy API
  slug: gloat-candidacy-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Certifications API from Gloat — 3 operation(s) for certifications.
  name: Gloat Certifications API
  slug: gloat-certifications-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Core Entities API from Gloat — 3 operation(s) for core entities.
  name: Gloat Core Entities API
  slug: gloat-core-entities-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Data Sharing API provides endpoints for accessing and downloading your Gloat data. The API enables to retrieve lists of available file types and generate pre-signed URLs for downloading specific d
  name: Gloat Data direct API
  slug: gloat-data-direct-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Groups API from Gloat — 3 operation(s) for groups.
  name: Gloat Groups API
  slug: gloat-groups-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: Presigned HTTPS PUT URLs for uploading files to the integration (e.g. Boomi) S3 bucket under your company prefix. Requires the upload_users permission. Configure INTEGRATION_UPLOADS_BUCKET and IRSA s3
  name: Gloat Integration uploads API
  slug: gloat-integration-uploads-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The integrations API from Gloat — 1 operation(s) for integrations.
  name: Gloat Integrations API
  slug: gloat-integrations-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: Positions/requisitions operations
  name: Gloat Job API
  slug: gloat-job-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Job Architecture > Job Code API from Gloat — 6 operation(s) for job architecture > job code.
  name: Gloat Job Architecture > Job Code API
  slug: gloat-job-architecture-job-code-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Job Architecture > Job Code > Insights API from Gloat — 1 operation(s) for job architecture > job code > insights.
  name: Gloat Job Architecture > Job Code > Insights API
  slug: gloat-job-architecture-job-code-insights-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Job Architecture > Job Code > Tasks API from Gloat — 1 operation(s) for job architecture > job code > tasks.
  name: Gloat Job Architecture > Job Code > Tasks API
  slug: gloat-job-architecture-job-code-tasks-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Job Architecture > Job Family API from Gloat — 3 operation(s) for job architecture > job family.
  name: Gloat Job Architecture > Job Family API
  slug: gloat-job-architecture-job-family-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Job Architecture > Job Function API from Gloat — 1 operation(s) for job architecture > job function.
  name: Gloat Job Architecture > Job Function API
  slug: gloat-job-architecture-job-function-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Job Architecture > Position Title API from Gloat — 4 operation(s) for job architecture > position title.
  name: Gloat Job Architecture > Position Title API
  slug: gloat-job-architecture-position-title-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Learning API from Gloat — 1 operation(s) for learning.
  name: Gloat Learning API
  slug: gloat-learning-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Management Console > Ontologies API from Gloat — 3 operation(s) for management console > ontologies.
  name: Gloat Management Console > Ontologies API
  slug: gloat-management-console-ontologies-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: Endpoints related to service, authentication and connectivity
  name: Gloat Meta API
  slug: gloat-meta-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: Hooks to be implemented, which Gloat can be configured to call on certain events. The payloads are defined here; the URLs are to be defined with the implementation specialist or customer success repre
  name: Gloat Outbound API
  slug: gloat-outbound-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Permissions API from Gloat — 2 operation(s) for permissions.
  name: Gloat Permissions API
  slug: gloat-permissions-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Projects & Projects Roles API from Gloat — 2 operation(s) for projects & projects roles.
  name: Gloat Projects & Projects Roles API
  slug: gloat-projects-projects-roles-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The RBAC Groups & Roles API from Gloat — 7 operation(s) for rbac groups & roles.
  name: Gloat RBAC Groups & Roles API
  slug: gloat-rbac-groups-roles-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Retrieval API from Gloat — 3 operation(s) for retrieval.
  name: Gloat Retrieval API
  slug: gloat-retrieval-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Roles API from Gloat — 4 operation(s) for roles.
  name: Gloat Roles API
  slug: gloat-roles-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Search API from Gloat — 2 operation(s) for search.
  name: Gloat Search API
  slug: gloat-search-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Skills API from Gloat — 1 operation(s) for skills.
  name: Gloat Skills API
  slug: gloat-skills-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Skills foundation > File Download API from Gloat — 4 operation(s) for skills foundation > file download.
  name: Gloat Skills foundation > File Download API
  slug: gloat-skills-foundation-file-download-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Skills Inventory > Users API from Gloat — 1 operation(s) for skills inventory > users.
  name: Gloat Skills Inventory > Users API
  slug: gloat-skills-inventory-users-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Stats API from Gloat — 1 operation(s) for stats.
  name: Gloat Stats API
  slug: gloat-stats-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: Employee operations
  name: Gloat User API
  slug: gloat-user-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The User Profile API from Gloat — 1 operation(s) for user profile.
  name: Gloat User Profile API
  slug: gloat-user-profile-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The User Skills API from Gloat — 1 operation(s) for user skills.
  name: Gloat User Skills API
  slug: gloat-user-skills-api
- baseURL: https://{company_slug}.gloat.com/api
  baseurl_source: declared
  description: The Users API from Gloat — 2 operation(s) for users.
  name: Gloat Users API
  slug: gloat-users-api
artifact_total: 72
asyncapis:
- description: ''
  name: Gloat Webhooks
  slug: gloat-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/agentic-access/gloat-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gloat-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/rules/gloat-rules.yml
  title: ''
  type: Spectral
  url: rules/gloat-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/json-ld/gloat-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gloat-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/vocabulary/gloat-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gloat-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/errors/gloat-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gloat-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/hosts/gloat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gloat-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/vendors/gloat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gloat-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://gloat.com/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://gloat.com/blog/feed/
- group: company
  title: ''
  type: Website
  url: https://www.gloat.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.gloat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.gloat.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.gloat.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.gloat.com/docs/using-gloat-apis
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/authentication/gloat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gloat-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/llms/gloat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gloat-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://gloat.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gloat.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gloat.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gloat.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://compliance.gloat.com/
- group: auth
  title: ''
  type: Compliance
  url: https://gloat.com/security-and-compliance/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/conformance/gloat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gloat-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/lifecycle/gloat-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gloat-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/conventions/gloat-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gloat-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/data-model/gloat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gloat-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/sandbox/gloat-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gloat-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/mcp/gloat-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gloat-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/asyncapi/gloat-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gloat-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/security/gloat-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gloat-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/security/gloat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gloat-domain-security.yml
created: '2026-07-17'
description: 'Gloat is an AI-native workforce orchestration and talent-marketplace platform. Its developer APIs let enterprises connect HR, learning, and skills data to Gloat: syncing users, jobs, projects, candidacies, and learning items, and maintaining a skills-and-job-architecture ontology (the Skills Foundation) of job families, job codes, and position titles. The platform also exposes RBAC authorization (roles, groups, permissions, access rules), certifications, applications, analytics embeds, and outbound sync webhooks. Customer APIs authenticate with a client-credentials JWT; Talent Marketplace APIs use an X-Gloat-API-Key header. All hosts are per-tenant at https://{company_slug}.gloat.com/api.'
image: https://www.gloat.com/favicon.ico
json_schemas:
- name: AccessRuleResponse
  property_count: 5
  slug: gloat-access-rule-response
- name: ApiKeyGetResponse
  property_count: 7
  slug: gloat-api-key-get-response
- name: ApiKeyRead
  property_count: 7
  slug: gloat-api-key-read
- name: ApplicationFileStatusResponse
  property_count: 12
  slug: gloat-application-file-status-response
- name: ApplicationGetSchema
  property_count: 11
  slug: gloat-application-get-schema
- name: CertificationGetData
  property_count: 8
  slug: gloat-certification-get-data
- name: GroupResponse
  property_count: 7
  slug: gloat-group-response
- name: IdentityProviderData
  property_count: 6
  slug: gloat-identity-provider-data
- name: JobCodeCreate
  property_count: 19
  slug: gloat-job-code-create
- name: JobCodeRead
  property_count: 27
  slug: gloat-job-code-read
- name: JobCodeWrite
  property_count: 19
  slug: gloat-job-code-write
- name: job_detail_object
  property_count: 1
  slug: gloat-job-detail-object
- name: job_object
  property_count: 26
  slug: gloat-job-object
- name: JobTitleRead
  property_count: 16
  slug: gloat-job-title-read
- name: JobTitleWrite
  property_count: 13
  slug: gloat-job-title-write
- name: learning_item
  property_count: 25
  slug: gloat-learning-item
- name: PaginatedAPIResponse[AccessRuleResponse]
  property_count: 4
  slug: gloat-paginated-apiresponse-access-rule-response
- name: Project
  property_count: 15
  slug: gloat-project-object
- name: project_role_object
  property_count: 21
  slug: gloat-project-role-object
- name: RoleGetResponse
  property_count: 8
  slug: gloat-role-get-response
- name: RoleRequestBody
  property_count: 4
  slug: gloat-role-request-body
- name: RoleResponse
  property_count: 8
  slug: gloat-role-response
- name: SimpleRetrievalRequest
  property_count: 6
  slug: gloat-simple-retrieval-request
- name: user_object
  property_count: 31
  slug: gloat-user-object
- name: XApiActionResult
  property_count: 5
  slug: gloat-xapi-action-result
- name: XApiStatement
  property_count: 5
  slug: gloat-xapi-statement
jsonld:
- class_count: 120
  name: Gloat Context
  property_count: 239
  slug: gloat-context
layout: provider
modified: '2026-10-06'
name: Gloat
nav: Providers
network: true
overview: 'Gloat publishes 39 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Rules API, Admin console access API, Analytics API, and 36 more. Tagged areas include Company, Artificial Intelligence, Human Resources, Talent Marketplace, and Skills.


  The Gloat catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Gloat''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, sandbox, and 26 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Gloat API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 2
    warn: 3
  slug: gloat-rules
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.1
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 70.7
    developer_ergonomics: 42.3
    discoverability: 80.4
    operational_transparency: 23.7
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 36.8
      derived: 0
      marker_coverage: 100.0
      total: 38
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 27.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/gloat/refs/heads/main/screenshots/gloat-2026-07-25T215912.png
security:
- kind: authentication
  name: Gloat Authentication
  slug: gloat-authentication
  summary_line: oauth2/apiKey/http · 2 schemes
- kind: domain-security
  name: Gloat Domain Security
  slug: gloat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gloat Trust Center
  slug: gloat-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, GDPR, CSA / Cloud Controls Matrix (CCM)
slug: gloat
tags:
- Company
- Artificial Intelligence
- Human Resources
- Talent Marketplace
- Skills
- Workforce
- Internal Mobility
website: https://www.gloat.com/
---
