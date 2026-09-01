---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Amkor Technology provides outsourced semiconductor packaging and test services for chip manufacturers worldwide. The company does not currently publish a public developer API.
  name: Amkor Technology Website
  slug: website
artifact_total: 22
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amkor-technology-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.amkor.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amkor.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amkor.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.amkor.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amkor-technology
- group: other
  title: ''
  type: X
  url: https://twitter.com/AmkorTech
created: '2024-01-01'
description: Amkor Technology is the world's largest US-based provider of outsourced semiconductor packaging and test services (OSAT), serving integrated device manufacturers, fabless semiconductor companies, and contract foundries. The company offers advanced packaging technologies including flip chip, wafer-level packaging, 2.5D/3D TSV, System-in-Package, and chiplet integration solutions for AI, automotive, communications, computing, consumer electronics, industrial, IoT, and networking markets.
features:
- description: Advanced laminate packages including CABGA, FBGA, fcCSP, FlipStack CSP, and interposer solutions for high-performance semiconductor devices.
  name: Laminate Packaging
- description: Leadframe-based packages including LQFP, TQFP, SOIC, SSOP, and fcMLF for cost-optimized semiconductor packaging.
  name: Leadframe Packaging
- description: WLCSP and WL3D wafer-level packaging for compact, high-performance semiconductor packages with minimal form factor.
  name: Wafer-Level Packaging
- description: Through-silicon via (TSV) technology for 2.5D and 3D stacked die configurations enabling high-bandwidth interconnects for AI and HPC applications.
  name: Advanced 2.5D and 3D Packaging
- description: SiP integration combining multiple chips, passives, and sensors into a single package for IoT, wearables, and complex electronic systems.
  name: System-in-Package
- description: Proprietary S-Connect and S-SWIFT technologies for advanced chiplet integration enabling heterogeneous integration of multiple die from different foundries.
  name: Chiplet Integration
- description: Power semiconductor packages including D2PAK, DPAK, PowerCSP, and PQFN for power management and motor control applications.
  name: Power Discrete Packaging
- description: Specialized packaging for MEMS, image sensors, memory modules, and other sensor devices requiring precision assembly.
  name: Memory and Sensor Packaging
- description: Comprehensive semiconductor test services including wafer test, final test, and burn-in for quality assurance and yield optimization.
  name: Semiconductor Testing
finops:
- name: Amkor Technology Finops
  service_category: API
  slug: amkor-technology-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amkor-technology.png
integrations:
- description: Collaboration with leading semiconductor foundries including TSMC, Samsung, and GlobalFoundries for seamless wafer-to-package supply chain integration.
  name: Foundry Partners
- description: Integration with electronic design automation tools for package design, thermal simulation, and signal integrity analysis.
  name: EDA Tool Providers
layout: provider
modified: '2026-04-19'
name: Amkor Technology
nav: Providers
network: true
overview: 'Amkor Technology publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Semiconductor Packaging, OSAT, Test Services, Advanced Packaging, and Chiplets.


  Amkor Technology''s developer surface includes developer portal, support, and 5 more developer resources.'
plans:
- name: Amkor Technology Plans Pricing
  plan_count: 3
  slug: amkor-technology-plans-pricing
press:
- date: '2026-05-25'
  title: Amkor Technology Expands U.S. Advanced Packaging ...
  url: https://ir.amkor.com/news-releases/news-release-details/amkor-technology-expands-us-advanced-packaging-footprint
- date: '2026-05-25'
  title: 'Amkor Technology: Semiconductor Packaging & Test Services'
  url: https://amkor.com/
- date: '2026-05-25'
  title: Amkor Technology, Inc.
  url: https://www.facebook.com/AmkorTechnology/posts/final-preparations-are-underway-for-amkors-investor-day-in-new-york-cityour-firs/1406416311514303/
- date: '2026-05-25'
  title: Amkor Technology to Host 2026 Investor Day and Ring ...
  url: https://www.businesswire.com/news/home/20260521361298/en/Amkor-Technology-to-Host-2026-Investor-Day-and-Ring-Nasdaq-Closing-Bell
- date: '2026-05-25'
  title: Amkor Technology to Present at the Morgan Stanley ...
  url: https://ir.amkor.com/news-releases/news-release-details/amkor-technology-present-morgan-stanley-technology-media-0
random_paper: 8
rate_limits:
- limit_count: 5
  name: Amkor Technology Rate Limits
  slug: amkor-technology-rate-limits
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 15.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amkor-technology/refs/heads/main/screenshots/amkor-technology-2026-06-20T171936.png
security:
- kind: domain-security
  name: Amkor Technology Domain Security
  slug: amkor-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amkor-technology
tags:
- Semiconductor Packaging
- OSAT
- Test Services
- Advanced Packaging
- Chiplets
- Automotive
- Artificial Intelligence
- Electronics Manufacturing
- Fortune 1000
use_cases:
- description: Advanced 2.5D/3D packaging and chiplet integration for AI accelerators, data center GPUs, and high-performance computing applications.
  name: AI and High-Performance Computing
- description: Automotive-grade semiconductor packaging for ADAS, electrification, infotainment, and powertrain control modules meeting AEC-Q100 standards.
  name: Automotive Electronics
- description: RF and mmWave packaging solutions for 5G base stations, smartphones, and infrastructure equipment requiring high-frequency performance.
  name: 5G Communications
- description: Cost-optimized packaging for smartphones, tablets, wearables, and consumer devices with compact form factors and high integration.
  name: Consumer Electronics
- description: Robust semiconductor packages for industrial automation, sensors, and IoT devices requiring wide operating temperature ranges.
  name: Industrial and IoT
- description: DRAM, NAND flash, and memory module packaging for storage and memory applications in enterprise and consumer markets.
  name: Memory Packaging
website: https://www.amkor.com
---
