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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/siriusxm-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/siriusxm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/siriusxm
- group: company
  title: ''
  type: Website
  url: https://www.siriusxm.com
- group: other
  title: ''
  type: CorporateSite
  url: https://corporate.siriusxm.com
- group: other
  title: ''
  type: BusinessServices
  url: https://www.siriusxm.com/business
- group: other
  title: ''
  type: PandoraStreaming
  url: https://www.pandora.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.siriusxm.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.siriusxm.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.siriusxm.com/privacy
created: '2026-05-02'
description: SiriusXM Holdings Inc. is an American broadcasting corporation providing satellite radio and online audio streaming services in North America. The company offers subscription-based satellite radio, the Pandora streaming music service, and business music services. SiriusXM does not offer a public developer API; its content is accessed through subscription services and automotive OEM partnerships.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/siriusxm.png
json_schemas:
- name: SiriusXM Channel
  property_count: 9
  slug: siriusxm-channel
jsonld:
- class_count: 15
  name: Siriusxm Context
  property_count: 0
  slug: siriusxm-context
layout: provider
modified: '2026-05-02'
name: SiriusXM
nav: Providers
network: true
overview: 'SiriusXM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Satellite Radio, Audio Streaming, Entertainment, Music, and Broadcasting.


  The SiriusXM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 45
rules:
- name: SiriusXM API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: siriusxm-jsonschema-spectral-rules
score:
  band: emerging
  composite: 20.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 20.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/siriusxm/refs/heads/main/screenshots/siriusxm-2026-06-20T193953.png
security:
- kind: domain-security
  name: Siriusxm Domain Security
  slug: siriusxm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: siriusxm
tags:
- Satellite Radio
- Audio Streaming
- Entertainment
- Music
- Broadcasting
website: https://www.siriusxm.com
---
