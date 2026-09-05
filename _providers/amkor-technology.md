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
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Amkor Technology provides outsourced semiconductor packaging and test services for chip manufacturers worldwide. The company does not currently publish a public developer API.
  name: Amkor Technology Website
  slug: website
- description: Amkor's centralized B2B infrastructure for exchanging manufacturing information between its factories, sales teams and customers. Delivery protocols published by Amkor are RosettaNet RNIF, FTP/SFTP, E
  name: Amkor B2B Integration Services
  slug: b2b-integration
artifact_total: 23
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amkor-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amkor.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amkor.com/privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amkor.com/legal/
- group: operate
  title: ''
  type: Support
  url: https://amkor.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://amkor.com/blog/
- group: design
  title: ''
  type: Conformance
  url: conformance/amkor-technology-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/amkor-technology-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amkor-technology-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/amkor-technology-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amkor-technology-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amkor-technology
- group: other
  title: ''
  type: X
  url: https://twitter.com/AmkorTech
coverage:
  checked: '2026-09-02'
  detail: Amkor publishes no web API at all; its only machine-to-machine surface is the B2B Integration Services stack (RosettaNet/EDI/AS2/SFTP/SOAP) whose endpoints, WSDLs and PIP numbers are issued only under a commercial agreement, and the one live application host, api.amkor.com, answers 403 from an Imperva/Incapsula edge to every anonymous request including the site root.
  evidence:
  - status: 403
    url: https://api.amkor.com/
  - status: 200
    url: https://amkor.com/b2b-integration-services-solutions/
  - status: 404
    url: https://amkor.com/openapi.json
  - status: 404
    url: https://amkor.com/.well-known/agent-card.json
  reason: partner-login
  state: gated
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
modified: '2026-09-02'
name: Amkor Technology
nav: Providers
network: true
overview: 'Amkor Technology publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Semiconductor Packaging, OSAT, Test Services, Advanced Packaging, and Chiplets.


  Amkor Technology''s developer surface includes support, engineering blog, and 11 more developer resources.'
plans:
- name: Amkor Technology Plans Pricing
  plan_count: 0
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
- limit_count: 0
  name: Amkor Technology Rate Limits
  slug: amkor-technology-rate-limits
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 15.8
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
website: https://amkor.com
---
