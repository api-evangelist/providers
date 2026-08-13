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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Lever Agentic Access
  operation_count: 55
  slug: lever-agentic-access
  summary_line: 55 operations · 18 acting
api_count: 41
apis:
- description: Legacy Candidates endpoints maintained for backward compatibility. New integrations should use Opportunities; Candidates remain available for historical record retrieval.
  name: Lever Candidates API
  slug: lever-candidates-api
- description: Contacts represent unique people across multiple opportunities, allowing Lever to deduplicate candidates who apply to multiple roles.
  name: Lever Contacts API
  slug: lever-contacts-api
- description: Manage job postings programmatically and power custom public job sites. The Postings API has a public read-only mode that does not require authentication for displaying job listings.
  name: Lever Postings API
  slug: lever-postings-api
- description: Submit candidate applications against postings, including resumes, cover letters, and EEO survey data, and retrieve historical application records.
  name: Lever Applications API
  slug: lever-applications-api
- description: List the configured pipeline stages and disposition stages used to route opportunities through screening, interviews, offer, and hire.
  name: Lever Stages API
  slug: lever-stages-api
- description: Read archive reasons used when an opportunity is archived (rejected, hired, withdrawn) for downstream EEO and analytics reporting.
  name: Lever Archive Reasons API
  slug: lever-archive-reasons-api
- description: Read interview events, panels, and schedules associated with an opportunity, including interviewer assignments and time slots.
  name: Lever Interviews API
  slug: lever-interviews-api
- description: Read feedback forms and scorecards completed by interviewers and hiring managers, with templated and free-form fields.
  name: Lever Feedback API
  slug: lever-feedback-api
- description: Manage feedback form templates, including question definitions and scoring rubrics applied across postings and stages.
  name: Lever Feedback Templates API
  slug: lever-feedback-templates-api
- description: Add and retrieve free-form notes attached to opportunities for recruiter and hiring manager collaboration.
  name: Lever Notes API
  slug: lever-notes-api
- description: Read offer records associated with opportunities, including offer letters, approval status, and compensation breakdowns.
  name: Lever Offers API
  slug: lever-offers-api
- description: Manage requisitions backing each posting — headcount, compensation bands, and approval state — typically synced from an HRIS.
  name: Lever Requisitions API
  slug: lever-requisitions-api
- description: List and apply tags to opportunities for cohorting, sourcing, and reporting workflows.
  name: Lever Tags API
  slug: lever-tags-api
- description: Read source attribution (job board, referral, sourced) for opportunities to drive sourcing analytics.
  name: Lever Sources API
  slug: lever-sources-api
- description: Upload and download files (resumes, cover letters, portfolio attachments) associated with opportunities; supports docx, doc, pdf, txt, jpg, png.
  name: Lever Files API
  slug: lever-files-api
- description: Read parsed resume data — work history, education, skills — extracted from candidate submissions.
  name: Lever Resumes API
  slug: lever-resumes-api
- description: Manage Lever users and their access roles (Super Admin, Admin, Team Member, Limited Team Member, Interviewer, Outsider).
  name: Lever Users API
  slug: lever-users-api
- description: Read tenant-scoped audit events for security monitoring and SOC reporting.
  name: Lever Audit Events API
  slug: lever-audit-events-api
- description: Read anonymous EEO survey data for compliance reporting; PII-isolated from the standard candidate endpoints.
  name: Lever EEO API
  slug: lever-eeo-api
- description: Subscribe to Lever events (applicationCreated, candidateHired, stageChange, contactUpdate). Events are signed with HMAC-SHA256 for receiver verification.
  name: Lever Webhooks API
  slug: lever-webhooks-api
- description: The unauthenticated public Postings API for retrieving live job listings from a Lever account, used by external careers pages.
  name: Lever Postings Public API
  slug: lever-postings-public-api
- description: XML feed of open postings used by job aggregators (Indeed, Glassdoor, LinkedIn) for syndication.
  name: Lever XML Feed
  slug: lever-xml-feed-api
- description: The Applications API from Lever — 2 operation(s) for applications.
  name: Lever Applications API
  slug: lever-applications-api
- description: The ArchiveReasons API from Lever — 2 operation(s) for archivereasons.
  name: Lever ArchiveReasons API
  slug: lever-archivereasons-api
- description: The AuditEvents API from Lever — 1 operation(s) for auditevents.
  name: Lever AuditEvents API
  slug: lever-auditevents-api
- description: The Contacts API from Lever — 1 operation(s) for contacts.
  name: Lever Contacts API
  slug: lever-contacts-api
- description: The EEO API from Lever — 2 operation(s) for eeo.
  name: Lever EEO API
  slug: lever-eeo-api
- description: The Feedback API from Lever — 2 operation(s) for feedback.
  name: Lever Feedback API
  slug: lever-feedback-api
- description: The Files API from Lever — 2 operation(s) for files.
  name: Lever Files API
  slug: lever-files-api
- description: The Forms API from Lever — 2 operation(s) for forms.
  name: Lever Forms API
  slug: lever-forms-api
- description: The Interviews API from Lever — 2 operation(s) for interviews.
  name: Lever Interviews API
  slug: lever-interviews-api
- description: The Notes API from Lever — 1 operation(s) for notes.
  name: Lever Notes API
  slug: lever-notes-api
- description: The Offers API from Lever — 1 operation(s) for offers.
  name: Lever Offers API
  slug: lever-offers-api
- description: The Opportunities API from Lever — 10 operation(s) for opportunities.
  name: Lever Opportunities API
  slug: lever-opportunities-api
- description: The Postings API from Lever — 5 operation(s) for postings.
  name: Lever Postings API
  slug: lever-postings-api
- description: The Requisitions API from Lever — 2 operation(s) for requisitions.
  name: Lever Requisitions API
  slug: lever-requisitions-api
- description: The Resumes API from Lever — 1 operation(s) for resumes.
  name: Lever Resumes API
  slug: lever-resumes-api
- description: The Sources API from Lever — 1 operation(s) for sources.
  name: Lever Sources API
  slug: lever-sources-api
- description: The Stages API from Lever — 3 operation(s) for stages.
  name: Lever Stages API
  slug: lever-stages-api
- description: The Tags API from Lever — 1 operation(s) for tags.
  name: Lever Tags API
  slug: lever-tags-api
- description: The Users API from Lever — 2 operation(s) for users.
  name: Lever Users API
  slug: lever-users-api
artifact_total: 60
collections:
- collection_type: open
  name: Lever API
  slug: open-lever
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lever-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lever-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lever-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lever-domain-security.yml
- group: auth
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
  url: https://www.lever.co/pricing/
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
  url: https://www.lever.co/legal/
- group: auth
  title: ''
  type: Authentication
  url: https://hire.lever.co/developer/oauth
- group: design
  title: ''
  type: Webhooks
  url: https://hire.lever.co/developer/documentation#webhooks
- group: commercial
  title: ''
  type: Plans
  url: plans/lever-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lever-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lever-finops.yml
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
- name: Lever Finops
  service_category: HR
  slug: lever-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Lever ATS (Applicant Tracking System) API. Lever's production API is REST-based (https://api.lever.co/v1), but this schema translates the fu
  name: Lever GraphQL Schema
  slug: lever-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lever.png
layout: provider
modified: '2026-05-19'
name: Lever
nav: Providers
network: true
overview: 'Lever publishes 34 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Postings API, Applications API, and 31 more. Tagged areas include HR, ATS, Recruiting, Talent Acquisition, and SaaS.


  Lever''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, and 16 more developer resources.'
plans:
- name: Lever Plans Pricing
  plan_count: 4
  slug: lever-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 4
  name: Lever Rate Limits
  slug: lever-rate-limits
score:
  band: developing
  composite: 45.1
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 58.2
    developer_ergonomics: 32.6
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lever/refs/heads/main/screenshots/lever-2026-06-20T184437.png
security:
- kind: authentication
  name: Lever Authentication
  slug: lever-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Lever Domain Security
  slug: lever-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lever Vulnerability Disclosure
  slug: lever-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Lever Trust Center
  slug: lever-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: lever
tags:
- HR
- ATS
- Recruiting
- Talent Acquisition
- SaaS
website: https://www.lever.co/
---
