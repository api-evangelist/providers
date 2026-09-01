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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kry-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kry-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.kry.se
- group: company
  title: ''
  type: About
  url: https://www.kry.se/om/
- group: operate
  title: ''
  type: Support
  url: https://www.kry.se/kontakt/
- group: company
  title: ''
  type: Blog
  url: https://www.kry.se/press/nyheter/
- group: company
  title: ''
  type: Press
  url: https://www.kry.se/press/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kry.se/sa-fungerar-det/priser-betalning/
- group: start
  title: ''
  type: SignUp
  url: https://www.kry.se/ladda-ned/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kry.se/en/legal/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kry.se/en/legal/privacy-policy/
- group: other
  title: ''
  type: Cookies
  url: https://www.kry.se/legal/cookies/
- group: company
  title: ''
  type: Partners
  url: https://www.kry.se/samarbetspartners/
- group: company
  title: ''
  type: Careers
  url: https://www.kry.se/karriar/business/lediga-tjanster/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kry/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/krycare
- group: auth
  title: ''
  type: Security
  url: https://www.kry.se/vulnerability-disclosure/
created: '2026-07-17'
description: KRY is a Swedish digital healthcare provider headquartered in Stockholm that operates internationally under the Livi brand. It delivers primary care through video and chat consultations with doctors, nurses, psychologists, physiotherapists, dietitians and midwives via its iOS and Android apps, and also runs physical primary care centres (vardcentraler), child health clinics and midwifery clinics across Sweden. KRY operates as Kry in Sweden (kry.se) and Norway (kry.no) and as Livi in the United Kingdom (livi.co.uk) and France (livi.fr). Services span digital consultations, prescription renewal, medical certificates, vaccination and testing, mental health programmes, occupational health for employers, and regional public healthcare contracts. KRY publishes no public developer program, partner API or SDK surface; the platform is consumer- and clinician-facing, so this profile captures the company identity plus its legal and security surface rather than an API surface.
image: https://www.kry.se/logos/kry-logo.svg
layout: provider
modified: '2026-07-19'
name: KRY
nav: Providers
network: true
overview: 'KRY is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Healthcare, Digital Health, and Telemedicine.


  KRY''s developer surface includes support, engineering blog, pricing, signup flow, and 14 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 18.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kry/refs/heads/main/screenshots/kry-2026-07-25T224307.png
security:
- kind: domain-security
  name: Kry Domain Security
  slug: kry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kry Vulnerability Disclosure
  slug: kry-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: kry
tags:
- Company
- Consumer
- Healthcare
- Digital Health
- Telemedicine
- Primary Care
- Mental Health
- Sweden
- Europe
website: https://www.kry.se
---
