---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nalu-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nalumed.com/
- group: company
  title: ''
  type: Blog
  url: https://nalumed.com/news-events/
- group: company
  title: ''
  type: BlogRSS
  url: https://nalumed.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://nalumed.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nalumed.com/website-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nalumed.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NaluMedical
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nalu-medical-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Nalu Medical ships an FDA-cleared implantable neurostimulator with a companion patient smartphone app and a clinician cloud portal, but exposes none of it to third parties - api.nalumed.com, developer.nalumed.com and docs.nalumed.com do not resolve, the 57-page sitemap has no developer section, and portal.nalumed.com (the Azure-hosted Nalu Cloud Portal) answers HTTP 404 with an empty body on every anonymous path including its own root.
  evidence:
  - status: 404
    url: https://nalumed.com/developers
  - status: 404
    url: https://nalumed.com/openapi.json
  - status: 404
    url: https://nalumed.com/llms.txt
  - status: 404
    url: https://portal.nalumed.com/
  - status: 200
    url: https://nalumed.com/sitemap_index.xml
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Nalu Medical, Inc. is a privately held, commercial-stage medical device company headquartered in Carlsbad, California, that develops the Nalu Neurostimulation System for the management of chronic pain. The system pairs a battery-free micro implantable pulse generator (mIPG) with an externally worn Therapy Disc that powers it wirelessly, and is controlled by the patient through a smartphone-based remote-control application; it is FDA-cleared for both spinal cord stimulation (SCS) and peripheral nerve stimulation (PNS). Nalu publishes patient and provider resources, instructions for use, clinical evidence and peer-reviewed publications on nalumed.com. It operates no public developer program - as of the 2026-08-26 enrichment pass there is no API reference, no OpenAPI/AsyncAPI/GraphQL contract, no SDK, no MCP server and no developer portal on any host the company controls.
image: https://nalumed.com/wp-content/uploads/2022/06/nalu-social.png
layout: provider
modified: '2026-08-26'
name: Nalu Medical
nav: Providers
network: true
overview: 'Nalu Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Neuromodulation, and Neurostimulation.


  Nalu Medical''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Nalu Medical Plans Pricing
  plan_count: 0
  slug: nalu-medical-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Nalu Medical Rate Limits
  slug: nalu-medical-rate-limits
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nalu-medical/refs/heads/main/screenshots/nalu-medical-2026-09-02T150718.png
security:
- kind: domain-security
  name: Nalu Medical Domain Security
  slug: nalu-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nalu-medical
tags:
- Company
- Medical Devices
- Healthcare
- Neuromodulation
- Neurostimulation
- Chronic Pain
- Implantable Devices
- Medical Technology
website: https://nalumed.com/
---
