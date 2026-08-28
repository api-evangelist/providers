---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.3
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Sense partner REST API used to synchronize applicant-tracking-system data into the Sense Talent Engagement Platform. It exposes batch upsert, single-entity fetch, partial update and dropdown possi
  name: Sense API
  slug: sense-talent-labs-sense-api
artifact_total: 9
asyncapis:
- description: ''
  name: Sense Talent Labs Writeback Webhooks
  slug: sense-talent-labs-writeback-webhooks
common:
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
  title: ''
  type: Compliance
  url: security/sense-talent-labs-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.warden-ai.com/sense/candidate-matching
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sense-talent-labs-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sense-talent-labs-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sense-talent-labs-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sense-talent-labs-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/sense-talent-labs-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sense-talent-labs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sense-talent-labs-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sense-talent-labs-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sense-talent-labs-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sense-talent-labs-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sense-talent-labs-writeback-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sense-talent-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sense-talent-labs-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/sense-talent-labs-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sense-talent-labs-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sense-talent-labs-domain-security.yml
created: '2026-08-26'
description: Sense Talent Labs, operating as Sense (sensehq.com), is an AI-powered talent engagement and recruiting automation platform founded in 2016 and used by staffing firms and enterprise talent-acquisition teams. The product suite spans recruiting automation, a talent CRM, campaigns and journeys, candidate scoring and matching, an AI recruiter and chatbot, SMS/WhatsApp messaging, interview scheduling and referrals. Sense publishes a public partner-facing REST API — the Sense API — documented as an OpenAPI 3.0.2 definition at developer.sensehq.com, which synchronizes applicant-tracking-system data (candidates, job orders, placements, submissions, companies, client contacts, internal users, appointments, certifications and leads) into the Sense platform to drive workflow automation. A companion Write-back API specification defines the event payloads Sense pushes back out to a customer or ATS endpoint.
image: https://cdn.prod.website-files.com/613f2494a7d5cd1817022b81/6193a3272e0a012eb26f998c_Fav-256.png
layout: provider
modified: '2026-08-26'
name: Sense Talent Labs
nav: Providers
network: true
overview: 'Sense Talent Labs publishes 1 API on the [APIs.io](https://apis.io/) network: Sense API. Tagged areas include Human Resources, Recruiting, Talent Acquisition, Staffing, and Applicant Tracking.


  The Sense Talent Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sense Talent Labs'' developer surface includes documentation, API reference, engineering blog, support, pricing, changelog, authentication, and 23 more developer resources.'
plans:
- name: Sense Talent Labs Plans Pricing
  plan_count: 6
  slug: sense-talent-labs-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Sense Talent Labs Rate Limits
  slug: sense-talent-labs-rate-limits
scopes:
- name: Sense Talent Labs Scopes
  scope_count: 1
  slug: sense-talent-labs-scopes
  summary_line: 1 scope
score:
  band: strong
  composite: 55.3
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 16.7
    contract_quality: 42.7
    developer_ergonomics: 47.0
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 81.6
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
- SaaS
website: https://www.sensehq.com/
---
