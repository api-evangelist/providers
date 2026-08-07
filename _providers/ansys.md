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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: 'Open-source Python ecosystem for Ansys products. The pyansys metapackage bundles 45+ libraries including PyMAPDL (Mechanical APDL), PyFluent (Fluent CFD), PyAEDT (Electronics Desktop / HFSS / Maxwell '
  name: PyAnsys
  slug: pyansys
- description: Ansys Cloud delivers on-demand HPC and Ansys product instances on Microsoft Azure for burst simulation workloads. Cloud access is gated through commercial entitlement and the Ansys Cloud portal; no pu
  name: Ansys Cloud
  slug: cloud
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ansys-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ansys.com
- group: other
  title: ''
  type: Products
  url: https://www.ansys.com/products
- group: other
  title: ''
  type: AllProducts
  url: https://www.ansys.com/products/all-products
- group: operate
  title: ''
  type: ReleaseHighlights
  url: https://www.ansys.com/products/release-highlights
- group: docs
  title: ''
  type: Documentation
  url: https://ansyshelp.ansys.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ansys.com
- group: other
  title: ''
  type: PyAnsys
  url: https://docs.pyansys.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ansys
- group: other
  title: ''
  type: AnsysCloud
  url: https://www.ansys.com/it-solutions/ansys-cloud
- group: learn
  title: ''
  type: AnsysLearningHub
  url: https://www.ansys.com/training-center/ansys-learning-hub
- group: other
  title: ''
  type: AnsysInnovationSpace
  url: https://innovationspace.ansys.com
- group: other
  title: ''
  type: Academic
  url: https://www.ansys.com/academic
- group: other
  title: ''
  type: AppStore
  url: https://catalog.ansys.com
- group: company
  title: ''
  type: Blog
  url: https://www.ansys.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ansys-inc
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/ansysinc
- group: operate
  title: ''
  type: Support
  url: https://www.ansys.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ansys.com/contact-us
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.ansys.com/legal/trust-center
created: '2026-05-23'
description: Ansys is a global engineering simulation company (now part of Synopsys) with a deep portfolio spanning structures (Mechanical, LS-DYNA, Motion), fluids (Fluent, CFX, Rocky), electronics (HFSS, Maxwell, SIwave, Icepak), semiconductors (RedHawk, Totem), optics, photonics, materials (Granta), 3D design (Discovery, SpaceClaim), embedded software (SCADE), and systems (optiSLang, Twin Builder). Ansys also runs Ansys Cloud for burst HPC and offers Ansys Apps in the Cloud. The primary public developer surface is PyAnsys — an open-source family of 45+ Python packages on GitHub (ansys/pyansys metapackage) that wrap individual Ansys products as Pythonic interfaces. There is no public web REST API portal; programmatic access is licensed per product and driven through PyAnsys, ACT (Ansys Customization Toolkit), product scripting (MAPDL, Fluent TUI/Scheme), and Ansys Cloud.
finops:
- name: Ansys Finops
  service_category: API
  slug: ansys-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ansys.png
layout: provider
modified: '2026-05-23'
name: Ansys
nav: Providers
network: true
overview: 'Ansys publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Simulation, Engineering, CAE, CFD, and FEA.


  Ansys'' developer surface includes documentation, GitHub presence, engineering blog, YouTube channel, support, pricing, and 14 more developer resources.'
plans:
- name: Ansys Plans Pricing
  plan_count: 1
  slug: ansys-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 2
  name: Ansys Rate Limits
  slug: ansys-rate-limits
score:
  band: emerging
  composite: 24.5
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ansys/refs/heads/main/screenshots/ansys-2026-06-20T172024.png
security:
- kind: domain-security
  name: Ansys Domain Security
  slug: ansys-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ansys
tags:
- Simulation
- Engineering
- CAE
- CFD
- FEA
- Electromagnetics
- Multiphysics
- Cloud
- Python
- SDK
website: https://www.ansys.com
---
