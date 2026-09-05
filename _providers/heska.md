---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.heska.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.antechdiagnostics.com/in-house-diagnostics/ — a different registrable domain (heska.com -> antechdiagnostics.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
api_count: 3
apis:
- description: Partner-gated integration surface for placing point-of-care laboratory orders from a practice information management system to Heska in-clinic analyzers. A completed order in the PIMS triggers a reque
  name: Heska Lab Orders API
  slug: heska-lab-orders-api
- description: 'Partner-gated integration surface for returning completed analyzer results back into the ordering PIMS patient record. HeskaView Connect provides consolidated reports, unlimited analyzer connections, '
  name: Heska Analyzer Results API
  slug: heska-analyzer-results-api
- description: Partner-gated integration surface for associating a lab order and its results with a patient/owner record so diagnostic charts are created and updated automatically in the integrating EMR. No public A
  name: Heska Patients API
  slug: heska-patients-api
artifact_total: 4
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/antech-diagnostics/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heska-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heska-corporation
- group: company
  title: ''
  type: Website
  url: https://www.heska.com/
- group: docs
  title: ''
  type: Documentation
  url: https://customerportal.heska.com/
- group: other
  title: ''
  type: Registration
  url: https://registration.heska.com/
created: '2026-07-05'
description: Heska is a veterinary diagnostics company that makes in-clinic point-of-care lab analyzers and imaging for veterinary practices - chemistry (Element DC/DCX/RC/RCX), hematology (Element HT5), blood gas and electrolytes (Element POC), immunodiagnostics (Element i), coagulation (Element COAG), and AI-guided urine/fecal/blood-morphology testing (Element AIM) - plus the HeskaView Connect lab data and workflow software. Heska was acquired by Antech Diagnostics, a subsidiary of Mars, Incorporated (Mars Petcare / Mars Science & Diagnostics), in 2023, and now operates as an Antech company. Heska exposes a partner-gated integration API that bidirectionally connects its analyzers to veterinary practice information management systems (PIMS/EMR) - orders flow out to the analyzers and results flow back into the patient record - but there is no public, self-service developer portal, published API reference, OpenAPI, or public pricing. Access is provisioned to approved integration partners
  (ezyVet, Instinct, Vetspire, NectarVet, Digitail, and others) via API Partner credentials.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heska.png
layout: provider
modified: '2026-07-05'
name: Heska
nav: Providers
network: true
overview: 'Heska publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Veterinary, Diagnostics, Animal Health, Point of Care, and Lab Analyzers.


  Heska''s developer surface includes documentation and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heska/refs/heads/main/screenshots/heska-2026-07-25T221053.png
security:
- kind: domain-security
  name: Heska Domain Security
  slug: heska-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: heska
tags:
- Veterinary
- Diagnostics
- Animal Health
- Point of Care
- Lab Analyzers
- Partner API
- Antech
- Mars
website: https://www.heska.com/
---
