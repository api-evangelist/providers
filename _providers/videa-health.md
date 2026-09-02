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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/videa-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.videa.ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/videaai
- group: other
  title: ''
  type: Resources
  url: https://videa.ai/resources
- group: other
  title: ''
  type: Platform
  url: https://www.videa.ai/platform
- group: company
  title: ''
  type: News
  url: https://www.videa.ai/news
created: '2026-07-05'
description: VideaHealth (VideaAI) is an FDA-cleared dental artificial intelligence platform that analyzes dental radiographs to detect clinical findings such as caries, bone loss, calculus, and periapical lesions, and to surface aligner and implant treatment opportunities. VideaAI runs as ambient, chairside AI embedded directly inside dental practice-management and imaging systems (Dentrix, Denticon, Open Dental, Eaglesoft, Carestream, Dexis, Apteryx XVWeb, and others) - as soon as an X-ray is captured, the platform analyzes it and returns findings in the tools clinicians already use. Its detection, findings, study, and integration capabilities are delivered through partner-gated, embedded integrations rather than a public, self-serve developer API; there is no publicly documented REST API, developer portal, SDK, or OpenAPI definition as of this writing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/videa-health.png
layout: provider
modified: '2026-07-05'
name: VideaHealth
nav: Providers
network: true
overview: 'VideaHealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Dental, Healthcare, Artificial Intelligence, Medical Imaging, and Radiograph Analysis.


  VideaHealth''s developer surface includes product news and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Videa Health Domain Security
  slug: videa-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: videa-health
tags:
- Dental
- Healthcare
- Artificial Intelligence
- Medical Imaging
- Radiograph Analysis
- Diagnostics
- Computer-Vision
- FDA Cleared
- Gated API
website: https://www.videa.ai
---
