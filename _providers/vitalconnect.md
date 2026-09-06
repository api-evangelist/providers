---
agent_readiness:
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: VistaCenter, VitalConnect's cloud clinician application, transmits events to third-party application servers by POSTing to a subscriber-supplied Target URL. Event classes are patient notifications, ne
  name: VistaCenter Webhooks
  slug: vistacenter-webhooks
artifact_total: 5
asyncapis:
- description: ''
  name: Vitalconnect Vistacenter Webhooks
  slug: vitalconnect-vistacenter-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://vitalconnect.com/
- group: docs
  title: ''
  type: Documentation
  url: https://vitalconnect.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://vitalconnect.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://vitalconnect.com/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://vitalconnect.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vitalconnect.com/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vitalconnect.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://vitalconnect.com/compliance/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vitalconnect-vistacenter-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vitalconnect-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vitalconnect-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vitalconnect-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vitalconnect-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vitalconnect-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vitalconnect-domain-security.yml
coverage:
  checked: '2026-09-04'
  detail: 'The FDA-cleared VitalPatch Instructions For Use state that the device works with software built on "the VitalConnect Application Programming Interface (API)" and then direct the reader to contact VitalConnect, Inc. to obtain MAN-001, the VitalConnect Platform Integration Manual - Developer Guide — so the reference exists, is named in a regulatory filing, and is published nowhere: vitalconnect.com has no /developers or /api page, api. and developer.vitalconnect.com do not resolve, docs.vitalconnect.com is an internal Google Drive share behind an hd=vitalconnect.com sign-in, and every named /.well-known/ and spec path 404s.'
  evidence:
  - status: 200
    url: https://www.fda.gov/media/137398/download
  - status: 404
    url: https://vitalconnect.com/developers/
  - status: 404
    url: https://vitalconnect.com/openapi.json
  - status: 404
    url: https://vitalconnect.com/.well-known/api-catalog
  - status: 404
    url: https://vitalconnect.com/llms.txt
  - status: 200
    url: https://docs.vitalconnect.com/
  - status: 0
    url: https://api.vitalconnect.com/
  reason: sales-gate
  state: gated
created: '2026-09-04'
description: VitalConnect is a San Jose, California medical device company whose VitalPatch biosensor and Vista Solution platform deliver continuous wireless remote patient monitoring and mobile cardiac telemetry. The single-use adhesive VitalPatch streams up to eleven physiological measurements — single-lead ECG, heart rate, heart rate variability, respiratory rate, skin temperature, body posture, fall detection and step count — to VistaPoint relay software running on a VistaTablet or VistaPhone, and on to the cloud-hosted VistaCenter clinician dashboard used for cardiac monitoring, hospital-at-home, inpatient expansion, chronic disease management and decentralized clinical trials. The VitalConnect Platform exposes an application programming interface documented in MAN-001, the VitalConnect Platform Integration Manual — Developer Guide, which the FDA-cleared VitalPatch Instructions For Use direct integrators to request directly from the company; no public developer portal, API reference
  or machine-readable specification is published. VistaCenter does publicly document an outbound webhook surface that POSTs notification, patient and device events to a customer-configured target URL for EHR, billing and alerting integrations. iRhythm Technologies agreed in August 2026 to acquire VitalConnect for approximately $287.5 million.
image: https://vitalconnect.com/wp-content/uploads/2026/02/VitalConnect%C2%AE-black-276px-center78px.png
layout: provider
modified: '2026-09-04'
name: VitalConnect
nav: Providers
network: true
overview: 'VitalConnect publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Healthcare, Medical Devices, Remote Patient Monitoring, and Cardiac Monitoring.


  The VitalConnect catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  VitalConnect''s developer surface includes documentation, support, engineering blog, and 12 more developer resources.'
plans:
- name: Vitalconnect Plans Pricing
  plan_count: 0
  slug: vitalconnect-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Vitalconnect Rate Limits
  slug: vitalconnect-rate-limits
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Vitalconnect Domain Security
  slug: vitalconnect-domain-security
  summary_line: TLSv1.3
slug: vitalconnect
tags:
- Health
- Healthcare
- Medical Devices
- Remote Patient Monitoring
- Cardiac Monitoring
- Biosensors
- Wearables
- Telehealth
- Clinical Trials
- Webhooks
website: https://vitalconnect.com/
---
