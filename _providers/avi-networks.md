---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://avinetworks.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.vmware.com/products/cloud-infrastructure/advanced-services/avi-load-balancer — a different registrable domain (avinetworks.com -> vmware.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/vmware/
- group: company
  title: ''
  type: Website
  url: https://avinetworks.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.vmware.com/products/cloud-infrastructure/avi-load-balancer
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avinetworks
- group: build
  title: ''
  type: Packages
  url: packages/avi-networks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/avi-networks-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avi-networks-domain-security.yml
created: '2026-07-17'
description: AVI Networks builds a software-defined application delivery platform - the Avi Vantage Platform / Avi Load Balancer - providing multi-cloud load balancing, web application firewall (WAF), GSLB, container ingress, and analytics driven by a central Avi Controller with a fully programmable REST API. Founded in 2012 and headquartered in Santa Clara, California, AVI Networks was acquired by VMware in 2019 and the product is now offered by Broadcom as the VMware Avi Load Balancer. The controller exposes a comprehensive REST API with first-party Python, Go, and Java SDKs, a Terraform provider, and Ansible automation for intent-based, self-service application services across VMware, AWS, Azure, GCP, OpenStack, and bare-metal environments.
image: https://avinetworks.com/wp-content/uploads/2018/03/avi-networks-logo.png
layout: provider
modified: '2026-08-21'
name: AVI Networks
nav: Providers
network: true
overview: AVI Networks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Load Balancing, Application Delivery, and Networking.
random_paper: 19
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avi-networks/refs/heads/main/screenshots/avi-networks-2026-07-25T201928.png
security:
- kind: domain-security
  name: Avi Networks Domain Security
  slug: avi-networks-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: avi-networks
tags:
- Company
- Infrastructure
- Load Balancing
- Application Delivery
- Networking
- Multi-Cloud
- Web Application Firewall
- Kubernetes Ingress
- Load Balancer
- REST API
website: https://avinetworks.com/
---
