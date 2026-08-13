---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Teachworks Agentic Access
  operation_count: 75
  slug: teachworks-agentic-access
  summary_line: 75 operations · 25 acting
api_count: 23
apis:
- description: Employee availability windows.
  name: Teachworks Availabilities API
  slug: teachworks-availabilities-api
- description: Cost premiums applied on top of base service rates.
  name: Teachworks Cost Premiums API
  slug: teachworks-cost-premiums-api
- description: Allocations of credit notes to invoices.
  name: Teachworks Credit Note Allocations API
  slug: teachworks-credit-note-allocations-api
- description: Billing accounts - families and independent students.
  name: Teachworks Customers API
  slug: teachworks-customers-api
- description: Teachers and staff, their status, earnings, and lesson totals.
  name: Teachworks Employees API
  slug: teachworks-employees-api
- description: Customer invoices.
  name: Teachworks Invoices API
  slug: teachworks-invoices-api
- description: Per-student rows attached to a lesson.
  name: Teachworks Lesson Participants API
  slug: teachworks-lesson-participants-api
- description: Scheduled lessons, participants, and completion.
  name: Teachworks Lessons API
  slug: teachworks-lessons-api
- description: Physical or virtual locations where lessons are delivered.
  name: Teachworks Locations API
  slug: teachworks-locations-api
- description: Employee compensation outside of lesson wages.
  name: Teachworks Other Compensation API
  slug: teachworks-other-compensation-api
- description: Non-teaching calendar events.
  name: Teachworks Other Events API
  slug: teachworks-other-events-api
- description: Allocations of payments to invoices.
  name: Teachworks Payment Allocations API
  slug: teachworks-payment-allocations-api
- description: Customer payments.
  name: Teachworks Payments API
  slug: teachworks-payments-api
- description: Repertoire items (e.g. for music lessons).
  name: Teachworks Repertoires API
  slug: teachworks-repertoires-api
- description: Groupings of student results.
  name: Teachworks Result Groups API
  slug: teachworks-result-groups-api
- description: Student progress results.
  name: Teachworks Results API
  slug: teachworks-results-api
- description: The billable services (lesson types) offered.
  name: Teachworks Services API
  slug: teachworks-services-api
- description: Groups of students for group lessons.
  name: Teachworks Student Groups API
  slug: teachworks-student-groups-api
- description: Child and independent students and their lesson totals.
  name: Teachworks Students API
  slug: teachworks-students-api
- description: Subjects taught.
  name: Teachworks Subjects API
  slug: teachworks-subjects-api
- description: Employee unavailability windows.
  name: Teachworks Unavailabilities API
  slug: teachworks-unavailabilities-api
- description: Wage payments to employees.
  name: Teachworks Wage Payments API
  slug: teachworks-wage-payments-api
- description: Teacher wage tiers used to calculate pay.
  name: Teachworks Wage Tiers API
  slug: teachworks-wage-tiers-api
artifact_total: 31
collections:
- collection_type: open
  name: Teachworks API
  slug: open-teachworks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/teachworks-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/teachworks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teachworks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/teachworks-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teachworks
- group: company
  title: ''
  type: Website
  url: https://teachworks.com
- group: docs
  title: ''
  type: Documentation
  url: https://teachworks.com/addons/api
- group: commercial
  title: ''
  type: Plans
  url: plans/teachworks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/teachworks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/teachworks-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.teachworks.com/feed/
created: '2026-07-03'
description: Teachworks is business management software for tutoring companies, music schools, test-prep centers, and other education businesses. It handles scheduling, student and family CRM, teacher management, lesson and event calendars, online billing and invoicing, payments, and teacher wages. The Teachworks API is a REST API (base https://api.teachworks.com/v1, token authentication over HTTPS) that exposes account data - customers, students, employees, lessons, services, invoices, payments, and wages - so companies can build custom integrations. The API is available on the Growth and Premium plans; there is no native webhook or WebSocket surface, and event-driven integrations are delivered through Zapier, Make, and Integrately polling.
finops:
- name: Teachworks Finops
  service_category: Business Management Software
  slug: teachworks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teachworks.png
layout: provider
modified: '2026-07-03'
name: Teachworks
nav: Providers
network: true
overview: 'Teachworks publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Availabilities API, Cost Premiums API, Credit Note Allocations API, and 20 more. Tagged areas include Education, Tutoring, EdTech, Scheduling, and Business Management.


  Teachworks'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Teachworks Plans Pricing
  plan_count: 4
  slug: teachworks-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Teachworks Rate Limits
  slug: teachworks-rate-limits
score:
  band: thin
  composite: 37.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Teachworks Authentication
  slug: teachworks-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Teachworks Domain Security
  slug: teachworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Teachworks Vulnerability Disclosure
  slug: teachworks-vulnerability-disclosure
  summary_line: disclosure policy published
slug: teachworks
tags:
- Education
- Tutoring
- EdTech
- Scheduling
- Business Management
- CRM
- Billing
website: https://teachworks.com
---
