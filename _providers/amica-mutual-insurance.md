---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Amica Mutual Insurance provides a full range of personal insurance products including auto, home, life, condo, renters, marine, motorcycle, umbrella, and flood insurance. The company does not currentl
  name: Amica Mutual Insurance Website
  slug: website
artifact_total: 23
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amica-mutual-insurance-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amicamutual
- group: start
  title: ''
  type: Portal
  url: https://www.amica.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amica.com/en/footer/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amica.com/en/footer/terms-of-use.html
- group: operate
  title: ''
  type: Support
  url: https://www.amica.com/en/contact-us.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amica-mutual-insurance-company
created: '2024-01-01'
description: Amica Mutual Insurance, founded in 1907, is a mutual insurance company providing automobile, homeowners, condo, renters, life, marine, motorcycle, umbrella liability, flood, and small business insurance to customers across the United States. As a mutual company, Amica is owned by its policyholders and known for award-winning customer service and competitive pricing through bundling discounts.
features:
- description: Comprehensive automobile insurance coverage including collision, comprehensive, liability, medical payments, and uninsured motorist protection with roadside assistance.
  name: Auto Insurance
- description: Homeowners insurance including Platinum Choice Home policy providing up to 30% additional dwelling coverage, personal property, and liability protection.
  name: Home Insurance
- description: Term life, whole life, and universal life insurance products plus annuities for retirement income planning.
  name: Life Insurance
- description: Condominium insurance covering personal property, liability, and loss assessment for condo owners.
  name: Condo Insurance
- description: Renters insurance protecting personal property and providing liability coverage for apartment and home renters.
  name: Renters Insurance
- description: Personal umbrella liability insurance providing additional liability coverage above auto and home policy limits.
  name: Umbrella Insurance
- description: Boat and watercraft insurance for pleasure craft, sailboats, and personal watercraft.
  name: Marine Insurance
- description: Flood insurance coverage for homes and personal property in flood-prone areas.
  name: Flood Insurance
- description: Commercial insurance solutions for small businesses including property, liability, and business owner policies.
  name: Small Business Insurance
- description: 24/7 online account management, mobile app access, claim reporting and tracking, and policy management tools.
  name: Digital Account Management
finops:
- name: Amica Mutual Insurance Finops
  service_category: Insurance
  slug: amica-mutual-insurance-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amica-mutual-insurance.png
integrations:
- description: Referral network connecting policyholders with pre-screened contractors for home repair and restoration after covered losses.
  name: Contractor Connection
- description: 24/7 roadside assistance service integration for towing, battery jump-starts, flat tire changes, and fuel delivery.
  name: Roadside Assistance Network
layout: provider
modified: '2026-04-19'
name: Amica Mutual Insurance
nav: Providers
network: true
overview: 'Amica Mutual Insurance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Auto Insurance, Home Insurance, Life Insurance, and Mutual Insurance.


  Amica Mutual Insurance''s developer surface includes developer portal, support, and 5 more developer resources.'
plans:
- name: Amica Mutual Insurance Plans Pricing
  plan_count: 1
  slug: amica-mutual-insurance-plans-pricing
press:
- date: '2026-05-25'
  title: Amica Mutual Insurance Joins HOVER and CoreLogic to ...
  url: https://iconoutlook.com/amica-mutual-insurance-joins-hover-and-corelogic-to-transform-underwriting-inspections/
- date: '2026-05-25'
  title: Amica Mutual Insurance Company Delivers Outstanding ...
  url: https://www.businesswire.com/news/home/20250319522296/en/Amica-Mutual-Insurance-Company-Delivers-Outstanding-Customer-Care-with-Strategy-One
- date: '2026-05-25'
  title: Amica Mutual Insurance Company News Monitoring
  url: https://insurance.einnews.com/news/amica-mutual-insurance-company
- date: '2026-05-25'
  title: Insurer Expands AI to Assess Climate Risk
  url: https://rethinking65.com/insurer-expands-ai-to-assess-climate-risk/
- date: '2026-05-25'
  title: Amica Mutual Insurance Expands Partnership With ZestyAI ...
  url: https://www.prnewswire.com/news-releases/amica-mutual-insurance-expands-partnership-with-zestyai-to-enhance-property-risk-assessment-in-the-face-of-increasing-climate-risks-302208765.html
random_paper: 3
rate_limits:
- limit_count: 1
  name: Amica Mutual Insurance Rate Limits
  slug: amica-mutual-insurance-rate-limits
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 9.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amica-mutual-insurance/refs/heads/main/screenshots/amica-mutual-insurance-2026-06-20T171928.png
security:
- kind: domain-security
  name: Amica Mutual Insurance Domain Security
  slug: amica-mutual-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amica-mutual-insurance
tags:
- Insurance
- Auto Insurance
- Home Insurance
- Life Insurance
- Mutual Insurance
- Personal Insurance
- Financial-Services
use_cases:
- description: Protect against vehicle damage, accidents, theft, and liability with comprehensive auto insurance and roadside assistance.
  name: Auto Coverage
- description: Insure homes against damage from fire, storms, theft, and other perils with flexible coverage options including extended replacement cost.
  name: Home Protection
- description: Combine multiple insurance policies (auto, home, life) for premium discounts and simplified policy management through a single insurer.
  name: Policy Bundling
- description: Secure family financial protection and retirement income planning with term, whole life, and annuity products.
  name: Life Insurance Planning
- description: Protect personal assets from large liability claims exceeding standard policy limits with umbrella insurance coverage.
  name: Liability Protection
- description: File, track, and manage insurance claims 24/7 through online portal, mobile app, or dedicated claims representatives.
  name: Claims Management
website: https://www.amica.com
---
