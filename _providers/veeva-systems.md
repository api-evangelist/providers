---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
- acting_count: 7
  human_in_the_loop: 0
  name: Veeva Systems Agentic Access
  operation_count: 12
  slug: veeva-systems-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 5
apis:
- description: The Authentication API from Veeva Systems — 4 operation(s) for authentication.
  name: Veeva Systems Authentication API
  slug: veeva-systems-authentication-api
- description: The DirectData API from Veeva Systems — 2 operation(s) for directdata.
  name: Veeva Systems DirectData API
  slug: veeva-systems-directdata-api
- description: The MDL API from Veeva Systems — 2 operation(s) for mdl.
  name: Veeva Systems MDL API
  slug: veeva-systems-mdl-api
- description: The Metadata API from Veeva Systems — 3 operation(s) for metadata.
  name: Veeva Systems Metadata API
  slug: veeva-systems-metadata-api
- description: The Query API from Veeva Systems — 1 operation(s) for query.
  name: Veeva Systems Query API
  slug: veeva-systems-query-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Veeva Vault Authentication API
  slug: open-veeva-systems-authentication-api
- collection_type: open
  name: Veeva Vault Authentication DirectData API
  slug: open-veeva-systems-directdata-api
- collection_type: open
  name: Veeva Vault Authentication MDL API
  slug: open-veeva-systems-mdl-api
- collection_type: open
  name: Veeva Vault Authentication Metadata API
  slug: open-veeva-systems-metadata-api
- collection_type: open
  name: Veeva Vault Authentication Query API
  slug: open-veeva-systems-query-api
- collection_type: open
  name: Veeva Vault API
  slug: open-veeva-systems
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/veeva-systems-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veeva-systems-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/veeva-systems-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veeva
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/veeva-systems
- group: company
  title: ''
  type: Website
  url: https://www.veeva.com
created: '2026-04-19'
description: Veeva Systems is a major US corporation and Fortune 1000 company. The Veeva Systems API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Veeva Systems Finops
  service_category: Life Sciences SaaS
  slug: veeva-systems-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/veeva-systems.png
layout: provider
modified: '2026-05-19'
name: Veeva Systems
nav: Providers
network: true
overview: 'Veeva Systems publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, DirectData API, MDL API, and 2 more. Tagged areas include Healthcare, Software-as-a-Service, and Life Sciences.


  Veeva Systems'' developer surface includes authentication and 5 more developer resources.'
plans:
- name: Veeva Systems Plans Pricing
  plan_count: 1
  slug: veeva-systems-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Veeva Systems Rate Limits
  slug: veeva-systems-rate-limits
score:
  band: emerging
  composite: 22.3
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 22.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/veeva-systems/refs/heads/main/screenshots/veeva-systems-2026-06-20T200853.png
security:
- kind: authentication
  name: Veeva Systems Authentication
  slug: veeva-systems-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Veeva Systems Domain Security
  slug: veeva-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: veeva-systems
tags:
- Healthcare
- Software-as-a-Service
- Life Sciences
website: https://www.veeva.com
---
