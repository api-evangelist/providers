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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Partnerstack Agentic Access
  operation_count: 6
  slug: partnerstack-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.partnerstack.com/api/v2
  baseurl_source: declared
  description: The Customers API from PartnerStack — 1 operation(s) for customers.
  name: PartnerStack Customers API
  slug: partnerstack-customers-api
- baseURL: https://api.partnerstack.com/api/v2
  baseurl_source: declared
  description: The Deals API from PartnerStack — 1 operation(s) for deals.
  name: PartnerStack Deals API
  slug: partnerstack-deals-api
- baseURL: https://api.partnerstack.com/api/v2
  baseurl_source: declared
  description: The Partnerships API from PartnerStack — 1 operation(s) for partnerships.
  name: PartnerStack Partnerships API
  slug: partnerstack-partnerships-api
- baseURL: https://api.partnerstack.com/api/v2
  baseurl_source: declared
  description: The Rewards API from PartnerStack — 1 operation(s) for rewards.
  name: PartnerStack Rewards API
  slug: partnerstack-rewards-api
- baseURL: https://api.partnerstack.com/api/v2
  baseurl_source: declared
  description: The Transactions API from PartnerStack — 1 operation(s) for transactions.
  name: PartnerStack Transactions API
  slug: partnerstack-transactions-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PartnerStack Customers API
  slug: open-partnerstack-customers-api
- collection_type: open
  name: PartnerStack Customers Deals API
  slug: open-partnerstack-deals-api
- collection_type: open
  name: PartnerStack Customers Partnerships API
  slug: open-partnerstack-partnerships-api
- collection_type: open
  name: PartnerStack Customers Rewards API
  slug: open-partnerstack-rewards-api
- collection_type: open
  name: PartnerStack Customers Transactions API
  slug: open-partnerstack-transactions-api
- collection_type: open
  name: PartnerStack API
  slug: open-partnerstack
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/partnerstack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/partnerstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/partnerstack-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/partnerstack
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/partnerstack
- group: company
  title: ''
  type: Website
  url: https://partnerstack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.partnerstack.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.partnerstack.com/reference
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.partnerstack.com/llms.txt
created: '2025-02-08'
description: PartnerStack is a partner-led growth platform that powers the partnerships programs of leading B2B SaaS companies. The PartnerStack API provides programmatic access to partnerships, customers, deals, transactions, and rewards.
finops:
- name: Partnerstack Finops
  service_category: API
  slug: partnerstack-finops
graphqls:
- description: Conceptual GraphQL schema for the [PartnerStack](https://partnerstack.com/) partner relationship management (PRM) platform. PartnerStack powers partner-led growth programs for B2B SaaS companies, prov
  name: PartnerStack GraphQL Schema
  slug: partnerstack-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/partnerstack.png
layout: provider
modified: '2026-05-19'
name: PartnerStack
nav: Providers
network: true
overview: 'PartnerStack publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Deals API, Partnerships API, and 2 more. Tagged areas include Partnerships, Affiliates, and Software-as-a-Service.


  PartnerStack''s developer surface includes authentication, documentation, API reference, and 6 more developer resources.'
plans:
- name: Partnerstack Plans Pricing
  plan_count: 3
  slug: partnerstack-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Partnerstack Rate Limits
  slug: partnerstack-rate-limits
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 56.0
    developer_ergonomics: 20.2
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 29.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/partnerstack/refs/heads/main/screenshots/partnerstack-2026-06-20T191432.png
security:
- kind: authentication
  name: Partnerstack Authentication
  slug: partnerstack-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Partnerstack Domain Security
  slug: partnerstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: partnerstack
tags:
- Partnerships
- Affiliates
- Software-as-a-Service
website: https://partnerstack.com/
---
