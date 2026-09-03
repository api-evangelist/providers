---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
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
  score: 5.4
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mobilion-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mobilionsystems.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MOBILionSystems
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/MOBILionSystems/MOBILion_MBI_SDK/blob/main/README.md
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/MOBILionSystems/MOBILion_MBI_SDK/tree/main/doc/html
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/MOBILionSystems/MOBILion_MBI_SDK/blob/main/README.md#quick-start
- group: company
  title: ''
  type: Blog
  url: https://www.mobilionsystems.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.mobilionsystems.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mobilionsystems.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/mobilion-systems-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mobilion-systems-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mobilion-systems-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mobilion-systems-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mobilion-systems-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mobilion-systems-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mobilion-systems-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/mobilion-systems-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mobilion-systems-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/mobilion-systems-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mobilion-systems-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/mobilion-systems-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mobilion-systems-rate-limits.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/MOBILionSystems/MOBILion_MBI_SDK/blob/main/LICENSE.md
created: '2026-08-25'
description: 'MOBILion Systems is a separation-science instrument company founded in 2015 and headquartered in Chadds Ford, Pennsylvania. It is the exclusive commercial licensee of SLIM (Structures for Lossless Ion Manipulation) and builds MOBIE, a high-resolution ion mobility (HRIM) platform that couples a serpentine ~13-metre ion path to third-party mass spectrometers for glycan, lipid, peptide, PFAS, lipid-nanoparticle and biotherapeutic characterisation. Its developer surface is not a web API: the MOBIE EyeOn acquisition system writes an HDF5-backed proprietary MBI file, and MOBILion publishes a first-party native SDK for reading it — a C++ library for Windows and Linux with SWIG-generated Python bindings and a mixed-mode .NET wrapper, shipped with a full Doxygen API reference from the MOBILionSystems GitHub organization.'
image: https://cdn.prod.website-files.com/6243e199d7710bbc2ee76c7e/62632cea3d90665f5362efba_MOBILion%20LOGO%204.svg
layout: provider
modified: '2026-08-25'
name: MOBILion Systems
nav: Providers
network: true
overview: 'MOBILion Systems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Scientific Instruments, Mass Spectrometry, Ion Mobility, and Proteomics.


  MOBILion Systems'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, and 17 more developer resources.'
plans:
- name: Mobilion Systems Plans Pricing
  plan_count: 0
  slug: mobilion-systems-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Mobilion Systems Rate Limits
  slug: mobilion-systems-rate-limits
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 26.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mobilion-systems/refs/heads/main/screenshots/mobilion-systems-2026-09-02T150607.png
security:
- kind: domain-security
  name: Mobilion Systems Domain Security
  slug: mobilion-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mobilion-systems
tags:
- Company
- Scientific Instruments
- Mass Spectrometry
- Ion Mobility
- Proteomics
- Lipidomics
- Life Sciences
- Laboratory Software
- SDK
- File Format
website: https://www.mobilionsystems.com/
---
