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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 6
apis:
- description: 'Access Westlaw legal research content including case law, statutes, regulations, and secondary sources. Includes SEC Filings API, Dockets API, and Litigation Analytics providing structured legal data '
  name: Thomson Reuters Westlaw API
  slug: westlaw-api
- description: Checkpoint Search API provides access to Thomson Reuters Checkpoint tax and accounting research content including tax regulations, guidance, and analytical tools for tax professionals and accountants.
  name: Thomson Reuters Checkpoint API
  slug: checkpoint-api
- description: ONESOURCE APIs provide integration with Thomson Reuters tax compliance software including income tax, indirect tax, transfer pricing, and global trade management. Enables workflow automation for tax c
  name: Thomson Reuters ONESOURCE API
  slug: onesource-api
- description: HighQ APIs support document synchronization between HighQ and external document management systems, enabling integration with legal matter management, client collaboration, and document automation wor
  name: Thomson Reuters HighQ API
  slug: highq-api
- description: Legal Tracker API enables users to create and manage legal matters, invoices, budgets, and vendor relationships programmatically, supporting e-billing and legal spend management integrations.
  name: Thomson Reuters Legal Tracker API
  slug: legal-tracker-api
- description: Risk and Fraud APIs automate customer onboarding, identity verification, risk assessments, adverse media screening, investigations, and compliance monitoring. Includes tools for KYC, AML, and third-pa
  name: Thomson Reuters Risk and Fraud API
  slug: risk-fraud-api
artifact_total: 11
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/thomson-reuters/refs/heads/main/plans/thomson-reuters-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thomson-reuters-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/thomson-reuters/refs/heads/main/rate-limits/thomson-reuters-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/thomson-reuters-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/thomson-reuters/refs/heads/main/finops/thomson-reuters-finops.yml
  title: ''
  type: FinOps
  url: finops/thomson-reuters-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thomson-reuters/refs/heads/main/security/thomson-reuters-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thomson-reuters-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thomson-reuters
- group: company
  title: ''
  type: Website
  url: https://www.thomsonreuters.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.thomsonreuters.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.thomsonreuters.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thomsonreuters
- group: company
  title: ''
  type: Blog
  url: https://www.thomsonreuters.com/en/technology/technology-blog.html
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.thomsonreuters.com/llms.txt
created: '2026-03-16'
description: Thomson Reuters provides over 137 APIs across legal, tax and accounting, risk and fraud, and trade and supply industries through their global developer portal. APIs cover Westlaw legal research, Checkpoint tax content, ONESOURCE tax software, HighQ document management, Legal Tracker matter management, and risk and fraud solutions including identity verification and adverse media screening.
finops:
- has_sources: false
  method: generated
  name: Thomson Reuters Finops
  primary_unit: ''
  service_category: API
  slug: thomson-reuters-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thomson-reuters.png
jsonld:
- class_count: 22
  name: Thomson Reuters Context
  property_count: 0
  slug: thomson-reuters-context
layout: provider
modified: '2026-05-03'
name: Thomson Reuters
nav: Providers
network: true
overview: 'Thomson Reuters is listed with 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Legal, Tax, Finance, Risk Management, and Fraud Prevention.


  The Thomson Reuters catalog on APIs.io includes 1 JSON-LD context.


  Thomson Reuters'' developer surface includes documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Thomson Reuters Plans Pricing
  plan_count: 3
  slug: thomson-reuters-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Thomson Reuters Rate Limits
  slug: thomson-reuters-rate-limits
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 0.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 69.6
    operational_transparency: 10.5
  previous_composite: 13.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/thomson-reuters/refs/heads/main/screenshots/thomson-reuters-2026-06-20T195310.png
security:
- kind: domain-security
  name: Thomson Reuters Domain Security
  slug: thomson-reuters-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: thomson-reuters
tags:
- Legal
- Tax
- Finance
- Risk Management
- Fraud Prevention
- Compliance
- Data
website: https://www.thomsonreuters.com/
---
