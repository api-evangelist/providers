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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/function-health/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/suppco-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/suppco-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/suppco-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://supp.co/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/suppco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://supp.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://supp.co/about/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://supp.co/about/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@supp.co
created: '2026-07-17'
description: SuppCo is a consumer supplement tracking and optimization platform, describing itself as the world's first real supplement tracker and optimizer. Its iOS and Android app lets people log their supplement stack and get a personalized StackScore across quality, dosing, goal coverage, and nutrient levels, plus a TrustScore that rates products on 29 attributes. It is backed by a database of 160,000+ products, 20,000+ research studies, and 80+ expert protocols from functional-medicine practitioners. SuppCo is in open beta (free, with an optional Pro tier) and was acquired by Function Health. No public developer API, OpenAPI, or developer portal is currently published; this profile captures its public web, security, and legal surface. Surfaced as a portfolio company of Union Square Ventures.
image: https://supp.co/favicon.ico
layout: provider
modified: '2026-07-21'
name: SuppCo
nav: Providers
network: true
overview: 'SuppCo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Supplements, Health, Wellness, and Nutrition.


  SuppCo''s developer surface includes support and 9 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Suppco Domain Security
  slug: suppco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Suppco Vulnerability Disclosure
  slug: suppco-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: suppco
tags:
- Company
- Supplements
- Health
- Wellness
- Nutrition
- Consumer App
- Mobile
- Health Data
website: https://supp.co
---
