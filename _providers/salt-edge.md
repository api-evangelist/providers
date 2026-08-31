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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Salt Edge Agentic Access
  operation_count: 18
  slug: salt-edge-agentic-access
  summary_line: 18 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: REST API for retrieving end-user accounts, transactions, balances, and identity across 5,000+ banks worldwide.
  name: Salt Edge Account Information API
  slug: account-information-api
- description: Initiate single, recurring, and bulk SEPA / domestic payments via PSD2 PISP.
  name: Salt Edge Payment Initiation API
  slug: payment-initiation-api
- description: APIs for banks adopting open banking - exposes their data to TPPs through Salt Edge's compliance gateway.
  name: Salt Edge Partners (Compliance Solution) API
  slug: partners-api
- description: Categorize and enrich transactions, identify merchants, and surface financial insights.
  name: Salt Edge Data Enrichment API
  slug: data-enrichment-api
- description: The Accounts API from Salt Edge — 1 operation(s) for accounts.
  name: Salt Edge Accounts API
  slug: salt-edge-accounts-api
- description: The Connect Sessions API from Salt Edge — 1 operation(s) for connect sessions.
  name: Salt Edge Connect Sessions API
  slug: salt-edge-connect-sessions-api
- description: The Connections API from Salt Edge — 4 operation(s) for connections.
  name: Salt Edge Connections API
  slug: salt-edge-connections-api
- description: The Consents API from Salt Edge — 2 operation(s) for consents.
  name: Salt Edge Consents API
  slug: salt-edge-consents-api
- description: The Countries API from Salt Edge — 1 operation(s) for countries.
  name: Salt Edge Countries API
  slug: salt-edge-countries-api
- description: The Customers API from Salt Edge — 2 operation(s) for customers.
  name: Salt Edge Customers API
  slug: salt-edge-customers-api
- description: The Holder Info API from Salt Edge — 1 operation(s) for holder info.
  name: Salt Edge Holder Info API
  slug: salt-edge-holder-info-api
- description: The Providers API from Salt Edge — 2 operation(s) for providers.
  name: Salt Edge Providers API
  slug: salt-edge-providers-api
- description: The Transactions API from Salt Edge — 1 operation(s) for transactions.
  name: Salt Edge Transactions API
  slug: salt-edge-transactions-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Salt Edge Account Information Accounts API
  slug: open-salt-edge-accounts-api
- collection_type: open
  name: Salt Edge Account Information Accounts Connect Sessions API
  slug: open-salt-edge-connect-sessions-api
- collection_type: open
  name: Salt Edge Account Information Accounts Connections API
  slug: open-salt-edge-connections-api
- collection_type: open
  name: Salt Edge Account Information Accounts Consents API
  slug: open-salt-edge-consents-api
- collection_type: open
  name: Salt Edge Account Information Accounts Countries API
  slug: open-salt-edge-countries-api
- collection_type: open
  name: Salt Edge Account Information Accounts Customers API
  slug: open-salt-edge-customers-api
- collection_type: open
  name: Salt Edge Account Information Accounts Holder Info API
  slug: open-salt-edge-holder-info-api
- collection_type: open
  name: Salt Edge Account Information Accounts Providers API
  slug: open-salt-edge-providers-api
- collection_type: open
  name: Salt Edge Account Information Accounts Transactions API
  slug: open-salt-edge-transactions-api
- collection_type: open
  name: Salt Edge Account Information API
  slug: open-salt-edge
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/salt-edge-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salt-edge-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salt-edge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/salt-edge-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.saltedge.com/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/saltedge
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/salt-edge
- group: start
  title: ''
  type: Portal
  url: https://www.saltedge.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.saltedge.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.saltedge.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/salt-edge-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/salt-edge-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/salt-edge-finops.yml
created: '2026-05-08'
description: Salt Edge is a global open-banking aggregator providing account information, payment initiation, data enrichment, merchant identification, AML transaction monitoring, and open-banking compliance solutions across 5,000+ banks. The Salt Edge API exposes Account Information (AIS) and Payment Initiation (PIS) services plus add-on Data Enrichment and AML endpoints under a single REST surface.
finops:
- name: Salt Edge Finops
  service_category: Open Banking
  slug: salt-edge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/salt-edge.png
layout: provider
modified: '2026-05-08'
name: Salt Edge
nav: Providers
network: true
overview: 'Salt Edge publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Connect Sessions API, Connections API, and 6 more. Tagged areas include Fintech, Open Banking, PSD2, Aggregator, and Global.


  Salt Edge''s developer surface includes authentication, engineering blog, developer portal, documentation, pricing, and 8 more developer resources.'
plans:
- name: Salt Edge Plans Pricing
  plan_count: 4
  slug: salt-edge-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Salt Edge Rate Limits
  slug: salt-edge-rate-limits
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 50.8
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salt-edge/refs/heads/main/screenshots/salt-edge-2026-06-20T193356.png
security:
- kind: authentication
  name: Salt Edge Authentication
  slug: salt-edge-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Salt Edge Domain Security
  slug: salt-edge-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: salt-edge
tags:
- Fintech
- Open Banking
- PSD2
- Aggregator
- Global
- AISP
- PISP
- Compliance
- AML
website: https://www.saltedge.com/
---
