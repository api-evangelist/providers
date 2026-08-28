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
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: Microsoft Power Automate is a cloud-based workflow automation platform that lets organizations build automated workflows, robotic process automation, business process flows, and AI-assisted automation
  name: Microsoft Power Automate
  slug: power-automate
- description: The Desktop Flows public API enables developers to programmatically manage, run, and monitor desktop flow automations as part of robotic process automation scenarios.
  name: Power Automate Desktop Flows Public API
  slug: desktop-flows-api
- description: Programmatic access for managing cloud flows in Power Automate including creating, updating, and running flows using Dataverse and the Power Platform APIs.
  name: Power Automate Cloud Flows API
  slug: cloud-flows-api
- description: Build, register, and certify custom connectors that extend Power Automate to communicate with any REST or SOAP API across the Power Platform.
  name: Power Automate Custom Connectors
  slug: custom-connectors-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/power-automate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/power-automate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://powerautomate.microsoft.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-automate/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/power-automate/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-automate/developer/dev-enterprise-intro
- group: commercial
  title: ''
  type: Pricing
  url: https://powerautomate.microsoft.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://make.powerautomate.com/
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/power-platform/blog/power-automate/
- group: learn
  title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/powerplatform/power-automate
- group: operate
  title: ''
  type: Community
  url: https://powerusers.microsoft.com/t5/Power-Automate-Community/ct-p/MPACommunity
- group: operate
  title: ''
  type: Support
  url: https://powerautomate.microsoft.com/support/
- group: other
  title: ''
  type: Ideas
  url: https://ideas.powerautomate.com/
- group: other
  title: ''
  type: Templates
  url: https://make.powerautomate.com/templates/
- group: operate
  title: ''
  type: StatusPage
  url: https://admin.powerplatform.microsoft.com/support/serviceshealth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/licensing/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: auth
  title: ''
  type: Trust
  url: https://www.microsoft.com/en-us/trust-center
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/power-platform/released-versions/
created: '2026-03-27'
description: Microsoft Power Automate is a cloud-based workflow automation platform that enables users to create automated workflows between apps and services to synchronize files, get notifications, collect data, and orchestrate business processes across cloud, desktop, and AI-driven flows.
finops:
- name: Power Automate Finops
  service_category: API
  slug: power-automate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/power-automate.png
layout: provider
modified: '2026-04-28'
name: Microsoft Power Automate
nav: Providers
network: true
overview: 'Microsoft Power Automate publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Workflow-Automation, Enterprise, Low-Code, RPA, and Cloud Flows.


  Microsoft Power Automate''s developer surface includes documentation, getting-started guide, pricing, signup flow, engineering blog, training material, support, and 12 more developer resources.'
plans:
- name: Power Automate Plans Pricing
  plan_count: 3
  slug: power-automate-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Power Automate Rate Limits
  slug: power-automate-rate-limits
score:
  band: thin
  composite: 26.4
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 26.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/power-automate/refs/heads/main/screenshots/power-automate-2026-06-20T192028.png
security:
- kind: domain-security
  name: Power Automate Domain Security
  slug: power-automate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Power Automate Vulnerability Disclosure
  slug: power-automate-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: power-automate
tags:
- Workflow-Automation
- Enterprise
- Low-Code
- RPA
- Cloud Flows
- Desktop Flows
- Artificial Intelligence
website: https://powerautomate.microsoft.com
---
