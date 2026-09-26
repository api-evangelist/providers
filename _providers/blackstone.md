---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: 'Blackstone provides institutional and individual investors with access to portfolio information, capital account statements, fund documents, and reporting through its Investor Portal, which is served '
  name: Blackstone Investor Portal
  slug: blackstone-investor-portal
artifact_total: 31
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/security/blackstone-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blackstone-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blackstoneinc
- group: company
  title: ''
  type: Website
  url: https://www.blackstone.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.blackstone.com/investor-resources/
- group: start
  title: ''
  type: Login
  url: https://www.bxaccess.com
- group: operate
  title: ''
  type: Support
  url: https://www.bxaccess.com/Auth/NeedHelp
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.blackstone.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/well-known/blackstone-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blackstone-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/authentication/blackstone-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blackstone-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/scopes/blackstone-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/blackstone-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/conformance/blackstone-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blackstone-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/security/blackstone-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blackstone-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/security/blackstone-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/blackstone-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/llms/blackstone-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blackstone-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/plans/blackstone-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blackstone-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/rate-limits/blackstone-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/blackstone-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/finops/blackstone-finops.yml
  title: ''
  type: FinOps
  url: finops/blackstone-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/rules/blackstone-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/blackstone-jsonschema-spectral-rules.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blackstone.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blackstone.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.blackstone.com/insights/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/rules/blackstone-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/blackstone-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/vocabulary/blackstone-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/blackstone-vocabulary.yaml
coverage:
  checked: '2026-08-10'
  detail: Blackstone runs a real GitBook developer-documentation site at docs.blackstone.com, but every path on it — including /openapi.json, /llms.txt and /robots.txt — 307s to the GitBook VA-Okta visitor-auth handshake against Blackstone's Okta tenant at login.bx.com, so no contract is readable without a Blackstone-issued identity.
  evidence:
  - status: 307
    url: https://docs.blackstone.com/openapi.json
  - status: 307
    url: https://docs.blackstone.com/llms.txt
  - status: 302
    url: https://www.bxaccess.com/openapi.json
  - status: 403
    url: https://www.blackstone.com/robots.txt
  - status: 200
    url: https://auth.bx.com/identity-broker/.well-known/openid-configuration
  reason: customer-only-docs
  state: gated
created: '2026-03-21'
description: Blackstone is the world's largest alternative asset manager with over $1 trillion in assets under management across private equity, real estate, credit, and hedge fund strategies. Blackstone serves institutional investors including pension funds, sovereign wealth funds, endowments, and foundations, as well as accredited individual investors through its private wealth solutions. Technology and data platforms are central to Blackstone's investment operations and portfolio company management.
examples:
- key_count: 12
  name: Blackstone Fund Example
  slug: blackstone-fund-example
- key_count: 8
  name: Blackstone Investor Account Example
  slug: blackstone-investor-account-example
features:
- description: Web-based portal providing investors with access to fund performance, capital account statements, distributions, and investor documents.
  name: Investor Portal
- description: Quarterly and annual fund-level reporting including audited financials, NAV calculations, and investor-level P&L attribution.
  name: Fund Reporting
- description: Blackstone's data science and technology teams develop proprietary data products and integrations to support portfolio company operations and investment research.
  name: Alternative Data Integration
- description: Blackstone actively supports portfolio companies in technology transformation, digital infrastructure buildout, and enterprise software adoption.
  name: Portfolio Company Technology
- description: Automated delivery of capital call and distribution notices to investors via the portal, email, and data feed integrations.
  name: Capital Call and Distribution Notices
- description: Annual K-1 and other tax documents delivered electronically to limited partners through the Investor Portal.
  name: Tax Document Delivery
finops:
- name: Blackstone Finops
  service_category: Alternative Asset Management
  slug: blackstone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blackstone.png
integrations:
- description: Blackstone distributes alternative investments to wealth management clients through iCapital Network's feeder fund and technology platform.
  name: iCapital Network
- description: Blackstone alternative investment products are available through the CAIS platform for independent and institutional advisors.
  name: CAIS
- description: Blackstone Real Estate uses Yardi for property management, accounting, and data reporting across its real estate portfolio.
  name: Yardi
- description: Blackstone's credit and private equity operations use Allvue for portfolio monitoring, investor reporting, and fund accounting.
  name: Allvue Systems
json_schemas:
- name: Blackstone Fund
  property_count: 12
  slug: blackstone-fund
- name: Blackstone Investor Account
  property_count: 8
  slug: blackstone-investor-account
json_structures:
- name: Blackstone Fund Structure
  property_count: 0
  slug: blackstone-fund-structure
- name: Blackstone Investor Account Structure
  property_count: 0
  slug: blackstone-investor-account-structure
jsonld:
- class_count: 13
  name: Blackstone Context
  property_count: 0
  slug: blackstone-context
layout: provider
modified: '2026-08-10'
name: Blackstone
nav: Providers
network: true
overview: 'Blackstone publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Alternative Assets, Finance, Investment Management, Private Equity, and Real Estate.


  The Blackstone catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Blackstone''s developer surface includes documentation, support, authentication, engineering blog, and 19 more developer resources.'
plans:
- name: Blackstone Plans Pricing
  plan_count: 1
  slug: blackstone-plans-pricing
press:
- date: ''
  title: The world's largest alternative asset manager, Blackstone ...
  url: https://www.facebook.com/abc27news/posts/the-worlds-largest-alternative-asset-manager-blackstone-announced-it-has-entered/1392458756245685/
- date: ''
  title: Blackstone Announces Joint Venture with Google to Create New TPU Cloud
  url: https://www.blackstone.com/news/press/blackstone-announces-joint-venture-with-google-to-create-new-tpu-cloud/
- date: ''
  title: Our People
  url: https://www.blackstone.com/the-firm/our-people/
- date: ''
  title: Blackstone Life Sciences Invests $250 Million in Anagram Therapeutics to Advance Novel and Patient-Friendly Oral Enzyme Replacement Therapy for Pancreatic Insufficiency
  url: https://www.blackstone.com/news/press/blackstone-life-sciences-invests-250-million-in-anagram-therapeutics-to-advance-novel-and-patient-friendly-oral-enzyme-replacement-therapy-for-pancreatic-insufficiency/
- date: ''
  title: Blackstone’s Global Infrastructure Head on Data Center Growth and Community Involvement
  url: https://www.blackstone.com/news/in-the-news/blackstones-global-infrastructure-head-on-data-center-growth-and-community-involvement/
- date: ''
  title: Private Investment Continues to Fuel AI Innovation Across ...
  url: https://www.investmentcouncil.org/private-investment-continues-to-fuel-ai-innovation-across-the-country/
- date: ''
  title: Anthropic Partners with Blackstone, Hellman & Friedman, and Goldman Sachs to Launch Enterprise AI Services Firm
  url: https://www.blackstone.com/news/press/anthropic-partners-with-blackstone-hellman-friedman-and-goldman-sachs-to-launch-enterprise-ai-services-firm/
- date: ''
  title: Blackstone confirms $13 billion investment in Britain for AI ...
  url: https://www.reuters.com/technology/artificial-intelligence/blackstone-confirms-13-bln-investment-britain-ai-data-centre-2024-09-25/
random_paper: 6
rate_limits:
- limit_count: 1
  name: Blackstone Rate Limits
  slug: blackstone-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Blackstone API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: blackstone-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Blackstone API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: blackstone-spectral-rules
scopes:
- name: Blackstone Scopes
  scope_count: 0
  slug: blackstone-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 80.8
    catalog_earned_first_party: 16.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.3
  facets:
    access_clarity: 46.1
    contract_governance: 28.0
    contract_quality: 29.2
    developer_ergonomics: 14.3
    discoverability: 73.2
    operational_transparency: 31.6
  previous_composite: 35.0
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/blackstone/refs/heads/main/screenshots/blackstone-2026-06-20T173341.png
security:
- kind: authentication
  name: Blackstone Authentication
  slug: blackstone-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Blackstone Domain Security
  slug: blackstone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Blackstone Vulnerability Disclosure
  slug: blackstone-vulnerability-disclosure
  summary_line: disclosure policy published
slug: blackstone
tags:
- Alternative Assets
- Finance
- Investment Management
- Private Equity
- Real Estate
- Fortune 500
use_cases:
- description: Institutional LPs access fund reporting, capital call and distribution notices, and tax documents through the investor portal or via data integrations.
  name: Institutional Investor Reporting
- description: Blackstone's investment teams use proprietary data platforms to monitor portfolio company performance metrics, market signals, and risk indicators.
  name: Portfolio Monitoring
- description: Third-party data aggregators and institutional investor platforms may access Blackstone investor data via direct data feed agreements.
  name: Data Aggregation
- description: Registered investment advisors and wealth managers access Blackstone alternative products through platform integrations for accredited investor clients.
  name: Wealth Management Distribution
website: https://www.blackstone.com
---
