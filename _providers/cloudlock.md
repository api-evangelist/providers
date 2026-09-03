---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://www.cloudlock.com/'', ''status'': 301, ''note'': ''declared website redirects to https://umbrella.cisco.com/products/cloud-access-security-broker-casb — a different registrable domain (cloudlock.com -> cisco.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: company
  title: ''
  type: Website
  url: https://www.cloudlock.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cisco.com/docs/cloud-security/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.umbrella.com/cloudlock-documentation/docs/cisco-cloudlock-apis
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cisco.com/docs/cloud-security/cloudlock-api-getting-started/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cisco.com/docs/cloud-security/cloudlock-api-getting-started/
- group: company
  title: ''
  type: Blog
  url: https://www.cloudlock.com/blog/
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudlock-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloudlock-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloudlock-problem-types.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudlock-domain-security.yml
created: '2026-07-17'
description: CloudLock is a cloud-native Cloud Access Security Broker (CASB) that protects data, users, and applications across SaaS, IaaS, PaaS, and IDaaS environments. Founded in 2011 and acquired by Cisco in 2016, it is now delivered as Cisco Cloudlock within Cisco Umbrella / Cisco Security Cloud. The platform uses an API-driven model to discover sensitive content, detect policy violations, flag anomalous user behavior, and manage cloud application (OAuth) risk. Developers integrate through the Cisco Cloudlock API (v2), a Bearer-token REST API exposing activities, incidents, incident entities, incident aggregates, policies, apps, entities, IP libraries, and anomalies. Originally a portfolio company of Bessemer Venture Partners, CloudLock's developer surface is documented on Cisco DevNet and the Cisco Umbrella documentation hub.
image: https://cdn.umbrella.marketops.umbrella.com/wp-content/uploads/2022/03/22160233/cisco-umbrella-social-share.jpg
layout: provider
modified: '2026-07-18'
name: CloudLock
nav: Providers
network: true
overview: 'CloudLock is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Security, CASB, and Cloud Access Security Broker.


  CloudLock''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, and 6 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudlock/refs/heads/main/screenshots/cloudlock-2026-07-25T205704.png
security:
- kind: authentication
  name: Cloudlock Authentication
  slug: cloudlock-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cloudlock Domain Security
  slug: cloudlock-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cloudlock
tags:
- Company
- Cloud
- Security
- CASB
- Cloud Access Security Broker
- Data Loss Prevention
- Cloud Security
- SaaS Security
- Cisco
website: https://www.cloudlock.com/
---
