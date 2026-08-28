---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Chroniclingamerica Agentic Access
  operation_count: 11
  slug: chroniclingamerica-agentic-access
  summary_line: 11 operations
api_count: 6
apis:
- description: Endpoints for retrieving digitization batch information.
  name: Chronicling America Batches API
  slug: chroniclingamerica-batches-api
- description: Endpoints for retrieving newspaper issue metadata.
  name: Chronicling America Issues API
  slug: chroniclingamerica-issues-api
- description: Endpoints for retrieving OCR text from digitized newspaper pages.
  name: Chronicling America OCR API
  slug: chroniclingamerica-ocr-api
- description: Endpoints for retrieving individual newspaper page metadata and content.
  name: Chronicling America Pages API
  slug: chroniclingamerica-pages-api
- description: Full-text search endpoints for newspaper pages and titles.
  name: Chronicling America Search API
  slug: chroniclingamerica-search-api
- description: Endpoints for retrieving newspaper title bibliographic metadata.
  name: Chronicling America Titles API
  slug: chroniclingamerica-titles-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Chronicling America Batches API
  slug: open-chroniclingamerica-batches-api
- collection_type: open
  name: Chronicling America Batches Issues API
  slug: open-chroniclingamerica-issues-api
- collection_type: open
  name: Chronicling America Batches OCR API
  slug: open-chroniclingamerica-ocr-api
- collection_type: open
  name: Chronicling America Batches Pages API
  slug: open-chroniclingamerica-pages-api
- collection_type: open
  name: Chronicling America Batches Search API
  slug: open-chroniclingamerica-search-api
- collection_type: open
  name: Chronicling America Batches Titles API
  slug: open-chroniclingamerica-titles-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chroniclingamerica-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chroniclingamerica-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chroniclingamerica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chroniclingamerica.loc.gov
- group: docs
  title: ''
  type: Documentation
  url: https://chroniclingamerica.loc.gov/about/api/
- group: company
  title: ''
  type: About
  url: https://chroniclingamerica.loc.gov/about/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/LibraryOfCongress
- group: other
  title: ''
  type: X
  url: https://twitter.com/librarycongress
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/library-of-congress
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.loc.gov/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.loc.gov/legal/privacy-policy/
- group: commercial
  title: ''
  type: Plans
  url: plans/chroniclingamerica-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chroniclingamerica-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chroniclingamerica-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/chroniclingamerica/refs/heads/main/json-ld/chroniclingamerica.jsonld
created: '2026-06-13'
description: Chronicling America is a Library of Congress initiative providing free public access to a searchable database of historic American newspaper pages from 1770 to 1963. The platform hosts over 20 million digitized newspaper pages from hundreds of US newspapers contributed by institutions in the National Digital Newspaper Program (NDNP). The API exposes search, title, issue, batch, and OCR text endpoints with no authentication required, returning responses in JSON and Atom feed formats.
finops:
- name: Chroniclingamerica Finops
  service_category: API
  slug: chroniclingamerica-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chroniclingamerica.png
jsonld:
- class_count: 0
  name: Chroniclingamerica Context
  property_count: 0
  slug: chroniclingamerica
layout: provider
modified: '2026-06-13'
name: Chronicling America
nav: Providers
network: true
overview: 'Chronicling America publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Batches API, Issues API, OCR API, and 3 more. Tagged areas include Newspapers, Historical, Archives, Library of Congress, and Government.


  The Chronicling America catalog on APIs.io includes 1 JSON-LD context.


  Chronicling America''s developer surface includes documentation and 14 more developer resources.'
plans:
- name: Chroniclingamerica Plans Pricing
  plan_count: 1
  slug: chroniclingamerica-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Chroniclingamerica Rate Limits
  slug: chroniclingamerica-rate-limits
score:
  band: developing
  composite: 41.9
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 56.5
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chroniclingamerica/refs/heads/main/screenshots/chroniclingamerica-2026-07-25T205316.png
security:
- kind: domain-security
  name: Chroniclingamerica Domain Security
  slug: chroniclingamerica-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Chroniclingamerica Vulnerability Disclosure
  slug: chroniclingamerica-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chroniclingamerica
tags:
- Newspapers
- Historical
- Archives
- Library of Congress
- Government
- Digitized
- OCR
- Search
- Cultural Heritage
website: https://chroniclingamerica.loc.gov
---
