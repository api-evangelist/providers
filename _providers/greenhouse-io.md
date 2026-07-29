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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 66
  human_in_the_loop: 0
  name: Greenhouse Io Agentic Access
  operation_count: 126
  slug: greenhouse-io-agentic-access
  summary_line: 126 operations · 66 acting
api_count: 27
apis:
- description: Event-driven webhooks from Greenhouse Recruiting. Greenhouse POSTs JSON to your HTTPS endpoint on each event; payloads carry a Greenhouse-Event-ID header for idempotency and HMAC SHA-256 signature ver
  name: Greenhouse Recruiting Webhooks
  slug: greenhouse-recruiting-webhooks
- description: 'Event-driven webhooks from Greenhouse Onboarding (currently in beta and gated by customer approval). Each event posts event_type, id, and payload to the customer''s HTTPS endpoint; signatures use HMAC '
  name: Greenhouse Onboarding Webhooks
  slug: greenhouse-onboarding-webhooks
- description: Per-candidate timeline of activity events.
  name: Greenhouse ActivityFeed API
  slug: greenhouse-io-activityfeed-api
- description: Candidate applications to specific jobs, including stage advancement, transfers, hires, rejections, and attachments.
  name: Greenhouse Applications API
  slug: greenhouse-io-applications-api
- description: Approval flows for jobs and offers.
  name: Greenhouse Approvals API
  slug: greenhouse-io-approvals-api
- description: JWT access token issuance.
  name: Greenhouse Auth API
  slug: greenhouse-io-auth-api
- description: Create or retrieve candidates / prospects in the customer's Greenhouse account.
  name: Greenhouse Candidates API
  slug: greenhouse-io-candidates-api
- description: Org-defined custom fields and their options.
  name: Greenhouse CustomFields API
  slug: greenhouse-io-customfields-api
- description: Organizational departments.
  name: Greenhouse Departments API
  slug: greenhouse-io-departments-api
- description: Audit log events.
  name: Greenhouse Events API
  slug: greenhouse-io-events-api
- description: Single GraphQL endpoint for all Onboarding operations.
  name: Greenhouse GraphQL API
  slug: greenhouse-io-graphql-api
- description: Individual openings under a Job.
  name: Greenhouse JobOpenings API
  slug: greenhouse-io-jobopenings-api
- description: Public-facing job postings and their statuses.
  name: Greenhouse JobPosts API
  slug: greenhouse-io-jobposts-api
- description: List jobs visible to the integrated user.
  name: Greenhouse Jobs API
  slug: greenhouse-io-jobs-api
- description: The interview/pipeline stages a job uses.
  name: Greenhouse JobStages API
  slug: greenhouse-io-jobstages-api
- description: Offers extended to candidates.
  name: Greenhouse Offers API
  slug: greenhouse-io-offers-api
- description: Office locations.
  name: Greenhouse Offices API
  slug: greenhouse-io-offices-api
- description: Read configured prospect pools and their stages.
  name: Greenhouse ProspectPools API
  slug: greenhouse-io-prospectpools-api
- description: Configured rejection reasons.
  name: Greenhouse RejectionReasons API
  slug: greenhouse-io-rejectionreasons-api
- description: Scheduled interview events on the calendar.
  name: Greenhouse ScheduledInterviews API
  slug: greenhouse-io-scheduledinterviews-api
- description: Interview scorecards captured by interviewers.
  name: Greenhouse Scorecards API
  slug: greenhouse-io-scorecards-api
- description: Candidate-source taxonomy (where the candidate came from).
  name: Greenhouse Sources API
  slug: greenhouse-io-sources-api
- description: Candidate tags.
  name: Greenhouse Tags API
  slug: greenhouse-io-tags-api
- description: Sending tests to candidates and reporting status.
  name: Greenhouse TestDelivery API
  slug: greenhouse-io-testdelivery-api
- description: Available tests offered by the partner.
  name: Greenhouse Tests API
  slug: greenhouse-io-tests-api
- description: Generate branded tracking links for sourcing campaigns.
  name: Greenhouse TrackingLinks API
  slug: greenhouse-io-trackinglinks-api
- description: Inspect the current authenticated user.
  name: Greenhouse Users API
  slug: greenhouse-io-users-api
artifact_total: 93
collections:
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed API
  slug: postman-greenhouse-io-activityfeed-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed Applications API
  slug: postman-greenhouse-io-applications-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed Approvals API
  slug: postman-greenhouse-io-approvals-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed Auth API
  slug: postman-greenhouse-io-auth-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed Candidates API
  slug: postman-greenhouse-io-candidates-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed CustomFields API
  slug: postman-greenhouse-io-customfields-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed Departments API
  slug: postman-greenhouse-io-departments-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed Events API
  slug: postman-greenhouse-io-events-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed GraphQL API
  slug: postman-greenhouse-io-graphql-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed JobOpenings API
  slug: postman-greenhouse-io-jobopenings-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed JobPosts API
  slug: postman-greenhouse-io-jobposts-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed Jobs API
  slug: postman-greenhouse-io-jobs-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed JobStages API
  slug: postman-greenhouse-io-jobstages-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed Offers API
  slug: postman-greenhouse-io-offers-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed Offices API
  slug: postman-greenhouse-io-offices-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed ProspectPools API
  slug: postman-greenhouse-io-prospectpools-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed RejectionReasons API
  slug: postman-greenhouse-io-rejectionreasons-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed ScheduledInterviews API
  slug: postman-greenhouse-io-scheduledinterviews-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed Scorecards API
  slug: postman-greenhouse-io-scorecards-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed Sources API
  slug: postman-greenhouse-io-sources-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed Tags API
  slug: postman-greenhouse-io-tags-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed TestDelivery API
  slug: postman-greenhouse-io-testdelivery-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed Tests API
  slug: postman-greenhouse-io-tests-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed TrackingLinks API
  slug: postman-greenhouse-io-trackinglinks-api
- collection_type: postman
  name: Greenhouse Assessment Partner ActivityFeed Users API
  slug: postman-greenhouse-io-users-api
- collection_type: open
  name: Greenhouse Assessment Partner API
  slug: open-greenhouse-assessment-api
- collection_type: open
  name: Greenhouse Audit Log API
  slug: open-greenhouse-audit-log-api
- collection_type: open
  name: Greenhouse Candidate Ingestion API
  slug: open-greenhouse-candidate-ingestion-api
- collection_type: open
  name: Greenhouse Harvest API
  slug: open-greenhouse-harvest-api
- collection_type: open
  name: Greenhouse Job Board API
  slug: open-greenhouse-job-board-api
- collection_type: open
  name: Greenhouse Onboarding API
  slug: open-greenhouse-onboarding-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/greenhouse/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/greenhouse-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/greenhouse-io-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/greenhouse-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/greenhouse-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/greenhouse-io-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/greenhouse-io-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.greenhouse.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.greenhouse.io
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
- group: commercial
  title: ''
  type: Plans
  url: https://www.greenhouse.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/greenhouse-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/greenhouse-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/greenhouse-io-finops.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.greenhouse.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.greenhouse.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.greenhouse.com/legal/terms
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.greenhouse.com
- group: operate
  title: ''
  type: Support
  url: https://support.greenhouse.io
- group: other
  title: ''
  type: Customers
  url: https://www.greenhouse.com/customers
- group: company
  title: ''
  type: Blog
  url: https://www.greenhouse.com/blog
- group: company
  title: ''
  type: Careers
  url: https://www.greenhouse.com/jobs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/greenhouse-software
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Greenhouse
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/grnhse
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/grnhse/greenhouse-api-docs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grnhse/greenhouse_io
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grnhse/greenhouse-tools-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grnhse/omniauth-greenhouse
created: '2026-05-25T00:00:00.000Z'
description: Greenhouse Software is an enterprise applicant tracking system (ATS) and end-to-end hiring platform spanning sourcing, structured interviewing, offer management, hiring decisions, and new-hire onboarding. The company markets itself across early-stage, scaling, and enterprise tiers (Core, Plus, Pro) and lists customers including DoorDash, Betterment, MLB, Coupang, HelloFresh, Trivago, and the NFL. Greenhouse exposes a broad developer surface — Harvest (REST), Job Board, Audit Log (Pro), Candidate Ingestion (Partner), Onboarding (GraphQL), Assessment (partner-hosted), and Recruiting / Onboarding Webhooks — that powers hundreds of pre-built integrations across sourcing, assessment, background-check, video-interviewing, HRIS, payroll, SSO, and e-signature vendors. The platform recently acquired Ezra AI Labs to integrate conversational AI into the hiring workflow and continues to invest in fraud detection and identity verification through its Real Talent feature set.
features:
- Structured hiring with interview kits, scorecards, and stage gates
- Sourcing and CRM with prospect pools, prospect owners, and prospect stages
- Greenhouse Sourcing Automation (Plus tier)
- Candidate texting (Plus tier)
- AI-powered job boards and AI candidate summaries
- Real Talent — fraud detection, identity verification, candidate matching
- Ezra AI Labs conversational AI (post-acquisition)
- MyGreenhouse candidate experience portal
- Hundreds of pre-built integrations across sourcing, assessment, background, video, HRIS, e-sign
- Granular per-endpoint API key permissions (Harvest API)
- On-Behalf-Of header pattern for partner-attributed actions
- Recruiting Webhooks with HMAC SHA-256 signature verification
- Onboarding Webhooks (beta)
- Audit Log API (Pro tier) with JWT bearer auth and 30-day retention
- Onboarding GraphQL API with query-complexity rate limiting
- Greenhouse Onboarding for new-hire workflows, employee profiles, departments, locations
- Job Board API for unauthenticated public read of careers data
- Developer sandbox and sync (Pro tier)
- SSO via SAML 2.0; SCIM-style user provisioning via Harvest /users
- Business Intelligence Connector (Plus tier)
- Custom fields across job, candidate, application, offer, opening, department, office, user, prospect
finops:
- name: Greenhouse Io Finops
  service_category: Business Applications
  slug: greenhouse-io-finops
graphqls:
- description: The Greenhouse Onboarding (GHO) API is a single GraphQL endpoint covering employees,
  name: Greenhouse GraphQL API
  slug: greenhouse-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/greenhouse-io.png
json_schemas:
- name: Greenhouse Candidate
  property_count: 21
  slug: greenhouse-candidate
- name: Greenhouse Job
  property_count: 15
  slug: greenhouse-job
jsonld:
- class_count: 0
  name: Greenhouse Io Context
  property_count: 11
  slug: greenhouse-io-context
layout: provider
modified: '2026-05-25'
name: Greenhouse
nav: Providers
network: true
overview: 'Greenhouse publishes 25 APIs on the [APIs.io](https://apis.io/) network, including ActivityFeed API, Applications API, Approvals API, and 22 more. Tagged areas include ATS, Recruiting, Hiring, Talent Acquisition, and Enterprise SaaS.


  The Greenhouse catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Greenhouse''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 31 more developer resources.'
plans:
- name: Greenhouse Io Plans Pricing
  plan_count: 3
  slug: greenhouse-io-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 5
  name: Greenhouse Io Rate Limits
  slug: greenhouse-io-rate-limits
rules:
- name: Greenhouse API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: greenhouse-io-jsonschema-spectral-rules
scopes:
- name: Greenhouse Io Scopes
  scope_count: 1
  slug: greenhouse-io-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: strong
  composite: 61.5
  delta: -3.8
  facets:
    commercial_clarity: 68.4
    contract_quality: 68.6
    developer_ergonomics: 54.3
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 65.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/greenhouse-io/refs/heads/main/screenshots/greenhouse-io-2026-06-20T182402.png
security:
- kind: authentication
  name: Greenhouse Io Authentication
  slug: greenhouse-io-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Greenhouse Io Domain Security
  slug: greenhouse-io-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Greenhouse Io Vulnerability Disclosure
  slug: greenhouse-io-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Greenhouse Io Trust Center
  slug: greenhouse-io-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
slug: greenhouse-io
tags:
- ATS
- Recruiting
- Hiring
- Talent Acquisition
- Enterprise SaaS
- Human Resources
- Onboarding
website: https://www.greenhouse.com
---
