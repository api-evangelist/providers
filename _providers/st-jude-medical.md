---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The Merlin.net Patient Care Network is Abbott''s (formerly St. Jude Medical''s) remote cardiac monitoring platform. It allows clinicians to receive scheduled transmissions and daily alert notifications '
  name: Merlin.net Patient Care Network API
  slug: merlin-net
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/st-jude-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cardiovascular.abbott/us/en/home.html
- group: company
  title: ''
  type: Website
  url: https://www.st-jude-medical.com
- group: company
  title: ''
  type: Website
  url: https://www.abbott.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.cardiovascular.abbott/us/en/hcp/products/cardiac-rhythm-management/connectivity-remote-care/merlin-patient-care-network.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/st-jude-medical-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/st-jude-medical-cardiac-device-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/st-jude-medical-vocabulary.yml
created: '2026-03-24'
description: St. Jude Medical was a global medical device company specializing in cardiovascular devices including implantable cardioverter defibrillators (ICDs), pacemakers, cardiac resynchronization therapy (CRT) devices, and electrophysiology products. The company was acquired by Abbott in January 2017 and now operates as Abbott's cardiac rhythm management division. Its flagship remote monitoring platform, Merlin.net Patient Care Network, enables clinicians to remotely monitor patients with implanted cardiac devices via the Merlin@home transmitter and the myMerlinPulse mobile application.
finops:
- name: St Jude Medical Finops
  service_category: API
  slug: st-jude-medical-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/st-jude-medical.png
json_schemas:
- name: Cardiac Device
  property_count: 12
  slug: st-jude-medical-cardiac-device
json_structures:
- name: St Jude Medical Cardiac Device Structure
  property_count: 11
  slug: st-jude-medical-cardiac-device-structure
jsonld:
- class_count: 27
  name: St Jude Medical Context
  property_count: 6
  slug: st-jude-medical-context
layout: provider
modified: '2026-05-02'
name: St. Jude Medical
nav: Providers
network: true
overview: 'St. Jude Medical publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cardiac, Cardiovascular, Healthcare, Medical Devices, and Patient Monitoring.


  The St. Jude Medical catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  St. Jude Medical''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: St Jude Medical Plans Pricing
  plan_count: 3
  slug: st-jude-medical-plans-pricing
press:
- date: '2026-05-25'
  title: The Impact of Artificial Intelligence on Medical Innovation in ...
  url: https://www.arnoldporter.com/-/media/files/perspectives/publications/2017/08/the-impact-of-artificial-inteelligence-on-medical-innovation.pdf
- date: '2026-05-25'
  title: Abbott Completes Acquisition of St. Jude Medical | DAIC
  url: https://www.dicardiology.com/content/abbott-completes-acquisition-st-jude-medical
- date: '2026-05-25'
  title: Abbott Completes the Acquisition of St. Jude Medical
  url: https://www.prnewswire.com/news-releases/abbott-completes-the-acquisition-of-st-jude-medical-300385823.html
- date: '2026-05-25'
  title: MN-ST.-JUDE-MEDICAL,-INC | Business Wire
  url: https://via.ritzau.dk/pressemeddelelse/5856506/mn-st-jude-medical-inc?publisherId=90456
- date: '2026-05-25'
  title: Cybersecurity
  url: https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity
random_paper: 15
rate_limits:
- limit_count: 5
  name: St Jude Medical Rate Limits
  slug: st-jude-medical-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: St. Jude Medical API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: st-jude-medical-jsonschema-spectral-rules
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 59.3
    catalog_earned_first_party: 0.0
    catalog_gap: 55.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 19.0
    discoverability: 63.0
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 19.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/st-jude-medical/refs/heads/main/screenshots/st-jude-medical-2026-06-20T194437.png
security:
- kind: domain-security
  name: St Jude Medical Domain Security
  slug: st-jude-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: st-jude-medical
tags:
- Cardiac
- Cardiovascular
- Healthcare
- Medical Devices
- Patient Monitoring
- Remote Care
- Fortune 500
website: https://www.cardiovascular.abbott/us/en/home.html
---
