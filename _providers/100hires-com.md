---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 71
  human_in_the_loop: 0
  name: 100Hires Com Agentic Access
  operation_count: 139
  slug: 100hires-com-agentic-access
  summary_line: 139 operations · 71 acting
api_count: 1
apis:
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: 'Application lifecycle: creation, stage movement, rejection/hire actions, and attachments.'
  name: 100Hires Applications API
  slug: 100hires-com-applications-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: Download attachment bytes by category and UUID. URLs in this format are returned in other API responses — resumes (`/candidates/{id}/resume`), candidate files (`/candidates/{id}/files`), application a
  name: 100Hires Attachments API
  slug: 100hires-com-attachments-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: Pricing state checks to gate paid-only API capabilities.
  name: 100Hires Billing API
  slug: 100hires-com-billing-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: 'Candidate profile lifecycle: search, deduplication, files, tags, and activity timeline.'
  name: 100Hires Candidates API
  slug: 100hires-com-candidates-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: Public API for career site integrations. Authenticates by company slug instead of Bearer token. Pass the company slug via the `X-Company-Slug` header (or `company_slug` query param). No user context i
  name: 100Hires Career Site API
  slug: 100hires-com-career-site-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: Partner multi-tenant company management, including restore and webhook registration.
  name: 100Hires Companies API
  slug: 100hires-com-companies-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: Email template CRUD for automation, nurture campaigns, and manual outreach.
  name: 100Hires Email Templates API
  slug: 100hires-com-email-templates-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: Filled evaluation forms with scores and answers submitted by interviewers for applications.
  name: 100Hires Evaluations API
  slug: 100hires-com-evaluations-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: Structured API feedback endpoint for agents and integrations to report issues and suggest improvements.
  name: 100Hires Feedback API
  slug: 100hires-com-feedback-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: Application forms and per-question required/optional/hidden status control.
  name: 100Hires Forms API
  slug: 100hires-com-forms-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: 'Interview scheduling: list, view, and create interviews linked to applications and candidates.'
  name: 100Hires Interviews API
  slug: 100hires-com-interviews-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: 'Job lifecycle and publishing: CRUD, status transitions, hiring team, boards, and webhooks.'
  name: 100Hires Jobs API
  slug: 100hires-com-jobs-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: Candidate communication history and scheduler-backed email delivery endpoints.
  name: 100Hires Messages API
  slug: 100hires-com-messages-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: Discussion notes linked to candidates for recruiter collaboration and context sharing.
  name: 100Hires Notes API
  slug: 100hires-com-notes-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: 'Manage notification emails (rejection, interview reminders, etc.) auto-created by the system: view, edit, cancel, or bulk-cancel before delivery.'
  name: 100Hires Notification Messages API
  slug: 100hires-com-notification-messages-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: Nurture campaign CRUD with multi-step sequences (email, SMS, voicemail, move stage, assign tag/task).
  name: 100Hires Nurture Campaigns API
  slug: 100hires-com-nurture-campaigns-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: Reusable question catalog and supported question type discovery.
  name: 100Hires Questions API
  slug: 100hires-com-questions-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: Reference dictionaries used across jobs, candidates, and workflow orchestration.
  name: 100Hires Taxonomy API
  slug: 100hires-com-taxonomy-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: Discover and prepare dynamic placeholders (e.g. first name, job title) for use in email templates. Placeholders are inserted as HTML `<tag>` elements returned by `POST /template-placeholders/prepare`;
  name: 100Hires Template Placeholders API
  slug: 100hires-com-template-placeholders-api
- baseURL: https://api.100hires.com/v2
  baseurl_source: declared
  description: Company user directory and role-aware identity lookups.
  name: 100Hires Users API
  slug: 100hires-com-users-api
artifact_total: 35
common:
- group: agent
  href: https://artifacts.apis.io/100hires-com/agentic-access/100hires-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/100hires-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/100hires-com/plans/100hires-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/100hires-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/100hires-com/rules/100hires-com-rules.yml
  title: ''
  type: Spectral
  url: rules/100hires-com-rules.yml
- group: design
  href: https://artifacts.apis.io/100hires-com/json-ld/100hires-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/100hires-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/100hires-com/vocabulary/100hires-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/100hires-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/100hires-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/100hires-com/data-model/100hires-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/100hires-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/100hires-com/errors/100hires-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/100hires-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/100hires-com/conformance/100hires-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/100hires-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/100hires-com/llms/100hires-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/100hires-com-llms.txt
- group: build
  href: https://artifacts.apis.io/100hires-com/mcp/100hires-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/100hires-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/100hires-com/mcp/100hires-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/100hires-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/100hires-com/hosts/100hires-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/100hires-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/100hires-com/vendors/100hires-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/100hires-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.100hires.com/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/100Hires
- group: auth
  href: https://artifacts.apis.io/100hires-com/security/100hires-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/100hires-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://100hires.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://100hires.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://100hires.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://100hires.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://100hires.com/api
- group: operate
  title: ''
  type: Support
  url: mailto:support@100hires.com
- group: company
  title: ''
  type: Blog
  url: https://100hires.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://100hires.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://100hires.com/page/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://100hires.com/page/privacy
created: '2026-10-31'
description: AI-powered recruiting software built for small businesses. Post jobs, screen candidates with AI, and hire faster — all in one place. Free trial, no credit card. Built for teams that hire 5-50 roles per quarter. Forbes-rated, Capterra-rated, used by 30,000+ companies. Ask any question about your pipeline. AI takes notes, scores candidates, and ranks them automatically.
image: https://100hires.com/images/og/t1-brand-purple.png
json_schemas:
- name: Application
  property_count: 25
  slug: 100hires-com-application
- name: Candidate
  property_count: 17
  slug: 100hires-com-candidate
- name: CandidateWriteRequest
  property_count: 13
  slug: 100hires-com-candidate-write-request
- name: JobCreateRequest
  property_count: 31
  slug: 100hires-com-job-create-request
- name: Job
  property_count: 38
  slug: 100hires-com-job
- name: JobUpdateRequest
  property_count: 30
  slug: 100hires-com-job-update-request
jsonld:
- class_count: 120
  name: 100Hires Com Context
  property_count: 243
  slug: 100hires-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at help.100hires.com.
  name: 100Hires MCP Server
  slug: 100hires-com-mcp-yml
modified: '2026-10-31'
name: 100Hires
nav: Providers
network: true
overview: '100Hires publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applications API, Attachments API, Billing API, and 17 more. Tagged areas include Recruiting, Artificial Intelligence, Human Resources, Software-as-a-Service, and Small Business.


  The 100Hires catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  100Hires'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: 100Hires Com Plans Pricing
  plan_count: 3
  slug: 100hires-com-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: 100Hires API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 2
  slug: 100hires-com-rules
scopes:
- name: 100Hires Com Scopes
  scope_count: 0
  slug: 100hires-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 66.6
    developer_ergonomics: 31.4
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 100Hires Com Authentication
  slug: 100hires-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 100Hires Com Domain Security
  slug: 100hires-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: create-candidate
  slug: 100hires-com-create-candidate
slug: 100hires-com
tags:
- Recruiting
- Artificial Intelligence
- Human Resources
- Software-as-a-Service
- Small Business
website: https://100hires.com/
---
