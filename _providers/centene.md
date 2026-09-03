---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: 'The Centene FHIR Patient Access API lets members of Centene health plans access their clinical, financial, and formulary data through third-party applications, as required by the CMS Interoperability '
  name: Centene FHIR Patient Access API
  slug: centene-fhir-patient-access
- description: The Centene FHIR Provider Directory API exposes in-network provider information for Centene members and the public via HL7 FHIR PDEX Provider Directory resources.
  name: Centene FHIR Provider Directory API
  slug: centene-fhir-provider-directory
- description: The Provider RTR FHIR Payer Data Exchange (PDEX) Directory API delivers provider directory data between payers and authorized external partners using HL7 FHIR PDEX profiles.
  name: Centene Provider RTR - FHIR PDEX Directory API
  slug: centene-fhir-pdex-rtr
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/centene-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Centene
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/centene-corporation
- group: company
  title: ''
  type: Website
  url: https://www.centene.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partners.centene.com/
- group: other
  title: ''
  type: API Catalog
  url: https://partners.centene.com/apis
- group: other
  title: ''
  type: Application Developer
  url: https://partners.centene.com/applicationDeveloper
- group: other
  title: ''
  type: Interoperability
  url: https://www.superiorhealthplan.com/members/medicaid/resources/interoperability-and-patient-access/interoperability-for-developers.html
created: '2024-01-15'
description: Centene Corporation is a leading managed care organization providing government-sponsored healthcare programs including Medicaid, Medicare, and Health Insurance Marketplace plans. Centene operates a developer portal at partners.centene.com publishing FHIR-based interoperability APIs under the 21st Century Cures Act and CMS Interoperability and Patient Access Rule, including Patient Access, Provider Directory, and Provider RTR (Payer Data Exchange) APIs.
finops:
- name: Centene Finops
  service_category: Healthcare Interoperability
  slug: centene-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/centene.png
layout: provider
modified: '2026-04-23'
name: Centene
nav: Providers
network: true
overview: Centene publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CMS Interoperability, FHIR, Formulary, Healthcare, and Insurance.
plans:
- name: Centene Plans Pricing
  plan_count: 1
  slug: centene-plans-pricing
press:
- date: '2026-05-25'
  title: Centene Signs Definitive Agreement to Acquire Apixio
  url: https://www.prnewswire.com/news-releases/centene-signs-definitive-agreement-to-acquire-apixio-301168433.html
- date: '2026-05-25'
  title: Healthcare Innovation and Thought Leadership
  url: https://www.centene.com/why-were-different/corporate-sustainability/empowering-health/innovation-thought-leadership.html
- date: '2026-05-25'
  title: CENTENE CORPORATION REPORTS 2025 RESULTS ...
  url: https://www.prnewswire.com/news-releases/centene-corporation-reports-2025-results-and-announces-2026-guidance-302680998.html
- date: '2026-05-25'
  title: CENTENE CORPORATION WITHDRAWS 2025 GUIDANCE
  url: https://investors.centene.com/2025-07-01-CENTENE-CORPORATION-WITHDRAWS-2025-GUIDANCE
- date: '2026-05-25'
  title: Apixio Acquisition by Centene Corporation
  url: https://www.triple-tree.com/experience/apixio-centene-corporation/
random_paper: 3
rate_limits:
- limit_count: 3
  name: Centene Rate Limits
  slug: centene-rate-limits
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 10.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/centene/refs/heads/main/screenshots/centene-2026-06-20T174122.png
security:
- kind: domain-security
  name: Centene Domain Security
  slug: centene-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: centene
tags:
- CMS Interoperability
- FHIR
- Formulary
- Healthcare
- Insurance
- Interoperability
- Managed Care
- Patient Access
- Provider Directory
- Fortune 500
website: https://www.centene.com
---
