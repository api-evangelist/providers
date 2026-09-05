---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Oneflow Agentic Access
  operation_count: 28
  slug: oneflow-agentic-access
  summary_line: 28 operations · 14 acting
api_count: 1
apis:
- baseURL: https://api.oneflow.com/v1
  baseurl_source: declared
  description: Inline collaboration comments on a contract.
  name: Oneflow Comments API
  slug: oneflow-comments-api
- baseURL: https://api.oneflow.com/v1
  baseurl_source: declared
  description: Download the files (PDF / signed documents) attached to a contract.
  name: Oneflow Contract Files API
  slug: oneflow-contract-files-api
- baseURL: https://api.oneflow.com/v1
  baseurl_source: declared
  description: Create, retrieve, update, publish, copy, and delete contracts.
  name: Oneflow Contracts API
  slug: oneflow-contracts-api
- baseURL: https://api.oneflow.com/v1
  baseurl_source: declared
  description: Custom / merge fields on contracts and template types.
  name: Oneflow Data Fields API
  slug: oneflow-data-fields-api
- baseURL: https://api.oneflow.com/v1
  baseurl_source: declared
  description: Signatories and viewers belonging to a party.
  name: Oneflow Participants API
  slug: oneflow-participants-api
- baseURL: https://api.oneflow.com/v1
  baseurl_source: declared
  description: Counterparty companies or individuals on a contract.
  name: Oneflow Parties API
  slug: oneflow-parties-api
- baseURL: https://api.oneflow.com/v1
  baseurl_source: declared
  description: Health check and token validation.
  name: Oneflow Ping API
  slug: oneflow-ping-api
- baseURL: https://api.oneflow.com/v1
  baseurl_source: declared
  description: Templates and template types used to create contracts.
  name: Oneflow Templates API
  slug: oneflow-templates-api
- baseURL: https://api.oneflow.com/v1
  baseurl_source: declared
  description: Users in an account.
  name: Oneflow Users API
  slug: oneflow-users-api
- baseURL: https://api.oneflow.com/v1
  baseurl_source: declared
  description: Subscriptions delivering contract lifecycle events to a callback URL.
  name: Oneflow Webhooks API
  slug: oneflow-webhooks-api
- baseURL: https://api.oneflow.com/v1
  baseurl_source: declared
  description: Organizational containers that scope templates and contracts.
  name: Oneflow Workspaces API
  slug: oneflow-workspaces-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Oneflow Public Comments API
  slug: open-oneflow-comments-api
- collection_type: open
  name: Oneflow Public Comments Contract Files API
  slug: open-oneflow-contract-files-api
- collection_type: open
  name: Oneflow Public Comments Contracts API
  slug: open-oneflow-contracts-api
- collection_type: open
  name: Oneflow Public Comments Data Fields API
  slug: open-oneflow-data-fields-api
- collection_type: open
  name: Oneflow Public Comments Participants API
  slug: open-oneflow-participants-api
- collection_type: open
  name: Oneflow Public Comments Parties API
  slug: open-oneflow-parties-api
- collection_type: open
  name: Oneflow Public Comments Ping API
  slug: open-oneflow-ping-api
- collection_type: open
  name: Oneflow Public Comments Templates API
  slug: open-oneflow-templates-api
- collection_type: open
  name: Oneflow Public Comments Users API
  slug: open-oneflow-users-api
- collection_type: open
  name: Oneflow Public Comments Webhooks API
  slug: open-oneflow-webhooks-api
- collection_type: open
  name: Oneflow Public Comments Workspaces API
  slug: open-oneflow-workspaces-api
- collection_type: open
  name: Oneflow Public API
  slug: open-oneflow
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oneflow-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/oneflow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oneflow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oneflow-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/oneflowcom
- group: company
  title: ''
  type: Website
  url: https://oneflow.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.oneflow.com
- group: commercial
  title: ''
  type: Plans
  url: plans/oneflow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/oneflow-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/oneflow-finops.yml
created: '2026-07-03'
description: Oneflow is a contract lifecycle management and e-signature platform that turns static documents into smart, data-rich digital contracts - covering creation from templates, negotiation, e-signing, and post-sign lifecycle management. The Oneflow Public API is a REST API at https://api.oneflow.com/v1 authenticated with an account API token (x-oneflow-api-token) plus an acting-user email header (x-oneflow-user-email) for permission checks. It lets teams programmatically create contracts from templates, add parties and participants, fill data fields and products, publish contracts for signing, download signed files, and subscribe to contract lifecycle events via webhooks. API access and webhooks are available on the Business and Enterprise plans.
finops:
- name: Oneflow Finops
  service_category: Contract Lifecycle Management and E-Signature
  slug: oneflow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oneflow.png
layout: provider
modified: '2026-07-03'
name: Oneflow
nav: Providers
network: true
overview: 'Oneflow publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Contract Files API, Contracts API, and 8 more. Tagged areas include Contract Management, Contract Lifecycle Management, E-Signature, Digital Contracts, and Document Automation.


  Oneflow''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Oneflow Plans Pricing
  plan_count: 4
  slug: oneflow-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Oneflow Rate Limits
  slug: oneflow-rate-limits
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.0
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oneflow/refs/heads/main/screenshots/oneflow-2026-08-07T190311.png
security:
- kind: authentication
  name: Oneflow Authentication
  slug: oneflow-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Oneflow Domain Security
  slug: oneflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Oneflow Vulnerability Disclosure
  slug: oneflow-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: oneflow
tags:
- Contract Management
- Contract Lifecycle Management
- E-Signature
- Digital Contracts
- Document Automation
- CLM
website: https://oneflow.com
---
