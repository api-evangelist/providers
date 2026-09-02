---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bayer-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bayer-Group
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bayer
- group: company
  title: ''
  type: Website
  url: https://www.bayer.com/
- group: other
  title: ''
  type: Pharmaceuticals
  url: https://www.bayer.com/en/pharma/pharmaceuticals
- group: other
  title: ''
  type: ConsumerHealth
  url: https://www.bayer.com/en/consumer-health/consumer-health
- group: other
  title: ''
  type: CropScience
  url: https://www.cropscience.bayer.com/
- group: build
  title: ''
  type: ClimateFieldView
  url: https://climate.com/
- group: start
  title: ''
  type: ClinicalTrials
  url: https://www.clinicaltrials.bayer.com/
- group: other
  title: ''
  type: DataSharing
  url: https://vivli.org/members/bayer/
- group: other
  title: ''
  type: Suppliers
  url: https://www.bayer.com/en/suppliers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bayer.com/en/data-protection
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bayer.com/en/terms-and-conditions
- group: operate
  title: ''
  type: Contact
  url: https://www.bayer.com/en/contact
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-05'
description: Bayer is a German multinational pharmaceutical and life sciences company operating across pharmaceuticals, consumer health, and crop science. Bayer does not publish a single corporate-level public developer portal; integration is delivered through enterprise partner programs, the Bayer Crop Science Climate FieldView ecosystem (partner-gated APIs and certified-partner integrations), pharmacovigilance and clinical-trial data exchange, and EDI / x12 channels with distributors and pharmacy benefit managers.
features:
- description: Bayer Crop Science's Climate FieldView platform supports certified third-party integrations for field data sharing, planting prescriptions, and equipment-monitor data via a partner program.
  name: Climate FieldView Partner Ecosystem
- description: Bayer publishes registered clinical trial information and posts results to public registries including clinicaltrials.gov and the EU CTR.
  name: Clinical Trial Information
- description: Anonymized patient-level clinical trial data is made available to qualified researchers via the Vivli platform.
  name: Patient-Level Data Sharing
- description: Healthcare professionals can request product and safety information through country-specific medical information sites.
  name: Medical Information Portal
- description: Drug ordering, returns, chargebacks, and shipment notifications are exchanged with distributors via standardized x12 EDI transactions.
  name: Distributor and Wholesaler EDI
- description: Adverse-event reports are received via regulatory channels (E2B, FAERS, EudraVigilance) rather than a public API.
  name: Pharmacovigilance Submissions
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bayer.png
layout: provider
modified: '2026-05-16'
name: Bayer
nav: Providers
network: true
overview: Bayer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pharmaceuticals, Agriculture, Healthcare, Chemicals, and Crop Science.
random_paper: 6
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bayer/refs/heads/main/screenshots/bayer-2026-06-20T173052.png
security:
- kind: domain-security
  name: Bayer Domain Security
  slug: bayer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bayer
tags:
- Pharmaceuticals
- Agriculture
- Healthcare
- Chemicals
- Crop Science
use_cases:
- description: Equipment OEMs, agronomy services, and ag-data platforms integrate with Climate FieldView to share planting, application, and harvest data.
  name: Precision Agriculture Integration
- description: Researchers find and link Bayer-sponsored studies into clinical evidence and real-world data platforms.
  name: Clinical Research Data Discovery
- description: Distributors integrate order, shipment, and chargeback flows with Bayer's commercial supply chain via EDI.
  name: Pharma Supply Chain Integration
- description: HCPs and medical-information vendors retrieve dosing, contraindication, and interaction information for clinical decision support.
  name: Medical Affairs Engagement
- description: Authorities, retailers, and growers consume Bayer-published stewardship guidance for safe and sustainable product use.
  name: Crop Protection Stewardship
website: https://www.bayer.com/
---
