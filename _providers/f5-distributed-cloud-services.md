---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: F5 Distributed Cloud Services Agentic Access
  operation_count: 21
  slug: f5-distributed-cloud-services-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 1
apis:
- description: Comprehensive REST API for managing F5 Distributed Cloud Services including load balancers, WAF/WAAP policies, API security, DNS, origin pools, certificates, cloud site connectors, and observability r
  name: F5 Distributed Cloud Services API
  slug: platform-api
- baseURL: https://console.ves.volterra.io/api
  baseurl_source: declared
  description: The Config API from F5 Distributed Cloud Services — 10 operation(s) for config.
  name: F5 Distributed Cloud Services Config API
  slug: f5-distributed-cloud-services-config-api
- baseURL: https://console.ves.volterra.io/api
  baseurl_source: declared
  description: The Data API from F5 Distributed Cloud Services — 1 operation(s) for data.
  name: F5 Distributed Cloud Services Data API
  slug: f5-distributed-cloud-services-data-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: F5 Distributed Cloud Services Config API
  slug: open-f5-distributed-cloud-services-config-api
- collection_type: open
  name: F5 Distributed Cloud Services Config Data API
  slug: open-f5-distributed-cloud-services-data-api
- collection_type: open
  name: F5 Distributed Cloud Services API
  slug: open-f5-distributed-cloud-services
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/f5-distributed-cloud-services-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/f5-distributed-cloud-services-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/f5-distributed-cloud-services-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/f5-distributed-cloud-services-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/f5devcentral
- group: company
  title: ''
  type: Website
  url: https://www.f5.com/products/distributed-cloud-services
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloud.f5.com/docs-v2
- group: commercial
  title: ''
  type: Pricing
  url: https://www.f5.com/products/distributed-cloud-services
- group: start
  title: ''
  type: Signup
  url: https://www.f5.com/trials/distributed-cloud-services
- group: start
  title: ''
  type: Console
  url: https://console.ves.volterra.io
- group: operate
  title: ''
  type: Support
  url: https://my.f5.com/manage/s/
- group: company
  title: ''
  type: Blog
  url: https://www.f5.com/company/blog
created: '2026-05-11'
description: F5 Distributed Cloud Services (F5 XC) is a SaaS-based platform providing distributed multi-cloud application security, networking, and edge infrastructure including web application and API protection (WAAP), DDoS mitigation, bot defense, multi-cloud networking, DNS, load balancing, and edge compute across F5's global private backbone. The platform's REST API exposes 200+ resource types covering HTTP/TCP/UDP load balancers, security policies, certificate management, cloud connectors, and observability, authenticated via API tokens and service credentials managed in the F5 Distributed Cloud Console.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/f5-distributed-cloud-services.png
layout: provider
modified: '2026-05-11'
name: F5 Distributed Cloud Services
nav: Providers
network: true
overview: 'F5 Distributed Cloud Services publishes 2 APIs on the [APIs.io](https://apis.io/) network: Config API and Data API. Tagged areas include Application Security, Web Application Firewall, API Security, Multi-Cloud Networking, and DDoS Protection.


  F5 Distributed Cloud Services'' developer surface includes authentication, documentation, pricing, signup flow, developer console, support, engineering blog, and 5 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 20.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/f5-distributed-cloud-services/refs/heads/main/screenshots/f5-distributed-cloud-services-2026-06-20T180955.png
security:
- kind: authentication
  name: F5 Distributed Cloud Services Authentication
  slug: f5-distributed-cloud-services-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: F5 Distributed Cloud Services Domain Security
  slug: f5-distributed-cloud-services-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: F5 Distributed Cloud Services Trust Center
  slug: f5-distributed-cloud-services-trust-center
  summary_line: PCI DSS, GDPR
slug: f5-distributed-cloud-services
tags:
- Application Security
- Web Application Firewall
- API Security
- Multi-Cloud Networking
- DDoS Protection
- Bot Defense
- Load Balancing
- Edge Compute
website: https://www.f5.com/products/distributed-cloud-services
---
