---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/indio-tech-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/indio-tech-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/indio-technologies
- group: company
  title: ''
  type: Website
  url: https://www.useindio.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.useindio.com/en/
- group: other
  title: ''
  type: DeveloperProgram
  url: https://devcenter.myappliedproducts.com/home
- group: other
  title: ''
  type: ParentCompany
  url: https://www1.appliedsystems.com/en-us/solutions/for-agents/insurance-application-software/indio/
- group: commercial
  title: ''
  type: Plans
  url: plans/indio-tech-plans-pricing.yml
created: '2026-07-10'
description: Indio Technologies is a cloud-based insurance application and submissions platform for commercial insurance agencies and brokers, acquired by and now part of Applied Systems. Indio replaces manual PDF forms and spreadsheets with a library of 10,000+ digitally enhanced "smart" insurance forms and ACORD applications, a submission workspace that packages digital applications, schedule workbooks, document-upload requests and e-signature requests, plus secure document sharing. Indio does not publish a self-service public developer API. Programmatic access is partner/carrier-gated and delivered through Applied Systems - the Applied Epic bi-directional integration and SDK, the IVANS data exchange API (used to move submission and proposal data between agencies, brokers and carriers), and the Applied DevCenter partner developer program. The API surfaces below are modeled from Indio's documented product concepts (submissions, forms/applications, clients, documents and e-signatures); they
  are logical groupings, not publicly documented endpoints (endpointsModeled).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/indio-tech.png
layout: provider
modified: '2026-07-25'
name: Indio Technologies
nav: Providers
network: true
overview: 'Indio Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Insurtech, Insurance Applications, Submissions, and Digital Forms.


  Indio Technologies'' developer surface includes documentation and 7 more developer resources.'
plans:
- name: Indio Tech Plans Pricing
  plan_count: 2
  slug: indio-tech-plans-pricing
random_paper: 9
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Indio Tech Domain Security
  slug: indio-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Indio Tech Vulnerability Disclosure
  slug: indio-tech-vulnerability-disclosure
  summary_line: Hackerone
slug: indio-tech
tags:
- Insurance
- Insurtech
- Insurance Applications
- Submissions
- Digital Forms
- ACORD
- E-Signature
- Commercial Insurance
- Applied Systems
- Partner API
website: https://www.useindio.com
---
