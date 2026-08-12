---
access_model:
  confidence: high
  label: Enterprise · Approval required
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - authentication
  - documentation
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 15
apis:
- description: 'Secure, real-time EOI decisioning on a benefit technology partner''s platform when required by an elected Guardian benefit. Employees required to submit EOI are presented the required health questions '
  name: Evidence of Insurability (EOI) API
  slug: evidence-of-insurability
- description: 'Secure, real-time access to read and update employee and dependent benefit data. Once a Guardian policy is established, benefit technology partners use the Member Benefits API endpoints to enroll and '
  name: Benefits API
  slug: benefits
- description: Secure, real-time access to Guardian benefit plan information including all of the insurance product rules, attributes, and rates required to configure a Guardian plan on a benefit technology partner'
  name: Policy API
  slug: policy
- description: Real-time quote and product info exposed through higher-level capabilities rather than lower-level APIs requiring intimate system knowledge, fronted by an orchestration layer so retail products can be
  name: Retail Individual Products
  slug: retail-individual-products
- description: Secure, real-time access to request and retrieve a quote for Guardian products. The technology partner requests a quote for any product by supplying specific details regarding the broker, policy holde
  name: Group Rating & Quoting API
  slug: group-rating-quoting
- description: Create and access membership information for the HMB membership.
  name: HMB API
  slug: hmb
- description: Centralized Underwriting Data API providing business and technical services for saving and retrieving underwriting data from the Centralized Underwriting Database. Services include saving UW data into
  name: Underwriting Data Service
  slug: underwriting-data-service
- description: Returns a list of providers with location information for Group Commercial Dental Insurance.
  name: Group Dental Provider API
  slug: group-dental-provider
- description: Generates illustrations for life insurance products.
  name: GPS Illustration API
  slug: gps-illustration
- description: 'Secure, real-time access to request provider benefits verification for members and dependents. The technology partner generates a request by supplying group policy number, patient relation to member, '
  name: Group Verification of Benefits API
  slug: group-verification-of-benefits
- description: Allows third parties such as agents and partners to securely send application prefill information related to a potential client's life or disability application, collected by the third party and inten
  name: Guardian eSuite Prefill API
  slug: esuite-prefill
- description: FileNet CM REST APIs allowing authorized external vendors and partners to add, search, retrieve, and update metadata of documents within the FileNet CM repository.
  name: IBM FileNet Content Manager API
  slug: filenet-content-manager
- description: API to post eOffer policy information.
  name: eOffer Policy External
  slug: eoffer-policy-external
- description: A Guardian Online (GOL) API that connects Avantos and SmartOffice to synchronize contact data and support SSN lookup for Avantos.
  name: Avantos to SmartOffice Contact Sync API
  slug: avantos-smartoffice-contact-sync
- description: Validates the regulatory licensing status of financial professionals or firms registered with the Financial Industry Regulatory Authority (FINRA), ensuring individuals or entities involved in securiti
  name: FINRA License Check API
  slug: finra-license-check
artifact_total: 17
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.guardianlife.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.guardianlife.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.guardianlife.com/getting-started
- group: operate
  title: ''
  type: FAQ
  url: https://developer.guardianlife.com/faq
- group: other
  title: ''
  type: Registration
  url: https://developer.guardianlife.com/partner/register/activate
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.guardianlife.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://developer.guardianlife.com/contact/feedback
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/guardian-life-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/guardian-life-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/guardian-life-insurance-co-of-america
- group: company
  title: ''
  type: Website
  url: https://www.guardianlife.com
- group: company
  title: ''
  type: About
  url: https://www.guardianlife.com/about-guardian
- group: operate
  title: ''
  type: Contact
  url: https://www.guardianlife.com/contact-us
- group: company
  title: ''
  type: PressCenter
  url: https://www.guardianlife.com/news/press-center
created: '2026-03-21'
description: 'The Guardian Life Insurance Company of America is one of the largest mutual life insurance companies in the United States, providing life insurance, disability income insurance, dental insurance, and other employee benefits. Guardian operates a partner developer portal, Guardian Connect, built on Apigee, exposing a catalog of group and retail insurance APIs covering evidence of insurability, member benefits enrollment, policy and plan configuration, group rating and quoting, dental provider directory and verification of benefits, underwriting data, and life illustration. The Member Benefits APIs implement the LIMRA Data Exchange (LDEx) Standards. Access is partner-gated: a partner agreement is established first, after which Guardian issues a registration code and partner key, and API keys are minted per partner app subject to administrator approval. Authentication is JWT with OpenID Connect login. No OpenAPI, Swagger, or other machine-readable contract is published publicly
  — the API reference sits behind partner login — so the APIs below are recorded from Guardian''s own public catalog descriptions.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/guardian-life.png
layout: provider
modified: '2026-08-06'
name: Guardian Life
nav: Providers
network: true
overview: 'Guardian Life publishes 15 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Life Insurance, Disability Insurance, Dental Insurance, and Employee Benefits.


  Guardian Life''s developer surface includes API reference, getting-started guide, FAQ, support, and 10 more developer resources.'
press:
- date: '2026-05-25'
  title: AM Best Affirms Credit Ratings of Guardian Life Insurance ...
  url: https://news.ambest.com/newscontent.aspx?refnum=242902&altsrc=23
random_paper: 28
score:
  band: emerging
  composite: 18.3
  delta: 2.2
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 24.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/guardian-life/refs/heads/main/screenshots/guardian-life-2026-06-20T182426.png
security:
- kind: domain-security
  name: Guardian Life Domain Security
  slug: guardian-life-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Guardian Life Vulnerability Disclosure
  slug: guardian-life-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: guardian-life
tags:
- Insurance
- Life Insurance
- Disability Insurance
- Dental Insurance
- Employee Benefits
- Benefits Administration
- Group Insurance
- Underwriting
- Claims Processing
- LDEx
- Fortune 500
website: https://www.guardianlife.com
---
