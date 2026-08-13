---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: REST API for managing Zoho Forms resources including forms, submissions, entries, and reports. Enables programmatic form data retrieval, submission creation, field updates, and integration with the br
  name: Zoho Forms API
  slug: zoho-forms-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-forms-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-forms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/forms/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/creator/help/api/v2.1/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zoho
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/zoho-forms
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/blog/forms
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/forms/pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://us.zohostatus.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/ZohoForms
- group: commercial
  title: ''
  type: Plans
  url: plans/zoho-forms-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zoho-forms-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zoho-forms-finops.yml
created: 2026-06-13
description: Online form builder with a REST API for managing forms, entries, reports, and integrating form data with other Zoho and third-party applications. Supports drag-and-drop form creation, conditional logic, workflow automation, payment collection, and offline mobile data capture with 150+ app integrations.
finops:
- name: Zoho Forms Finops
  service_category: ''
  slug: zoho-forms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-forms.png
layout: provider
modified: 2026-06-13
name: Zoho Forms
nav: Providers
network: true
overview: 'Zoho Forms publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Forms, Form Builder, Surveys, Data Collection, and Workflow Automation.


  Zoho Forms'' developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Zoho Forms Plans Pricing
  plan_count: 5
  slug: zoho-forms-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 6
  name: Zoho Forms Rate Limits
  slug: zoho-forms-rate-limits
score:
  band: thin
  composite: 33.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 33.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-forms/refs/heads/main/screenshots/zoho-forms-2026-06-20T201939.png
security:
- kind: domain-security
  name: Zoho Forms Domain Security
  slug: zoho-forms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Forms Vulnerability Disclosure
  slug: zoho-forms-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-forms
tags:
- Forms
- Form Builder
- Surveys
- Data Collection
- Workflow Automation
- No-Code
- Zoho
website: https://www.zoho.com/forms/
---
