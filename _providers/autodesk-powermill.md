---
access_model:
  confidence: high
  label: Contact sales · 30-day free trial
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.autodesk.com/products/powermill/buy
  - plans/autodesk-powermill-plans-pricing.yml
  trial: true
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.8
  scored_at: '2026-10-03'
api_count: 2
apis:
- description: The PowerMill Macro API provides an automation interface using macro commands to control PowerMill operations and workflows for CNC machining automation. Macros can automate repetitive toolpath genera
  name: PowerMill Macro API
  slug: powermill-macro-api
- description: The PowerMill .NET and COM API provides an object model for integrating PowerMill with Windows applications, ERP systems, and manufacturing execution systems. Enables external applications to drive Po
  name: PowerMill .NET / COM API
  slug: powermill-dotnet-com-api
artifact_total: 24
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autodesk-powermill/refs/heads/main/security/autodesk-powermill-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autodesk-powermill-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.autodesk.com/products/powermill/overview
- group: docs
  title: ''
  type: Documentation
  url: https://help.autodesk.com/view/PWRM/2026/ENU/
- group: start
  title: ''
  type: Portal
  url: https://www.autodesk.com/developer-network
- group: operate
  title: ''
  type: Support
  url: https://www.autodesk.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.autodesk.com/company/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.autodesk.com/company/legal-notices-trademarks/privacy-statement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Autodesk
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Autodesk/PowerShapeAndPowerMillAPI
- group: docs
  title: ''
  type: APIReference
  url: https://damassets.autodesk.net/content/dam/autodesk/external-assets/support-articles/powermill-2024-offline-help-and-macros-and-plugin-documentation/pm-macro-programming-guide.pdf
- group: commercial
  title: ''
  type: Pricing
  url: https://www.autodesk.com/products/powermill/buy
- group: start
  title: ''
  type: SignUp
  url: https://accounts.autodesk.com/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/autodesk-powermill/refs/heads/main/packages/autodesk-powermill-packages.yml
  title: ''
  type: Packages
  url: packages/autodesk-powermill-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/autodesk-powermill/refs/heads/main/packages/autodesk-powermill-packages.yml
  title: ''
  type: SDKs
  url: packages/autodesk-powermill-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autodesk-powermill/refs/heads/main/components/autodesk-powermill-components.yml
  title: ''
  type: Components
  url: components/autodesk-powermill-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autodesk-powermill/refs/heads/main/lifecycle/autodesk-powermill-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/autodesk-powermill-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://health.autodesk.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/autodesk-powermill/refs/heads/main/changelog/autodesk-powermill-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/autodesk-powermill-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autodesk-powermill/refs/heads/main/security/autodesk-powermill-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/autodesk-powermill-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/autodesk
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autodesk-powermill/refs/heads/main/security/autodesk-powermill-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/autodesk-powermill-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.autodesk.com/trust/compliance
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autodesk-powermill/refs/heads/main/conformance/autodesk-powermill-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autodesk-powermill-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/autodesk-powermill/refs/heads/main/llms/autodesk-powermill-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autodesk-powermill-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/autodesk-powermill/refs/heads/main/plans/autodesk-powermill-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autodesk-powermill-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/autodesk-powermill/refs/heads/main/rate-limits/autodesk-powermill-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/autodesk-powermill-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autodesk-powermill/refs/heads/main/vocabulary/autodesk-powermill-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/autodesk-powermill-vocabulary.yml
created: '2025-01-01'
description: Autodesk PowerMill is a leading CAM (Computer-Aided Manufacturing) software solution for high-speed and 5-axis CNC machining. It is used by aerospace, automotive, mold and die, and precision engineering industries to generate toolpaths for complex part manufacturing. PowerMill provides multiple programming interfaces including Macro scripts, Python API, and .NET/COM interfaces for automating manufacturing workflows, customizing toolpath generation, and integrating with broader manufacturing execution systems.
features:
- description: Optimized toolpath strategies for high-speed machining operations including trochoidal milling, constant Z, and rest machining for aerospace and automotive part manufacturing.
  name: High-Speed Machining
- description: Simultaneous 5-axis toolpath generation for complex sculptured surfaces, undercuts, and deep cavities in mold, die, and aerospace component manufacturing.
  name: 5-Axis Machining
- description: Record and replay macro scripts to automate repetitive CAM programming tasks, standardize manufacturing processes, and reduce programming time for similar part families.
  name: Macro Automation
- description: Python API for programmatic control of toolpath generation, manufacturing data management, and integration with broader manufacturing software ecosystems.
  name: Python Scripting
- description: Full machine kinematics simulation to verify toolpaths, detect collisions, and validate CNC programs before cutting to prevent costly machine crashes and scrap parts.
  name: Machine Simulation
- description: Flexible post-processor framework for generating machine-specific G-code output for a wide variety of CNC machines and controllers.
  name: Post-Processor Support
finops:
- name: Autodesk Powermill Finops
  service_category: API
  slug: autodesk-powermill-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autodesk-powermill.png
integrations:
- description: Direct integration with Autodesk Inventor for importing CAD models and associative design-to-manufacturing workflows.
  name: Autodesk Inventor
- description: Integration with Autodesk Fusion for cloud-connected design and manufacturing workflows combining CAD and CAM capabilities.
  name: Autodesk Fusion
- description: COM/API-based integration with SAP and other ERP systems for production scheduling, work order management, and manufacturing data exchange.
  name: SAP and ERP Systems
- description: Neutral CAD file format support enabling data exchange with any CAD system via STEP and IGES file formats.
  name: STEP and IGES
jsonld:
- class_count: 7
  name: Autodesk Powermill Context
  property_count: 16
  slug: autodesk-powermill-context
layout: provider
modified: '2026-09-06'
name: Autodesk PowerMill
nav: Providers
network: true
overview: 'Autodesk PowerMill publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include 5-Axis Machining, CAM, CNC, Machining, and Manufacturing.


  The Autodesk PowerMill catalog on APIs.io includes 1 JSON-LD context.


  Autodesk PowerMill''s developer surface includes documentation, developer portal, support, API reference, pricing, signup flow, changelog, and 20 more developer resources.'
plans:
- name: Autodesk Powermill Plans Pricing
  plan_count: 2
  slug: autodesk-powermill-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Autodesk Powermill Rate Limits
  slug: autodesk-powermill-rate-limits
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 63.5
    catalog_earned_first_party: 8.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 89.5
    contract_governance: 13.6
    contract_quality: 21.2
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 44.7
  previous_composite: 46.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/autodesk-powermill/refs/heads/main/screenshots/autodesk-powermill-2026-06-20T172635.png
security:
- kind: domain-security
  name: Autodesk Powermill Domain Security
  slug: autodesk-powermill-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Autodesk Powermill Vulnerability Disclosure
  slug: autodesk-powermill-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Autodesk Powermill Trust Center
  slug: autodesk-powermill-trust-center
  summary_line: ISO/IEC 27001 Information Security Management, ISO/IEC 27017 (cloud security controls), ISO/IEC 27018 (cloud PII protection), ISO/IEC 27701 (privacy information management), SOC 2 attestation, SOC 3 (6-month and 12-month) attestation
slug: autodesk-powermill
tags:
- 5-Axis Machining
- CAM
- CNC
- Machining
- Manufacturing
- Aerospace
- Automotive
- Toolpath Generation
use_cases:
- description: Programming complex aerospace structural components, engine parts, and airframe components from titanium, aluminum, and composites with 5-axis machining strategies.
  name: Aerospace Part Machining
- description: Generating high-quality toolpaths for injection molds, die casting tools, and stamping dies with complex surface finishes and tight tolerances.
  name: Mold and Die Manufacturing
- description: Rapid prototyping and short-run production of automotive body panels, interior components, and powertrain parts using high-speed machining.
  name: Automotive Prototyping
- description: Automating CAM programming workflows using Python and macro APIs to reduce programming time for families of similar manufacturing parts.
  name: CAM Automation
- description: Integrating PowerMill with ERP and Manufacturing Execution Systems via .NET/COM APIs to automate production scheduling and manufacturing data exchange.
  name: ERP and MES Integration
website: https://www.autodesk.com/products/powermill/overview
---
