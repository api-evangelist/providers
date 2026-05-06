---
aid: runsignup
name: RunSignup
description: RunSignup is an all-in-one race registration and event management platform serving running events, triathlons, cycling events, and obstacle courses. Their open REST API enables race directors, timing companies, affiliates, and technology partners to integrate race registration, participant management, results posting, fundraising, volunteer management, and event analytics into their own applications. The API supports OAuth 2.0 authentication and covers 100+ endpoints across 29 categories for comprehensive event lifecycle management.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Race Registration
  - Event Management
  - Running
  - Sports
  - Fitness
  - Timing
  - Fundraising
url: https://raw.githubusercontent.com/api-evangelist/runsignup/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: runsignup:runsignup
    name: RunSignup API
    description: 'The RunSignup REST API provides access to race and event management operations including race listings, participant registration and management, results import and posting, bib and chip management, division and corral management, team and group management, donations and fundraising, volunteer management, and user account management. The API uses a base URL of https://runsignup.com/Rest and supports both JSON and XML response formats. Authentication options include OAuth 2.0 (preferred), permanent API keys for partners and timers, and login-based credentials. Access levels vary by role: affiliates, partners, race directors, users, timers, and super partners each have different endpoint permissions.'
    humanURL: https://runsignup.com/API
    baseURL: https://runsignup.com/Rest
    tags:
      - Race Registration
      - Event Management
      - Running
      - Sports
      - Timing
      - Participants
      - Results
      - Fundraising
    properties:
      - type: Documentation
        url: https://runsignup.com/API/DocOverview
      - type: OpenAPI
        url: openapi/runsignup-openapi.yml
      - type: Getting Started
        url: https://runsignup.com/API/GettingStarted
      - type: Authentication
        url: https://runsignup.com/API/GettingStarted
      - type: GitHub Repository
        url: https://github.com/RunSignUp-Team/OpenSource
      - type: Spectral Rules
        url: rules/runsignup-rules.yml
      - type: Vocabulary
        url: vocabulary/runsignup-vocabulary.yml
      - type: JSONSchema
        url: json-schema/runsignup-race-schema.json
      - type: JSONStructure
        url: json-structure/runsignup-race-structure.json
      - type: JSONLD
        url: json-ld/runsignup-context.jsonld
      - type: NaftikoCapability
        url: capabilities/race-event-management.yaml
common:
  - type: Website
    url: https://runsignup.com
  - type: Documentation
    url: https://runsignup.com/API
  - type: GitHub Organization
    url: https://github.com/RunSignUp-Team
  - type: GitHub Repository
    url: https://github.com/RunSignUp-Team/OpenSource
  - type: Blog
    url: https://runsignup.blog
  - type: Support
    url: https://runsignup.com/support
  - type: Pricing
    url: https://runsignup.com/pricing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
