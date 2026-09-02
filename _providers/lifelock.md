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
- group: company
  title: ''
  type: Website
  url: https://lifelock.norton.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lifelock-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lifelock-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lifelock-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.gendigital.com/us/en/contact-us/report-a-potential-security-vulnerability/
- group: company
  title: ''
  type: Blog
  url: https://lifelock.norton.com/learn
- group: operate
  title: ''
  type: Support
  url: https://support.norton.com/lifelock/en/us/home/current/help-center
- group: commercial
  title: ''
  type: Pricing
  url: https://lifelock.norton.com/products
- group: start
  title: ''
  type: SignUp
  url: https://lifelock.norton.com/free-trials/free-identity-theft-protection
- group: start
  title: ''
  type: Login
  url: https://my.norton.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://us.norton.com/legal/lsa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://us.norton.com/privacy/products-privacy-notice
created: '2026-07-17'
description: 'LifeLock is a consumer identity-theft-protection brand founded in 2005 in Tempe, Arizona and owned by Gen Digital, Inc. (Nasdaq: GEN). It monitors members'' personal information — Social Security numbers, names, addresses, credit applications and public records — for signs of misuse, alerts them through its proprietary Identity Alert System, and provides U.S.-based restoration specialists plus reimbursement coverage when identity theft occurs. Current plans (Core, Advanced, Total) layer on credit-bureau monitoring, dark-web monitoring, automatic data-broker removal, scam support and reimbursement, home-title and SIM-swap monitoring, and the Million Dollar Protection Package. LifeLock is also sold bundled with Norton device security as Norton 360 with LifeLock. It is a direct-to-consumer subscription service and publishes no public developer API, SDKs, or developer portal; its machine-readable surface is a first-party llms.txt at lifelock.norton.com.'
image: https://lifelock.norton.com/content/dam/lifelock/logos/logo_lifelock-by-norton-light-bg.svg
layout: provider
modified: '2026-07-19'
name: LifeLock
nav: Providers
network: true
overview: 'LifeLock is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Identity, Identity Theft Protection, and Fraud Detection.


  LifeLock''s developer surface includes engineering blog, support, pricing, signup flow, and 8 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 17.5
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
  previous_composite: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lifelock/refs/heads/main/screenshots/lifelock-2026-07-25T225042.png
security:
- kind: domain-security
  name: Lifelock Domain Security
  slug: lifelock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lifelock Vulnerability Disclosure
  slug: lifelock-vulnerability-disclosure
  summary_line: security.txt
slug: lifelock
tags:
- Company
- Cybersecurity
- Identity
- Identity Theft Protection
- Fraud Detection
- Credit Monitoring
- Dark Web Monitoring
- Consumer Security
- Privacy
website: https://lifelock.norton.com/
---
