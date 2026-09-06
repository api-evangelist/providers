---
access_model:
  confidence: high
  label: Public · no key, no account, no published plan
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 24.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://www.davita.com/wp-json
  baseurl_source: declared
  description: 'The public, unauthenticated REST API that DaVita''s own web platform serves at https://www.davita.com/wp-json/. It carries a first-party davita/v1 namespace — a dialysis center locator, a Kidney Smart '
  name: DaVita Web REST API
  slug: davita-web-rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/davita-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/davita-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/davita
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/davita
- group: company
  title: ''
  type: Website
  url: https://www.davita.com
- group: start
  title: ''
  type: Patient Portal
  url: https://www.davita.com/mydavita/
- group: other
  title: ''
  type: Education
  url: https://www.davita.com/education
- group: other
  title: ''
  type: Find a Center
  url: https://davita.com/tools/find-a-dialysis-center/
- group: company
  title: ''
  type: Investor Relations
  url: https://investors.davita.com/
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.davita.com/
- group: company
  title: ''
  type: Careers
  url: https://careers.davita.com/
- group: company
  title: ''
  type: Hospital Partnerships
  url: https://davita.com/partners/hospitals/
- group: company
  title: ''
  type: Physician Partnerships
  url: https://www.davita.com/physicians
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.davita.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.davita.com/terms-of-use
- group: company
  title: ''
  type: Blog
  url: https://newsroom.davita.com/feed/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/davita-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://davita.com/help-center/
- group: auth
  title: ''
  type: Compliance
  url: https://davita.com/privacy-practices/
created: '2026-03-21'
description: 'DaVita Inc. is a Fortune 500 kidney care company operating in-center hemodialysis, home hemodialysis, and peritoneal dialysis programs in the United States and abroad, alongside transplant support, integrated kidney care, hospital partnerships, and clinical research. DaVita runs no developer program and publishes no API documentation, but its own web platform serves a live, public, unauthenticated REST API at https://www.davita.com/wp-json/ with a first-party davita/v1 namespace: a dialysis center locator, a Kidney Smart class finder, a USDA-sourced food and nutrient lookup shaped for the kidney diet, and 1,258 kidney-friendly recipes, 570 education articles and a kidney vocabulary alongside them. Clinical integration remains sales-led through payer, hospital and physician partnerships and EHR data exchange; there is no public FHIR endpoint.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/davita.png
layout: provider
modified: '2026-09-05'
name: DaVita
nav: Providers
network: true
overview: 'DaVita publishes 1 API on the [APIs.io](https://apis.io/) network: Web REST API. Tagged areas include Chronic Kidney Disease, Dialysis, Fortune 500, Healthcare, and Home Dialysis.


  DaVita''s developer surface includes authentication, engineering blog, support, and 16 more developer resources.'
plans:
- name: Davita Plans Pricing
  plan_count: 0
  slug: davita-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Davita Rate Limits
  slug: davita-rate-limits
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 27.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 60.5
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 9.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/davita/refs/heads/main/screenshots/davita-2026-06-20T175733.png
security:
- kind: authentication
  name: Davita Authentication
  slug: davita-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Davita Domain Security
  slug: davita-domain-security
  summary_line: TLSv1.3 · DMARC
slug: davita
tags:
- Chronic Kidney Disease
- Dialysis
- Fortune 500
- Healthcare
- Home Dialysis
- Hospital Partnerships
- Integrated Kidney Care
- Kidney Care
- Nutrition
- Patient Education
- Recipes
website: https://www.davita.com
---
