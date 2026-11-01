---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - '{''url'': ''https://www.workramp.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.confirm.com/scale-up/products/learn-up — a different registrable domain (workramp.com -> confirm.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 55
  human_in_the_loop: 0
  name: Workramp Agentic Access
  operation_count: 137
  slug: workramp-agentic-access
  summary_line: 137 operations · 55 acting
api_count: 2
apis:
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Academies API from WorkRamp — 48 operation(s) for academies.
  name: WorkRamp Academies API
  slug: workramp-academies-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Api Settings API from WorkRamp — 1 operation(s) for api settings.
  name: WorkRamp Api Settings API
  slug: workramp-api-settings-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Assignments API from WorkRamp — 3 operation(s) for assignments.
  name: WorkRamp Assignments API
  slug: workramp-assignments-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Attributes API from WorkRamp — 2 operation(s) for attributes.
  name: WorkRamp Attributes API
  slug: workramp-attributes-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Certifications API from WorkRamp — 2 operation(s) for certifications.
  name: WorkRamp Certifications API
  slug: workramp-certifications-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Challenge API from WorkRamp — 1 operation(s) for challenge.
  name: WorkRamp Challenge API
  slug: workramp-challenge-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Content Catalog API from WorkRamp — 1 operation(s) for content catalog.
  name: WorkRamp Content Catalog API
  slug: workramp-content-catalog-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Copy Content API from WorkRamp — 1 operation(s) for copy content.
  name: WorkRamp Copy Content API
  slug: workramp-copy-content-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Events API from WorkRamp — 4 operation(s) for events.
  name: WorkRamp Events API
  slug: workramp-events-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Groups API from WorkRamp — 4 operation(s) for groups.
  name: WorkRamp Groups API
  slug: workramp-groups-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Guide Assignments API from WorkRamp — 2 operation(s) for guide assignments.
  name: WorkRamp Guide Assignments API
  slug: workramp-guide-assignments-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Guides API from WorkRamp — 2 operation(s) for guides.
  name: WorkRamp Guides API
  slug: workramp-guides-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Instant Auth API from WorkRamp — 1 operation(s) for instant auth.
  name: WorkRamp Instant Auth API
  slug: workramp-instant-auth-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Item Folders API from WorkRamp — 3 operation(s) for item folders.
  name: WorkRamp Item Folders API
  slug: workramp-item-folders-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Logs API from WorkRamp — 2 operation(s) for logs.
  name: WorkRamp Logs API
  slug: workramp-logs-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The New Endpoint API from WorkRamp — 1 operation(s) for new endpoint.
  name: WorkRamp New Endpoint API
  slug: workramp-new-endpoint-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Path Assignments API from WorkRamp — 1 operation(s) for path assignments.
  name: WorkRamp Path Assignments API
  slug: workramp-path-assignments-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Paths API from WorkRamp — 2 operation(s) for paths.
  name: WorkRamp Paths API
  slug: workramp-paths-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Reseller Customers API from WorkRamp — 1 operation(s) for reseller customers.
  name: WorkRamp Reseller Customers API
  slug: workramp-reseller-customers-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Resources API from WorkRamp — 1 operation(s) for resources.
  name: WorkRamp Resources API
  slug: workramp-resources-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Scim API from WorkRamp — 4 operation(s) for scim.
  name: WorkRamp SCIM API
  slug: workramp-scim-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Scorm API from WorkRamp — 1 operation(s) for scorm.
  name: WorkRamp Scorm API
  slug: workramp-scorm-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Scorm Assigmments API from WorkRamp — 1 operation(s) for scorm assigmments.
  name: WorkRamp Scorm Assigmments API
  slug: workramp-scorm-assigmments-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Scorm Assignments API from WorkRamp — 3 operation(s) for scorm assignments.
  name: WorkRamp Scorm Assignments API
  slug: workramp-scorm-assignments-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Scorms API from WorkRamp — 1 operation(s) for scorms.
  name: WorkRamp Scorms API
  slug: workramp-scorms-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Search API from WorkRamp — 2 operation(s) for search.
  name: WorkRamp Search API
  slug: workramp-search-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Universities API from WorkRamp — 3 operation(s) for universities.
  name: WorkRamp Universities API
  slug: workramp-universities-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Users API from WorkRamp — 5 operation(s) for users.
  name: WorkRamp Users API
  slug: workramp-users-api
- baseURL: https://app.workramp.com/api/v1
  baseurl_source: declared
  description: The Webhook Subscriptions API from WorkRamp — 2 operation(s) for webhook subscriptions.
  name: WorkRamp Webhook Subscriptions API
  slug: workramp-webhook-subscriptions-api
artifact_total: 43
asyncapis:
- description: ''
  name: Workramp Webhooks
  slug: workramp-webhooks
common:
- group: other
  href: https://artifacts.apis.io/workramp/capabilities/workramp-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/workramp-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/workramp/overlays/workramp-api-settings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/workramp-api-settings-overlay.yaml
- group: other
  href: https://artifacts.apis.io/workramp/overlays/workramp-json-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/workramp-json-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/workramp/agentic-access/workramp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/workramp-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/workramp/authentication/workramp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/workramp-authentication.yml
- group: design
  href: https://artifacts.apis.io/workramp/conventions/workramp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/workramp-conventions.yml
- group: design
  href: https://artifacts.apis.io/workramp/errors/workramp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/workramp-problem-types.yml
- group: design
  href: https://artifacts.apis.io/workramp/data-model/workramp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/workramp-data-model.yml
- group: design
  href: https://artifacts.apis.io/workramp/conformance/workramp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/workramp-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.confirm.com/
- group: auth
  href: https://artifacts.apis.io/workramp/security/workramp-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/workramp-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/workramp/security/workramp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/workramp-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/workramp/security/workramp-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/workramp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.confirm.com/policies/security
- group: design
  href: https://artifacts.apis.io/workramp/lifecycle/workramp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/workramp-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://workramp.statuspage.io/
- group: design
  href: https://artifacts.apis.io/workramp/asyncapi/workramp-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/workramp-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/workramp/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/workramp/llms/workramp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/workramp-llms.txt
- group: build
  href: https://artifacts.apis.io/workramp/packages/workramp-packages.yml
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
  href: https://artifacts.apis.io/workramp/plans/workramp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/workramp-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/workramp/rate-limits/workramp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/workramp-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/workramp/finops/workramp-finops.yml
  title: ''
  type: FinOps
  url: finops/workramp-finops.yml
created: '2026-06-13'
description: WorkRamp is a revenue-enablement and learning platform now sold by Confirm as two products — Learn:Up (the employee LMS, formerly WorkRamp) and Academy (customer and partner training) — after Learning Pool rebranded as Confirm and consolidated WorkRamp, Confirm HR, AI Sims and Elucidat under one Workforce Enablement System. The API is still served from app.workramp.com and documented at developers.workramp.com as the "Confirm Learn:Up & Academy API". It is a private REST API — access is granted per enterprise on request — and covers users, groups, custom attributes, guides/courses, paths (training series), challenges, SCORM courses and assignments, resources, events and event sessions, item folders and libraries, the content catalog, Academy contacts, segments, trainings, certifications, registrations and email domains, plus webhook subscriptions and SCIM 2.0 provisioning. Authentication is a static admin-scoped API key sent as a bearer token; published rate limits are 3,000
  calls/hour sustained with a 13,000 calls/hour burst, and EU tenants call app.eu.workramp.com.
finops:
- has_sources: true
  method: derived
  name: Workramp Finops
  primary_unit: user
  service_category: ''
  slug: workramp-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workramp.png
layout: provider
modified: '2026-08-13'
name: WorkRamp
nav: Providers
network: true
overview: 'WorkRamp publishes 29 API contracts indexed on the [APIs.io](https://apis.io/) network, including Academies API, Api Settings API, Assignments API, and 26 more. Tagged areas include LMS, Revenue Enablement, Sales Enablement, Training, and Onboarding.


  The WorkRamp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WorkRamp''s developer surface includes authentication, documentation, support, engineering blog, changelog, status page, pricing, and 32 more developer resources.'
plans:
- name: Workramp Plans Pricing
  plan_count: 7
  slug: workramp-plans-pricing
- name: Workramp Price Estimates
  plan_count: 0
  slug: workramp-price-estimates
random_paper: 19
rate_limits:
- limit_count: 2
  name: Workramp Rate Limits
  slug: workramp-rate-limits
score:
  band: strong
  composite: 64.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 55.6
    developer_ergonomics: 58.9
    discoverability: 66.1
    operational_transparency: 71.1
  previous_composite: 63.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/workramp/workramp-2026-06-20T201617.png
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
skill_count: 4
skills:
- name: Enroll an Academy contact in a certification
  slug: workramp-enroll-academy-contact-in-certification
- name: Onboard an employee and assign learning
  slug: workramp-onboard-employee-and-assign-learning
- name: Provision and deprovision users with SCIM
  slug: workramp-scim-provisioning-and-deprovisioning
- name: Subscribe to assignment webhooks and reconcile completions
  slug: workramp-subscribe-to-assignment-webhooks
slug: workramp
tags:
- LMS
- Revenue Enablement
- Sales Enablement
- Training
- Onboarding
- Assessment
- Certification
- Coaching
- Go-To-Market
- SCIM
- SCORM
- Webhook
- Customer Education
website: https://www.workramp.com/
---
