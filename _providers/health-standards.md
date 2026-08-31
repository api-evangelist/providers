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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/health-standards-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hl7.org
- group: other
  title: ''
  type: FHIR
  url: https://hl7.org/fhir/
- group: other
  title: ''
  type: HL7v2
  url: https://www.hl7.org/implement/standards/product_brief.cfm?product_id=185
- group: other
  title: ''
  type: CDA
  url: https://www.hl7.org/implement/standards/product_brief.cfm?product_id=7
- group: other
  title: ''
  type: USCore
  url: https://www.hl7.org/fhir/us/core/
- group: docs
  title: ''
  type: ImplementationGuides
  url: http://www.fhir.org/guides/registry
- group: start
  title: ''
  type: Registry
  url: https://registry.fhir.org/
- group: other
  title: ''
  type: DICOM
  url: https://www.dicomstandard.org/
- group: other
  title: ''
  type: IHE
  url: https://www.ihe.net/
- group: other
  title: ''
  type: SNOMEDCT
  url: https://www.snomed.org/
- group: other
  title: ''
  type: LOINC
  url: https://loinc.org/
- group: other
  title: ''
  type: RxNorm
  url: https://www.nlm.nih.gov/research/umls/rxnorm/
- group: other
  title: ''
  type: ICD
  url: https://www.who.int/standards/classifications/classification-of-diseases
- group: operate
  title: ''
  type: Community
  url: http://chat.fhir.org/
created: '2025'
description: Health Standards covers the collection of technical standards and specifications used in healthcare interoperability, including HL7 FHIR, HL7 v2, CDA, DICOM, IHE profiles, ICD codes, SNOMED CT, LOINC, RxNorm, US Core, and other health data exchange and coding standards. This index curates the canonical specifications, reference implementations, registries, and developer resources for building interoperable healthcare applications.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/health-standards.png
layout: provider
modified: '2026-04-28'
name: Health Standards
nav: Providers
network: true
overview: Health Standards is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include CDA, DICOM, FHIR, Health Standards, and Healthcare Interoperability.
random_paper: 1
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/health-standards/refs/heads/main/screenshots/health-standards-2026-06-20T182557.png
security:
- kind: domain-security
  name: Health Standards Domain Security
  slug: health-standards-domain-security
  summary_line: TLSv1.3 · DMARC
slug: health-standards
tags:
- CDA
- DICOM
- FHIR
- Health Standards
- Healthcare Interoperability
- HL7
- ICD
- LOINC
- SNOMED CT
- US Core
website: https://www.hl7.org
---
