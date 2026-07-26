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
api_count: 2
apis:
- description: Modeled view of Whova's attendee integration surface. Whova exposes attendee data to organizers only through the Zapier CRM integration - a Get Attendees trigger that fires when the attendee list chan
  name: Whova Attendees API (Modeled)
  slug: whova-attendees-api
- description: Modeled view of Whova's registration and order surface. The Zapier integration provides a Get Orders trigger (fires on order-list changes) and a Get Registrants trigger (fires when a registrant submit
  name: Whova Registration and Orders API (Modeled)
  slug: whova-registration-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whova-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/whova
- group: company
  title: ''
  type: Website
  url: https://whova.com/
- group: docs
  title: ''
  type: Documentation
  url: https://whova.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/whova-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://whova.com/blog/
- group: other
  title: ''
  type: ProductPage
  url: https://whova.com/blog/openreview-integration/
- group: other
  title: ''
  type: ProductPage
  url: https://whova.com/pages/whova-app-exhibitor-guide/
created: '2026-07-05'
description: Whova is an award-winning all-in-one event management platform built around a mobile event app that carries the agenda, speaker profiles, attendee networking, live polls, and session Q&A, plus registration, ticketing, name badges, surveys, abstract/speaker management, and exhibitor/sponsor tools. Whova does NOT publish an open, self-serve developer API - there is no public developer portal, no documented REST reference, no OpenAPI definition, and no SDKs. Its only programmatic surface for organizers is a partner/CRM integration layer exposed through Zapier (triggers for attendee, order, and registrant changes plus a create/update-attendee action), reached from the organizer dashboard under Attendees > Integrations > CRM Integration, alongside prebuilt connectors to Eventbrite, Cvent, Constant Contact, RegFox, OpenReview, SharePoint/OneDrive, MailChimp, Wild Apricot, and Google Drive. The API entries below are logical, HONESTLY MODELED views of that integration surface (see endpointsModeled)
  - they are not sourced from a public Whova API reference, and no base URL, auth scheme, or endpoint paths are published by Whova.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/whova.png
layout: provider
modified: '2026-07-25'
name: Whova
nav: Providers
network: true
overview: 'Whova publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Events, Event Management, Event App, Registration, and Conferences.


  Whova''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Whova Plans Pricing
  plan_count: 2
  slug: whova-plans-pricing
random_paper: 45
security:
- kind: domain-security
  name: Whova Domain Security
  slug: whova-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: whova
tags:
- Events
- Event Management
- Event App
- Registration
- Conferences
- Attendees
- Exhibitors
- Gated API
- Modeled
website: https://whova.com/
---
