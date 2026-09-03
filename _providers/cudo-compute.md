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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 22
  human_in_the_loop: 4
  name: Cudo Compute Agentic Access
  operation_count: 49
  slug: cudo-compute-agentic-access
  summary_line: 49 operations · 22 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://rest.compute.cudo.org
  baseurl_source: declared
  description: The Billing API from CUDO Compute — 4 operation(s) for billing.
  name: CUDO Compute Billing API
  slug: cudo-compute-billing-api
- baseURL: https://rest.compute.cudo.org
  baseurl_source: declared
  description: The Data Centers API from CUDO Compute — 3 operation(s) for data centers.
  name: CUDO Compute Data Centers API
  slug: cudo-compute-data-centers-api
- baseURL: https://rest.compute.cudo.org
  baseurl_source: declared
  description: The Disks API from CUDO Compute — 5 operation(s) for disks.
  name: CUDO Compute Disks API
  slug: cudo-compute-disks-api
- baseURL: https://rest.compute.cudo.org
  baseurl_source: declared
  description: The Images API from CUDO Compute — 3 operation(s) for images.
  name: CUDO Compute Images API
  slug: cudo-compute-images-api
- baseURL: https://rest.compute.cudo.org
  baseurl_source: declared
  description: The Machine Types API from CUDO Compute — 4 operation(s) for machine types.
  name: CUDO Compute Machine Types API
  slug: cudo-compute-machine-types-api
- baseURL: https://rest.compute.cudo.org
  baseurl_source: declared
  description: The Networks API from CUDO Compute — 5 operation(s) for networks.
  name: CUDO Compute Networks API
  slug: cudo-compute-networks-api
- baseURL: https://rest.compute.cudo.org
  baseurl_source: declared
  description: The SSH Keys API from CUDO Compute — 3 operation(s) for ssh keys.
  name: CUDO Compute SSH Keys API
  slug: cudo-compute-ssh-keys-api
- baseURL: https://rest.compute.cudo.org
  baseurl_source: declared
  description: The Virtual Machines API from CUDO Compute — 10 operation(s) for virtual machines.
  name: CUDO Compute Virtual Machines API
  slug: cudo-compute-virtual-machines-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CUDO Compute Billing API
  slug: open-cudo-compute-billing-api
- collection_type: open
  name: CUDO Compute Billing Data Centers API
  slug: open-cudo-compute-data-centers-api
- collection_type: open
  name: CUDO Compute Billing Disks API
  slug: open-cudo-compute-disks-api
- collection_type: open
  name: CUDO Compute Billing Images API
  slug: open-cudo-compute-images-api
- collection_type: open
  name: CUDO Compute Billing Machine Types API
  slug: open-cudo-compute-machine-types-api
- collection_type: open
  name: CUDO Compute Billing Networks API
  slug: open-cudo-compute-networks-api
- collection_type: open
  name: CUDO Compute Billing SSH Keys API
  slug: open-cudo-compute-ssh-keys-api
- collection_type: open
  name: CUDO Compute Billing Virtual Machines API
  slug: open-cudo-compute-virtual-machines-api
- collection_type: open
  name: CUDO Compute API
  slug: open-cudo-compute
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cudo-compute-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cudo-compute-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cudo-compute-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cudo-compute-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CudoVentures
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cudo-ventures
- group: company
  title: ''
  type: Website
  url: https://www.cudocompute.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.cudocompute.com/docs/api
- group: commercial
  title: ''
  type: Plans
  url: plans/cudo-compute-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cudo-compute-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cudo-compute-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cudocompute.com/feed/
created: '2026-06-21'
description: CUDO Compute is a global GPU and cloud compute platform and marketplace that provisions on-demand and reserved virtual machines, bare metal, and multi-node GPU clusters across a distributed network of data centers. Its versioned, resource-oriented REST API (with a parallel gRPC surface) lets developers create and manage virtual machines, machine types, data centers, disks, networks, images, SSH keys, object storage, and billing programmatically.
finops:
- name: Cudo Compute Finops
  service_category: Compute
  slug: cudo-compute-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cudo-compute.png
layout: provider
modified: '2026-06-21'
name: CUDO Compute
nav: Providers
network: true
overview: 'CUDO Compute publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Data Centers API, Disks API, and 5 more. Tagged areas include GPU, Cloud Compute, Infrastructure, Virtual Machines, and Marketplace.


  CUDO Compute''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Cudo Compute Plans Pricing
  plan_count: 3
  slug: cudo-compute-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Cudo Compute Rate Limits
  slug: cudo-compute-rate-limits
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cudo-compute/refs/heads/main/screenshots/cudo-compute-2026-07-25T210908.png
security:
- kind: authentication
  name: Cudo Compute Authentication
  slug: cudo-compute-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cudo Compute Domain Security
  slug: cudo-compute-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cudo-compute
tags:
- GPU
- Cloud Compute
- Infrastructure
- Virtual Machines
- Marketplace
website: https://www.cudocompute.com
---
