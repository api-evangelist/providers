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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Submittable Agentic Access
  operation_count: 19
  slug: submittable-agentic-access
  summary_line: 19 operations · 5 acting
api_count: 1
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
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Submittable Assignments API
  slug: open-submittable-assignments-api
- collection_type: open
  name: Submittable Assignments Entries API
  slug: open-submittable-entries-api
- collection_type: open
  name: Submittable Assignments Funds API
  slug: open-submittable-funds-api
- collection_type: open
  name: Submittable Assignments Labels API
  slug: open-submittable-labels-api
- collection_type: open
  name: Submittable Assignments Messaging API
  slug: open-submittable-messaging-api
- collection_type: open
  name: Submittable Assignments Payments API
  slug: open-submittable-payments-api
- collection_type: open
  name: Submittable Assignments Projects API
  slug: open-submittable-projects-api
- collection_type: open
  name: Submittable Assignments Submissions API
  slug: open-submittable-submissions-api
- collection_type: open
  name: Submittable Assignments Teams API
  slug: open-submittable-teams-api
- collection_type: open
  name: Submittable Assignments Users API
  slug: open-submittable-users-api
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
overview: 'Submittable publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Assignments API, Entries API, Funds API, and 7 more. Tagged areas include Submission Management, Grants Management, Application, Forms, and Non-Profit.


  Submittable''s developer surface includes authentication, documentation, pricing, and 9 more developer resources.'
plans:
- name: Submittable Plans Pricing
  plan_count: 3
  slug: submittable-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Submittable Rate Limits
  slug: submittable-rate-limits
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 56.4
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Application
- Forms
- Non-Profit
- Corporate Social Responsibility
- Workflows
website: https://www.submittable.com
---
