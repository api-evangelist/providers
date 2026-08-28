---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 23
  human_in_the_loop: 7
  name: Voltage Park Agentic Access
  operation_count: 48
  slug: voltage-park-agentic-access
  summary_line: 48 operations · 23 acting · 7 human-in-the-loop
api_count: 7
apis:
- description: Provision and manage multi-node bare-metal GPU rentals and clusters.
  name: Voltage Park Bare Metal API
  slug: voltage-park-bare-metal-api
- description: Hourly rates and historical billing transactions.
  name: Voltage Park Billing API
  slug: voltage-park-billing-api
- description: Locations, host nodes, and instant-deploy presets.
  name: Voltage Park Locations API
  slug: voltage-park-locations-api
- description: Organization details, address, and SSH keys.
  name: Voltage Park Organization API
  slug: voltage-park-organization-api
- description: Shared storage volumes attachable to bare-metal rentals.
  name: Voltage Park Storage API
  slug: voltage-park-storage-api
- description: Validate cloud-init scripts before deployment.
  name: Voltage Park Validation API
  slug: voltage-park-validation-api
- description: Deploy and manage on-demand GPU virtual machines and instant VMs.
  name: Voltage Park Virtual Machines API
  slug: voltage-park-virtual-machines-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Voltage Park On-Demand Bare Metal API
  slug: open-voltage-park-bare-metal-api
- collection_type: open
  name: Voltage Park On-Demand Bare Metal Billing API
  slug: open-voltage-park-billing-api
- collection_type: open
  name: Voltage Park On-Demand Bare Metal Locations API
  slug: open-voltage-park-locations-api
- collection_type: open
  name: Voltage Park On-Demand Bare Metal Organization API
  slug: open-voltage-park-organization-api
- collection_type: open
  name: Voltage Park On-Demand Bare Metal Storage API
  slug: open-voltage-park-storage-api
- collection_type: open
  name: Voltage Park On-Demand Bare Metal Validation API
  slug: open-voltage-park-validation-api
- collection_type: open
  name: Voltage Park On-Demand Bare Metal Virtual Machines API
  slug: open-voltage-park-virtual-machines-api
- collection_type: open
  name: Voltage Park On-Demand API
  slug: open-voltage-park
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/voltage-park-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/voltage-park-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voltage-park-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/voltage-park-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voltage-park
- group: company
  title: ''
  type: Website
  url: https://www.voltagepark.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.voltagepark.com
- group: commercial
  title: ''
  type: Plans
  url: plans/voltage-park-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/voltage-park-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/voltage-park-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.voltagepark.com/blog/rss.xml
created: '2026-06-21'
description: Voltage Park is a GPU cloud offering on-demand and reserved NVIDIA H100 and H200 clusters as bare metal and virtual machines. Its On-Demand API (served at cloud-api.voltagepark.com, running on TensorDock infrastructure) lets developers deploy and manage instant VMs, bare-metal GPU rentals, SSH keys, shared storage, and billing programmatically with bearer-token authentication.
finops:
- name: Voltage Park Finops
  service_category: Compute
  slug: voltage-park-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/voltage-park.png
layout: provider
modified: '2026-06-21'
name: Voltage Park
nav: Providers
network: true
overview: 'Voltage Park publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Bare Metal API, Billing API, Locations API, and 4 more. Tagged areas include GPU, Cloud, AI Infrastructure, H100, and H200.


  Voltage Park''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Voltage Park Plans Pricing
  plan_count: 2
  slug: voltage-park-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Voltage Park Rate Limits
  slug: voltage-park-rate-limits
score:
  band: thin
  composite: 36.1
  delta: 1.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 53.5
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Voltage Park Authentication
  slug: voltage-park-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Voltage Park Domain Security
  slug: voltage-park-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Voltage Park Trust Center
  slug: voltage-park-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: voltage-park
tags:
- GPU
- Cloud
- AI Infrastructure
- H100
- H200
- Bare Metal
website: https://www.voltagepark.com
---
