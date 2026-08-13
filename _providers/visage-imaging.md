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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 5
apis:
- description: Open API for integrating third-party and customer AI algorithms into the Visage 7 platform and Visage AI Accelerator research server, unifying research and diagnostic imaging. Publicly described as su
  name: Visage 7 AI Open API
  slug: visage-imaging-ai-open-api
- description: REST API introduced in Visage 7 release notes supporting a data-quality (QA) workflow based on delete-and-resend of studies/objects between Visage 7 and connected archives and modalities. Documented o
  name: Visage 7 QA REST API
  slug: visage-imaging-qa-rest-api
- description: Standards-based DICOMweb interface for querying, retrieving, and storing imaging studies against the Visage 7 archive-neutral platform - QIDO-RS (query), WADO-RS / WADO-URI (retrieve), and STOW-RS (st
  name: Visage 7 DICOMweb API
  slug: visage-imaging-dicomweb-api
- description: HL7 v2 messaging and FHIR-based interoperability for order/result and imaging-context exchange between Visage 7, the EHR, and RIS (including FHIR ImagingStudy / DiagnosticReport resources referenced b
  name: Visage 7 HL7 / FHIR Interoperability API
  slug: visage-imaging-hl7-fhir-api
- description: Context / URL launch interface used to open the Visage 7 zero-footprint thin-client viewer to a specific patient, study, or accession from an EHR, RIS, or portal (single sign-on and deep-link paramete
  name: Visage 7 Viewer Launch API
  slug: visage-imaging-viewer-launch-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/visage-imaging-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/visage-imaging
- group: company
  title: ''
  type: Website
  url: https://visageimaging.com/
- group: docs
  title: ''
  type: Documentation
  url: https://visageimaging.com/support/product-documentation/
- group: start
  title: ''
  type: ClientPortal
  url: http://www2013.visageimaging.com/support/client-portal/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.promedicus.com/
created: '2026-07-05'
description: Visage Imaging is a global enterprise imaging vendor and a wholly-owned subsidiary of Pro Medicus Limited (ASX PME). Its flagship Visage 7 Enterprise Imaging Platform delivers server-side rendered images adaptively streamed to an intelligent zero-footprint thin-client viewer for diagnostic radiology, cardiology, and mobile reading, alongside Visage 7 Open Archive and the Visage AI Accelerator research platform. Interoperability is built on healthcare imaging standards - DICOM / DICOMweb, HL7, FHIR, and IHE profiles - and Visage exposes REST and open-API surfaces for AI algorithm integration and QA workflows. There is no public self-service developer portal; API access is partner- and customer-gated (Client Portal login, product documentation login, and an invitation-only AI Accelerator Program), so the API entries below are logically modeled from public product and release-note material rather than a published API reference.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/visage-imaging.png
layout: provider
modified: '2026-07-05'
name: Visage Imaging
nav: Providers
network: true
overview: 'Visage Imaging publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise Imaging, Medical Imaging, Radiology, PACS, and DICOM.


  Visage Imaging''s developer surface includes documentation and 5 more developer resources.'
random_paper: 96
score:
  band: minimal
  composite: 8.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Visage Imaging Domain Security
  slug: visage-imaging-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: visage-imaging
tags:
- Enterprise Imaging
- Medical Imaging
- Radiology
- PACS
- DICOM
- DICOMweb
- HL7
- FHIR
- Healthcare
- AI
- Pro Medicus
website: https://visageimaging.com/
---
