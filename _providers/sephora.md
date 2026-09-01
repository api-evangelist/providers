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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sephora-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sephora-US-Digital
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sephora
- group: company
  title: ''
  type: Website
  url: https://www.sephora.com/
- group: other
  title: ''
  type: BeautyInsiderLoyalty
  url: https://www.sephora.com/beauty/beauty-insider
- group: other
  title: ''
  type: AffiliateProgram
  url: https://www.sephora.com/help/article/sephora-affiliate-program
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sephora-vocabulary.yml
created: '2026-05-05'
description: Sephora is a French multinational chain of personal care and beauty stores and a subsidiary of LVMH, operating 2,700+ locations worldwide and a large ecommerce footprint. Sephora does not publish a public developer API and does not maintain a public GitHub organization. The Sephora storefront and Beauty Insider loyalty program are accessed only through consumer apps and the website; affiliate marketing partnerships are brokered through third-party networks such as Rakuten Advertising and Skimlinks rather than a Sephora-owned API.
features:
- description: Sephora.com sells cosmetics, skincare, fragrance, and body products
  name: Beauty Storefront
- description: Tiered loyalty program with points, perks, and exclusive events
  name: Beauty Insider Loyalty
- description: Affiliate partnerships brokered through Rakuten Advertising and similar networks
  name: Affiliate Marketing
- description: Hundreds of cosmetic and beauty brands curated for stores and online
  name: Brand Portfolio
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sephora.png
layout: provider
modified: '2026-05-16'
name: Sephora
nav: Providers
network: true
overview: Sephora is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Beauty, Personal Care, and E-Commerce.
random_paper: 19
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 15.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 15.2
    operational_transparency: 2.6
  previous_composite: 6.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sephora/refs/heads/main/screenshots/sephora-2026-06-20T193713.png
security:
- kind: domain-security
  name: Sephora Domain Security
  slug: sephora-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sephora
tags:
- Retail
- Beauty
- Personal Care
- E-Commerce
use_cases:
- description: Customers browse, review, and purchase beauty products
  name: Consumer Beauty Discovery
- description: Beauty Insider members redeem points for products and experiences
  name: Loyalty Redemption
- description: Bloggers earn commissions on referred sales via third-party networks
  name: Content Affiliate Marketing
website: https://www.sephora.com/
---
