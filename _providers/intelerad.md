---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Intelerad Agentic Access
  operation_count: 15
  slug: intelerad-agentic-access
  summary_line: 15 operations · 14 acting
api_count: 9
apis:
- description: The HL7 API from Intelerad — 1 operation(s) for hl7.
  name: Intelerad HL7 API
  slug: intelerad-hl7-api
- description: The Namespace API from Intelerad — 1 operation(s) for namespace.
  name: Intelerad Namespace API
  slug: intelerad-namespace-api
- description: The Order API from Intelerad — 2 operation(s) for order.
  name: Intelerad Order API
  slug: intelerad-order-api
- description: The Patient API from Intelerad — 2 operation(s) for patient.
  name: Intelerad Patient API
  slug: intelerad-patient-api
- description: The Report API from Intelerad — 1 operation(s) for report.
  name: Intelerad Report API
  slug: intelerad-report-api
- description: The Session API from Intelerad — 2 operation(s) for session.
  name: Intelerad Session API
  slug: intelerad-session-api
- description: The Storage API from Intelerad — 1 operation(s) for storage.
  name: Intelerad Storage API
  slug: intelerad-storage-api
- description: The Study API from Intelerad — 4 operation(s) for study.
  name: Intelerad Study API
  slug: intelerad-study-api
- description: The Webhook API from Intelerad — 1 operation(s) for webhook.
  name: Intelerad Webhook API
  slug: intelerad-webhook-api
artifact_total: 16
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/intelerad-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/intelerad-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intelerad-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/intelerad-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/intelerad-medical-systems
- group: company
  title: ''
  type: Website
  url: https://www.intelerad.com/
- group: docs
  title: ''
  type: Documentation
  url: https://access.dicomgrid.com/api/v3/api.html
- group: commercial
  title: ''
  type: Plans
  url: plans/intelerad-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/intelerad-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/intelerad-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.intelerad.com/en/blog/
created: '2026-07-05'
description: Intelerad Medical Systems is an enterprise medical imaging company whose platform spans diagnostic PACS (IntelePACS), the InteleViewer / zero-footprint web viewer, a vendor-neutral archive (VNA), and the cloud image-exchange platform InteleShare - the product formed after Intelerad acquired Ambra Health (Ambra Image Exchange) in 2021. The InteleShare / Ambra platform exposes a documented public "v3 Services" REST-like API plus a Storage API for programmatically managing DICOM studies, patients, orders, reports, HL7 message flows, routing, and multi-tenant namespaces. Integration is built on medical-imaging interoperability standards - DICOM and DICOMweb (WADO / QIDO / STOW), HL7 v2 (ORM, ORU, ADT), and FHIR - with a Gateway that routes DICOM and HL7 between on-premise systems and the cloud, plus EHR/RIS integrations (Epic, Cerner, Athena). Core PACS/RIS APIs are partner- and contract-gated; the InteleShare / Ambra v3 API is the publicly documented developer surface.
finops:
- name: Intelerad Finops
  service_category: Healthcare Imaging Platform
  slug: intelerad-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/intelerad.png
layout: provider
modified: '2026-07-05'
name: Intelerad
nav: Providers
network: true
overview: 'Intelerad publishes 9 APIs on the [APIs.io](https://apis.io/) network, including HL7 API, Namespace API, Order API, and 6 more. Tagged areas include Medical Imaging, PACS, Enterprise Imaging, Radiology, and DICOM.


  Intelerad''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Intelerad Plans Pricing
  plan_count: 1
  slug: intelerad-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 3
  name: Intelerad Rate Limits
  slug: intelerad-rate-limits
score:
  band: thin
  composite: 33.2
  delta: -4.1
  facets:
    commercial_clarity: 36.8
    contract_quality: 48.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intelerad/refs/heads/main/screenshots/intelerad-2026-07-25T222644.png
security:
- kind: authentication
  name: Intelerad Authentication
  slug: intelerad-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Intelerad Domain Security
  slug: intelerad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Intelerad Trust Center
  slug: intelerad-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: intelerad
tags:
- Medical Imaging
- PACS
- Enterprise Imaging
- Radiology
- DICOM
- DICOMweb
- HL7
- FHIR
- Healthcare
- Interoperability
- Image Exchange
website: https://www.intelerad.com/
---
