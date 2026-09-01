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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
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
modified: '2026-07-25'
name: Color Health
nav: Providers
network: true
overview: Color Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Genomics, Genetic Testing, Precision Health, and Population Health.
random_paper: 13
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/color-genomics/refs/heads/main/screenshots/color-genomics-2026-07-25T210055.png
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
