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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: CVS Health does not publish a unified public REST API or developer portal. Pharmacy, PBM, and Aetna integrations are conducted via contracted partner channels using industry-standard rails such as NCP
  name: CVS Health Partner Integrations
  slug: partner-integrations
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cvs-health-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cvs-health
- group: company
  title: ''
  type: Website
  url: https://www.cvshealth.com/
- group: company
  title: ''
  type: AboutUs
  url: https://www.cvshealth.com/about
- group: other
  title: ''
  type: BusinessStrategy
  url: https://www.cvshealth.com/about/business-strategy.html
- group: other
  title: ''
  type: DigitalHealth
  url: https://www.cvshealth.com/social-responsibility/digital-health
- group: other
  title: ''
  type: CVSPharmacy
  url: https://www.cvs.com/
- group: other
  title: ''
  type: Caremark
  url: https://www.caremark.com/
- group: other
  title: ''
  type: Aetna
  url: https://www.aetna.com/
- group: build
  title: ''
  type: MinuteClinic
  url: https://www.cvs.com/minuteclinic/
- group: other
  title: ''
  type: OakStreetHealth
  url: https://www.oakstreethealth.com/
- group: other
  title: ''
  type: SignifyHealth
  url: https://www.signifyhealth.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cvshealth.com/news
- group: company
  title: ''
  type: Careers
  url: https://jobs.cvshealth.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cvshealth.com/legal/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cvshealth.com/legal/terms-of-use.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cvs-health/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/CVSHealth
created: '2026-03-21'
description: CVS Health is a Fortune 50 healthcare services and retail pharmacy company. Its core operating units include CVS Pharmacy (retail pharmacy and mail-order), CVS Caremark (pharmacy benefit management / PBM), Aetna (health insurance, Medicare, Medicaid, dental and vision), MinuteClinic (walk-in clinics), Oak Street Health (primary care for Medicare patients), and Signify Health (in-home health evaluations). CVS Health does not currently operate a public developer portal or generally available REST API. Programmatic integrations with CVS Pharmacy, Caremark, and Aetna are typically established through business partnership agreements, EDI / NCPDP pharmacy networks, and HIPAA-aligned interoperability channels (e.g., FHIR endpoints exposed to qualifying healthcare partners under regulatory mandates such as the CMS Interoperability Rule). Developer-facing artifacts in this index are limited to public marketing, corporate, and digital health references.
finops:
- name: Cvs Health Finops
  service_category: Healthcare
  slug: cvs-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvs-health.png
layout: provider
modified: '2026-04-28'
name: CVS Health
nav: Providers
network: true
overview: CVS Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Aetna, Caremark, CVS Pharmacy, Digital Health, and FHIR.
plans:
- name: Cvs Health Plans Pricing
  plan_count: 2
  slug: cvs-health-plans-pricing
press:
- date: '2026-05-25'
  title: CVS Health News and Press Releases
  url: https://www.prnewswire.com/news/cvs-health/
- date: '2026-05-25'
  title: CVS Health and Google have partnered to use artificial ...
  url: https://www.facebook.com/forbes/posts/cvs-health-and-google-have-partnered-to-use-artificial-intelligence-and-related-/1299449658711688/
- date: '2026-05-25'
  title: CVS Health and Google Cloud announce new strategic ...
  url: https://www.cvshealth.com/news/company-news/cvs-health-and-google-cloud-announce-new-strategic-partnership.html
- date: '2026-05-25'
  title: Improving health plan member experiences with AI
  url: https://www.cvshealth.com/news/innovation/improving-health-plan-member-experiences-with-ai.html
- date: '2026-05-25'
  title: Aetna Launches New AI and Digital Tools to Improve ...
  url: https://www.cvshealth.com/news/innovation/aetna-launches-new-ai-and-digital-tools-to-improve-access-and-care.html
random_paper: 57
rate_limits:
- limit_count: 2
  name: Cvs Health Rate Limits
  slug: cvs-health-rate-limits
score:
  band: emerging
  composite: 19.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cvs-health/refs/heads/main/screenshots/cvs-health-2026-06-20T175405.png
security:
- kind: domain-security
  name: Cvs Health Domain Security
  slug: cvs-health-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: cvs-health
tags:
- Aetna
- Caremark
- CVS Pharmacy
- Digital Health
- FHIR
- Health Insurance
- Healthcare
- HIPAA
- Interoperability
- Medicare
- MinuteClinic
- Oak Street Health
- Pharmacy
- Pharmacy Benefits Management
- Prescriptions
- Retail Pharmacy
- Signify Health
- Fortune 100
website: https://www.cvshealth.com/
---
