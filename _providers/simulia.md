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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Industry-standard finite element analysis suite covering Abaqus/Standard, Abaqus/Explicit, Abaqus/CAE, Abaqus Multiphysics, CAD Associative Interface, Composites Modeler, and Czone. Automation and int
  name: SIMULIA Abaqus
  slug: abaqus
- description: '3D electromagnetic analysis software for antenna and filter design, EMC/EMI, bioelectromagnetics, electrical machines, and high-power thermal effects. Combines FIT, FEM, and integral-equation solvers '
  name: SIMULIA CST Studio Suite
  slug: cst-studio-suite
- description: Process automation and design optimization framework that chains simulation tools into workflows and runs Design of Experiments, optimization, and Six Sigma studies across SIMULIA and third-party solv
  name: SIMULIA Isight
  slug: isight
- description: Durability and fatigue analysis software for advanced multi-axial strain-based fatigue, integrated with Abaqus and other FEA solvers for life prediction of metals, composites, and elastomers.
  name: SIMULIA fe-safe
  slug: fe-safe
- description: Topology, shape, sizing, and bead optimization for structural and flow problems, layered on top of Abaqus and other commercial solvers.
  name: SIMULIA Tosca
  slug: tosca
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/simulia-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simulia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.3ds.com/products-services/simulia/
- group: other
  title: Dassault Systemes (parent company)
  type: Parent
  url: https://www.3ds.com/
- group: operate
  title: 3DEXPERIENCE / SIMULIA user communities
  type: Community
  url: https://community.3ds.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.3ds.com/HelpProductsDS.aspx
- group: learn
  title: ''
  type: Training
  url: https://www.3ds.com/products-services/simulia/training/
- group: operate
  title: ''
  type: Support
  url: https://www.3ds.com/support/
- group: other
  title: ''
  type: Events
  url: https://www.3ds.com/events/
- group: other
  title: ''
  type: ChampionsProgram
  url: https://www.3ds.com/products-services/simulia/champions/
created: '2026-05-23'
description: SIMULIA is Dassault Systemes' multidisciplinary simulation portfolio for evaluating product performance, reliability, and safety before physical prototyping. The product family includes Abaqus (nonlinear FEA), CST Studio Suite (electromagnetics), Isight (process automation and design optimization), fe-safe (durability), Tosca (topology and shape optimization), and additional structural, CFD, multibody, and vibro-acoustics solvers, integrated on the 3DEXPERIENCE platform. Programmatic access is delivered through scripting interfaces (Python for Abaqus, Visual Basic / macros for CST, Java/JavaScript for Isight) rather than a public web API.
finops:
- name: Simulia Finops
  service_category: API
  slug: simulia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simulia.png
layout: provider
modified: '2026-05-23'
name: SIMULIA (Dassault Systemes)
nav: Providers
network: true
overview: 'SIMULIA (Dassault Systemes) publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Simulation, FEA, CFD, Electromagnetics, and Optimization.


  SIMULIA (Dassault Systemes)''s developer surface includes documentation, training material, support, and 7 more developer resources.'
plans:
- name: Simulia Plans Pricing
  plan_count: 1
  slug: simulia-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 2
  name: Simulia Rate Limits
  slug: simulia-rate-limits
score:
  band: emerging
  composite: 20.1
  delta: -2.6
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simulia/refs/heads/main/screenshots/simulia-2026-06-20T193942.png
security:
- kind: domain-security
  name: Simulia Domain Security
  slug: simulia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Simulia Trust Center
  slug: simulia-trust-center
  summary_line: ISO 27001, GDPR
slug: simulia
tags:
- Simulation
- FEA
- CFD
- Electromagnetics
- Optimization
- Engineering
- Dassault Systemes
- 3DEXPERIENCE
website: https://www.3ds.com/products-services/simulia/
---
