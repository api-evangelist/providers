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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-18'
api_count: 0
artifact_total: 15
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/belden/refs/heads/main/security/belden-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/belden-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beldeninc
- group: company
  title: ''
  type: Website
  url: https://www.belden.com
- group: docs
  title: Hirschmann Product Documentation
  type: Documentation
  url: https://www.doc.hirschmann.com/
- group: operate
  title: Hirschmann Technical Support
  type: Support
  url: https://hirschmann-support.belden.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/belden/refs/heads/main/security/belden-vulnerability-disclosure.yml
  title: Belden PSIRT vulnerability disclosure
  type: Security
  url: security/belden-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/belden/refs/heads/main/security/belden-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/belden-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Blog
  url: https://www.belden.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.belden.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.belden.com/privacy-policy/terms-of-use
coverage:
  checked: '2026-09-18'
  detail: Belden's programmable surfaces are on-device (Hirschmann HiOS CLI/SNMP/OPC UA, Lumberg LioN-X IO-Link masters) and are documented only as 644 PDF manuals on www.doc.hirschmann.com; no OpenAPI, YANG, WSDL or other spec file is served on any Belden host, the Belden Horizon console at belden.io is login-only with no published API, and www.belden.com itself sits behind a Cloudflare managed challenge for crawlers.
  evidence:
  - status: 200
    url: https://www.doc.hirschmann.com/
  - status: 404
    url: https://www.doc.hirschmann.com/openapi.json
  - status: 301
    url: https://www.belden.io/
  - status: 404
    url: https://www.belden.io/openapi.json
  - status: 403
    url: https://www.belden.com/products/industrial-networking-cybersecurity/software-solutions/device-software/hios-switch-software
  reason: pdf-only-docs
  state: unreadable
created: '2026-03-23'
description: Belden Inc. designs, manufactures, and markets networking, connectivity, and cable products and solutions for industrial automation, smart buildings, and broadcast markets. The company delivers end-to-end signal transmission solutions for mission-critical applications, including industrial Ethernet infrastructure, cybersecurity, and IIoT connectivity. Belden's Hirschmann brand is a leading provider of industrial network switches and management software with CLI, SNMP, and REST API interfaces for network device management.
features:
- description: End-to-end industrial Ethernet infrastructure including managed switches, routers, and network access controllers for factory automation, process control, and critical infrastructure environments.
  name: Industrial Ethernet Networking
- description: IO-Link masters with direct IIoT communication protocols including OPC UA, MQTT, CoAP, and REST API for cloud-to-sensor connectivity in Industry 4.0 deployments.
  name: IIoT Connectivity
- description: Industrial HiVision network management system for configuration, monitoring, and management of SNMP-enabled devices across multi-vendor industrial networks.
  name: Network Management Software
- description: Industrial cybersecurity products and solutions including firewalls, intrusion detection, and secure remote access for operational technology (OT) networks.
  name: Cybersecurity Solutions
- description: High-performance cable and connectivity products for broadcast, industrial, and enterprise signal transmission applications, including fiber optic and copper solutions.
  name: Signal Transmission
- description: SPE technology with Time Sensitive Networking (TSN) capability and Power over Data Lines (PoDL) for lightweight, low-EMI connectivity to field devices with up to 1000-meter reach.
  name: Single Pair Ethernet
- description: Hirschmann industrial switches support command-line interface (CLI), SNMP, and REST API management interfaces for programmatic device configuration and monitoring via HiOS software.
  name: Hirschmann CLI and SNMP
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/belden.png
jsonld:
- class_count: 4
  name: Belden Context
  property_count: 36
  slug: belden-context
layout: provider
modified: '2026-09-18'
name: Belden
nav: Providers
network: true
overview: 'Belden is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Broadcast, Cable, Connectivity, Industrial Automation, and Industrial Ethernet.


  The Belden catalog on APIs.io includes 1 JSON-LD context.


  Belden''s developer surface includes documentation, support, engineering blog, and 7 more developer resources.'
press:
- date: '2026-05-25'
  title: Belden Inc. - Financials - Quarterly Results
  url: https://investor.belden.com/financials/quarterly-results/default.aspx
- date: '2026-05-25'
  title: Belden honors InUse with second annual Joseph C. ...
  url: https://www.businesswire.com/news/home/20250619566500/en/Belden-honors-InUse-with-second-annual-Joseph-C.-Belden-Innovation-Award
- date: '2026-05-25'
  title: AI-driven data centers build the backbone of our digital future
  url: https://www.belden.com/blog/ai-driven-data-centers-build-the-backbone-of-our-digital-future
- date: '2026-05-25'
  title: Belden to buy RUCKUS Networks for $1.85B | BDC 8-K Filing
  url: https://www.stocktitan.net/sec-filings/BDC/8-k-belden-inc-reports-material-event-0c4fa99e9907.html
- date: '2026-05-25'
  title: Belden earnings up next as investors eye Physical AI push
  url: https://www.investing.com/news/earnings/belden-earnings-up-next-as-investors-eye-physical-ai-push-93CH-4500853
random_paper: 2
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 10.5
  previous_composite: 9.6
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/belden/refs/heads/main/screenshots/belden-2026-06-20T173137.png
security:
- kind: domain-security
  name: Belden Domain Security
  slug: belden-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Belden Vulnerability Disclosure
  slug: belden-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: belden
tags:
- Broadcast
- Cable
- Connectivity
- Industrial Automation
- Industrial Ethernet
- IIoT
- Networking
- Signal Transmission
- Smart Buildings
- Fortune 1000
use_cases:
- description: Deploy ruggedized industrial Ethernet infrastructure to connect PLCs, sensors, and control systems in manufacturing plants and process facilities.
  name: Industrial Automation Networking
- description: Connect field-level sensors and actuators to cloud and enterprise systems using IO-Link masters with OPC UA, MQTT, and REST API protocols.
  name: IIoT Device Integration
- description: Build converged network infrastructure for building automation, security, lighting, and HVAC control systems using Belden structured cabling and active networking products.
  name: Smart Building Networks
- description: Deploy broadcast-grade signal distribution and connectivity solutions for live production, post-production, and media transport workflows.
  name: Broadcast Infrastructure
- description: Protect operational technology networks with industrial firewalls, secure remote access, and network segmentation solutions designed for OT environments.
  name: OT Network Security
website: https://www.belden.com
---
