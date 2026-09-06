---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Seon Tech Agentic Access
  operation_count: 6
  slug: seon-tech-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 11
apis:
- description: SEON Device Intelligence is the device-fingerprinting product surfaced through JavaScript, iOS, Android, Flutter, React Native, Cordova, and Unity SDKs. Captured device signals (True Device ID, hashes
  name: SEON Device Intelligence
  slug: device-intelligence
- description: SEON Identity Verification (IDV) is an AI-powered identity verification product combining document checks, biometric liveness, and enriched fraud signals. Integration is via native iOS and Android SDK
  name: SEON Identity Verification
  slug: idv
- description: SEON Orchestration lets customers compose multi-step fraud, KYC, and risk workflows that combine SEON enrichment with third-party providers. Integration is via the Orchestration SDKs for iOS, Android,
  name: SEON Orchestration
  slug: orchestration
- description: User Session Monitoring streams in-session behavioral, device, and risk signals for continuous account-takeover and session-hijacking detection across web, iOS, and Android. Delivered via dedicated St
  name: SEON User Session Monitoring
  slug: user-session-monitoring
- baseURL: https://api.seon.io/SeonRestService/fraud-api/v2/
  baseurl_source: declared
  description: The AML API from SEON — 1 operation(s) for aml.
  name: SEON AML API
  slug: seon-tech-aml-api
- baseURL: https://api.seon.io/SeonRestService/fraud-api/v2/
  baseurl_source: declared
  description: The BIN API from SEON — 1 operation(s) for bin.
  name: SEON BIN API
  slug: seon-tech-bin-api
- baseURL: https://api.seon.io/SeonRestService/fraud-api/v2/
  baseurl_source: declared
  description: The Email API from SEON — 1 operation(s) for email.
  name: SEON Email API
  slug: seon-tech-email-api
- baseURL: https://api.seon.io/SeonRestService/fraud-api/v2/
  baseurl_source: declared
  description: The Fraud API from SEON — 1 operation(s) for fraud.
  name: SEON Fraud API
  slug: seon-tech-fraud-api
- baseURL: https://api.seon.io/SeonRestService/fraud-api/v2/
  baseurl_source: declared
  description: The IP API from SEON — 1 operation(s) for ip.
  name: SEON IP API
  slug: seon-tech-ip-api
- baseURL: https://api.seon.io/SeonRestService/fraud-api/v2/
  baseurl_source: declared
  description: The Phone API from SEON — 1 operation(s) for phone.
  name: SEON Phone API
  slug: seon-tech-phone-api
- baseURL: https://api.seon.io/SeonRestService/fraud-api/v2/
  baseurl_source: declared
  description: Transaction outcome labeling for machine-learning feedback.
  name: SEON Labels API
  slug: seon-tech-labels-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SEON AML API
  slug: open-seon-tech-aml-api
- collection_type: open
  name: SEON AML BIN API
  slug: open-seon-tech-bin-api
- collection_type: open
  name: SEON AML Email API
  slug: open-seon-tech-email-api
- collection_type: open
  name: SEON AML Fraud API
  slug: open-seon-tech-fraud-api
- collection_type: open
  name: SEON AML IP API
  slug: open-seon-tech-ip-api
- collection_type: open
  name: SEON REST AML Labels API
  slug: open-seon-tech-labels-api
- collection_type: open
  name: SEON AML Phone API
  slug: open-seon-tech-phone-api
- collection_type: open
  name: SEON API
  slug: open-seon-tech
- collection_type: open
  name: SEON REST API
  slug: open-seon
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/seon-tech-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/seon-tech-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seon-tech-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/seon-tech-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://seon.io/
- group: start
  title: ''
  type: Portal
  url: https://docs.seon.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.seon.io/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.seon.io/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://docs.seon.io/api-reference/introduction
- group: start
  title: ''
  type: Signup
  url: https://admin.seon.io/sign-up
- group: start
  title: ''
  type: Login
  url: https://admin.seon.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://seon.io/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.seon.io/
- group: company
  title: ''
  type: Blog
  url: https://seon.io/resources/
- group: company
  title: ''
  type: BlogRSS
  url: https://seon.io/resources/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seon.io/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seon.io/privacy-policy/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://seon.io/security/
- group: auth
  title: ''
  type: ResponsibleDisclosure
  url: https://seon.io/rdp/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seontechnologies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/seon-tech
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/seon_tech
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/seon-technologies
- group: other
  title: ''
  type: Customers
  url: https://seon.io/customers/
- group: other
  title: ''
  type: CaseStudies
  url: https://seon.io/case-studies/
- group: company
  title: ''
  type: Careers
  url: https://seon.io/careers/
- group: operate
  title: ''
  type: ContactUs
  url: https://seon.io/contact-us/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.seon.io/llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/seon-tech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/seon-tech-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/seon-tech-finops.yml
created: '2026-05-25'
description: SEON is a Budapest-headquartered fraud prevention, AML compliance, and digital footprint analysis platform that exposes a modular REST API for fraud scoring, identity verification, email enrichment, phone enrichment, IP intelligence, BIN lookup, AML screening, device intelligence, and identity verification (IDV). SEON combines real-time enrichment of email, phone, IP, BIN, and device signals with customer-defined rules and machine learning to score risk and prevent fraud, account takeover, multi-accounting, and money laundering across digital channels.
finops:
- name: Seon Tech Finops
  service_category: API
  slug: seon-tech-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seon-tech.png
layout: provider
modified: '2026-08-08'
name: SEON
nav: Providers
network: true
overview: 'SEON publishes 7 APIs on the [APIs.io](https://apis.io/) network, including AML API, BIN API, Email API, and 4 more. Tagged areas include AML Compliance, Device Intelligence, Digital Footprint, Fraud Prevention, and Identity Verification.


  SEON''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 24 more developer resources.'
plans:
- name: Seon Tech Plans Pricing
  plan_count: 3
  slug: seon-tech-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Seon Tech Rate Limits
  slug: seon-tech-rate-limits
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 0.0
    contract_quality: 52.5
    developer_ergonomics: 61.9
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seon-tech/refs/heads/main/screenshots/seon-tech-2026-06-20T193713.png
security:
- kind: authentication
  name: Seon Tech Authentication
  slug: seon-tech-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Seon Tech Domain Security
  slug: seon-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Seon Tech Trust Center
  slug: seon-tech-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: seon-tech
tags:
- AML Compliance
- Device Intelligence
- Digital Footprint
- Fraud Prevention
- Identity Verification
- Risk Scoring
website: https://seon.io/
---
