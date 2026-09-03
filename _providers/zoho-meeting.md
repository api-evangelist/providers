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
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'REST API for creating, updating, and reporting on Zoho Meeting sessions and Zoho Webinar events, including registrants, recordings, and meeting links. Requests are authenticated with OAuth 2.0 access '
  name: Zoho Meeting REST API
  slug: rest-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-meeting-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-meeting-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoho
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/zoho-meeting
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/meeting/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/meeting/api-integration/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/meeting/pricing.html
- group: start
  title: ''
  type: Signup
  url: https://www.zoho.com/meeting/signup.html
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/meeting/blog/feed/
created: '2026-05-11'
description: Zoho Meeting is an online meeting, video conferencing, and webinar platform from Zoho that lets teams host secure meetings, presentations, and recorded webinars from any device. The Zoho Meeting REST API enables programmatic scheduling, management, and reporting of meetings and webinars, including registrant handling and session lifecycle. Authentication uses Zoho's OAuth 2.0 (Zoho-oauthtoken) with domain-specific API endpoints.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-meeting.png
layout: provider
modified: '2026-05-11'
name: Zoho Meeting
nav: Providers
network: true
overview: 'Zoho Meeting publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Online Meetings, Video Conferencing, Webinars, Collaboration, and Zoho.


  Zoho Meeting''s developer surface includes documentation, pricing, signup flow, engineering blog, and 5 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 18.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-meeting/refs/heads/main/screenshots/zoho-meeting-2026-06-20T201943.png
security:
- kind: domain-security
  name: Zoho Meeting Domain Security
  slug: zoho-meeting-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Meeting Vulnerability Disclosure
  slug: zoho-meeting-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-meeting
tags:
- Online Meetings
- Video Conferencing
- Webinars
- Collaboration
- Zoho
website: https://www.zoho.com/meeting/
---
