---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Usaspending Agentic Access
  operation_count: 14
  slug: usaspending-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 9
apis:
- description: Per-agency profile, budget, and award data.
  name: USAspending.gov Agency API
  slug: usaspending-agency-api
- description: Advanced search and filtering across award and subaward spending.
  name: USAspending.gov Awards Search API
  slug: usaspending-awards-search-api
- description: Federal budget functional classification reference data.
  name: USAspending.gov Budget Functions API
  slug: usaspending-budget-functions-api
- description: Asynchronous bulk CSV/TSV/text export of filtered spending data.
  name: USAspending.gov Bulk Download API
  slug: usaspending-bulk-download-api
- description: Disaster and emergency (including COVID-19) supplemental funding data.
  name: USAspending.gov Disaster API
  slug: usaspending-disaster-api
- description: Federal account and Treasury Account Symbol (TAS) data.
  name: USAspending.gov Federal Accounts API
  slug: usaspending-federal-accounts-api
- description: Recipient (awardee) profile and search data.
  name: USAspending.gov Recipient API
  slug: usaspending-recipient-api
- description: Reference and typeahead/autocomplete lookup data.
  name: USAspending.gov References API
  slug: usaspending-references-api
- description: Subaward (pass-through award) listings scoped to a prime award.
  name: USAspending.gov Subawards API
  slug: usaspending-subawards-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USAspending Agency API
  slug: open-usaspending-agency-api
- collection_type: open
  name: USAspending Agency Awards Search API
  slug: open-usaspending-awards-search-api
- collection_type: open
  name: USAspending Agency Budget Functions API
  slug: open-usaspending-budget-functions-api
- collection_type: open
  name: USAspending Agency Bulk Download API
  slug: open-usaspending-bulk-download-api
- collection_type: open
  name: USAspending Agency Disaster API
  slug: open-usaspending-disaster-api
- collection_type: open
  name: USAspending Agency Federal Accounts API
  slug: open-usaspending-federal-accounts-api
- collection_type: open
  name: USAspending Agency Recipient API
  slug: open-usaspending-recipient-api
- collection_type: open
  name: USAspending Agency References API
  slug: open-usaspending-references-api
- collection_type: open
  name: USAspending Agency Subawards API
  slug: open-usaspending-subawards-api
- collection_type: open
  name: USAspending API
  slug: open-usaspending
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/usaspending-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usaspending-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fedspendingtransparency
- group: company
  title: ''
  type: Website
  url: https://www.usaspending.gov
- group: docs
  title: ''
  type: Documentation
  url: https://api.usaspending.gov/docs/endpoints
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/usaspending-rate-limits.yml
created: '2026-07-03'
description: USAspending.gov is the official open data source of federal spending information operated by the U.S. Department of the Treasury's Bureau of the Fiscal Service, implementing the DATA Act's transparency mandate. The underlying USAspending API (api.usaspending.gov) is a free, public, unauthenticated REST API that exposes federal contracts, grants, loans, direct payments, and other financial assistance awards, along with agency budgets, federal account and Treasury Account Symbol data, recipient profiles, and COVID-19 / disaster emergency relief spending. Most search and listing endpoints accept a POST with a JSON filter object rather than query parameters, given the complexity of the filter combinations; simpler lookup endpoints use GET with path parameters. The API and the usaspending-api server are open source.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usaspending.png
layout: provider
modified: '2026-07-03'
name: USAspending.gov
nav: Providers
network: true
overview: 'USAspending.gov publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Agency API, Awards Search API, Budget Functions API, and 6 more. Tagged areas include Government, Federal Spending, Open Data, Contracts, and Grants.


  USAspending.gov''s developer surface includes documentation and 5 more developer resources.'
random_paper: 9
rate_limits:
- limit_count: 3
  name: Usaspending Rate Limits
  slug: usaspending-rate-limits
score:
  band: emerging
  composite: 25.1
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 51.9
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 25.1
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
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Usaspending Domain Security
  slug: usaspending-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: usaspending
tags:
- Government
- Federal Spending
- Open Data
- Contracts
- Grants
- DATA Act
- Transparency
- Public Sector
website: https://www.usaspending.gov
---
