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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Solventum's Health Information Systems (formerly 3M HIS) provides APIs for clinical documentation, coding and grouping, computer-assisted coding (CAC), revenue cycle management, and healthcare analyti
  name: Solventum Health Information Systems API
  slug: health-information-systems
- description: APIs supporting computer-assisted clinical documentation improvement (CDI) workflows, providing real-time query generation, physician query management, and documentation quality analysis to improve sp
  name: Solventum Clinical Documentation Improvement API
  slug: clinical-documentation-improvement
artifact_total: 30
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solventum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.solventum.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.solventum.com/en-us/home/health-information-systems/
- group: company
  title: ''
  type: Blog
  url: https://www.solventum.com/en-us/home/about-solventum/newsroom/
- group: company
  title: ''
  type: Investors
  url: https://investors.solventum.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/solventum/
- group: operate
  title: ''
  type: Support
  url: https://www.solventum.com/en-us/home/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solventum.com/en-us/home/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.solventum.com/en-us/home/terms-of-use/
created: '2026-03-21'
description: Solventum is a Fortune 500 healthcare company spun off from 3M in 2024, focused on healthcare technology including medical-surgical solutions, dental and orthodontic products, health information systems, and purification and filtration technologies. Solventum serves hospitals, clinics, dental practices, and healthcare IT organizations worldwide.
examples:
- key_count: 13
  name: Solventum Clinical Encounter Example
  slug: solventum-clinical-encounter-example
- key_count: 7
  name: Solventum Coding Result Example
  slug: solventum-coding-result-example
features:
- description: AI-powered ICD-10, CPT, and DRG coding from clinical documentation.
  name: Computer-Assisted Coding
- description: Real-time CDI queries and documentation quality analysis.
  name: Clinical Documentation Improvement
- description: Diagnosis-related group calculation for inpatient reimbursement.
  name: DRG Grouping
- description: End-to-end revenue cycle analytics and workflow tools.
  name: Revenue Cycle Management
- description: Native integration with Epic, Cerner, Oracle Health, and other EHR systems.
  name: EHR Integration
- description: Clinical and financial analytics for quality and performance reporting.
  name: Healthcare Analytics
finops:
- name: Solventum Finops
  service_category: API
  slug: solventum-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/solventum.png
integrations:
- description: Native integration with Epic EHR for embedded coding workflows.
  name: Epic
- description: Integration with Cerner/Oracle Health for clinical documentation.
  name: Oracle Health (Cerner)
- description: Integration with MEDITECH EHR platform.
  name: MEDITECH
- description: FHIR-based data exchange for interoperability.
  name: HL7 FHIR
- description: ICD-10-CM/PCS coding standard support.
  name: ICD-10
- description: Current Procedural Terminology coding support.
  name: CPT
json_schemas:
- name: ClinicalEncounter
  property_count: 13
  slug: solventum-clinical-encounter
- name: CodingResult
  property_count: 7
  slug: solventum-coding-result
json_structures:
- name: Solventum His Structure
  property_count: 0
  slug: solventum-his-structure
jsonld:
- class_count: 1
  name: Solventum Context
  property_count: 6
  slug: solventum-context
layout: provider
modified: '2026-05-02'
name: Solventum
nav: Providers
network: true
overview: 'Solventum publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Dental, EHR, Electronic Health Records, Healthcare, and Healthcare IT.


  The Solventum catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Solventum''s developer surface includes documentation, engineering blog, support, and 6 more developer resources.'
plans:
- name: Solventum Plans Pricing
  plan_count: 3
  slug: solventum-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Solventum Rate Limits
  slug: solventum-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Solventum API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: solventum-jsonschema-spectral-rules
score:
  band: emerging
  composite: 12.3
  delta: -13.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 7.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 26.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/solventum/refs/heads/main/screenshots/solventum-2026-06-20T194155.png
security:
- kind: domain-security
  name: Solventum Domain Security
  slug: solventum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: solventum
tags:
- Dental
- EHR
- Electronic Health Records
- Healthcare
- Healthcare IT
- Health Information Systems
- Medical Devices
- Medical Technology
use_cases:
- description: Automate ICD-10-CM/PCS coding for inpatient encounters.
  name: Inpatient Coding
- description: Automate CPT and ICD-10-CM coding for outpatient and ambulatory encounters.
  name: Outpatient Coding
- description: Generate CMS quality measure data for value-based care programs.
  name: Quality Reporting
- description: Identify missed revenue opportunities through coding accuracy analysis.
  name: Revenue Optimization
- description: Improve physician documentation specificity for accurate reimbursement.
  name: Clinical Documentation
website: https://www.solventum.com
---
