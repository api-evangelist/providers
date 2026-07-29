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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Submittable Agentic Access
  operation_count: 19
  slug: submittable-agentic-access
  summary_line: 19 operations · 5 acting
api_count: 10
apis:
- description: Routing of submissions to reviewers.
  name: Submittable Assignments API
  slug: submittable-assignments-api
- description: Form-field responses captured on submissions.
  name: Submittable Entries API
  slug: submittable-entries-api
- description: Budgets and grant distributions.
  name: Submittable Funds API
  slug: submittable-funds-api
- description: Tags used to categorize submissions.
  name: Submittable Labels API
  slug: submittable-labels-api
- description: Message attachments.
  name: Submittable Messaging API
  slug: submittable-messaging-api
- description: Payment records.
  name: Submittable Payments API
  slug: submittable-payments-api
- description: The forms/programs people apply through.
  name: Submittable Projects API
  slug: submittable-projects-api
- description: Applications and entries sent to your projects.
  name: Submittable Submissions API
  slug: submittable-submissions-api
- description: Organization team members and reviewers.
  name: Submittable Teams API
  slug: submittable-teams-api
- description: Submitters - the people who send submissions.
  name: Submittable Users API
  slug: submittable-users-api
artifact_total: 18
collections:
- collection_type: open
  name: Submittable API (v4)
  slug: open-submittable
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/submittable-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/submittable-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/submittable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/submittable-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/submittable
- group: company
  title: ''
  type: Website
  url: https://www.submittable.com
- group: docs
  title: ''
  type: Documentation
  url: https://submittable-api.submittable.com/docs/v4/index.html
- group: docs
  title: ''
  type: SupportDocumentation
  url: https://submittable.help/en/collections/1728753-integrations-api
- group: commercial
  title: ''
  type: Plans
  url: plans/submittable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/submittable-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/submittable-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.submittable.com/pricing/
created: '2026-07-05'
description: Submittable is a submission management, grants, and applications platform used by foundations, nonprofits, corporations, and governments to collect, review, and manage forms, applications, submissions, and awards. Its public REST API (v4, base https://submittable-api.submittable.com) provides read-and-write, programmatic access to account data - submissions and their form-field entries, projects and forms, submitters (users), labels, review team members and assignments, funds and payment distributions, and message attachments. The API uses HTTP Basic Authentication (an account access token sent as the password) and is throttled at roughly 10 transactions per second and 10,000 transactions per hour. API access is enabled per account under More > Integrations > API Access, and Submittable pricing is quote-based (bundled Grant/Application Management and Corporate Social Responsibility products, plus Enterprise) via contact-sales.
finops:
- name: Submittable Finops
  service_category: Business Applications
  slug: submittable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/submittable.png
layout: provider
modified: '2026-07-05'
name: Submittable
nav: Providers
network: true
overview: 'Submittable publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Assignments API, Entries API, Funds API, and 7 more. Tagged areas include Submission Management, Grants Management, Applications, Forms, and Nonprofit.


  Submittable''s developer surface includes authentication, documentation, pricing, and 9 more developer resources.'
plans:
- name: Submittable Plans Pricing
  plan_count: 3
  slug: submittable-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 2
  name: Submittable Rate Limits
  slug: submittable-rate-limits
score:
  band: thin
  composite: 40.7
  delta: -2.1
  facets:
    commercial_clarity: 57.9
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Submittable Authentication
  slug: submittable-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Submittable Domain Security
  slug: submittable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Submittable Trust Center
  slug: submittable-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: submittable
tags:
- Submission Management
- Grants Management
- Applications
- Forms
- Nonprofit
- Corporate Social Responsibility
- Workflow
website: https://www.submittable.com
---
