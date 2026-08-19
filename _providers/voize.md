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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voize-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.voize.ai
- group: company
  title: ''
  type: About
  url: https://www.voize.ai/us/about
- group: company
  title: ''
  type: Blog
  url: https://www.voize.ai/us/blog
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.voize.ai/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/voize-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.voize.ai/us/bug-bounty
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.voize.ai/us/datenschutz
- group: start
  title: ''
  type: SignUp
  url: https://www.voize.ai/us/book-a-demo
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voize-llms.txt
created: '2026-07-17'
description: voize is a German healthcare AI company (voize GmbH) building a voice-documentation platform for long-term care, skilled nursing, and disability-support facilities. Caregivers speak naturally on a smartphone during patient care and voize's on-device and cloud speech models convert the free speech into structured, categorized entries that sync bi-directionally in real time into the facility's electronic health record (EHR) system. The product reduces documentation burden for nursing staff, works offline, recognizes patient names and corrects grammar, and integrates directly with major EHRs used in skilled nursing. voize is backed by HV Capital and operates in Germany and the United States. It ships a mobile application rather than a public developer API, but exposes EHR integrations, a trust center, and a vulnerability disclosure / bug bounty program on its public surface.
image: https://www.voize.ai/favicon.ico
layout: provider
modified: '2026-07-21'
name: voize
nav: Providers
network: true
overview: 'voize is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, AI, Speech Recognition, and Voice Documentation.


  voize''s developer surface includes engineering blog, signup flow, and 8 more developer resources.'
random_paper: 110
score:
  band: emerging
  composite: 16.2
  delta: -0.5
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Voize Domain Security
  slug: voize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Voize Vulnerability Disclosure
  slug: voize-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Voize Trust Center
  slug: voize-trust-center
  summary_line: trust center published
slug: voize
tags:
- Company
- Healthcare
- AI
- Speech Recognition
- Voice Documentation
- Nursing
- Electronic Health Records
- Long-term Care
website: https://www.voize.ai
---
