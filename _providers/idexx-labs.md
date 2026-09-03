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
  scored_at: '2026-09-02'
api_count: 5
apis:
- description: Retrieve diagnostic results from IDEXX Reference Laboratories and IDEXX in-house analyzers (VetLab Station), including real-time test status updates and the full IDEXX diagnostic history for a patient
  name: IDEXX VetConnect PLUS Diagnostic Results API
  slug: idexx-labs-vetconnect-plus-results-api
- description: Submit electronic test requests (orders) from a practice management system to IDEXX Reference Laboratories and configure in-house analyzer runs, then track order status through VetConnect PLUS. Partne
  name: IDEXX VetConnect PLUS Diagnostic Orders API
  slug: idexx-labs-vetconnect-plus-orders-api
- description: The IDEXX Web PACS "API Partner" integration lets an imaging or practice management partner send diagnostic imaging requests and link captured DICOM studies (x-ray, ultrasound, CT, MR, IO) back to the
  name: IDEXX Web PACS Diagnostic Imaging API
  slug: idexx-labs-web-pacs-imaging-api
- description: Reference resources that underpin ordering and results - the IDEXX test and panel catalog, analyte/test codes, units, and reference ranges - used to map a partner's requests and result displays to IDE
  name: IDEXX VetConnect PLUS Reference Data API
  slug: idexx-labs-vetconnect-plus-reference-data-api
- description: OAuth 2.0-style authentication for IDEXX partner integrations. The developer.vetconnectplus.com portal is login-gated (the sign-in flow carries OAuth parameters), and Web PACS API Partner integrations
  name: IDEXX VetConnect PLUS Authentication
  slug: idexx-labs-vetconnect-plus-authentication
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/idexx-labs-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/idexx-labs-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/idexx-laboratories
- group: company
  title: ''
  type: Website
  url: https://www.idexx.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.vetconnectplus.com/
- group: build
  title: ''
  type: SoftwareIntegrations
  url: https://software.idexx.com/integrations
- group: build
  title: ''
  type: IntegrationRequest
  url: https://www.idexx.com/en/veterinary/software-services/idexx-practice-management-software-integration-request-form/
created: '2026-07-05'
description: IDEXX Laboratories is a global leader in veterinary diagnostics, offering reference laboratory testing, in-house analyzers (IDEXX VetLab Station), diagnostic imaging (IDEXX Web PACS), and practice management software (Cornerstone, Neo, and ezyVet, which IDEXX acquired in 2021). IDEXX connects the practice to its diagnostic ecosystem through VetConnect PLUS - a diagnostic results and ordering platform - and through partner integration APIs for Web PACS imaging and reference/in-house lab results. These developer integrations are partner-gated - the developer portal at developer.vetconnectplus.com requires an authenticated login, and partner access is granted only after an approved IDEXX integration request. Web PACS API Partner integrations authenticate with OAuth 2.0-style credentials (Client ID, Client Secret, and Grant Type) issued by IDEXX customer support. IDEXX does not publish an open, unauthenticated API reference, OpenAPI description, or pricing; the logical APIs below
  are modeled from IDEXX's public product and integration pages, not from a public endpoint reference.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/idexx-labs.png
layout: provider
modified: '2026-07-05'
name: IDEXX
nav: Providers
network: true
overview: 'IDEXX publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Veterinary, Diagnostics, Reference Labs, Diagnostic Imaging, and Animal Health.


  IDEXX''s developer surface includes documentation and 6 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/idexx-labs/refs/heads/main/screenshots/idexx-labs-2026-07-25T222026.png
security:
- kind: domain-security
  name: Idexx Labs Domain Security
  slug: idexx-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Idexx Labs Trust Center
  slug: idexx-labs-trust-center
  summary_line: SOC 2, GDPR
slug: idexx-labs
tags:
- Veterinary
- Diagnostics
- Reference Labs
- Diagnostic Imaging
- Animal Health
- Healthcare
- VetConnect PLUS
- Web PACS
- Partner Gated
website: https://www.idexx.com
---
