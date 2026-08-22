---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - docs
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 55
  human_in_the_loop: 0
  name: Workramp Agentic Access
  operation_count: 137
  slug: workramp-agentic-access
  summary_line: 137 operations · 55 acting
api_count: 1
apis:
- description: 'REST API for the Confirm Learn:Up and Academy platform (formerly WorkRamp): manage users, groups and custom attributes, guides/courses, paths, challenges, SCORM courses and assignments, resources, eve'
  name: WorkRamp API
  slug: workramp-api
artifact_total: 10
asyncapis:
- description: ''
  name: Workramp Webhooks
  slug: workramp-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workramp-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workramp-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/workramp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/workramp-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/workramp-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/workramp-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.confirm.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/workramp-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workramp-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/workramp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.confirm.com/policies/security
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/workramp-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://workramp.statuspage.io/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/workramp-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/workramp-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/workramp-packages.yml
- group: company
  title: ''
  type: Website
  url: https://www.workramp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.workramp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.workramp.com/reference/getting-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.workramp.com/en/
- group: operate
  title: ''
  type: Support
  url: https://help.workramp.com/en/collections/2493185-api
- group: company
  title: ''
  type: Blog
  url: https://www.confirm.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.workramp.com/changelog
- group: operate
  title: ''
  type: Status
  url: https://workramp.statuspage.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/workramp
- group: other
  title: ''
  type: X
  url: https://x.com/workramp
- group: commercial
  title: ''
  type: Pricing
  url: https://www.confirm.com/scale-up/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.confirm.com/book-a-demo
- group: start
  title: ''
  type: Login
  url: https://app.workramp.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.confirm.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.confirm.com/policies/privacy-policy-us
- group: operate
  title: ''
  type: SLA
  url: https://www.confirm.com/policies/tol-service-level-agreement
- group: commercial
  title: ''
  type: Plans
  url: plans/workramp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/workramp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/workramp-finops.yml
created: '2026-06-13'
description: WorkRamp is a revenue-enablement and learning platform now sold by Confirm as two products — Learn:Up (the employee LMS, formerly WorkRamp) and Academy (customer and partner training) — after Learning Pool rebranded as Confirm and consolidated WorkRamp, Confirm HR, AI Sims and Elucidat under one Workforce Enablement System. The API is still served from app.workramp.com and documented at developers.workramp.com as the "Confirm Learn:Up & Academy API". It is a private REST API — access is granted per enterprise on request — and covers users, groups, custom attributes, guides/courses, paths (training series), challenges, SCORM courses and assignments, resources, events and event sessions, item folders and libraries, the content catalog, Academy contacts, segments, trainings, certifications, registrations and email domains, plus webhook subscriptions and SCIM 2.0 provisioning. Authentication is a static admin-scoped API key sent as a bearer token; published rate limits are 3,000
  calls/hour sustained with a 13,000 calls/hour burst, and EU tenants call app.eu.workramp.com.
finops:
- name: Workramp Finops
  service_category: ''
  slug: workramp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workramp.png
layout: provider
modified: '2026-08-13'
name: WorkRamp
nav: Providers
network: true
overview: 'WorkRamp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Learning Management, Revenue Enablement, Sales Enablement, Training, and Onboarding.


  The WorkRamp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WorkRamp''s developer surface includes authentication, documentation, support, engineering blog, changelog, status page, pricing, and 29 more developer resources.'
plans:
- name: Workramp Plans Pricing
  plan_count: 7
  slug: workramp-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Workramp Rate Limits
  slug: workramp-rate-limits
score:
  band: strong
  composite: 63.6
  delta: 2.6
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 16.7
    contract_quality: 60.0
    developer_ergonomics: 24.4
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 63.2
  previous_composite: 61.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 66.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workramp/refs/heads/main/screenshots/workramp-2026-06-20T201617.png
security:
- kind: authentication
  name: Workramp Authentication
  slug: workramp-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Workramp Domain Security
  slug: workramp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Workramp Vulnerability Disclosure
  slug: workramp-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Workramp Trust Center
  slug: workramp-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, Cyber Essentials, GDPR, CCPA
slug: workramp
tags:
- Learning Management
- Revenue Enablement
- Sales Enablement
- Training
- Onboarding
- LMS
- Assessments
- Certifications
- Coaching
- Go-to-Market
- SCIM
- SCORM
- Webhooks
- Customer Education
website: https://www.workramp.com/
---
