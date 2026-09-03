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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bizible-marketing-analytics-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://experienceleague.adobe.com/en/docs/marketo-measure/using/home
- group: company
  title: ''
  type: Website
  url: https://bizible.com/
- group: build
  title: ''
  type: Packages
  url: packages/bizible-marketing-analytics-packages.yml
- group: design
  title: ''
  type: Components
  url: components/bizible-marketing-analytics-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bizible-marketing-analytics-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bizible-marketing-analytics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bizible-marketing-analytics-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bizible-marketing-analytics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bizible-marketing-analytics-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bizible-marketing-analytics-llms.txt
coverage:
  checked: '2026-08-13'
  detail: The Bizible brand is fully absorbed into Adobe — bizible.com and www.bizible.com answer HTTP 301 on every path (including /robots.txt and every /.well-known/ path) and redirect to Adobe's Marketo Measure product page, leaving only an Akamai CDN serving the bizible.js tracking tag as a live first-party surface; no api./developers./docs.bizible.com subdomain resolves at all.
  evidence:
  - status: 301
    url: https://bizible.com/.well-known/agent-card.json
  - status: 301
    url: https://bizible.com/openapi.json
  - status: 0
    url: https://api.bizible.com/
  - status: 200
    url: https://cdn.bizible.com/scripts/bizible.js
  reason: defunct
  state: none
created: '2026-07-17'
description: Bizible was a B2B marketing attribution and revenue analytics platform that connected marketing activity to pipeline and revenue across advertising, web, CRM, and marketing-automation channels. Acquired by Marketo in 2018 and subsequently by Adobe, the product now ships as Adobe Marketo Measure (formerly Bizible); the bizible.com domain 301-redirects to Adobe and its product documentation has moved to the Adobe Experience League. It has no standalone public developer portal, OpenAPI, or API reference of its own — integration is handled through Adobe/Marketo Measure and CRM connectors.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bizible-marketing-analytics.png
layout: provider
modified: '2026-08-13'
name: Bizible Marketing Analytics
nav: Providers
network: true
overview: 'Bizible Marketing Analytics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Analytics, Marketing Attribution, and Revenue Analytics.


  Bizible Marketing Analytics'' developer surface includes documentation, changelog, and 9 more developer resources.'
plans:
- name: Bizible Marketing Analytics Plans Pricing
  plan_count: 0
  slug: bizible-marketing-analytics-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Bizible Marketing Analytics Rate Limits
  slug: bizible-marketing-analytics-rate-limits
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 11
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 11.9
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bizible-marketing-analytics/refs/heads/main/screenshots/bizible-marketing-analytics-2026-07-25T203222.png
security:
- kind: domain-security
  name: Bizible Marketing Analytics Domain Security
  slug: bizible-marketing-analytics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bizible-marketing-analytics
tags:
- Company
- Marketing
- Analytics
- Marketing Attribution
- Revenue Analytics
- B2B
- Adobe
- Marketo
website: https://bizible.com/
---
