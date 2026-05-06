---
aid: comeet
url: https://raw.githubusercontent.com/api-evangelist/comeet/refs/heads/main/apis.yml
name: Comeet
tags:
  - ATS
  - Candidates
  - Careers
  - Interviews
  - Jobs
  - Recruiting
  - Talent Acquisition
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
x-type: company
created: '2025-01-07'
modified: '2026-04-26'
position: Consumer
description: Comeet (now Spark Hire Recruit, after Spark Hire's acquisition of Comeet) is a collaborative talent acquisition platform that helps companies post jobs, source and screen candidates, schedule interviews, and coordinate hiring teams. Comeet exposes a public Careers API (used to embed published positions on a custom careers website), a Recruiting API (used by integration partners to manage candidates and pipeline events), and a Hires API (used to push new-hire data into HRIS/onboarding systems).
apis:
  - aid: comeet:comeet-careers-api
    name: Comeet Careers API
    tags:
      - Careers
      - Jobs
      - Recruiting
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.comeet.co/careers-api/2.0
    humanURL: https://developers.comeet.com/reference/careers-api-overview
    properties:
      - url: https://developers.comeet.com/reference/careers-api-overview
        type: Documentation
      - url: openapi/comeet-careers-api-openapi.yml
        type: OpenAPI
    description: Public, tokenized REST API that returns the list of published positions for a Comeet customer (and details for a single position). Used to power custom-branded careers websites, embed jobs into marketing pages, and syndicate openings to third-party job boards. Each company's data is scoped by a company UID and a public company token issued by Comeet.
    x-features:
      - Public company-token authentication via query parameter
      - List and retrieve published positions
      - Optional details=true expansion for description and requirements
      - JSON responses with stable position UIDs
      - Backs Comeet's official Careers Website Widget
    x-use-cases:
      - Embedding live job listings on a corporate careers site
      - Syndicating jobs to aggregators and job boards
      - Generating sitemaps and SEO landing pages per position
      - Powering "we're hiring" components in marketing apps
  - aid: comeet:comeet-recruiting-api
    name: Comeet Recruiting API
    tags:
      - ATS
      - Candidates
      - Pipeline
      - Recruiting
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.comeet.com/reference/recruiting-api-overview
    properties:
      - url: https://developers.comeet.com/reference/recruiting-api-overview
        type: Documentation
    description: The Recruiting API is a partner-scoped REST API for building on top of Spark Hire Recruit (Comeet). It supports listing companies, positions, candidates, and pipeline events, and is the underlying interface used by ATS unification platforms (Merge, Finch, etc.) to integrate Comeet data into HR tooling. Access is granted to approved integration partners.
    x-features:
      - Partner-scoped authentication
      - Companies, positions, candidates, and pipeline event endpoints
      - Used by Merge, Finch, and other ATS unification platforms
      - Webhooks for candidate status changes (via partner integrations)
    x-use-cases:
      - Building ATS integrations with HRIS and onboarding tools
      - Bidirectional candidate sync with sourcing platforms
      - Reporting/analytics across hiring pipelines
  - aid: comeet:comeet-hires-api
    name: Comeet Hires API
    tags:
      - HRIS
      - Hiring
      - Onboarding
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.comeet.com/reference/hires-api-overview
    properties:
      - url: https://developers.comeet.com/reference/hires-api-overview
        type: Documentation
    description: The Hires API captures new-hire data from Comeet and pushes employee profile information into downstream HRIS, onboarding, and provisioning systems. It is typically used to trigger an onboarding workflow the moment a candidate is marked as hired.
    x-features:
      - New-hire payloads scoped to a Comeet customer
      - Triggered when a candidate moves to the Hired stage
      - Designed for HRIS, onboarding, and IT-provisioning consumers
    x-use-cases:
      - Auto-creating employee profiles in BambooHR, Workday, ADP, etc.
      - Triggering laptop and SaaS-account provisioning at hire time
      - Synchronizing offer-letter and start-date data into onboarding tools
common:
  - type: Website
    url: https://www.comeet.com/
  - type: Portal
    url: https://developers.comeet.com/
  - type: HelpCenter
    url: https://recruit-support.sparkhire.com/hc/en-us
  - type: ParentCompany
    url: https://www.sparkhire.com/
  - type: PrivacyPolicy
    url: https://www.comeet.com/privacy-policy/
  - url: json-ld/comeet-context.jsonld
    type: JSON-LD
  - url: json-schema/comeet-position-schema.json
    type: JSONSchema
  - url: rules/comeet-rules.yml
    type: Spectral
  - url: capabilities/comeet-careers-website-capabilities.yml
    type: NaftikoCapabilities
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
