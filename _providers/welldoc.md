---
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/welldoc-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/welldoc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/welldoc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.welldoc.com/
- group: company
  title: ''
  type: About
  url: https://www.welldoc.com/welldoc-about-us
- group: company
  title: ''
  type: Partners
  url: https://www.welldoc.com/platform/partnering
- group: operate
  title: ''
  type: Support
  url: https://helpdesk.welldoc.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.welldoc.com/individuals/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.welldoc.com/news-events
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.welldoc.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.welldoc.com/terms
- group: operate
  title: ''
  type: ContactUs
  url: https://www.welldoc.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.welldoc.com/get-a-demo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/welldoc-inc
- group: other
  title: ''
  type: X
  url: https://x.com/welldoc
- group: design
  title: ''
  type: Conformance
  url: conformance/welldoc-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.welldoc.com/platform/security
- group: auth
  title: ''
  type: Security
  url: https://www.welldoc.com/platform/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/welldoc-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/welldoc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/welldoc-rate-limits.yml
- group: company
  title: ''
  type: Careers
  url: https://www.welldoc.com/careers/united-states
- group: other
  title: ''
  type: CaseStudies
  url: https://www.welldoc.com/resources
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/welldocinc/
coverage:
  checked: '2026-09-04'
  detail: Welldoc markets SDK and API access on /platform/partnering — "we offer our capabilities, AI models, and data integration through your interface via SDK and API" — but its entire 367-URL sitemap contains no developer portal, API reference or spec, and every technical page terminates in a Get-a-Demo form.
  evidence:
  - status: 200
    url: https://www.welldoc.com/platform/partnering
  - status: 200
    url: https://www.welldoc.com/platform/solutions
  - status: 0
    url: https://developer.welldoc.com/
  - status: 0
    url: https://api.welldoc.com/
  - status: 404
    url: https://www.welldoc.com/openapi.json
  - status: 302
    url: https://helpdesk.welldoc.com/support/solutions
  reason: sales-gate
  state: gated
created: '2026-09-04'
description: Welldoc is a Columbia, Maryland digital health company whose FDA-cleared, AI-driven cardiometabolic care platform — best known through its BlueStar digital therapeutic for type 1 and type 2 diabetes — delivers personalized, real-time coaching and clinical decision support across 30+ chronic conditions including diabetes, hypertension, weight management and complex comorbid cardiometabolic disease. The platform ingests data from 400+ connected devices and data sources (blood glucose meters, CGMs, pharmacies, labs, activity trackers) and is sold to health plans, health systems, employers, life science companies, DMEs and medtech partners rather than to developers. Welldoc markets SDK and API access as a partnering option — "we offer our capabilities, AI models, and data integration through your interface via SDK and API" — but publishes no developer portal, API reference, or machine-readable contract; access is negotiated through a demo/partnering conversation.
image: https://cdn.prod.website-files.com/68ff656dfd889fd60fdf65a2/69172c699c1caf9d490535f3_Opengraph%20(1).png
layout: provider
modified: '2026-09-04'
name: Welldoc
nav: Providers
network: true
overview: 'Welldoc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Health, Healthcare, Chronic Care Management, and Diabetes.


  Welldoc''s developer surface includes support, engineering blog, signup flow, and 21 more developer resources.'
plans:
- name: Welldoc Plans Pricing
  plan_count: 0
  slug: welldoc-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Welldoc Rate Limits
  slug: welldoc-rate-limits
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 10.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: domain-security
  name: Welldoc Domain Security
  slug: welldoc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Welldoc Vulnerability Disclosure
  slug: welldoc-vulnerability-disclosure
  summary_line: security.txt
- kind: trust-center
  name: Welldoc Trust Center
  slug: welldoc-trust-center
  summary_line: HITRUST r2, SOC 2 Type 2, MDSAP / ISO 13485, HIPAA, GDPR, FDA 510(k), CE Mark, Health Canada, DiMe Seal
slug: welldoc
tags:
- Company
- Digital Health
- Healthcare
- Chronic Care Management
- Diabetes
- Digital Therapeutics
- Cardiometabolic Health
- Artificial Intelligence
- Remote Patient Monitoring
- Medical Device Software
website: https://www.welldoc.com/
---
