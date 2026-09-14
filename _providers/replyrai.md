---
access_model:
  confidence: medium
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://replyr.ai/
  - https://app.replyr.ai/en/login
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://app.replyr.ai/api
  baseurl_source: declared
  description: The Accounts API from Replyr.ai — 13 operation(s) for accounts.
  name: Replyr.ai Accounts API
  slug: replyrai-accounts-api
- baseURL: https://app.replyr.ai/api
  baseurl_source: declared
  description: The AI Agents API from Replyr.ai — 5 operation(s) for ai agents.
  name: Replyr.ai AI Agents API
  slug: replyrai-ai-agents-api
- baseURL: https://app.replyr.ai/api
  baseurl_source: declared
  description: The Appointment Management API from Replyr.ai — 2 operation(s) for appointment management.
  name: Replyr.ai Appointment Management API
  slug: replyrai-appointment-management-api
- baseURL: https://app.replyr.ai/api
  baseurl_source: declared
  description: The Contacts API from Replyr.ai — 12 operation(s) for contacts.
  name: Replyr.ai Contacts API
  slug: replyrai-contacts-api
- baseURL: https://app.replyr.ai/api
  baseurl_source: declared
  description: The Ecommerce API from Replyr.ai — 6 operation(s) for ecommerce.
  name: Replyr.ai Ecommerce API
  slug: replyrai-ecommerce-api
- baseURL: https://app.replyr.ai/api
  baseurl_source: declared
  description: The Pipelines API from Replyr.ai — 9 operation(s) for pipelines.
  name: Replyr.ai Pipelines API
  slug: replyrai-pipelines-api
- baseURL: https://app.replyr.ai/api
  baseurl_source: declared
  description: The Templates API from Replyr.ai — 1 operation(s) for templates.
  name: Replyr.ai Templates API
  slug: replyrai-templates-api
artifact_total: 11
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/replyrai-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://replyr.ai
- group: docs
  title: ''
  type: APIReference
  url: https://app.replyr.ai/api
- group: docs
  title: ''
  type: Documentation
  url: https://app.replyr.ai/api
- group: start
  title: ''
  type: Login
  url: https://app.replyr.ai/en/login
- group: operate
  title: ''
  type: Support
  url: https://wa.me/60109696912
- group: auth
  title: ''
  type: DomainSecurity
  url: security/replyrai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/replyrai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/replyrai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/replyrai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/replyrai-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/replyrai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/replyrai-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/replyrai-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/replyrai-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/replyrai-platform-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/replyrai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/replyrai-rate-limits.yml
created: '2026-07-17'
description: Replyr.ai (Replyr Sdn Bhd, Kuala Lumpur, Malaysia) is an AI-powered customer engagement and patient-acquisition platform aimed at Malaysian clinics. It builds GPT-style chat assistants that reply instantly in multiple languages across WhatsApp, Instagram, Facebook Messenger and other chat channels to qualify leads, answer FAQs, recommend products and book appointments 24/7, and packages that with Meta and Google advertising campaigns and a BookAClinic discovery marketplace. The operator console at app.replyr.ai runs a white-labeled deployment of the ChatRace conversational-commerce platform and exposes a REST API of its own at https://app.replyr.ai/api, documented with a live Swagger UI and a Swagger 2.0 specification covering accounts, contacts, tags and custom fields, message sending across channels, sales pipelines and opportunities, AI agents, appointment calendars, templates and an ecommerce cart/order surface. Authentication is a single X-ACCESS-TOKEN API key header. Surfaced
  as a 500 Global portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/replyrai.png
layout: provider
modified: '2026-08-13'
name: Replyr.ai
nav: Providers
network: true
overview: 'Replyr.ai publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, AI Agents API, Appointment Management API, and 4 more. Tagged areas include Company, Artificial Intelligence, Chatbots, Conversational AI, and Customer Engagement.


  Replyr.ai''s developer surface includes API reference, documentation, support, authentication, and 15 more developer resources.'
plans:
- name: Replyrai Plans Pricing
  plan_count: 0
  slug: replyrai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Replyrai Rate Limits
  slug: replyrai-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/replyrai/refs/heads/main/screenshots/replyrai-2026-09-02T153511.png
security:
- kind: authentication
  name: Replyrai Authentication
  slug: replyrai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Replyrai Domain Security
  slug: replyrai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: replyrai
tags:
- Company
- Artificial Intelligence
- Chatbots
- Conversational AI
- Customer Engagement
- Lead Generation
- WhatsApp
- Marketing
- Messaging
- CRM
- Appointment Scheduling
- Healthcare
- Malaysia
website: https://replyr.ai
---
