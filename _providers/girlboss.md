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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/girlboss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://girlboss.com
- group: start
  title: ''
  type: Login
  url: https://girlboss.com/account
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://girlboss.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://girlboss.com/policies/terms-of-service
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/girlboss-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/girlboss-well-known.yml
created: '2026-07-17'
description: 'Girlboss is a community and media brand for ambitious women, positioned as a navigator for the future of work — created to spark the thrill of possibility and to inspire and inform so members can find success on their own terms. Founded by Sophia Amoruso (author of #GIRLBOSS and founder of Nasty Gal), Girlboss grew from editorial content, newsletters, and the Girlboss Rally events into a community brand. Today girlboss.com runs as a Shopify-hosted storefront and brand site. Girlboss was surfaced as a portfolio company of Lightspeed Venture Partners; it publishes no first-party developer API, so this profile captures its public web, policy, and agent-facing (llms.txt / well-known) surface rather than an API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/girlboss.png
layout: provider
modified: '2026-07-19'
name: Girlboss
nav: Providers
network: true
overview: Girlboss is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Community, E-Commerce, and Retail.
random_paper: 8
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/girlboss/refs/heads/main/screenshots/girlboss-2026-08-07T165721.png
security:
- kind: domain-security
  name: Girlboss Domain Security
  slug: girlboss-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: girlboss
tags:
- Company
- Media
- Community
- E-Commerce
- Retail
- Women
- Careers
- Shopify
website: https://girlboss.com
---
