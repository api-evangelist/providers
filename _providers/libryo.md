---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'The Libryo Platform''s partner-facing RESTful API. Third-party applications integrate on behalf of a Libryo user using the OAuth 2.0 authorization-code flow, then call the versioned /api/v1 surface to '
  name: Libryo API
  slug: libryo-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://libryo.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/libryo/libryo-api-oauth-docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/libryo
- group: operate
  title: ''
  type: Support
  url: https://libryo.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://libryo.com/faqs/
- group: commercial
  title: ''
  type: Pricing
  url: https://libryo.com/pricing-regulatory-tracking/
- group: start
  title: ''
  type: Login
  url: https://my.libryo.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://libryo.com/privacy-policy/
- group: other
  title: ''
  type: CaseStudies
  url: https://libryo.com/case-studies/
- group: other
  title: ''
  type: Resources
  url: https://libryo.com/resources-legaltech/
- group: company
  title: ''
  type: About
  url: https://libryo.com/about-us/
- group: build
  title: ''
  type: Packages
  url: packages/libryo-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/libryo-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/libryo-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/libryo-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/libryo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/libryo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/libryo-lifecycle.yml
created: '2026-07-17'
description: Libryo (ERM Libryo) is a regulatory compliance management platform for Environmental, Health and Safety (EHS) teams. It automates legal registers, streams site-specific regulatory obligations across jurisdictions, and tracks legislative change so that operators know which laws apply to each of their sites. Founded in 2016 with a distributed team across Cape Town, London, Toronto, Nairobi and Berlin, Libryo is now part of ERM, the sustainability consultancy. The product surface spans Libryo Sites (site-specific EHS regulatory intelligence), Libryo Assess (assessment and audit management), Libryo Collaborate, and custom legal registers, and is used in manufacturing, energy and utilities, chemicals, mining, logistics and telecoms. Libryo exposes a partner-facing RESTful API secured with OAuth 2.0 authorization-code flow, documented publicly in the libryo/libryo-api-oauth-docs repository, and also offers its regulatory content as a data-as-a-service feed into third-party GRC platforms.
image: https://libryo.com/wp-content/uploads/2025/03/cropped-favicon-32x32.png
layout: provider
modified: '2026-07-19'
name: Libryo
nav: Providers
network: true
overview: 'Libryo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Regulatory Compliance, Legal Tech, Environmental Health and Safety, and Governance Risk and Compliance.


  Libryo''s developer surface includes documentation, support, pricing, and 15 more developer resources.'
random_paper: 6
scopes:
- name: Libryo Scopes
  scope_count: 3
  slug: libryo-scopes
  summary_line: 3 scopes
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 25.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/libryo/refs/heads/main/screenshots/libryo-2026-07-25T225027.png
security:
- kind: authentication
  name: Libryo Authentication
  slug: libryo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Libryo Domain Security
  slug: libryo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: libryo
tags:
- Company
- Regulatory Compliance
- Legal Tech
- Environmental Health and Safety
- Governance Risk and Compliance
- Legal Registers
- Regulatory Change Management
- Sustainability
- Authentication
website: https://libryo.com
---
