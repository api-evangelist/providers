---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - finops
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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Lever Agentic Access
  operation_count: 55
  slug: lever-agentic-access
  summary_line: 55 operations · 18 acting
api_count: 33
apis:
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: Legacy Candidates endpoints maintained for backward compatibility. New integrations should use Opportunities; Candidates remain available for historical record retrieval.
  name: Lever Candidates API
  slug: lever-candidates-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: Manage feedback form templates, including question definitions and scoring rubrics applied across postings and stages.
  name: Lever Feedback Templates API
  slug: lever-feedback-templates-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: Subscribe to Lever events (applicationCreated, candidateHired, stageChange, contactUpdate). Events are signed with HMAC-SHA256 for receiver verification.
  name: Lever Webhooks API
  slug: lever-webhooks-api
- description: The unauthenticated public Postings API for retrieving live job listings from a Lever account, used by external careers pages.
  name: Lever Postings Public API
  slug: lever-postings-public-api
- description: XML feed of open postings used by job aggregators (Indeed, Glassdoor, LinkedIn) for syndication.
  name: Lever XML Feed
  slug: lever-xml-feed-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: Submit candidate applications against postings, including resumes, cover letters, and EEO survey data, and retrieve historical application records.
  name: Lever Applications API
  slug: lever-applications-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: Contacts represent unique people across multiple opportunities, allowing Lever to deduplicate candidates who apply to multiple roles.
  name: Lever Contacts API
  slug: lever-contacts-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: Read anonymous EEO survey data for compliance reporting; PII-isolated from the standard candidate endpoints.
  name: Lever EEO API
  slug: lever-eeo-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: Upload and download files (resumes, cover letters, portfolio attachments) associated with opportunities; supports docx, doc, pdf, txt, jpg, png.
  name: Lever Files API
  slug: lever-files-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Opportunities API from Lever — 10 operation(s) for opportunities.
  name: Lever Opportunities API
  slug: lever-opportunities-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: Manage job postings programmatically and power custom public job sites. The Postings API has a public read-only mode that does not require authentication for displaying job listings.
  name: Lever Postings API
  slug: lever-postings-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: Manage requisitions backing each posting — headcount, compensation bands, and approval state — typically synced from an HRIS.
  name: Lever Requisitions API
  slug: lever-requisitions-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: Read source attribution (job board, referral, sourced) for opportunities to drive sourcing analytics.
  name: Lever Sources API
  slug: lever-sources-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: List the configured pipeline stages and disposition stages used to route opportunities through screening, interviews, offer, and hire.
  name: Lever Stages API
  slug: lever-stages-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: List and apply tags to opportunities for cohorting, sourcing, and reporting workflows.
  name: Lever Tags API
  slug: lever-tags-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: Manage Lever users and their access roles (Super Admin, Admin, Team Member, Limited Team Member, Interviewer, Outsider).
  name: Lever Users API
  slug: lever-users-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Archive Reasons API from Lever — 2 operation(s) for archive reasons.
  name: Lever Archive Reasons API
  slug: lever-archive-reasons-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Audit Events API from Lever — 1 operation(s) for audit events.
  name: Lever Audit Events API
  slug: lever-audit-events-api
- description: The authorization server partner integrations use to obtain Lever API access tokens (authorization code grant with refresh tokens, audience https://api.lever.co/v1/, 50 documented resource scopes). Le
  name: Lever OAuth 2.0 Authorization Server
  slug: oauth-authorization-server
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Candidates API from Lever — 11 operation(s) for candidates.
  name: Lever Candidates API
  slug: lever-candidates-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Disposition Stages API from Lever — 1 operation(s) for disposition stages.
  name: Lever Disposition Stages API
  slug: lever-disposition-stages-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Feedback Templates API from Lever — 2 operation(s) for feedback templates.
  name: Lever Feedback Templates API
  slug: lever-feedback-templates-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Form Templates API from Lever — 2 operation(s) for form templates.
  name: Lever Form Templates API
  slug: lever-form-templates-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Profile Forms API from Lever — 1 operation(s) for profile forms.
  name: Lever Profile Forms API
  slug: lever-profile-forms-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Requisition Fields API from Lever — 3 operation(s) for requisition fields.
  name: Lever Requisition Fields API
  slug: lever-requisition-fields-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Surveys API from Lever — 1 operation(s) for surveys.
  name: Lever Surveys API
  slug: lever-surveys-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Webhooks API from Lever — 2 operation(s) for webhooks.
  name: Lever Webhooks API
  slug: lever-webhooks-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Feedback API from Lever — 2 operation(s) for feedback.
  name: Lever Feedback API
  slug: lever-feedback-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Forms API from Lever — 2 operation(s) for forms.
  name: Lever Forms API
  slug: lever-forms-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Interviews API from Lever — 2 operation(s) for interviews.
  name: Lever Interviews API
  slug: lever-interviews-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Notes API from Lever — 1 operation(s) for notes.
  name: Lever Notes API
  slug: lever-notes-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Offers API from Lever — 1 operation(s) for offers.
  name: Lever Offers API
  slug: lever-offers-api
- baseURL: https://api.lever.co/v1
  baseurl_source: declared
  description: The Resumes API from Lever — 1 operation(s) for resumes.
  name: Lever Resumes API
  slug: lever-resumes-api
artifact_total: 86
asyncapis:
- description: ''
  name: Lever Webhooks
  slug: lever-webhooks
collections:
- collection_type: open
  name: Lever Applications API
  slug: open-lever-applications-api
- collection_type: open
  name: Lever Applications ArchiveReasons API
  slug: open-lever-archivereasons-api
- collection_type: open
  name: Lever Applications AuditEvents API
  slug: open-lever-auditevents-api
- collection_type: open
  name: Lever Applications Contacts API
  slug: open-lever-contacts-api
- collection_type: open
  name: Lever Applications EEO API
  slug: open-lever-eeo-api
- collection_type: open
  name: Lever Applications Feedback API
  slug: open-lever-feedback-api
- collection_type: open
  name: Lever Applications Files API
  slug: open-lever-files-api
- collection_type: open
  name: Lever Applications Forms API
  slug: open-lever-forms-api
- collection_type: open
  name: Lever Applications Interviews API
  slug: open-lever-interviews-api
- collection_type: open
  name: Lever Applications Notes API
  slug: open-lever-notes-api
- collection_type: open
  name: Lever Applications Offers API
  slug: open-lever-offers-api
- collection_type: open
  name: Lever Applications Opportunities API
  slug: open-lever-opportunities-api
- collection_type: open
  name: Lever Applications Postings API
  slug: open-lever-postings-api
- collection_type: open
  name: Lever Applications Requisitions API
  slug: open-lever-requisitions-api
- collection_type: open
  name: Lever Applications Resumes API
  slug: open-lever-resumes-api
- collection_type: open
  name: Lever Applications Sources API
  slug: open-lever-sources-api
- collection_type: open
  name: Lever Applications Stages API
  slug: open-lever-stages-api
- collection_type: open
  name: Lever Applications Tags API
  slug: open-lever-tags-api
- collection_type: open
  name: Lever Applications Users API
  slug: open-lever-users-api
- collection_type: open
  name: Lever API
  slug: open-lever
common:
- group: design
  href: https://artifacts.apis.io/lever/rules/lever-rules.yml
  title: ''
  type: Spectral
  url: rules/lever-rules.yml
- group: design
  href: https://artifacts.apis.io/lever/json-ld/lever-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lever-context.jsonld
- group: design
  href: https://artifacts.apis.io/lever/vocabulary/lever-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lever-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/lever/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/lever/asyncapi/lever-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lever-webhooks.yml
- group: design
  href: https://artifacts.apis.io/lever/data-model/lever-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lever-data-model.yml
- group: design
  href: https://artifacts.apis.io/lever/components/lever-components.yml
  title: ''
  type: Components
  url: components/lever-components.yml
- group: operate
  href: https://artifacts.apis.io/lever/changelog/lever-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lever-changelog.yml
- group: design
  href: https://artifacts.apis.io/lever/conventions/lever-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lever-conventions.yml
- group: start
  href: https://artifacts.apis.io/lever/sandbox/lever-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/lever-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.lever.co/security
- group: design
  href: https://artifacts.apis.io/lever/lifecycle/lever-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lever-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/lever/errors/lever-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lever-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lever/conformance/lever-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lever-conformance.yml
- group: auth
  href: https://artifacts.apis.io/lever/well-known/lever-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lever-status-security.txt
- group: agent
  href: https://artifacts.apis.io/lever/well-known/lever-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lever-well-known.yml
- group: other
  href: https://artifacts.apis.io/lever/hosts/lever-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lever-hosts.yml
- group: build
  href: https://artifacts.apis.io/lever/integrations/lever-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/lever-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/lever/vendors/lever-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lever-vendors.yml
- group: other
  href: https://artifacts.apis.io/lever/capabilities/lever-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lever-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/lever/agentic-access/lever-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lever-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/lever/security/lever-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lever-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/lever/security/lever-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lever-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lever/security/lever-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lever-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/lever/authentication/lever-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lever-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lever-
- group: company
  title: ''
  type: Website
  url: https://www.lever.co/
- group: docs
  title: ''
  type: Documentation
  url: https://hire.lever.co/developer
- group: docs
  title: ''
  type: APIReference
  url: https://hire.lever.co/developer/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lever.co/pricing
- group: start
  title: ''
  type: Login
  url: https://hire.lever.co/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lever.co/
- group: company
  title: ''
  type: Blog
  url: https://www.lever.co/blog
- group: operate
  title: ''
  type: Support
  url: https://help.lever.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lever
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lever.co/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lever.co/legal/terms-of-service
- group: auth
  title: ''
  type: Authentication
  url: https://hire.lever.co/developer/oauth
- group: design
  title: ''
  type: Webhooks
  url: https://hire.lever.co/developer/documentation#webhooks
- group: operate
  href: https://artifacts.apis.io/lever/rate-limits/lever-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lever-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lever/finops/lever-finops.yml
  title: ''
  type: FinOps
  url: finops/lever-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hire.lever.co/developer
- group: start
  title: ''
  type: GettingStarted
  url: https://hire.lever.co/developer/partner
- group: operate
  title: ''
  type: ChangeLog
  url: https://hire.lever.co/developer/updates
- group: build
  title: ''
  type: Postman
  url: https://github.com/lever/integrator-resources/blob/main/DataAPIPostman/Lever-DataAPI-Collection.json
- group: operate
  title: ''
  type: FAQ
  url: https://hire.lever.co/developer/support
- group: operate
  title: ''
  type: SLA
  url: https://www.lever.co/agreements/sla
- group: commercial
  title: ''
  type: Legal
  url: https://www.lever.co/legal
- group: other
  title: ''
  type: Marketplace
  url: https://www.lever.co/marketplace
- group: company
  title: ''
  type: Partners
  url: https://www.lever.co/partners
- group: auth
  title: ''
  type: Security
  url: https://www.lever.co/security
created: '2026-05-08'
description: Lever is a talent acquisition and applicant tracking platform built on the Opportunities data model. The Lever API exposes candidates, opportunities, postings, interviews, feedback, requisitions, users, files, webhooks, and a public Postings API for embedding job sites.
features:
- REST API at https://api.lever.co/v1 (JSON over HTTPS)
- Basic Auth (API key) and OAuth 2.0 for partner apps
- 10 requests/second per API key with burst to 20 req/s (token bucket)
- Pagination via limit (1-100) and cursor-based offset tokens
- include / expand parameters for projection and inline expansion
- HMAC-SHA256 signed webhook events
- Public Postings API for unauthenticated job-listing retrieval
- XML feed for aggregator syndication
- Custom-quoted SaaS pricing — no public price list
finops:
- has_sources: true
  method: generated
  name: Lever Finops
  primary_unit: ''
  service_category: HR
  slug: lever-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lever.png
json_schemas:
- name: GetOpportunitiesOpportunityFeedbackFeedbackResponse
  property_count: 13
  slug: lever-get-opportunities-opportunity-feedback-feedback-response
- name: GetOpportunitiesOpportunityPanelsPanelResponse
  property_count: 14
  slug: lever-get-opportunities-opportunity-panels-panel-response
- name: GetPostingsPostingResponse
  property_count: 21
  slug: lever-get-postings-posting-response
- name: GetRequisitionsRequisitionResponse
  property_count: 26
  slug: lever-get-requisitions-requisition-response
- name: PostCandidatesRequest
  property_count: 17
  slug: lever-post-candidates-request
- name: PostOpportunitiesRequest
  property_count: 15
  slug: lever-post-opportunities-request
jsonld:
- class_count: 120
  name: Lever Context
  property_count: 124
  slug: lever-context
layout: provider
modified: '2026-05-19'
name: Lever
nav: Providers
network: true
overview: 'Lever is listed with 33 APIs on the [APIs.io](https://apis.io/) network, including Candidates API, Feedback Templates API, Webhooks API, and 30 more. Tagged areas include Human Resources, Applicant Tracking, Recruiting, Talent Acquisition, and Software-as-a-Service.


  The Lever catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Lever''s developer surface includes changelog, sandbox, authentication, documentation, API reference, pricing, engineering blog, and 44 more developer resources.'
plans:
- name: Lever Plans Pricing
  plan_count: 0
  slug: lever-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Lever Rate Limits
  slug: lever-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Lever API Rules
  rule_count: 45
  severity_counts:
    error: 38
    hint: 0
    info: 3
    warn: 4
  slug: lever-rules
scopes:
- name: Lever Scopes
  scope_count: 51
  slug: lever-scopes
  summary_line: 51 scopes
score:
  band: strong
  composite: 58.2
  coverage:
    artifact_dirs: 37
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 19.9
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 44.8
    developer_ergonomics: 54.2
    discoverability: 71.4
    operational_transparency: 73.7
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 21
      marker_coverage: 72.4
      total: 29
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 52.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lever/lever-2026-06-20T184437.png
security:
- kind: authentication
  name: Lever Authentication
  slug: lever-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Lever Domain Security
  slug: lever-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lever Vulnerability Disclosure
  slug: lever-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Lever Trust Center
  slug: lever-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
skill_count: 6
skills:
- name: lever-create-opportunity
  slug: lever-create-opportunity
- name: lever-interview-feedback
  slug: lever-interview-feedback
- name: lever-list-opportunities
  slug: lever-list-opportunities
- name: lever-postings-and-applications
  slug: lever-postings-and-applications
- name: lever-requisitions
  slug: lever-requisitions
- name: lever-webhooks
  slug: lever-webhooks
slug: lever
tags:
- Human Resources
- Applicant Tracking
- Recruiting
- Talent Acquisition
- Software-as-a-Service
website: https://www.lever.co/
---
