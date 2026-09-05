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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/floy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.floy.com/vrp
- group: auth
  title: ''
  type: DomainSecurity
  url: security/floy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.floy.com
- group: company
  title: ''
  type: Blog
  url: https://www.floy.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.floy.com/datenschutz
- group: operate
  title: ''
  type: Support
  url: https://www.floy.com/kontakt-floy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/floy-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/floy-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/floy-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.floy.com/ueber-floy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/floy-llms.txt
created: '2026-07-17'
description: Floy is a Munich-based healthcare AI company (founded 2021) that builds AI-powered radiology software for medical imaging. Its two products — opportunistic screening and diagnostic assistance — analyse CT and MRI examinations to surface additional findings beyond the initial radiologist assessment, enabling earlier diagnosis and better patient outcomes. The models are trained on 17 million medical examinations. Floy is an ISO 13485:2016 certified, EU MDR Class IIb medical-device manufacturer and is GDPR compliant, with research partnerships including DKFZ, LMU Klinikum Munich, Stanford, and the University of Oxford. It is backed by HV Capital, 10x Founders, xdeck, and Acurio Ventures. Floy is a clinical B2B product and does not publish a public developer API.
image: https://cdn.prod.website-files.com/66f7b48c0855a2b7dbf4f206/670a9ce67cb7024ec518cf2d_Floy_Open_Graph_Maximize%20Human%20Health.jpg
layout: provider
modified: '2026-07-19'
name: Floy
nav: Providers
network: true
overview: 'Floy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Imaging, Radiology, and Artificial Intelligence.


  Floy''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 16.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/floy/refs/heads/main/screenshots/floy-2026-07-25T214842.png
security:
- kind: domain-security
  name: Floy Domain Security
  slug: floy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Floy Vulnerability Disclosure
  slug: floy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: floy
tags:
- Company
- Healthcare
- Medical Imaging
- Radiology
- Artificial Intelligence
- Diagnostics
- Clinical Decision Support
- Medical Devices
website: https://www.floy.com
---
