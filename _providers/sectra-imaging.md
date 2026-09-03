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
  scored_at: '2026-09-03'
api_count: 5
apis:
- description: 'Web-based access to imaging studies, series, and instances using the DICOM standard''s RESTful services - QIDO-RS (query), WADO-RS (retrieve), and STOW-RS (store). Sectra''s enterprise imaging platform '
  name: Sectra DICOMweb API
  slug: sectra-imaging-dicomweb-api
- description: HL7 v2 messaging interface for exchanging orders, scheduling, worklist, and results/reports between Sectra PACS/RIS and surrounding EMR/RIS systems. This is a message-based (typically MLLP/HL7 v2) int
  name: Sectra HL7 Integration Interface
  slug: sectra-imaging-hl7-integration-interface
- description: 'Clinical context synchronization using the FHIRcast standard, which Sectra helped originate (with Epic) and for which Sectra published the first open-source sandbox and reference implementation under '
  name: Sectra FHIRcast Interface
  slug: sectra-imaging-fhircast-interface
- description: Web Content API for embedding third-party web content, results, and applications into the Sectra diagnostic viewer in patient/study context, and for launching Sectra in context from other systems. Thi
  name: Sectra Web Content API
  slug: sectra-imaging-web-content-api
- description: IHE Cross-Enterprise Document Sharing (XDS/XDS-I) interface for registering, querying, and retrieving imaging documents and manifests across enterprise boundaries. A profile-based interoperability int
  name: Sectra IHE XDS Interface
  slug: sectra-imaging-xds-interface
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sectra-imaging-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sectra-imaging-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sectra
- group: company
  title: ''
  type: Website
  url: https://sectra.com/
- group: company
  title: ''
  type: Website
  url: https://medical.sectra.com/
- group: docs
  title: ''
  type: Documentation
  url: https://medical.sectra.com/solutionarea/enterprise-imaging-platform/
- group: docs
  title: ''
  type: Documentation
  url: https://amplifiermarketplace.sectra.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/fhircast
created: '2026-07-05'
description: Sectra is a Swedish medical technology company providing an enterprise imaging platform (PACS/VNA) for radiology, pathology, cardiology, orthopaedics, and other -ologies. Integration is delivered through established healthcare interoperability standards rather than a single open developer API - DICOM and DICOMweb for imaging, HL7 for orders/results messaging, IHE XDS for cross-enterprise document sharing, FHIR/FHIRcast for clinical context synchronization, and a Web Content API for embedding third-party content and applications into the diagnostic viewer. AI and third-party applications integrate through the Sectra Amplifier Marketplace / Amplifier Services ecosystem. Sectra's API and integration surface is partner- and customer-gated (deployed per-site, no public self-service developer portal); the API entries below are honestly modeled from Sectra's documented standards and interfaces, not scraped from an open OpenAPI catalog. Sectra also authored the first open-source FHIRcast
  sandbox and reference implementation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sectra-imaging.png
layout: provider
modified: '2026-07-25'
name: Sectra
nav: Providers
network: true
overview: 'Sectra publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Imaging, Enterprise Imaging, PACS, VNA, and Radiology.


  Sectra''s developer surface includes documentation and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 2
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 8.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sectra-imaging/refs/heads/main/screenshots/sectra-imaging-2026-09-02T154711.png
security:
- kind: domain-security
  name: Sectra Imaging Domain Security
  slug: sectra-imaging-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sectra Imaging Vulnerability Disclosure
  slug: sectra-imaging-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sectra-imaging
tags:
- Medical Imaging
- Enterprise Imaging
- PACS
- VNA
- Radiology
- Pathology
- Healthcare
- DICOM
- DICOMweb
- HL7
- FHIR
- FHIRcast
- IHE XDS
- Interoperability
- Partner API
- Sweden
website: https://sectra.com/
---
