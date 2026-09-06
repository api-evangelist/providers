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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/caya-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caya-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.caya.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.caya.com/tarife
- group: start
  title: ''
  type: Login
  url: https://app.caya.com/login
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.caya.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.caya.com/downloads/agb-geschaeftskunden
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.caya.com/datenschutzerklaerung
- group: auth
  title: ''
  type: Compliance
  url: https://www.caya.com/compliance
created: '2026-07-17'
description: Caya (Caya GmbH, Berlin) is a German intelligent document processing (IDP) company whose Document Automation Suite digitizes, classifies, and routes business documents end to end. Its core capabilities are Post Scan (physical mail intake with OCR and automatic classification), Document Extractions (AI-powered structured data extraction), and Document Automations (rule-based routing and distribution into downstream systems). Caya connects to 100+ tools across accounting, ERP, HR, cloud storage, and e-signature, and hosts data in a high-security Frankfurt data center. It is certified and compliant against ISO 27001, GDPR/DSGVO, DORA, GoBD, and German HGB/AO retention rules, with a public Vanta-hosted trust center. Surfaced as an HV Capital portfolio company and enriched into the API Evangelist network.
image: https://cdn.prod.website-files.com/6278c3c168fca8824b100ce4/62dea86a305e71077637a0d6_Alle%20Dokumente%20-%20Visual%201200x627.png
layout: provider
modified: '2026-07-18'
name: Caya
nav: Providers
network: true
overview: 'Caya is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Enterprise Software, Document Automation, Intelligent Document Processing, and Document-Management.


  Caya''s developer surface includes pricing and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 16.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/caya/refs/heads/main/screenshots/caya-2026-07-25T204819.png
security:
- kind: domain-security
  name: Caya Domain Security
  slug: caya-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Caya Trust Center
  slug: caya-trust-center
  summary_line: ISO 27001, GDPR/DSGVO, DORA, GoBD, BaFin-compliant, HGB, AO (Abgabenordnung)
slug: caya
tags:
- Company
- Ai Enterprise Software
- Document Automation
- Intelligent Document Processing
- Document-Management
- OCR
- Data Extraction
- Mail Digitization
- Compliance
- Germany
website: https://www.caya.com/
---
