---
access_model:
  confidence: high
  label: Sales-gated
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - https://www.openprisetech.com/pricing
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: API Factory turns any Openprise Job or Bot into a REST endpoint with a single "Enable API" action. The caller sends an HTTP POST carrying a JSON array of records and receives a JSON array of processed
  name: Openprise API Factory
  slug: openprise-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.openprisetech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://helpcenter.openprisetech.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://helpcenter.openprisetech.com/hc/en-us/articles/24107925788180-API-Factory-Overview-and-Use-Guide
- group: start
  title: ''
  type: GettingStarted
  url: https://helpcenter.openprisetech.com/hc/en-us/articles/24107502554772-Quick-Start-Guide
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.openprisetech.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.openprisetech.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openprisetech
- group: commercial
  title: ''
  type: Pricing
  url: https://www.openprisetech.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.openprisecloud.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.openprisetech.com/legal/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.openprisetech.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/openprise-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openprise-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openprise-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openprise-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/openprise-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/openprise-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openprise-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/openprise-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://helpcenter.openprisetech.com/hc/en-us/categories/24103645602580-Release-Notes-Announcements
- group: commercial
  title: ''
  type: Plans
  url: plans/openprise-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openprise-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/openprise-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openprise-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://openprisetech.com/llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openprise
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCWd7PYa-TtRq7SdRkfnFcow
created: '2025-02-08'
description: Openprise is an AI and data orchestration platform built for enterprise go-to-market teams — RevOps, marketing operations and sales operations. It cleans, unifies and activates GTM data across CRM, marketing automation and data warehouse systems through no-code Jobs and Bots, with 400+ pre-built connectors, multi-vendor enrichment waterfalls, deduplication, lead-to-account matching, routing, scoring and segmentation. Its developer-facing surface is API Factory, a licensed feature that turns any configured Job or Bot into a per-tenant REST endpoint callable from Marketo webhooks, Salesforce triggers, web forms or any system that can issue an HTTP POST. Openprise coined the term "data orchestration" in 2017 and is headquartered in San Mateo, California.
finops:
- name: Openprise Finops
  service_category: API
  slug: openprise-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openprise.png
layout: provider
modified: '2026-08-14'
name: Openprise
nav: Providers
network: true
overview: 'Openprise publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Automation, Data Quality, Data Orchestration, AI Orchestration, and Data Enrichment.


  Openprise''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 20 more developer resources.'
plans:
- name: Openprise Plans Pricing
  plan_count: 2
  slug: openprise-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Openprise Rate Limits
  slug: openprise-rate-limits
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 16
    catalog_gap: 60.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 72.4
    commercial_clarity: 72.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 39.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openprise/refs/heads/main/screenshots/openprise-2026-06-20T191021.png
security:
- kind: authentication
  name: Openprise Authentication
  slug: openprise-authentication
  summary_line: apiKey/saml2 · 3 schemes
- kind: domain-security
  name: Openprise Domain Security
  slug: openprise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Openprise Trust Center
  slug: openprise-trust-center
  summary_line: SOC 2
slug: openprise
tags:
- Data Automation
- Data Quality
- Data Orchestration
- AI Orchestration
- Data Enrichment
- Deduplication
- Marketing Operations
- Revenue Operations
- Sales Operations
- Go-To-Market
website: https://www.openprisetech.com/
---
