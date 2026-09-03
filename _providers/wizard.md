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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wizard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wizard.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.wizard.com/beta
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wizard.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wizard.com/privacy-notice
created: '2026-07-17'
description: Wizard is an AI-powered personal shopping agent for consumers. Shoppers describe what they want in natural language and Wizard searches across retailer websites, customer reviews, trusted editorial, and social content to return a tightly curated set of product recommendations, with direct checkout from retailers such as Amazon, Best Buy, Apple, and Target. The company is backed by Accel. As of this enrichment pass Wizard is a consumer-facing web/app product and exposes no public developer API, SDK, documentation, or well-known discovery surface (developer/docs/api subdomains and /.well-known/security.txt all return 404).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wizard.png
layout: provider
modified: '2026-07-21'
name: Wizard
nav: Providers
network: true
overview: 'Wizard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Shopping, E-Commerce, and Artificial Intelligence.


  Wizard''s developer surface includes signup flow and 4 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wizard/refs/heads/main/screenshots/wizard-2026-09-02T170851.png
security:
- kind: domain-security
  name: Wizard Domain Security
  slug: wizard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wizard
tags:
- Company
- Consumer
- Shopping
- E-Commerce
- Artificial Intelligence
- Shopping Assistant
- Conversational Commerce
website: https://wizard.com/
---
