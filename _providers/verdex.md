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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/verdex-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/verdex-security.txt
- group: company
  title: ''
  type: Website
  url: https://www.verdexai.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/verdex-llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/verdex-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/verdex-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verdex-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://www.verdexai.com/#contact
created: '2026-07-17'
description: 'Verdex builds AI for the clinical workflow. Its first product rooms patients and takes their history by voice before the physician walks into the room: the agent gathers and organizes the patient''s story, hands the physician a three-sentence summary, and lands a structured, signable history back in the electronic health record (EHR) the practice already runs. The agent never diagnoses or advises, escalates anything urgent to staff immediately, keeps every line of the note traceable to its source, and is built to be HIPAA compliant. Verdex is aimed at clinicians, practice owners, and health-system teams. The company is an early-stage Y Combinator startup; verdexai.com is a browser-rendered marketing site that publishes machine-readable llms.txt, robots.txt, and a security.txt but does not (yet) expose a public API, developer portal, SDKs, or OpenAPI surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/verdex.png
layout: provider
modified: '2026-07-21'
name: Verdex
nav: Providers
network: true
overview: 'Verdex is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Clinical Documentation, Artificial Intelligence, and Voice AI.


  Verdex''s developer surface includes support and 7 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 10.0
  delta: -1.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Verdex Domain Security
  slug: verdex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Verdex Vulnerability Disclosure
  slug: verdex-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: verdex
tags:
- Company
- Healthcare
- Clinical Documentation
- Artificial Intelligence
- Voice AI
- Electronic Health Records
- HIPAA
- Medical Scribe
website: https://www.verdexai.com/
---
