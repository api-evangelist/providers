---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.empirix.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.infovista.com/vistacx-continuous-cx-assurance — a different registrable domain (empirix.com -> infovista.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/empirix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.empirix.com
- group: operate
  title: ''
  type: Support
  url: https://support.hammer.com/
created: '2026-07-17'
description: Empirix was a communications and contact-center test, assurance, and monitoring company backed by Matrix Partners. Its products spanned network and application performance testing, VoIP and IVR quality assurance, contact-center monitoring, and end-to-end customer-experience assurance for carriers and enterprises. Empirix was acquired by Infovista in 2020; its testing and monitoring portfolio now operates under the Hammer Technologies brand, which is evolving into VistaCX (Voice Explorer, CallMaster, VoiceWatch, HammerRTC, VistaOne). The company exposes no public developer API, OpenAPI definition, or developer portal; empirix.com now redirects to hammer.com. This profile is a network stub enriched from public web surfaces only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/empirix.png
layout: provider
modified: '2026-07-19'
name: Empirix
nav: Providers
network: true
overview: 'Empirix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Network Testing, Contact Center, and Monitoring.


  Empirix''s developer surface includes support and 2 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 2.8
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/empirix/refs/heads/main/screenshots/empirix-2026-07-25T213250.png
security:
- kind: domain-security
  name: Empirix Domain Security
  slug: empirix-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: empirix
tags:
- Company
- Infrastructure
- Network Testing
- Contact Center
- Monitoring
- Quality Assurance
- Telecommunications
- Customer Experience
website: https://www.empirix.com
---
