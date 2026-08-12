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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Visualforce is the Salesforce framework for building custom user interfaces using tag-based markup and Apex server-side controllers. Developers use it to create pages, email templates, and PDF documen
  name: Visualforce
  slug: visualforce-api
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/visualforce-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.salesforce.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/
- group: start
  title: ''
  type: GettingStarted
  url: https://trailhead.salesforce.com/en/content/learn/modules/visualforce_fundamentals
- group: company
  title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs
- group: operate
  title: ''
  type: Support
  url: https://developer.salesforce.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/agreements/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/privacy/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/visualforce
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salesforce
- group: learn
  title: ''
  type: Training
  url: https://trailhead.salesforce.com/en/content/learn/modules/visualforce_fundamentals
created: '2024-01-01'
description: Visualforce is a framework that enables developers to build sophisticated, custom user interfaces that can be hosted natively on the Salesforce platform. It uses a tag-based markup language similar to HTML and provides a component-based development model for building pages, email templates, and PDF documents within Salesforce.
features:
- description: HTML-like tag-based markup for building custom Salesforce pages without JavaScript frameworks.
  name: Tag-Based Markup Language
- description: Reusable Visualforce components for consistent UI patterns across Salesforce applications.
  name: Component-Based Architecture
- description: Server-side Apex controllers for business logic, data access, and page flow control.
  name: Apex Controller Integration
- description: Built-in controllers for CRUD operations on standard and custom Salesforce objects.
  name: Standard Controllers
- description: Render Visualforce pages as PDF documents for invoices, reports, and printable content.
  name: PDF Generation
- description: Build dynamic HTML email templates with merge fields and conditional content.
  name: Email Templates
finops:
- name: Visualforce Finops
  service_category: API
  slug: visualforce-finops
image: /assets/icons/visualforce.png
integrations:
- description: Visualforce pages can be embedded in Lightning Experience as components and tabs.
  name: Salesforce Lightning
- description: Server-side controller integration with Apex for database access and business logic.
  name: Apex
- description: Asynchronous JavaScript calls to Apex methods for dynamic page interactions.
  name: JavaScript Remoting
- description: Client-side integration with Salesforce REST APIs for CRUD operations.
  name: Salesforce REST API
- description: Embed external applications within Visualforce pages using Canvas framework.
  name: Force.com Canvas
layout: provider
modified: '2026-04-18'
name: Visualforce
nav: Providers
network: true
overview: 'Visualforce publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Salesforce, UI Framework, and Web Development.


  Visualforce''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, support, Stack Overflow tag, training material, and 4 more developer resources.'
plans:
- name: Visualforce Plans Pricing
  plan_count: 3
  slug: visualforce-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Visualforce Rate Limits
  slug: visualforce-rate-limits
score:
  band: emerging
  composite: 21.0
  delta: -7.8
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 28.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/visualforce/refs/heads/main/screenshots/visualforce-2026-06-20T201104.png
security:
- kind: domain-security
  name: Visualforce Domain Security
  slug: visualforce-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: visualforce
tags:
- Salesforce
- UI Framework
- Web Development
use_cases:
- description: Build custom UI pages that extend Salesforce functionality beyond standard page layouts.
  name: Custom Salesforce Pages
- description: Generate branded PDFs for invoices, quotes, contracts, and reports from Salesforce data.
  name: PDF Document Generation
- description: Create rich HTML email templates with dynamic content from Salesforce records.
  name: Custom Email Templates
- description: Build custom analytics dashboards and data visualization pages within Salesforce.
  name: Embedded Dashboards
- description: Create multi-step form workflows for complex data entry processes.
  name: Wizard-Style Forms
website: https://developer.salesforce.com
---
