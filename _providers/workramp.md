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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 55
  human_in_the_loop: 0
  name: Workramp Agentic Access
  operation_count: 137
  slug: workramp-agentic-access
  summary_line: 137 operations · 55 acting
api_count: 2
apis:
- description: The Academies API from WorkRamp — 48 operation(s) for academies.
  name: WorkRamp Academies API
  slug: workramp-academies-api
- description: The Api Settings API from WorkRamp — 1 operation(s) for api settings.
  name: WorkRamp Api Settings API
  slug: workramp-api-settings-api
- description: The Assignments API from WorkRamp — 3 operation(s) for assignments.
  name: WorkRamp Assignments API
  slug: workramp-assignments-api
- description: The Attributes API from WorkRamp — 2 operation(s) for attributes.
  name: WorkRamp Attributes API
  slug: workramp-attributes-api
- description: The Certifications API from WorkRamp — 2 operation(s) for certifications.
  name: WorkRamp Certifications API
  slug: workramp-certifications-api
- description: The Challenge API from WorkRamp — 1 operation(s) for challenge.
  name: WorkRamp Challenge API
  slug: workramp-challenge-api
- description: The Content Catalog API from WorkRamp — 1 operation(s) for content catalog.
  name: WorkRamp Content Catalog API
  slug: workramp-content-catalog-api
- description: The Copy Content API from WorkRamp — 1 operation(s) for copy content.
  name: WorkRamp Copy Content API
  slug: workramp-copy-content-api
- description: The Events API from WorkRamp — 4 operation(s) for events.
  name: WorkRamp Events API
  slug: workramp-events-api
- description: The Groups API from WorkRamp — 4 operation(s) for groups.
  name: WorkRamp Groups API
  slug: workramp-groups-api
- description: The Guide Assignments API from WorkRamp — 2 operation(s) for guide assignments.
  name: WorkRamp Guide Assignments API
  slug: workramp-guide-assignments-api
- description: The Guides API from WorkRamp — 2 operation(s) for guides.
  name: WorkRamp Guides API
  slug: workramp-guides-api
- description: The Instant Auth API from WorkRamp — 1 operation(s) for instant auth.
  name: WorkRamp Instant Auth API
  slug: workramp-instant-auth-api
- description: The Item Folders API from WorkRamp — 3 operation(s) for item folders.
  name: WorkRamp Item Folders API
  slug: workramp-item-folders-api
- description: The Logs API from WorkRamp — 2 operation(s) for logs.
  name: WorkRamp Logs API
  slug: workramp-logs-api
- description: The New Endpoint API from WorkRamp — 1 operation(s) for new endpoint.
  name: WorkRamp New Endpoint API
  slug: workramp-new-endpoint-api
- description: The Path Assignments API from WorkRamp — 1 operation(s) for path assignments.
  name: WorkRamp Path Assignments API
  slug: workramp-path-assignments-api
- description: The Paths API from WorkRamp — 2 operation(s) for paths.
  name: WorkRamp Paths API
  slug: workramp-paths-api
- description: The Reseller Customers API from WorkRamp — 1 operation(s) for reseller customers.
  name: WorkRamp Reseller Customers API
  slug: workramp-reseller-customers-api
- description: The Resources API from WorkRamp — 1 operation(s) for resources.
  name: WorkRamp Resources API
  slug: workramp-resources-api
- description: The Scim API from WorkRamp — 4 operation(s) for scim.
  name: WorkRamp SCIM API
  slug: workramp-scim-api
- description: The Scorm API from WorkRamp — 1 operation(s) for scorm.
  name: WorkRamp Scorm API
  slug: workramp-scorm-api
- description: The Scorm Assigmments API from WorkRamp — 1 operation(s) for scorm assigmments.
  name: WorkRamp Scorm Assigmments API
  slug: workramp-scorm-assigmments-api
- description: The Scorm Assignments API from WorkRamp — 3 operation(s) for scorm assignments.
  name: WorkRamp Scorm Assignments API
  slug: workramp-scorm-assignments-api
- description: The Scorms API from WorkRamp — 1 operation(s) for scorms.
  name: WorkRamp Scorms API
  slug: workramp-scorms-api
- description: The Search API from WorkRamp — 2 operation(s) for search.
  name: WorkRamp Search API
  slug: workramp-search-api
- description: The Universities API from WorkRamp — 3 operation(s) for universities.
  name: WorkRamp Universities API
  slug: workramp-universities-api
- description: The Users API from WorkRamp — 5 operation(s) for users.
  name: WorkRamp Users API
  slug: workramp-users-api
- description: The Webhook Subscriptions API from WorkRamp — 2 operation(s) for webhook subscriptions.
  name: WorkRamp Webhook Subscriptions API
  slug: workramp-webhook-subscriptions-api
artifact_total: 38
asyncapis:
- description: ''
  name: Workramp Webhooks
  slug: workramp-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/workramp-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/workramp-api-settings-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workramp-json-api-overlay.yaml
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
overview: 'WorkRamp publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Academies API, Api Settings API, Assignments API, and 26 more. Tagged areas include Learning Management, Revenue Enablement, Sales Enablement, Training, and Onboarding.


  The WorkRamp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WorkRamp''s developer surface includes authentication, documentation, support, engineering blog, changelog, status page, pricing, and 32 more developer resources.'
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
  composite: 65.8
  coverage:
    artifact_dirs: 24
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 67.1
    developer_ergonomics: 33.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 63.2
  previous_composite: 65.8
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Go-To-Market
- SCIM
- SCORM
- Webhook
- Customer Education
website: https://www.workramp.com/
---
