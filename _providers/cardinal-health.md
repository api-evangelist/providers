---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Cardinal Health operates an EDI trading partner program for customers and suppliers covering pharmaceutical distribution, medical products, and specialty pharmacy. Integrations use X12 EDI transaction
  name: Cardinal Health EDI Trading Partner Integration
  slug: edi-trading-partner
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/cardinal-health/plans/cardinal-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cardinal-health-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cardinal-health/rate-limits/cardinal-health-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cardinal-health-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cardinal-health/finops/cardinal-health-finops.yml
  title: ''
  type: FinOps
  url: finops/cardinal-health-finops.yml
- group: auth
  href: https://artifacts.apis.io/cardinal-health/security/cardinal-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cardinal-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cardinalhealth.com/
- group: other
  title: ''
  type: Products and Services
  url: https://www.cardinalhealth.com/en/services.html
- group: company
  title: ''
  type: About
  url: https://www.cardinalhealth.com/en/about-us.html
- group: company
  title: ''
  type: Investor Relations
  url: https://ir.cardinalhealth.com/
- group: company
  title: ''
  type: Careers
  url: https://www.cardinalhealth.com/en/about-us/careers.html
- group: operate
  title: ''
  type: Contact
  url: https://www.cardinalhealth.com/en/contact-us.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cardinalhealth.com/en/notices/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cardinalhealth.com/en/notices/privacy-policy.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cardinal-health
- group: other
  title: ''
  type: X
  url: https://x.com/cardinalhealth
- group: design
  href: https://artifacts.apis.io/cardinal-health/conformance/cardinal-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cardinal-health-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cardinal-health/llms/cardinal-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cardinal-health-llms.txt
- group: auth
  href: https://artifacts.apis.io/cardinal-health/security/cardinal-health-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cardinal-health-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cardinal-health/security/cardinal-health-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cardinal-health-vulnerability-disclosure.yml
coverage:
  checked: '2026-09-05'
  detail: 'Cardinal Health runs a real API gateway at api.cardinalhealth.com — Sectigo OV certificate, O=Cardinal Health, Inc. — but it sits inside a Google Cloud VPC Service Controls perimeter and returns 403 SecurityPolicyViolated to every anonymous request, /robots.txt included, while the developer portal that search engines still index as "Cardinal Health API Developer Portal: Home" at developer.np.cardinalhealth.com no longer resolves publicly, leaving the login-only partnerportal.cardinalhealth.com and a contracted trading-partner onboarding as the only way in.'
  evidence:
  - status: 403
    url: https://api.cardinalhealth.com/openapi.json
  - status: 403
    url: https://api.cardinalhealth.com/robots.txt
  - status: 0
    url: https://developer.np.cardinalhealth.com/
  - status: 200
    url: https://partnerportal.cardinalhealth.com/.well-known/api-catalog
  reason: partner-login
  state: gated
created: '2026-03-21'
description: Cardinal Health is a Fortune 15 global integrated healthcare services and products company that provides pharmaceutical distribution, medical-surgical product distribution, and customized solutions for hospitals, health systems, pharmacies, ambulatory surgery centers, clinical laboratories, and physician offices. Cardinal Health does not publish a public developer portal, but it exchanges high volumes of B2B trading data with customers and suppliers via standard X12 EDI transactions (850, 810, 855, 856, 846, 832, 867) over AS2, SFTP, and private API channels. Third-party EDI platforms such as Orderful, Crossfire, SPS Commerce, Zenbridge, DataTrans, Alluvia, ConnectPointz, and Spark Shipping offer managed connectors into Cardinal Health for order-to-cash, inventory, and supply-chain automation.
finops:
- has_sources: false
  method: generated
  name: Cardinal Health Finops
  primary_unit: request
  service_category: API
  slug: cardinal-health-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cardinal-health.png
layout: provider
modified: '2026-09-05'
name: Cardinal Health
nav: Providers
network: true
overview: Cardinal Health is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include B2B, Distribution, EDI, Healthcare, and Medical-Surgical.
plans:
- name: Cardinal Health Plans Pricing
  plan_count: 0
  slug: cardinal-health-plans-pricing
press:
- date: ''
  title: Artificial intelligence policy
  url: https://www.cardinalhealth.com/en/support/artificial-intelligence-policy.html
- date: ''
  title: How artificial intelligence helps patients get the right care
  url: https://newsroom.cardinalhealth.com/2022-06-22-How-artificial-intelligence-helps-patients-get-the-right-care
- date: ''
  title: Cardinal Health Oncology Insights Fifth Edition
  url: https://www.prnewswire.com/news-releases/cardinal-health-oncology-insights-fifth-edition-oncologists-are-optimistic-artificial-intelligence-will-enhance-the-quality-of-patient-care-and-outcomes-300857409.html
- date: ''
  title: How Cardinal Health Uses Technology to Build a Cognitive ...
  url: https://www.fourkites.com/blogs/how-cardinal-health-is-building-a-best-in-class-supply-chain/
- date: ''
  title: Artificial Intelligence at Cardinal Health - Two Use Cases
  url: https://emerj.com/artificial-intelligence-at-cardinal-health/
random_paper: 17
rate_limits:
- limit_count: 0
  name: Cardinal Health Rate Limits
  slug: cardinal-health-rate-limits
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 13.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cardinal-health/cardinal-health-2026-06-20T173956.png
security:
- kind: domain-security
  name: Cardinal Health Domain Security
  slug: cardinal-health-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Cardinal Health Vulnerability Disclosure
  slug: cardinal-health-vulnerability-disclosure
  summary_line: Hackerone
slug: cardinal-health
tags:
- B2B
- Distribution
- EDI
- Healthcare
- Medical-Surgical
- Order-to-Cash
- Pharmaceuticals
- Supply Chain
- Trading Partner
- Fortune 100
website: https://www.cardinalhealth.com/
---
