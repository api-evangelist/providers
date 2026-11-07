---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://partner-api.sensehq.com/v1
  baseurl_source: declared
  description: An interview or a meeting with a Candidate or Contact.
  name: Sense Talent Labs Appointment API
  slug: sense-talent-labs-appointment-api
- baseURL: https://partner-api.sensehq.com/v1
  baseurl_source: declared
  description: Authenticate using client credentials to obtain a Bearer access_token.
  name: Sense Talent Labs Authentication API
  slug: sense-talent-labs-authentication-api
- baseURL: https://partner-api.sensehq.com/v1
  baseurl_source: declared
  description: A person seeking a job.
  name: Sense Talent Labs Candidate API
  slug: sense-talent-labs-candidate-api
- baseURL: https://partner-api.sensehq.com/v1
  baseurl_source: declared
  description: The credential and or certificate of Candidate, or as required by a Job.
  name: Sense Talent Labs Certification API
  slug: sense-talent-labs-certification-api
- baseURL: https://partner-api.sensehq.com/v1
  baseurl_source: declared
  description: A company that is a client of your organization.
  name: Sense Talent Labs Company API
  slug: sense-talent-labs-company-api
- baseURL: https://partner-api.sensehq.com/v1
  baseurl_source: declared
  description: An internal person at your organization.
  name: Sense Talent Labs Internal User API
  slug: sense-talent-labs-internaluser-api
- baseURL: https://partner-api.sensehq.com/v1
  baseurl_source: declared
  description: A job to be filled by a Candidate.
  name: Sense Talent Labs Job Order API
  slug: sense-talent-labs-joborder-api
- baseURL: https://partner-api.sensehq.com/v1
  baseurl_source: declared
  description: A new prospective client or contact
  name: Sense Talent Labs Lead API
  slug: sense-talent-labs-lead-api
- baseURL: https://partner-api.sensehq.com/v1
  baseurl_source: declared
  description: A job that has been filled by a Candidate.
  name: Sense Talent Labs Placement API
  slug: sense-talent-labs-placement-api
- baseURL: https://partner-api.sensehq.com/v1
  baseurl_source: declared
  description: Sending a Candidate’s info for additional review.
  name: Sense Talent Labs Submission API
  slug: sense-talent-labs-submission-api
- baseURL: https://partner-api.sensehq.com/v1
  baseurl_source: declared
  description: A contact person at a Company.
  name: Sense Talent Labs Client Contact API
  slug: sense-talent-labs-client-contact-api
artifact_total: 25
asyncapis:
- description: ''
  name: Sense Talent Labs Writeback Webhooks
  slug: sense-talent-labs-writeback-webhooks
common:
- group: other
  href: https://artifacts.apis.io/sense-talent-labs/capabilities/sense-talent-labs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sense-talent-labs-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/sense-talent-labs/overlays/sense-talent-labs-sense-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sense-talent-labs-sense-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.sensehq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sensehq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sensehq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.sensehq.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sensehq.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.sensehq.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sensehq.com/sense-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sensehq.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sensehq.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sensehq.com/
- group: auth
  title: ''
  type: Security
  url: https://www.sensehq.com/security
- group: auth
  href: https://artifacts.apis.io/sense-talent-labs/security/sense-talent-labs-trust-center.yml
  title: ''
  type: Compliance
  url: security/sense-talent-labs-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.warden-ai.com/sense/candidate-matching
- group: auth
  href: https://artifacts.apis.io/sense-talent-labs/security/sense-talent-labs-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sense-talent-labs-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/sense-talent-labs/lifecycle/sense-talent-labs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sense-talent-labs-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/sense-talent-labs/changelog/sense-talent-labs-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sense-talent-labs-changelog.yml
- group: design
  href: https://artifacts.apis.io/sense-talent-labs/conventions/sense-talent-labs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sense-talent-labs-conventions.yml
- group: design
  href: https://artifacts.apis.io/sense-talent-labs/conventions/sense-talent-labs-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sense-talent-labs-conventions.yml
- group: auth
  href: https://artifacts.apis.io/sense-talent-labs/authentication/sense-talent-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sense-talent-labs-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sense-talent-labs/scopes/sense-talent-labs-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sense-talent-labs-scopes.yml
- group: design
  href: https://artifacts.apis.io/sense-talent-labs/conformance/sense-talent-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sense-talent-labs-conformance.yml
- group: design
  href: https://artifacts.apis.io/sense-talent-labs/errors/sense-talent-labs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sense-talent-labs-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sense-talent-labs/data-model/sense-talent-labs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sense-talent-labs-data-model.yml
- group: design
  href: https://artifacts.apis.io/sense-talent-labs/asyncapi/sense-talent-labs-writeback-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sense-talent-labs-writeback-webhooks.yml
- group: commercial
  href: https://artifacts.apis.io/sense-talent-labs/plans/sense-talent-labs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sense-talent-labs-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sense-talent-labs/rate-limits/sense-talent-labs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sense-talent-labs-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/sense-talent-labs/packages/sense-talent-labs-packages.yml
  title: ''
  type: Packages
  url: packages/sense-talent-labs-packages.yml
- group: agent
  href: https://artifacts.apis.io/sense-talent-labs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/sense-talent-labs/llms/sense-talent-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sense-talent-labs-llms.txt
- group: auth
  href: https://artifacts.apis.io/sense-talent-labs/security/sense-talent-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sense-talent-labs-domain-security.yml
created: '2026-08-26'
description: Sense Talent Labs, operating as Sense (sensehq.com), is an AI-powered talent engagement and recruiting automation platform founded in 2016 and used by staffing firms and enterprise talent-acquisition teams. The product suite spans recruiting automation, a talent CRM, campaigns and journeys, candidate scoring and matching, an AI recruiter and chatbot, SMS/WhatsApp messaging, interview scheduling and referrals. Sense publishes a public partner-facing REST API — the Sense API — documented as an OpenAPI 3.0.2 definition at developer.sensehq.com, which synchronizes applicant-tracking-system data (candidates, job orders, placements, submissions, companies, client contacts, internal users, appointments, certifications and leads) into the Sense platform to drive workflow automation. A companion Write-back API specification defines the event payloads Sense pushes back out to a customer or ATS endpoint.
finops:
- has_sources: true
  method: derived
  name: Sense Talent Labs Finops
  primary_unit: subscription
  service_category: ''
  slug: sense-talent-labs-finops
  template: false
image: https://cdn.prod.website-files.com/613f2494a7d5cd1817022b81/6193a3272e0a012eb26f998c_Fav-256.png
layout: provider
modified: '2026-08-26'
name: Sense Talent Labs
nav: Providers
network: true
overview: 'Sense Talent Labs publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Appointment API, Authentication API, Candidate API, and 8 more. Tagged areas include Human Resources, Recruiting, Talent Acquisition, Staffing, and Applicant Tracking.


  The Sense Talent Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Sense Talent Labs'' developer surface includes documentation, API reference, engineering blog, support, pricing, changelog, authentication, and 25 more developer resources.'
plans:
- name: Sense Talent Labs Plans Pricing
  plan_count: 6
  slug: sense-talent-labs-plans-pricing
- name: Sense Talent Labs Price Estimates
  plan_count: 0
  slug: sense-talent-labs-price-estimates
random_paper: 18
rate_limits:
- limit_count: 3
  name: Sense Talent Labs Rate Limits
  slug: sense-talent-labs-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Sense Talent Labs API Rules
  rule_count: 55
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 5
  slug: sense-talent-labs-rules
scopes:
- name: Sense Talent Labs Scopes
  scope_count: 1
  slug: sense-talent-labs-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: strong
  composite: 65.7
  coverage:
    artifact_dirs: 30
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 58.3
    developer_ergonomics: 47.0
    discoverability: 66.1
    operational_transparency: 81.6
  previous_composite: 65.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 41.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/sense-talent-labs/sense-talent-labs-2026-09-02T154856.png
security:
- kind: authentication
  name: Sense Talent Labs Authentication
  slug: sense-talent-labs-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Sense Talent Labs Domain Security
  slug: sense-talent-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sense Talent Labs Vulnerability Disclosure
  slug: sense-talent-labs-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Sense Talent Labs Trust Center
  slug: sense-talent-labs-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: sense-incremental-change-events
  slug: sense-talent-labs-incremental-change-events
- name: sense-initial-ats-sync
  slug: sense-talent-labs-initial-ats-sync
- name: sense-receive-writebacks
  slug: sense-talent-labs-receive-writebacks
slug: sense-talent-labs
tags:
- Human Resources
- Recruiting
- Talent Acquisition
- Staffing
- Applicant Tracking
- Candidate Engagement
- Recruiting Automation
- Talent CRM
- Messaging
- Interview Scheduling
- Artificial Intelligence
- Software-as-a-Service
website: https://www.sensehq.com/
---
