---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Messaging Api Agentic Access
  operation_count: 6
  slug: messaging-api-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Managing, sending, and receiving of messages via SMS and other channels.
  name: Messaging API Messages API
  slug: messaging-api-messages-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Messaging API Messages API
  slug: open-messaging-api-messages-api
- collection_type: open
  name: Messaging API Messages API
  slug: open-messaging-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/messaging-api-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/messaging-api-authentication.yml
created: '2024-12-29'
description: A template and concept entry for messaging APIs. This represents the pattern and structure for messaging API implementations used in storytelling, training, and knowledge bases.
finops:
- name: Messaging Api Finops
  service_category: API
  slug: messaging-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/messaging-api.png
layout: provider
modified: '2026-05-19'
name: Messaging API
nav: Providers
network: true
overview: 'Messaging API publishes 1 API on the [APIs.io](https://apis.io/) network: Messages API. Tagged areas include API Pattern, Messaging, and Template.


  Messaging API''s developer surface includes authentication and 1 more developer resources.'
plans:
- name: Messaging Api Plans Pricing
  plan_count: 3
  slug: messaging-api-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Messaging Api Rate Limits
  slug: messaging-api-rate-limits
security:
- kind: authentication
  name: Messaging Api Authentication
  slug: messaging-api-authentication
  summary_line: apiKey · 1 scheme
slug: messaging-api
tags:
- API Pattern
- Messaging
- Template
---
