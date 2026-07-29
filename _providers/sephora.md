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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
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
overview: Sephora is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Beauty, Personal Care, and Ecommerce.
random_paper: 34
score:
  band: minimal
  composite: 6.0
  delta: -1.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 10.4
    operational_transparency: 5.3
  previous_composite: 7.8
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- Ecommerce
use_cases:
- description: Customers browse, review, and purchase beauty products
  name: Consumer Beauty Discovery
- description: Beauty Insider members redeem points for products and experiences
  name: Loyalty Redemption
- description: Bloggers earn commissions on referred sales via third-party networks
  name: Content Affiliate Marketing
website: https://www.sephora.com/
---
