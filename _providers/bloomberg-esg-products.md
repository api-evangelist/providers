---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: Access Bloomberg ESG scores, environmental metrics, social indicators, and governance data for thousands of publicly listed companies globally. Data sourced directly from company disclosures and stand
  name: Bloomberg ESG Data API
  slug: esg-data-api
- description: Access physical and transition climate risk data, carbon emissions data, TCFD-aligned metrics, and scenario analysis tools through Bloomberg's climate data solutions.
  name: Bloomberg Climate Data API
  slug: climate-data-api
- description: Comprehensive data on green, social, sustainability, and sustainability-linked bonds including use of proceeds, certifications, and post-issuance reporting aligned to ICMA principles.
  name: Bloomberg Green Bond Data
  slug: green-bond-data
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-esg-products-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bloomberg.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
created: '2024-01-01'
description: Bloomberg ESG Products provide environmental, social, and governance data, analytics, and scores to help investors assess sustainability risks and opportunities. Bloomberg collects ESG data from thousands of companies globally, offering ESG scores, climate data, green bond data, and sustainable finance analytics through the Bloomberg Terminal and API.
features:
- description: Standardized ESG scores for thousands of companies based on disclosed data.
  name: ESG Scores
- description: Carbon emissions, water usage, energy consumption, and waste data.
  name: Environmental Metrics
- description: Employee relations, diversity metrics, health and safety, and community data.
  name: Social Indicators
- description: Board composition, executive compensation, shareholder rights, and audit data.
  name: Governance Data
- description: Physical and transition climate risk metrics aligned to TCFD framework.
  name: Climate Risk Analytics
- description: Green bond, social bond, and sustainability-linked loan data.
  name: Sustainable Finance Data
finops:
- name: Bloomberg Esg Products Finops
  service_category: API
  slug: bloomberg-esg-products-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-esg-products.png
layout: provider
modified: '2026-04-21'
name: Bloomberg ESG Products
nav: Providers
network: true
overview: 'Bloomberg ESG Products publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ESG, Sustainability, Environmental Data, Social Data, and Governance Data.


  Bloomberg ESG Products'' developer surface includes developer portal, documentation, support, and 3 more developer resources.'
plans:
- name: Bloomberg Esg Products Plans Pricing
  plan_count: 3
  slug: bloomberg-esg-products-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Bloomberg Esg Products Rate Limits
  slug: bloomberg-esg-products-rate-limits
score:
  band: emerging
  composite: 19.6
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 19.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-esg-products/refs/heads/main/screenshots/bloomberg-esg-products-2026-06-20T173426.png
security:
- kind: domain-security
  name: Bloomberg Esg Products Domain Security
  slug: bloomberg-esg-products-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-esg-products
tags:
- ESG
- Sustainability
- Environmental Data
- Social Data
- Governance Data
- Climate Data
- Bloomberg
use_cases:
- description: Integrate ESG factors into investment analysis and portfolio construction.
  name: ESG Integration
- description: Support SFDR, EU Taxonomy, and other ESG regulatory reporting requirements.
  name: Regulatory Reporting
- description: Use ESG data to support shareholder engagement and proxy voting decisions.
  name: Stewardship and Engagement
- description: Develop ESG-linked financial products and indices.
  name: Sustainable Product Development
- description: Assess and disclose climate-related financial risks in portfolios.
  name: Climate Risk Assessment
website: https://www.bloomberg.com/professional/
---
