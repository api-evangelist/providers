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
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://mentimeter.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mentimeter.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mentimeter
- group: auth
  title: ''
  type: TrustCenter
  url: security/mentimeter-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.mentimeter.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/mentimeter-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mentimeter-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mentimeter-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mentimeter-vulnerability-disclosure.yml
created: '2026-07-17'
description: Mentimeter is a Swedish audience-engagement and interactive-presentation platform used to run live polls, quizzes, word clouds, ranking, open-ended questions and Q&A during meetings, classrooms and events, with results updating in real time as participants respond from their phones. Founded in Stockholm in 2014, it is used across education and enterprise for interactive presentations and workshops. Mentimeter does not publish a public developer REST API; its extensibility surface is delivered through LMS integrations (Canvas, Blackboard, Moodle, Brightspace via LTI), presentation add-ins (PowerPoint, Microsoft Teams, Zoom) and SSO, rather than a documented HTTP API. This profile was surfaced as a 500 Global portfolio company and enriched by the API Evangelist pipeline against its public developer, security and trust surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mentimeter.png
layout: provider
modified: '2026-07-20'
name: Mentimeter
nav: Providers
network: true
overview: 'Mentimeter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Presentations, Audience Engagement, Live Polling, and Quizzes.


  Mentimeter''s developer surface includes pricing and 8 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mentimeter/refs/heads/main/screenshots/mentimeter-2026-08-07T172530.png
security:
- kind: domain-security
  name: Mentimeter Domain Security
  slug: mentimeter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mentimeter Vulnerability Disclosure
  slug: mentimeter-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mentimeter Trust Center
  slug: mentimeter-trust-center
  summary_line: GDPR
slug: mentimeter
tags:
- Company
- Presentations
- Audience Engagement
- Live Polling
- Quizzes
- Surveys
- Interactive Presentations
- Education
- Sweden
website: https://mentimeter.com
---
