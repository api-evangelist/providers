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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 5
apis:
- description: Modeled surface for placing and tracking genetic test orders and sample-collection kits within a Color population health program - creating an order for a participant, assigning and shipping a kit, an
  name: Color Orders & Kits API (Modeled)
  slug: color-orders-kits-api
- description: Modeled surface for retrieving clinical genetic test results and reports (hereditary cancer, cardiovascular, pharmacogenomics) for participants in a program. In practice, results delivery to health sy
  name: Color Results API (Modeled)
  slug: color-results-api
- description: Modeled surface for enrolling and managing the members/participants of an employer, union, or public-health population - eligibility, enrollment status, demographics, and consent. Not a public API; me
  name: Color Members & Participants API (Modeled)
  slug: color-members-participants-api
- description: 'Modeled surface for configuring and reporting on population health programs - cancer early detection and screening campaigns, risk-based care pathways, and aggregate program engagement/outcomes for a '
  name: Color Programs API (Modeled)
  slug: color-programs-api
- description: Modeled surface for exchanging clinical data (observations, diagnostic reports, care-gap and screening status) between Color and a health system's EHR. Real-world exchange uses FHIR/HL7 through intero
  name: Color Clinical Data API (Modeled)
  slug: color-clinical-data-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/color-genomics-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/color-genomics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.color.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/color
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/color
- group: other
  title: ''
  type: Interoperability
  url: https://www.redoxengine.com/healthcare-product/color/
created: '2026-07-05'
description: Color Health (founded as Color Genomics in 2015) is a population health technology company that operates a nationwide, oncologist-led Virtual Cancer Clinic and delivers population-scale precision health programs - hereditary cancer and cardiovascular genetic testing, pharmacogenomics, cancer early detection and screening, and clinical care management - for employers, unions, health plans, governments, and public health institutions. Color does NOT publish a public, self-service developer API. Access to its platform is enterprise/partner-gated and contracted directly with organizations; data exchange with health systems and EHRs is handled through interoperability partners (e.g. Redox) using FHIR/HL7 rather than an open developer portal. The APIs listed here are logical, honestly-modeled surfaces (endpointsModeled) that describe how such a program is typically integrated - they are not confirmed public endpoints.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/color-genomics.png
layout: provider
modified: '2026-07-05'
name: Color Health
nav: Providers
network: true
overview: Color Health publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Genomics, Genetic Testing, Precision Health, and Population Health.
random_paper: 13
score:
  band: minimal
  composite: 13.0
  delta: 2.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.0
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Color Genomics Domain Security
  slug: color-genomics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Color Genomics Trust Center
  slug: color-genomics-trust-center
  summary_line: SOC 2, HIPAA, CSA STAR
slug: color-genomics
tags:
- Health
- Genomics
- Genetic Testing
- Precision Health
- Population Health
- Cancer Screening
- Clinical
- Enterprise
- Gated
website: https://www.color.com/
---
