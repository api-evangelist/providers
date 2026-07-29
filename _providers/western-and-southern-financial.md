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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: Life insurance, annuities, and retirement products offered by Western & Southern Life Insurance Company. Customers can access account information, policy details, and manage their coverage through dig
  name: Western & Southern Life
  slug: western-southern-life
- description: Gerber Life Insurance Company (a W&S subsidiary) provides term life, whole life, accident protection, and college savings plans for families and children.
  name: Gerber Life Insurance
  slug: gerber-life
- description: 'Touchstone Investments provides mutual funds, separate accounts, and investment management services. Asset managers and advisors integrate fund data, performance, and documentation through the firm''s '
  name: Touchstone Investments
  slug: touchstone-investments
- description: Fort Washington Investment Advisors is the institutional asset management arm of Western & Southern, providing portfolio management and alternative investment strategies to institutional clients and i
  name: Fort Washington Investment Advisors
  slug: fort-washington-investment
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/western-and-southern-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.westernsouthern.com
- group: company
  title: ''
  type: About
  url: https://www.westernsouthern.com/about
- group: start
  title: ''
  type: Portal
  url: https://www.westernsouthern.com/about/family-of-companies
- group: operate
  title: ''
  type: Contact
  url: https://www.westernsouthern.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.westernsouthern.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.westernsouthern.com/terms-of-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/western-&-southern-financial-group
description: Western & Southern Financial Group is a diversified family of financial services companies headquartered in Cincinnati, Ohio, offering life insurance, annuities, mutual funds, asset management, and other financial products through multiple subsidiary brands including Western & Southern Life, Gerber Life, Columbus Life, and Fort Washington Investment Advisors.
finops:
- name: Western And Southern Financial Finops
  service_category: Insurance
  slug: western-and-southern-financial-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/western-and-southern-financial.png
json_schemas:
- name: Annuity Contract
  property_count: 13
  slug: western-and-southern-financial-annuity
- name: Insurance Policy
  property_count: 13
  slug: western-and-southern-financial-policy
json_structures:
- name: Western And Southern Financial Policy Structure
  property_count: 0
  slug: western-and-southern-financial-policy-structure
jsonld:
- class_count: 5
  name: Western And Southern Financial Context
  property_count: 25
  slug: western-and-southern-financial-context
layout: provider
modified: '2026-05-03'
name: western-and-southern-financial
nav: Providers
network: true
overview: 'western-and-southern-financial publishes 4 APIs on the [APIs.io](https://apis.io/) network.


  The western-and-southern-financial catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  western-and-southern-financial''s developer surface includes developer portal and 7 more developer resources.'
plans:
- name: Western And Southern Financial Plans Pricing
  plan_count: 1
  slug: western-and-southern-financial-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 1
  name: Western And Southern Financial Rate Limits
  slug: western-and-southern-financial-rate-limits
rules:
- name: western-and-southern-financial API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: western-and-southern-financial-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.8
  delta: -4.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 17.7
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 36.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/western-and-southern-financial/refs/heads/main/screenshots/western-and-southern-financial-2026-06-20T201402.png
security:
- kind: domain-security
  name: Western And Southern Financial Domain Security
  slug: western-and-southern-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: western-and-southern-financial
website: https://www.westernsouthern.com
---
