---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.laranetworks.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.infineon.com/about/company?site=www.laranetworks.com — a different registrable domain (laranetworks.com -> infineon.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lara-networks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.laranetworks.com
- group: other
  title: ''
  type: Successor
  url: https://www.infineon.com
created: '2026-07-17'
description: 'Lara Networks, Inc. (founded as Lara Technology) was a fabless semiconductor company headquartered at 110 Nortech Parkway, San Jose, California, that architected, designed, and marketed silicon-based packet-processing solutions for high-speed Internet and networking infrastructure. Its products were built on a patent-pending Associative Processing Technology (APT) and manufactured on 0.18-micron process technology: Network Database Search Engine (NDSE) devices, network coprocessors, and NDSE subsystems, with Content-Aware Switching (CAS) solutions in development. The devices were content-addressable memory search engines that offloaded ultra-large table lookups from network processors — holding tables of more than three million addresses and sustaining over 100 million lookups per second so switches and routers could process packets from Layer 2 to Layer 7 at full line rate at OC-48 (2.5Gbps) and above. The company raised a $40 million second round in October 2000 led by Raza
  Ventures with Battery Ventures, InveStar Capital, and TeleSoft Venture Partners, alongside a long-term co-development agreement and minority equity investment from STMicroelectronics. Lara Networks no longer operates independently: by January 2003 its laranetworks.com domain served Cypress Semiconductor Corporation content, and today every path on the domain 301-redirects to Infineon Technologies, which acquired Cypress in April 2020. As a fabless chip company selling silicon to network equipment manufacturers, Lara Networks never operated a web or developer API program, and no public API surface exists to enrich. This profile is retained as an acquired-company lead.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lara-networks.png
layout: provider
modified: '2026-07-19'
name: Lara Networks
nav: Providers
network: true
overview: Lara Networks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Networking, Packet Processing, and Content Addressable Memory.
random_paper: 10
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lara-networks/refs/heads/main/screenshots/lara-networks-2026-07-25T224534.png
security:
- kind: domain-security
  name: Lara Networks Domain Security
  slug: lara-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lara-networks
tags:
- Company
- Semiconductors
- Networking
- Packet Processing
- Content Addressable Memory
- Network Search Engine
- Internet Infrastructure
- Fabless
- Hardtech
- Acquired
website: https://www.laranetworks.com
---
