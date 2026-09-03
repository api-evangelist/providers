---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://bentoforbusiness.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.usbank.com/business-banking/business-credit-cards/spend-management.html — a different registrable domain (bentoforbusiness.com -> usbank.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://bentoforbusiness.com
- group: other
  title: ''
  type: Acquisition
  url: https://www.usbank.com/about-us-bank/company-blog/article-library/us-bank-to-acquire-small-business-payments-software-company-Bento-Technologies.html
- group: company
  title: ''
  type: Investor
  url: https://www.anthemis.com/portfolio/bento/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bento-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bento-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bento-llms.txt
created: '2026-07-17'
description: 'Bento (Bento Technologies, Inc., dba Bento for Business) was a Chicago- and San Francisco-based small-business fintech that provided card-based payment and expense management for small and mid-size businesses: virtual and physical employee and utility cards, per-card spend controls and category restrictions, real-time spend tracking, and accounting integrations. Bento published a public REST API at api.bentoforbusiness.com (documented at apidocs.bentoforbusiness.com) for issuing employee and utility virtual cards, retrieving card numbers, activating and customizing billing addresses, and reading card transactions, plus outbound webhooks for card transaction completed and declined events; API access was granted per account via an Access Key and Secret Key issued by api-support@bentoforbusiness.com. Bento raised a $2.5M seed round led by Anthemis Group in 2015, with Blumberg Capital, LionBird, Pivot Investment Partners, Edison Partners and Espresso Capital also investing. U.S.
  Bank agreed to acquire Bento Technologies on August 11, 2021 and closed the acquisition on August 31, 2021, folding the product into U.S. Bank''s small-business spend management offering. The Bento card program was then wound down: card reloads stopped April 30, 2024 and all card program services were discontinued June 25, 2024, with customers directed to alternative providers. The developer surface is retired — apidocs.bentoforbusiness.com and api.bentoforbusiness.com no longer resolve in DNS, and bentoforbusiness.com now redirects to U.S. Bank. This profile is retained as a historical record of a former API provider; there is no live API to consume.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bento.png
layout: provider
modified: '2026-07-20'
name: Bento
nav: Providers
network: true
overview: Bento is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Payments, and Spend Management.
random_paper: 11
score:
  band: minimal
  composite: 2.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bento/refs/heads/main/screenshots/bento-2026-07-25T202736.png
security:
- kind: domain-security
  name: Bento Domain Security
  slug: bento-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bento
tags:
- Company
- Financial-Services
- Fintech
- Payments
- Spend Management
- Expense Management
- Corporate Cards
- Virtual Cards
- Small Business
- Acquired
website: https://bentoforbusiness.com
---
