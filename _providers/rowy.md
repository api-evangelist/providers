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
api_count: 1
apis:
- baseURL: https://docs.rowy.io
  baseurl_source: spec
  description: Rowy's primary inbound API surface. Each table can generate an HTTPS webhook endpoint running on Google Cloud Run (the rowy-hooks service) that receives POST requests from external systems. Built-in t
  name: Rowy Webhooks
  slug: rowy-webhooks
- baseURL: https://docs.rowy.io
  baseurl_source: spec
  description: Rowy Run is a group of Google Cloud Run services (rowy-backend and rowy-hooks) deployed into the user's own GCP project that powers derivatives, action scripts, webhooks, user management, and one-clic
  name: Rowy Run / Cloud Functions
  slug: rowy-run-cloud-functions
- baseURL: https://docs.rowy.io
  baseurl_source: spec
  description: Rowy tables map directly onto Google Cloud Firestore collections. Programmatic data access is not a Rowy-specific REST API; it is the underlying Firestore data store reached via the Firebase/Google Cl
  name: Rowy Firestore Data
  slug: rowy-firestore-data
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rowy
  slug: open-rowy
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rowy-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rowyio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rowyio
- group: company
  title: ''
  type: Website
  url: https://www.rowy.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rowy.io
- group: commercial
  title: ''
  type: Plans
  url: plans/rowy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rowy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rowy-finops.yml
created: '2026-06-20'
description: Rowy is an open-source low-code backend platform that puts an Airtable-like spreadsheet UI on top of Google Cloud Firestore, with JavaScript/TypeScript Cloud Functions, column automations, and webhooks. It is primarily a UI plus a Firebase/GCP framework deployed into the user's own project; its main inbound API surface is per-table webhooks running on Cloud Run, alongside Rowy Run backend services and the underlying Firestore data store accessed via the Firebase SDK.
finops:
- name: Rowy Finops
  service_category: Developer Tools and Low-Code
  slug: rowy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rowy.png
layout: provider
modified: '2026-06-20'
name: Rowy
nav: Providers
network: true
overview: 'Rowy publishes 3 APIs on the [APIs.io](https://apis.io/) network: Webhooks, Run / Cloud Functions, and Firestore Data. Tagged areas include Low-Code, Backend, Firestore, Firebase, and Webhook.


  Rowy''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Rowy Plans Pricing
  plan_count: 3
  slug: rowy-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Rowy Rate Limits
  slug: rowy-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/rowy/refs/heads/main/screenshots/rowy-2026-06-20T193228.png
security:
- kind: domain-security
  name: Rowy Domain Security
  slug: rowy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rowy
tags:
- Low-Code
- Backend
- Firestore
- Firebase
- Webhook
- Cloud Functions
website: https://www.rowy.io
---
