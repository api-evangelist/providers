---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: 'AMETEK provides advanced electronic instruments and electromechanical devices for energy, aerospace, power, research, medical, and industrial markets. The corporate site is not a developer surface: th'
  name: AMETEK Website
  slug: website
- baseURL: http://{device_host}:{port}/api/v1
  baseurl_source: declared
  description: Read-only REST API embedded in the AMETEK Powervar iSite PRO network management card, the adapter fitted to Powervar UPS systems for secure remote monitoring. Three GET operations over HTTP or HTTPS r
  name: AMETEK Powervar iSite PRO REST API
  slug: powervar-isite-pro
- description: The public API reference for Crank Storyboard, the embedded graphical-interface development platform AMETEK acquired with Crank Software. Nine documented API families across 313 server-rendered, versi
  name: Crank Storyboard APIs
  slug: crank-storyboard
artifact_total: 24
common:
- group: company
  title: ''
  type: Website
  url: https://www.ametek.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ametek-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ametek-domain-security.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/ametek-powervar-isite-pro-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ametek-powervar-isite-pro-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ametek-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ametek-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ametek-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ametek-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/ametek-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ametek-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ametek-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ametek-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ametek-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ametek-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/ametek-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ametek-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ametek-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ametek-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ametek-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crank-software
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cranksoftware.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cranksoftware.com/docs/9.0/category/storyboard-apis
- group: company
  title: ''
  type: Blog
  url: https://www.ametek.com/newsroom
- group: company
  title: ''
  type: Careers
  url: https://www.ametek.com/careers
- group: start
  title: ''
  type: Portal
  url: https://www.ametek.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ametek.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ametek.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.ametek.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ametek
- group: other
  title: ''
  type: X
  url: https://twitter.com/AMETEKInc
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/ametek
created: '2024-01-01'
description: 'AMETEK is a leading global manufacturer of electronic instruments and electromechanical devices with annual sales of over $6 billion. The company operates through two differentiated business segments: Electronic Instruments Group (EIG) and Electromechanical Group (EMG), serving industries including energy, aerospace, power, medical, research, and industrial markets with advanced analytical, test and measurement instrumentation, and precision motion control solutions.'
features:
- description: Advanced analytical, test and measurement instrumentation for energy, aerospace, power, research, medical, and industrial markets worldwide.
  name: Electronic Instruments Group
- description: Automation and precision motion control solutions, highly engineered electrical interconnects, specialty metals, and thermal management systems.
  name: Electromechanical Group
- description: Complex energy management solutions for data center operators including real-time simulation technology for power systems risk management.
  name: Data Center Power Management
- description: High-performance motors, drives, and motion control systems for aerospace, defense, medical, and industrial automation applications.
  name: Precision Motion Control
- description: Specialty metals, engineered materials, and thermal management components for demanding applications in aerospace, defense, and industrial markets.
  name: Advanced Materials
- description: Precision instruments for measuring electrical, physical, and chemical properties in laboratory, industrial, and field environments.
  name: Test and Measurement Instruments
- description: Real-time process monitoring and control instrumentation for energy production, chemical processing, and manufacturing industries.
  name: Process Monitoring and Control
finops:
- name: Ametek Finops
  service_category: Electronic Instruments
  slug: ametek-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ametek.png
integrations:
- description: Integrated supplier to major aerospace and defense OEMs providing precision components and subsystems for aircraft and defense systems.
  name: Aerospace and Defense Supply Chain
- description: Solutions integrated with oil and gas, power generation, and utilities for real-time process monitoring and control.
  name: Energy Industry Partners
jsonld:
- class_count: 18
  name: Ametek Context
  property_count: 21
  slug: ametek-context
layout: provider
modified: '2026-09-02'
name: AMETEK
nav: Providers
network: true
overview: 'AMETEK publishes 1 API on the [APIs.io](https://apis.io/) network: Powervar iSite PRO REST API. Tagged areas include Electronic Instruments, Test and Measurement, Aerospace, Energy, and Industrial.


  The AMETEK catalog on APIs.io includes 1 JSON-LD context.


  AMETEK''s developer surface includes authentication, changelog, documentation, API reference, engineering blog, developer portal, support, and 26 more developer resources.'
plans:
- name: Ametek Plans Pricing
  plan_count: 0
  slug: ametek-plans-pricing
press:
- date: '2026-05-25'
  title: AMETEK Announces Record First Quarter 2026 Results ...
  url: https://www.prnewswire.com/news-releases/ametek-announces-record-first-quarter-2026-results-and-raises-full-year-guidance-302757938.html
- date: '2026-05-25'
  title: Looking Toward the Future of Deep Learning
  url: https://www.ametekaegis.com/resources/blog/2019/december/looking-toward-the-future-of-deep-learning
- date: '2026-05-25'
  title: News
  url: https://virtekvision.com/blogs/news
- date: '2026-05-25'
  title: AMETEK Expands Ultra Precision Technologies Division ...
  url: https://metrology.news/ametek-expands-ultra-precision-technologies-division-with-completion-of-faro-acquisition-completion/
- date: '2026-05-25'
  title: Enabling Artificial Intelligence through advanced ...
  url: https://www.ametek.com/our-stories/stories/innovation/2023/august/ametek-enabling-ai
random_paper: 1
rate_limits:
- limit_count: 0
  name: Ametek Rate Limits
  slug: ametek-rate-limits
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 49.0
    catalog_earned_first_party: 0.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 20.7
    developer_ergonomics: 49.4
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 32.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 28.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ametek/refs/heads/main/screenshots/ametek-2026-06-20T171929.png
security:
- kind: authentication
  name: Ametek Authentication
  slug: ametek-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ametek Domain Security
  slug: ametek-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ametek
tags:
- Electronic Instruments
- Test and Measurement
- Aerospace
- Energy
- Industrial
- Medical Instruments
- Precision Motion Control
- Manufacturing
- Fortune 1000
use_cases:
- description: Test and measurement instrumentation for aerospace and defense component and system validation across critical performance parameters.
  name: Aerospace and Defense Testing
- description: Process monitoring and analytical instrumentation for oil and gas, power generation, and renewable energy applications.
  name: Energy Industry Monitoring
- description: Precision motion control and specialized components supporting medical device manufacturers and healthcare equipment applications.
  name: Medical Device Manufacturing
- description: Electromechanical devices and precision motion control for factory automation, robotics, and industrial process control.
  name: Industrial Automation
- description: Advanced analytical instruments for scientific research, quality control, and materials characterization in laboratory environments.
  name: Research and Laboratory Analysis
- description: Power management and monitoring solutions for data center operators managing complex energy and thermal challenges.
  name: Data Center Infrastructure
website: https://www.ametek.com/
---
