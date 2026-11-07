---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API to generate narrated, captioned videos from a topic or script. Provides three endpoints, bearer-token authentication, and a JSON manifest of every scene.
  name: Automated Video App API
  slug: automated-video-app-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/automatedvideoapp-com/well-known/automatedvideoapp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/automatedvideoapp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/automatedvideoapp-com/hosts/automatedvideoapp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/automatedvideoapp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/automatedvideoapp-com/vendors/automatedvideoapp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/automatedvideoapp-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/automatedvideoapp-com/security/automatedvideoapp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/automatedvideoapp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://automatedvideoapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://automatedvideoapp.com/docs/api.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://automatedvideoapp.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://automatedvideoapp.com/privacy.html
coverage:
  checked: '2026-11-02'
  detail: API documentation is provided as HTML pages without a machine‑readable OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://automatedvideoapp.com/docs/api.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Automated Video App provides an AI-powered platform that transforms text, scripts, or ideas into fully edited videos. Users can generate multilingual voiceovers, add AI‑generated or stock visuals, include captions, and publish directly to YouTube or social platforms. The service offers integrations via a REST API and a Claude connector, supports custom branding, scheduling, and webhook notifications, and includes tools for uploading user images. It aims to simplify video creation for marketers, educators, and developers without requiring video editing expertise.
image: https://automatedvideoapp.com/examples/explainer-poster.jpg
layout: provider
modified: '2026-11-02'
name: Automated Video App
nav: Providers
network: true
overview: 'Automated Video App is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, Artificial Intelligence, Automation, and Media.


  Automated Video App''s developer surface includes documentation and 7 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 12.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Automatedvideoapp Com Domain Security
  slug: automatedvideoapp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: automatedvideoapp-com
tags:
- Company
- Video
- Artificial Intelligence
- Automation
- Media
website: https://automatedvideoapp.com/
---
