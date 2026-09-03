---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://ermetic.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.tenable.com/solutions/cloud-security — a different registrable domain (ermetic.com -> tenable.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/ermetic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ermetic.com/
- group: docs
  title: ''
  type: APIReference
  url: https://us.app.ermetic.com/docs/api/index
- group: company
  title: ''
  type: Blog
  url: https://ermetic.com/blog/
created: '2026-07-17'
description: Ermetic is a cloud security company founded in 2019 that pioneered cloud infrastructure entitlement management (CIEM) as part of a unified, identity-first cloud-native application protection platform (CNAPP) spanning AWS, Azure, and GCP. The platform provides full visibility into permissions and entitlements across multi-cloud environments, least-privilege and just-in-time access controls, anomaly detection against behavioral baselines, and compliance and cloud security posture management (CSPM). Ermetic raised roughly $100M from investors including Accel, Norwest Venture Partners, Glilot Capital Partners, and Target Global, and was acquired by Tenable in October 2023 for approximately $265M. The product now ships as Tenable Cloud Security; the ermetic.com domain redirects to Tenable, and the former Ermetic customer application (us.app.ermetic.com) exposes a login-gated REST API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ermetic.png
layout: provider
modified: '2026-07-19'
name: Ermetic
nav: Providers
network: true
overview: 'Ermetic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cloud Security, CIEM, and CNAPP.


  Ermetic''s developer surface includes API reference, engineering blog, and 2 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ermetic/refs/heads/main/screenshots/ermetic-2026-07-25T213610.png
security:
- kind: domain-security
  name: Ermetic Domain Security
  slug: ermetic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ermetic
tags:
- Company
- Security
- Cloud Security
- CIEM
- CNAPP
- Identity
- Entitlements
- Multi-Cloud
website: https://ermetic.com/
---
