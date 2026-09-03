---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Pinata Agentic Access
  operation_count: 5
  slug: pinata-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- description: REST API for uploading, listing, organizing, and deleting files pinned to IPFS or stored privately. Supports public and private (Submarine) modes, signed URLs, and Groups.
  name: Pinata Files API
  slug: files-api
- description: Implementation of the IPFS Pinning Service API standard for compatibility with go-ipfs / kubo and js-ipfs clients.
  name: Pinata IPFS Pinning Service API
  slug: pinning-service-api
- description: Dedicated IPFS HTTP gateway endpoint per account for content retrieval with custom subdomain, access controls, and analytics.
  name: Pinata Dedicated Gateway
  slug: gateway-api
- description: REST API for organizing CIDs into named Groups with bulk add/remove operations.
  name: Pinata Groups API
  slug: groups-api
- baseURL: https://api.pinata.cloud/v3
  baseurl_source: declared
  description: Test API credentials.
  name: Pinata Auth API
  slug: pinata-auth-api
- baseURL: https://api.pinata.cloud/v3
  baseurl_source: declared
  description: Upload, list, and manage pinned files.
  name: Pinata Files API
  slug: pinata-files-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pinata Auth API
  slug: open-pinata-auth-api
- collection_type: open
  name: Pinata Auth Files API
  slug: open-pinata-files-api
- collection_type: open
  name: Pinata API
  slug: open-pinata
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pinata-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pinata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pinata-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PinataCloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pinatacloud
- group: company
  title: ''
  type: Website
  url: https://pinata.cloud/
- group: commercial
  title: ''
  type: Plans
  url: plans/pinata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pinata-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pinata-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.pinata.cloud/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://pinata.cloud/blog/rss/
created: '2026-05-08'
description: Pinata is an IPFS pinning and dedicated-gateway provider with a Files API, IPFS Pinning Service API, dedicated Gateways, Groups, and Workspaces. Built around IPFS CIDs with JWT-authenticated REST APIs and an SDK.
finops:
- name: Pinata Finops
  service_category: Web3
  slug: pinata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pinata.png
layout: provider
modified: '2026-05-08'
name: Pinata
nav: Providers
network: true
overview: 'Pinata publishes 2 APIs on the [APIs.io](https://apis.io/) network: Auth API and Files API. Tagged areas include Web3, IPFS, Storage, and Gateway.


  Pinata''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: Pinata Plans Pricing
  plan_count: 5
  slug: pinata-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Pinata Rate Limits
  slug: pinata-rate-limits
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 56.5
    developer_ergonomics: 23.8
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 29.7
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
screenshot: https://raw.githubusercontent.com/api-evangelist/pinata/refs/heads/main/screenshots/pinata-2026-06-20T191714.png
security:
- kind: authentication
  name: Pinata Authentication
  slug: pinata-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pinata Domain Security
  slug: pinata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pinata
tags:
- Web3
- IPFS
- Storage
- Gateway
website: https://pinata.cloud/
---
