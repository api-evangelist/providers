---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Lever Co Agentic Access
  operation_count: 53
  slug: lever-co-agentic-access
  summary_line: 53 operations · 24 acting
api_count: 20
apis:
- description: XML feed of all published job postings for a Lever site, designed for distribution to third-party job boards. Returned by appending `?mode=xml` to the Postings API list endpoint. Fields include positi
  name: Lever Postings XML Feed
  slug: lever-postings-xml-feed
- description: Lever publishes ten webhook events covering the application and candidate lifecycle — applicationCreated, candidateHired, candidateStageChange, candidateArchiveChange, candidateDeleted, interviewCreat
  name: Lever Webhooks
  slug: lever-webhooks
- description: A candidate's application to a specific posting on an opportunity.
  name: Lever Applications API
  slug: lever-co-applications-api
- description: Reasons candidates are archived (rejected, withdrew, hired, etc).
  name: Lever Archive Reasons API
  slug: lever-co-archive-reasons-api
- description: Audit log of admin and security-relevant actions.
  name: Lever Audit Events API
  slug: lever-co-audit-events-api
- description: Equal Employment Opportunity survey responses.
  name: Lever EEO Responses API
  slug: lever-co-eeo-responses-api
- description: Structured interview feedback from interviewers.
  name: Lever Feedback API
  slug: lever-co-feedback-api
- description: Resumes and other attachments on an opportunity.
  name: Lever Files API
  slug: lever-co-files-api
- description: Scheduled interviews on an opportunity.
  name: Lever Interviews API
  slug: lever-co-interviews-api
- description: Free-form notes captured on an opportunity.
  name: Lever Notes API
  slug: lever-co-notes-api
- description: Offer records associated with hired candidates.
  name: Lever Offers API
  slug: lever-co-offers-api
- description: Opportunities are the unified record for a candidate at a posting (replaces legacy Candidates).
  name: Lever Opportunities API
  slug: lever-co-opportunities-api
- description: Interview panels comprising multiple interviewers.
  name: Lever Panels API
  slug: lever-co-panels-api
- description: Job postings published to the company careers site.
  name: Lever Postings API
  slug: lever-co-postings-api
- description: Headcount-tracking job requisitions backing postings.
  name: Lever Requisitions API
  slug: lever-co-requisitions-api
- description: How candidates entered the pipeline (referral, agency, job board, sourced, etc).
  name: Lever Sources API
  slug: lever-co-sources-api
- description: Pipeline stages (lead, applicant, phone screen, on-site, offer, hired, archived).
  name: Lever Stages API
  slug: lever-co-stages-api
- description: Free-form tags applied to opportunities.
  name: Lever Tags API
  slug: lever-co-tags-api
- description: Lever users (recruiters, hiring managers, interviewers, admins).
  name: Lever Users API
  slug: lever-co-users-api
- description: Outbound event subscriptions.
  name: Lever Webhooks API
  slug: lever-co-webhooks-api
artifact_total: 54
collections:
- collection_type: postman
  name: Lever Data Applications API
  slug: postman-lever-co-applications-api
- collection_type: postman
  name: Lever Data Applications Archive Reasons API
  slug: postman-lever-co-archive-reasons-api
- collection_type: postman
  name: Lever Data Applications Audit Events API
  slug: postman-lever-co-audit-events-api
- collection_type: postman
  name: Lever Data Applications EEO Responses API
  slug: postman-lever-co-eeo-responses-api
- collection_type: postman
  name: Lever Data Applications Feedback API
  slug: postman-lever-co-feedback-api
- collection_type: postman
  name: Lever Data Applications Files API
  slug: postman-lever-co-files-api
- collection_type: postman
  name: Lever Data Applications Interviews API
  slug: postman-lever-co-interviews-api
- collection_type: postman
  name: Lever Data Applications Notes API
  slug: postman-lever-co-notes-api
- collection_type: postman
  name: Lever Data Applications Offers API
  slug: postman-lever-co-offers-api
- collection_type: postman
  name: Lever Data Applications Opportunities API
  slug: postman-lever-co-opportunities-api
- collection_type: postman
  name: Lever Data Applications Panels API
  slug: postman-lever-co-panels-api
- collection_type: postman
  name: Lever Data Applications Postings API
  slug: postman-lever-co-postings-api
- collection_type: postman
  name: Lever Data Applications Requisitions API
  slug: postman-lever-co-requisitions-api
- collection_type: postman
  name: Lever Data Applications Sources API
  slug: postman-lever-co-sources-api
- collection_type: postman
  name: Lever Data Applications Stages API
  slug: postman-lever-co-stages-api
- collection_type: postman
  name: Lever Data Applications Tags API
  slug: postman-lever-co-tags-api
- collection_type: postman
  name: Lever Data Applications Users API
  slug: postman-lever-co-users-api
- collection_type: postman
  name: Lever Data Applications Webhooks API
  slug: postman-lever-co-webhooks-api
- collection_type: open
  name: Lever Data API
  slug: open-lever-data-api
- collection_type: open
  name: Lever Postings API
  slug: open-lever-postings-api
- collection_type: open
  name: Lever Webhooks
  slug: open-lever-webhooks-asyncapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/lever/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lever-co-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lever-co-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lever-co-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lever-co-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lever-co-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lever-co-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.lever.co/
- group: start
  title: ''
  type: Portal
  url: https://hire.lever.co/developer
- group: docs
  title: ''
  type: Documentation
  url: https://hire.lever.co/developer/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://hire.lever.co/developer/usecases
- group: docs
  title: ''
  type: Documentation
  url: https://hire.lever.co/developer/partner
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/lever
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/lever/postings-api
- group: company
  title: ''
  type: Partners
  url: https://leverpartner.com
- group: operate
  title: ''
  type: Support
  url: https://help.lever.co/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lever.co/
- group: company
  title: ''
  type: Blog
  url: https://www.lever.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lever.co/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lever.co/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.employinc.com/privacy/
- group: auth
  title: ''
  type: Security
  url: https://www.employinc.com/legal/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lever-co
- group: docs
  title: ''
  type: Documentation
  url: https://www.employinc.com/
- group: commercial
  title: ''
  type: Plans
  url: https://www.lever.co/pricing
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lever-co-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lever-co-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lever-co-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: https://hire.lever.co/developer/documentation
finops:
- name: Lever Co Finops
  service_category: Human Resources
  slug: lever-co-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lever-co.png
json_schemas:
- name: Lever Opportunity
  property_count: 23
  slug: lever-opportunity
- name: Lever Posting
  property_count: 22
  slug: lever-posting
jsonld:
- class_count: 0
  name: Lever Co Context
  property_count: 9
  slug: lever-co-context
layout: provider
name: Lever
nav: Providers
network: true
overview: 'Lever publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Applications API, Archive Reasons API, and 16 more. Tagged areas include Applicant Tracking, ATS, CRM, Recruiting, and Hiring.


  The Lever catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lever''s developer surface includes authentication, developer portal, documentation, support, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Lever Co Plans Pricing
  plan_count: 1
  slug: lever-co-plans-pricing
random_paper: 101
rate_limits:
- limit_count: 3
  name: Lever Co Rate Limits
  slug: lever-co-rate-limits
rules:
- name: Lever API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: lever-co-jsonschema-spectral-rules
scopes:
- name: Lever Co Scopes
  scope_count: 22
  slug: lever-co-scopes
  summary_line: 22 scopes · authorizationCode
score:
  band: strong
  composite: 59.4
  delta: -0.6
  facets:
    commercial_clarity: 68.4
    contract_quality: 71.2
    developer_ergonomics: 39.1
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 57.9
  previous_composite: 60.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 94.7
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lever-co/refs/heads/main/screenshots/lever-co-2026-06-20T184439.png
security:
- kind: authentication
  name: Lever Co Authentication
  slug: lever-co-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Lever Co Domain Security
  slug: lever-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lever Co Vulnerability Disclosure
  slug: lever-co-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Lever Co Trust Center
  slug: lever-co-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: lever-co
tags:
- Applicant Tracking
- ATS
- CRM
- Recruiting
- Hiring
- Talent Acquisition
- Human Resources
- HR Tech
- Postings
- Webhooks
- OAuth
website: https://www.lever.co/
---
