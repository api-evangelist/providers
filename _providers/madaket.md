---
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
    error_semantics: documented
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
  score: 21.8
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: RESTful JSON endpoints published by Madaket Health for clean, high-quality US healthcare provider data. 211 operations across 57 resource families covering provider demographics, professional and DEA/
  name: Madaket Provider API
  slug: provider-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.madakethealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://madakethealth.zendesk.com/hc/en-us/categories/360001173491-Documentation
- group: operate
  title: ''
  type: Support
  url: https://madakethealth.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.madakethealth.com/blogs
- group: company
  title: ''
  type: BlogRSS
  url: https://www.madakethealth.com/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/madakethealth
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/marketplace/pp/prodview-octwyfc6hrf6o
- group: start
  title: ''
  type: Login
  url: https://enrollment.madakethealth.com/services/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.madakethealth.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.madakethealth.com/privacy-policy
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/madaket-providerjson.md
- group: build
  title: ''
  type: Packages
  url: packages/madaket-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/madaket-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/madaket-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/madaket-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/madaket-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/madaket-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/madaket-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/madaket-llms.txt
created: '2026-08-25'
description: Madaket Health is a Cambridge, Massachusetts healthcare administration company whose Provider Data Management (PDM) platform automates payer enrollment, EDI enrollment, credentialing, licensing and provider directory data management between healthcare providers and payers. Madaket maintains connections to thousands of US payers and publishes a REST Provider API for clean, high-quality provider data — demographics, licensure, education, sanctions, malpractice and payer records — alongside ProviderJSON, an open JSON format for representing US healthcare providers derived from NPI/NPPES enumeration data.
image: https://www.madakethealth.com/wp-content/uploads/2022/02/Logo-Lockup-Reverse.svg
layout: provider
modified: '2026-08-25'
name: Madaket
nav: Providers
network: true
overview: 'Madaket publishes 1 API on the [APIs.io](https://apis.io/) network: Provider API. Tagged areas include Company, Healthcare, Provider Data Management, Payer Enrollment, and Credentialing.


  Madaket''s developer surface includes documentation, support, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Madaket Plans Pricing
  plan_count: 3
  slug: madaket-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Madaket Rate Limits
  slug: madaket-rate-limits
score:
  band: developing
  composite: 46.7
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 27.3
    contract_quality: 51.7
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 27.3
    operational_transparency: 2.6
  provenance:
    conformance: derived
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
    score: 31.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Madaket Authentication
  slug: madaket-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Madaket Domain Security
  slug: madaket-domain-security
  summary_line: TLSv1.3 · DMARC
slug: madaket
tags:
- Company
- Healthcare
- Provider Data Management
- Payer Enrollment
- Credentialing
- Provider Directory
- EDI
- Health Insurance
- Licensing
- Healthcare Administration
website: https://www.madakethealth.com/
---
