---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.4
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: REST API for the Fountain Hire product, covering applicants (create, retrieve, update, delete, list, latest applicant, duplicate detection, notes, labels, file uploads, transitions, bulk advance, bulk
  name: Fountain Hire API v2
  slug: hire-api
- description: Post-hire REST API covering worker profiles (activation and deactivation), employment records, document submissions, I-9 verification processing, attendance, shift creation and assignment, demands, al
  name: Fountain Worker API
  slug: worker-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fountain-tech-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fountain-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fountain.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fountain.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.fountain.com/reference/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developer.fountain.com/reference/wx-authentication
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.fountain.com/llms.txt
- group: start
  title: ''
  type: PartnerPortal
  url: https://partners.fountain.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fountain.com/
- group: operate
  title: ''
  type: Support
  url: https://support.fountain.com/en/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.fountain.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fountain.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.fountain.com/users/sign_in
- group: company
  title: ''
  type: Blog
  url: https://www.fountain.com/blog
- group: other
  title: ''
  type: Customers
  url: https://www.fountain.com/customers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fountain-inc
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/FountainInc
- group: company
  title: ''
  type: CrunchBase
  url: https://www.crunchbase.com/organization/fountain-3
created: '2026-05-25'
description: Fountain is an AI-powered frontline workforce platform that helps high-volume employers source, screen, hire, onboard, schedule, and retain hourly workers across quick-service restaurants, retail, logistics, hospitality, healthcare, manufacturing, grocery, and franchise operations. The integrated product suite spans an applicant tracking system, candidate CRM, agentic sourcing ("Source"), digital onboarding with document collection and background-check integrations, shift and scheduling for active workers, and an orchestration layer called Cue that automates workflows across all products. AI agents Anna (recruiter screening), Emma (24/7 candidate support), and Sam (employee engagement) sit across the funnel and the post-hire workforce. Fountain exposes a versioned REST API at developer.fountain.com covering the Hire API (applicants, funnels/openings, stages, calendar slots, labels, custom exports, webhooks) and the post-hire Worker API (worker profiles, employment records, document
  submissions, I-9 verification, attendance, shifts, demands, breaks, and holidays), with authentication via the X-ACCESS-TOKEN header on per-tenant base URLs or OAuth 2.0 through the unified services.fountain.com hire service base URL for partner integrations.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fountain-tech.png
layout: provider
modified: '2026-05-25'
name: Fountain
nav: Providers
network: true
overview: 'Fountain publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Hiring, Recruiting, Onboarding, Applicant Tracking, and Workforce Management.


  Fountain''s developer surface includes documentation, API reference, authentication, support, pricing, engineering blog, and 12 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 19.4
  delta: 0.5
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 19.7
  previous_composite: 18.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fountain-tech/refs/heads/main/screenshots/fountain-tech-2026-06-20T181458.png
security:
- kind: domain-security
  name: Fountain Tech Domain Security
  slug: fountain-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fountain Tech Vulnerability Disclosure
  slug: fountain-tech-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: fountain-tech
tags:
- Hiring
- Recruiting
- Onboarding
- Applicant Tracking
- Workforce Management
- Hourly Workers
- Frontline
- Shift Management
- Scheduling
- Background Checks
- I-9 Verification
- Webhook
- HRIS
- Talent Acquisition
- AI Agents
website: https://www.fountain.com
---
