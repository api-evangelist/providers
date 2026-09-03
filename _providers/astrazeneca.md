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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/astrazeneca-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AstraZeneca
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/astrazeneca
- group: company
  title: ''
  type: Website
  url: https://www.astrazeneca.com/
- group: start
  title: ''
  type: ClinicalTrials
  url: https://www.astrazenecaclinicaltrials.com/
- group: other
  title: ''
  type: DataSharing
  url: https://www.astrazenecaclinicaltrials.com/transparency/data-sharing/
- group: company
  title: ''
  type: Partnerships
  url: https://www.astrazeneca.com/partnerships.html
- group: other
  title: ''
  type: Suppliers
  url: https://www.astrazeneca.com/suppliers.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.astrazeneca.com/legal/integrated-privacy-notice.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.astrazeneca.com/legal/terms-of-use.html
- group: operate
  title: ''
  type: Contact
  url: https://www.astrazeneca.com/contact-us.html
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-05'
description: AstraZeneca is a British-Swedish multinational pharmaceutical and biotechnology company focused on oncology, cardiovascular, renal, metabolism, and respiratory therapies. AstraZeneca does not publish a general developer portal or commercial public APIs; technology integration is delivered through enterprise partner programs, clinical trial data portals such as clinicaltrials.gov and the Vivli platform, and EDI/x12 channels used by distributors and pharmacy benefit managers.
features:
- description: Clinical trial registrations and results are publicly accessible via clinicaltrials.gov, the EU Clinical Trials Register, and AstraZeneca's own trial site.
  name: Clinical Trial Information
- description: Anonymized patient-level clinical trial data is made available to qualified researchers through the Vivli platform.
  name: Patient-Level Data Sharing
- description: Healthcare professionals can request product and safety information via country-specific medical information sites.
  name: Medical Information Portal
- description: Drug ordering, returns, chargebacks, and shipment notifications are exchanged with distributors via standardized x12 EDI transactions.
  name: Distributor and Wholesaler EDI
- description: Adverse-event reports are received via regulatory channels (E2B, FAERS) rather than a public API.
  name: Pharmacovigilance Submissions
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/astrazeneca.png
layout: provider
modified: '2026-05-16'
name: AstraZeneca
nav: Providers
network: true
overview: AstraZeneca is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pharmaceuticals, Biotechnology, and Healthcare.
random_paper: 14
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 93.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Astrazeneca Domain Security
  slug: astrazeneca-domain-security
  summary_line: TLSv1.3 · DMARC
slug: astrazeneca
tags:
- Pharmaceuticals
- Biotechnology
- Healthcare
use_cases:
- description: Find and link AstraZeneca-sponsored studies into clinical research and evidence-generation platforms.
  name: Clinical Research Data Discovery
- description: Distributors integrate order, shipment, and chargeback flows with AstraZeneca's commercial supply chain via EDI.
  name: Pharma Supply Chain Integration
- description: HCPs and medical-information vendors retrieve dosing, contraindication, and interaction information for clinical decision support.
  name: Medical Affairs Engagement
- description: Researchers use the Vivli platform to combine AstraZeneca trial data with external real-world evidence sources.
  name: Real-World Evidence Studies
website: https://www.astrazeneca.com/
---
