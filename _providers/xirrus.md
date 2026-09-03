---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.xirrus.com/'', ''status'': 302, ''note'': ''declared website redirects to https://www.cambiumnetworks.com/products/wifi/ — a different registrable domain (xirrus.com -> cambiumnetworks.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: company
  title: ''
  type: Website
  url: https://www.xirrus.com/
- group: build
  title: ''
  type: Packages
  url: packages/xirrus-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xirrus-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xirrus-llms.txt
created: '2026-07-17'
description: Xirrus was an enterprise Wi-Fi company that made high-density wireless access points and arrays managed through the Xirrus Management System (XMS), which exposed a management API that community client libraries were built against. Backed by Canaan Partners, Xirrus was acquired by Riverbed Technology in April 2017 to power cloud-managed Wi-Fi in SteelConnect, and Riverbed sold the Xirrus Wi-Fi business to Cambium Networks in 2019. The Xirrus brand has since been absorbed into Cambium Networks' enterprise Wi-Fi portfolio, and xirrus.com now redirects to cambiumnetworks.com, leaving no independent Xirrus API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xirrus.png
layout: provider
modified: '2026-07-21'
name: Xirrus
nav: Providers
network: true
overview: Xirrus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wi-Fi, Wireless, Networking, and Access Points.
random_paper: 13
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 5
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xirrus/refs/heads/main/screenshots/xirrus-2026-09-02T171137.png
security:
- kind: domain-security
  name: Xirrus Domain Security
  slug: xirrus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: xirrus
tags:
- Company
- Wi-Fi
- Wireless
- Networking
- Access Points
- Network Management
- Enterprise
website: https://www.xirrus.com/
---
