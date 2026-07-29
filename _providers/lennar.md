---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
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
api_count: 2
apis:
- description: 'Azure API Management developer portal for Lennar Corporation. Allows developers to discover Lennar APIs, sign up for an API key, read the auto-generated reference, and exercise endpoints from the API '
  name: Lennar Corporation Developer Portal
  slug: lennar-corporation-developer-portal
- description: Lennar Mortgage, LLC is listed as a Fannie Mae technology integration partner using Fannie Mae's lending APIs. The technical contract is owned by Fannie Mae; Lennar Mortgage is the consumer.
  name: Lennar Mortgage Fannie Mae Integration
  slug: lennar-mortgage-fannie-mae
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lennar-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lennar
- group: company
  title: ''
  type: Website
  url: https://www.lennar.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://azu-lndscapmu01e.portal.azure-api.net/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor-marketplace.lennar.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lennar.com/privacypolicy
- group: other
  title: ''
  type: BusinessInquiries
  url: https://www.lennar.com/contact/business-inquiry
created: '2026-03-21'
description: Lennar Corporation is a Fortune 500 company and one of the leading homebuilders of new homes for sale in the United States. Lennar operates an internal Azure-hosted API Management developer portal where Lennar developers and partners discover and consume Lennar Corporation APIs. Public OpenAPI artifacts have not been observed; access generally requires sign-in and partner approval.
finops:
- name: Lennar Finops
  service_category: Real Estate / API
  slug: lennar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lennar.png
layout: provider
modified: '2026-04-28'
name: Lennar
nav: Providers
network: true
overview: Lennar publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Homebuilder, Real Estate, Fortune 500, and Mortgage.
plans:
- name: Lennar Plans Pricing
  plan_count: 1
  slug: lennar-plans-pricing
press:
- date: '2026-05-25'
  title: Lennar Sees a $92M Increase and Saves $650K in Costs
  url: https://3cloudsolutions.com/case-studies/lennar-increases-revenue-with-azure-data-warehouse/
- date: '2026-05-25'
  title: Q4-2025 LEN Earnings Call Transcript
  url: https://investors.lennar.com/~/media/Files/L/Lennar-IR-V3/reports-and-presentations/len-q4-25-earnings-call-transcript.pdf
- date: '2026-05-25'
  title: Lennar builds faster, smarter homebuying journeys with ...
  url: https://www.salesforce.com/customer-stories/lennar/
- date: '2026-05-25'
  title: len-4q24-10-k.pdf
  url: https://investors.lennar.com/~/media/Files/L/Lennar-IR-V3/documents/earnings-releases/len-4q24-10-k.pdf
- date: '2026-05-25'
  title: 'Lennar: Statement on Land-Light Strategy'
  url: https://www.prnewswire.com/news-releases/lennar-statement-on-land-light-strategy-302728846.html
random_paper: 8
rate_limits:
- limit_count: 1
  name: Lennar Rate Limits
  slug: lennar-rate-limits
score:
  band: emerging
  composite: 17.4
  delta: -1.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lennar/refs/heads/main/screenshots/lennar-2026-06-20T184422.png
security:
- kind: domain-security
  name: Lennar Domain Security
  slug: lennar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lennar
tags:
- Homebuilder
- Real Estate
- Fortune 500
- Mortgage
website: https://www.lennar.com
---
