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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: AMETEK provides advanced electronic instruments and electromechanical devices for energy, aerospace, power, research, medical, and industrial markets. The company does not currently publish a public d
  name: AMETEK Website
  slug: website
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ametek-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.ametek.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ametek.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ametek.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.ametek.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ametek-inc-
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
modified: '2026-04-19'
name: AMETEK
nav: Providers
network: true
overview: 'AMETEK publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Electronic Instruments, Test and Measurement, Aerospace, Energy, and Industrial.


  The AMETEK catalog on APIs.io includes 1 JSON-LD context.


  AMETEK''s developer surface includes developer portal, support, YouTube channel, and 5 more developer resources.'
plans:
- name: Ametek Plans Pricing
  plan_count: 1
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
- limit_count: 1
  name: Ametek Rate Limits
  slug: ametek-rate-limits
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 60.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 18.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ametek/refs/heads/main/screenshots/ametek-2026-06-20T171929.png
security:
- kind: domain-security
  name: Ametek Domain Security
  slug: ametek-domain-security
  summary_line: TLSv1.3 · DMARC
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
website: https://www.ametek.com
---
