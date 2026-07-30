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
api_count: 4
apis:
- description: Human Resources surface of the legacy Certn API used to invite applicants to a hosted screening application, run instant "quick" screens from a single request body, add package items to existing appli
  name: Certn HR API (Legacy v1)
  slug: certn-hr-api
- description: Property Management surface of the legacy Certn API for tenant screening — invite an applicant to complete a screen, run an instant quick screen, add packages to an existing applicant, and list applic
  name: Certn Property Management API (Legacy v2)
  slug: certn-pm-api
- description: Next-generation Certn screening API replacing the deprecated v1/v2 industry-split surfaces. Provides a unified RESTful contract for embedding background checks (criminal, identity, employment, educati
  name: CertnCentric API
  slug: certncentric-api
- description: 'Outbound webhook delivery for asynchronous screening events. Certn posts JSON payloads containing applicant status, result, check_executions, enhanced_identity_verification, rcmp_result, information, '
  name: Certn Webhooks
  slug: certn-webhooks
artifact_total: 23
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/certn-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/certn-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://certn.co
- group: start
  title: ''
  type: Portal
  url: https://certn.co/background-screening-api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.certn.co/api
- group: docs
  title: ''
  type: Documentation
  url: https://centric-api-docs.certn.co/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.certn.co/api/certn-api-v-1.0
- group: commercial
  title: ''
  type: Pricing
  url: https://certn.co/pricing/
- group: start
  title: ''
  type: Signup
  url: https://client.certn.co/ca/login
- group: start
  title: ''
  type: Login
  url: https://client.certn.co/ca/login
- group: other
  title: ''
  type: PersonalProduct
  url: https://mycrc.ca
- group: company
  title: ''
  type: Blog
  url: https://certn.co/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://certn.co/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vault.pactsafe.io
- group: operate
  title: ''
  type: Contact
  url: https://certn.co/contact/
- group: company
  title: ''
  type: Careers
  url: https://certn.co/careers/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.certn.co/
- group: operate
  title: ''
  type: Support
  url: https://certn.zendesk.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://certn.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Partners
  url: https://certn.co/partner-marketplace/
- group: other
  title: ''
  type: Quote
  url: https://certn.co/request-a-quote/
- group: other
  title: ''
  type: CaseStudies
  url: https://certn.co/resources/case-studies/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/certn
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/certn
created: '2026-05-25'
description: Certn is a Canadian background screening platform headquartered in Victoria, British Columbia, providing fast, FCRA / SOC 2 Type II / ISO 27001 compliant background checks for employment, tenant, and partner screening across more than 195 countries. The Certn platform delivers criminal record checks (Canadian Basic and Enhanced, SOQUIJ Quebec, international), identity verification (OneID across 13,500+ document types), employment, education, and credential verification, credit reports, public records and social media screening, reference checks, driver's abstract / MVR, and white-label candidate experiences. Certn exposes a REST API used by 100+ ATS / HRIS partners (Workable, Greenhouse, Lever, Workday and others) to embed screening directly into hiring and leasing workflows, with webhook callbacks for asynchronous result delivery. The legacy v1/v2 API (`api.certn.co`, industry-split HR and Property Management surfaces) was deprecated on 2026-04-13 and will be retired on 2026-08-05;
  new integrations target the CertnCentric API at `centric-api-docs.certn.co`.
features:
- Canadian Basic and Enhanced criminal record checks with RCMP-aligned results
- Quebec SOQUIJ record checks
- International criminal background checks across 200+ countries and territories
- OneID identity verification supporting 13,500+ government document types
- Employment, education, and professional credential verification
- Credit report and public records checks
- Social media screening
- Phone and digital reference checks
- Driver's abstract / motor vehicle records (MVR) checks
- Personal background checks via mycrc.ca consumer brand
- White-label candidate experience embeddable in customer ATS/HRIS
- 100+ pre-built integrations including Workable, Greenhouse, Lever, Workday
- REST API with token authentication and demo (`demo-api.certn.co`) environment
- Outbound webhooks with HMAC-SHA256 signed payloads (`Certn-Signature`) and replay protection
- Rate limits — 120 requests/minute burst, 14,400 requests/24h sustained
- FCRA, SOC 2 Type II, and ISO 27001 compliance posture
- CertnCentric API replacing the legacy HR (`/hr/v1/`) and PM (`/api/v2/`) surfaces
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/certn-com.png
layout: provider
modified: '2026-05-25'
name: Certn
nav: Providers
network: true
overview: 'Certn publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Background Checks, Background Screening, Identity Verification, Criminal Record Checks, and Employment Verification.


  Certn''s developer surface includes developer portal, documentation, getting-started guide, pricing, signup flow, engineering blog, support, and 17 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 24.6
  delta: -2.3
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/certn-com/refs/heads/main/screenshots/certn-com-2026-06-20T174150.png
security:
- kind: domain-security
  name: Certn Com Domain Security
  slug: certn-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Certn Com Vulnerability Disclosure
  slug: certn-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: certn-com
tags:
- Background Checks
- Background Screening
- Identity Verification
- Criminal Record Checks
- Employment Verification
- Education Verification
- Credential Verification
- Credit Checks
- Reference Checks
- Tenant Screening
- Property Management
- Human Resources
- HR Tech
- Compliance
- FCRA
- SOC 2
- ISO 27001
- Canada
website: https://certn.co
---
