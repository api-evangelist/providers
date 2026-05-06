---
aid: constructiononline
name: ConstructionOnline
url: https://raw.githubusercontent.com/api-evangelist/constructiononline/refs/heads/main/apis.yml
tags:
  - Construction
  - Estimating
  - Project Management
  - Projects
  - Scheduling
  - Subcontractors
  - Time Tracking
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-29'
position: Consumer
specificationVersion: '0.19'
x-type: company
description: ConstructionOnline is UDA Technologies' cloud construction project management platform covering estimating, scheduling, budgets, change orders, daily logs, file sharing, and client and subcontractor collaboration. UDA exposes the platform through a documented REST API available to ConstructionOnline Business and Enterprise customers, with read and write access for projects, contacts, schedules, and financials. Access is gated by an application process (api@uda1.com), authenticated with company-issued credentials, and rate-limited to 500 requests per hour per account.
apis:
  - aid: constructiononline:rest-api
    name: ConstructionOnline REST API
    tags:
      - Construction
      - Project Management
      - REST
      - Scheduling
      - Subcontractors
    humanURL: https://us.constructiononline.com/api-access
    properties:
      - url: https://us.constructiononline.com/api-access
        type: Documentation
      - url: https://help.constructiononline.com/developers
        type: Reference
      - url: https://help.constructiononline.com/en/faq-constructiononline-api
        type: FAQ
    description: REST API for the ConstructionOnline platform that lets approved Business and Enterprise customers programmatically read and write projects, contacts, schedules, daily logs, change orders, budgets, and time-tracking records. Used to integrate ConstructionOnline with Zapier, HubSpot, Salesforce, custom dashboards, and ERP systems. Limited to 500 requests per hour per account.
common:
  - type: Website
    url: https://www.constructiononline.com
  - type: API Access
    url: https://us.constructiononline.com/api-access
  - type: Developer Help
    url: https://help.constructiononline.com/developers
  - type: FAQ
    url: https://help.constructiononline.com/en/faq-constructiononline-api
  - type: Software Integrations
    url: https://us.constructiononline.com/construction-software-integrations
  - type: Pricing
    url: https://us.constructiononline.com/enterprise-pricing
  - type: Newsroom
    url: https://news.constructiononline.com
  - type: Support
    url: https://help.constructiononline.com
  - type: Privacy Policy
    url: https://www.constructiononline.com/privacy
  - type: Terms of Service
    url: https://www.constructiononline.com/terms
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
