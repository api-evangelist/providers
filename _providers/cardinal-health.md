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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Cardinal Health operates an EDI trading partner program for customers and suppliers covering pharmaceutical distribution, medical products, and specialty pharmacy. Integrations use X12 EDI transaction
  name: Cardinal Health EDI Trading Partner Integration
  slug: edi-trading-partner
artifact_total: 6
common:
- group: auth
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
  title: ''
  type: Conformance
  url: conformance/cardinal-health-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cardinal-health-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cardinal-health-vulnerability-disclosure.yml
- group: auth
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
- name: Cardinal Health Finops
  service_category: API
  slug: cardinal-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cardinal-health.png
layout: provider
modified: '2026-09-05'
name: Cardinal Health
nav: Providers
network: true
overview: Cardinal Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include B2B, Distribution, EDI, Healthcare, and Medical-Surgical.
plans:
- name: Cardinal Health Plans Pricing
  plan_count: 0
  slug: cardinal-health-plans-pricing
press:
- date: '2026-05-25'
  title: Artificial intelligence policy
  url: https://www.cardinalhealth.com/en/support/artificial-intelligence-policy.html
- date: '2026-05-25'
  title: How artificial intelligence helps patients get the right care
  url: https://newsroom.cardinalhealth.com/2022-06-22-How-artificial-intelligence-helps-patients-get-the-right-care
- date: '2026-05-25'
  title: Cardinal Health Oncology Insights Fifth Edition
  url: https://www.prnewswire.com/news-releases/cardinal-health-oncology-insights-fifth-edition-oncologists-are-optimistic-artificial-intelligence-will-enhance-the-quality-of-patient-care-and-outcomes-300857409.html
- date: '2026-05-25'
  title: How Cardinal Health Uses Technology to Build a Cognitive ...
  url: https://www.fourkites.com/blogs/how-cardinal-health-is-building-a-best-in-class-supply-chain/
- date: '2026-05-25'
  title: Artificial Intelligence at Cardinal Health - Two Use Cases
  url: https://emerj.com/artificial-intelligence-at-cardinal-health/
random_paper: 14
rate_limits:
- limit_count: 0
  name: Cardinal Health Rate Limits
  slug: cardinal-health-rate-limits
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 13.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cardinal-health/refs/heads/main/screenshots/cardinal-health-2026-06-20T173956.png
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
