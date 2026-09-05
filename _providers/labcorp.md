---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Labcorp supports HL7 FHIR-based exchange of laboratory orders, results, and diagnostic reports with provider and health-system EHR systems. The interface typically exposes FHIR resources such as Servi
  name: Labcorp FHIR API
  slug: labcorp-fhir-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/labcorp-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/labcorp-clinical-development
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/labcorp
- group: company
  title: ''
  type: Website
  url: https://www.labcorp.com
- group: operate
  title: ''
  type: Support
  url: https://www.labcorp.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.labcorp.com/about/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.labcorp.com/hipaa-privacy
- group: company
  title: ''
  type: Investor Relations
  url: https://ir.labcorp.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.labcorp.com/labcorp-link
created: '2026-03-21'
description: Labcorp helps patients, providers, organizations, and biopharma companies guide vital healthcare decisions every day. Labcorp supports HL7 / FHIR-based integration for laboratory orders and results exchange with electronic health record (EHR) systems, but does not publish a fully open public developer portal; access is granted through health-system and biopharma integration agreements.
finops:
- name: Labcorp Finops
  service_category: Healthcare / Diagnostics
  slug: labcorp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/labcorp.png
layout: provider
modified: '2026-07-25'
name: Labcorp
nav: Providers
network: true
overview: 'Labcorp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Diagnostics, FHIR, Fortune 500, Healthcare, and Laboratory.


  Labcorp''s developer surface includes support, engineering blog, and 7 more developer resources.'
plans:
- name: Labcorp Plans Pricing
  plan_count: 2
  slug: labcorp-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Labcorp Rate Limits
  slug: labcorp-rate-limits
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/labcorp/refs/heads/main/screenshots/labcorp-2026-06-20T184236.png
security:
- kind: domain-security
  name: Labcorp Domain Security
  slug: labcorp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: labcorp
tags:
- Diagnostics
- FHIR
- Fortune 500
- Healthcare
- Laboratory
- Life Sciences
website: https://www.labcorp.com
---
