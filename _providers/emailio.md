---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emailio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.emailio.com
- group: start
  title: ''
  type: SignUp
  url: https://www.emailio.com
created: '2026-07-17'
description: Emailio is a Y Combinator (Winter 2014) and Thiel Fellowship-backed startup building "email built for wellness" — a consumer email client for iPhone, iPad, and Mac that centers user wellbeing and mental health rather than traditional inbox-productivity metrics. Its pre-launch landing page describes inbox management, email batching, mood tracking, one-click unsubscribe, and Smart Rule Suggestions, with early access gated behind a waitlist. Founded by Martin Stoyanov and Teo Teodosiev with a roughly five-person team, Emailio sits at the intersection of the productivity and health & wellness categories. It was surfaced as a Y Combinator portfolio company and added to the API Evangelist network as a stub for enrichment; as of this pass it exposes a consumer product only — no public API, developer portal, documentation, or SDKs could be found.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/emailio.png
layout: provider
modified: '2026-07-19'
name: Emailio
nav: Providers
network: true
overview: 'Emailio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, Email Client, Productivity, and Health and Wellness.


  Emailio''s developer surface includes signup flow and 2 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emailio/refs/heads/main/screenshots/emailio-2026-07-25T213215.png
security:
- kind: domain-security
  name: Emailio Domain Security
  slug: emailio-domain-security
  summary_line: TLSv1.2
slug: emailio
tags:
- Company
- Email
- Email Client
- Productivity
- Health and Wellness
- Consumer
- Y Combinator
- Thiel Fellowship
website: https://www.emailio.com
---
