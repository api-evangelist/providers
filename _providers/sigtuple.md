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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sigtuple-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sigtuple.com
- group: company
  title: ''
  type: Blog
  url: https://sigtuple.com/blogs
- group: operate
  title: ''
  type: Support
  url: https://sigtuple.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sigtuple.com/terms
created: '2026-07-17'
description: SigTuple Technologies is a medical-technology company that combines artificial intelligence, robotics, microfluidics and high-resolution digital microscopy to automate the microscopic analysis of biological samples across human and veterinary diagnostics. Its product portfolio includes AS76, a CE-IVDR compliant automated digital cell morphology analyzer for peripheral blood smears with true 100X oil immersion; AI100, an FDA- and CE-cleared multi-purpose analyzer for blood smear and urine sediment analysis; and SigVet, an AI point-of-care platform for veterinary clinics. Backed by Accel, the company reports 10+ years of R&D, 27 patents and 350+ deployments globally. As of this enrichment pass SigTuple publishes no public developer/API surface (no docs portal, OpenAPI, /.well-known discovery, or llms.txt were found); this profile captures identity plus a probed domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sigtuple.png
layout: provider
modified: '2026-07-21'
name: SigTuple
nav: Providers
network: true
overview: 'SigTuple is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Healthcare, Diagnostics, and Pathology.


  SigTuple''s developer surface includes engineering blog, support, and 3 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sigtuple/refs/heads/main/screenshots/sigtuple-2026-09-02T155441.png
security:
- kind: domain-security
  name: Sigtuple Domain Security
  slug: sigtuple-domain-security
  summary_line: TLSv1.2 · DMARC
slug: sigtuple
tags:
- Company
- Artificial Intelligence
- Healthcare
- Diagnostics
- Pathology
- Medical Devices
- Microscopy
- Machine-Learning
website: https://sigtuple.com
---
