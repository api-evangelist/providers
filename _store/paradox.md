---
aid: paradox
name: Paradox
description: APIs and resources for Paradox, a conversational AI recruiting assistant platform powered by Olivia, an AI assistant that automates candidate screening, interview scheduling, and hiring workflows through chat, SMS, and mobile-driven experiences.
type: Index
image: https://www.paradox.ai/images/paradox-logo.png
url: https://raw.githubusercontent.com/api-evangelist/paradox/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Artificial Intelligence
  - Candidate Screening
  - Chatbot
  - Conversational AI
  - Hiring Automation
  - HR Technology
  - Interview Scheduling
  - Recruiting
  - SMS
  - Talent Acquisition
common:
  - type: Portal
    url: https://readme.paradox.ai/
  - type: Documentation
    url: https://readme.paradox.ai/docs
  - type: Authentication
    url: https://readme.paradox.ai/reference/authentication
  - type: Changelog
    url: https://readme.paradox.ai/changelog
  - type: Status
    url: https://status.paradox.ai/
  - type: Login
    url: https://olivia.paradox.ai/login
  - type: Privacy Policy
    url: https://www.paradox.ai/legal/privacy-policy
  - type: Terms of Service
    url: https://www.paradox.ai/legal/service-terms
  - type: Security
    url: https://www.paradox.ai/legal/security
  - type: FAQ
    url: https://www.paradox.ai/faqs
  - type: Integrations
    url: https://www.paradox.ai/partners/integrations
  - type: Contact
    url: https://www.paradox.ai/contact
  - type: Blog
    url: https://www.paradox.ai/blog
  - type: LinkedIn
    url: https://www.linkedin.com/company/paradoxolivia
  - type: About
    url: https://www.paradox.ai/about
  - type: OpenAPI
    url: openapi/paradox-api-openapi.yml
  - type: JSON Schema
    url: json-schema/paradox-candidate-schema.json
  - type: JSON-LD Context
    url: json-ld/paradox-context.jsonld
apis:
  - name: Paradox Conversational AI API
    description: API for integrating Paradox conversational AI recruiting assistant capabilities into your applications.
    image: https://www.paradox.ai/images/api-icon.png
    humanURL: https://www.paradox.ai
    baseURL: https://api.paradox.ai
    tags:
      - AI
      - Candidate Experience
      - Chatbot
      - Conversational AI
      - HR Technology
      - Recruiting
    properties:
      - type: Documentation
        url: https://developers.paradox.ai/docs
      - type: OpenAPI
        url: openapi/paradox-api-openapi.yml
      - type: Authentication
        url: https://developers.paradox.ai/docs/authentication
      - type: Rate Limits
        url: https://developers.paradox.ai/docs/rate-limits
    contact:
      - type: Support
        url: https://www.paradox.ai/support
      - type: Email
        url: mailto:support@paradox.ai
  - name: Paradox Company API
    description: API for accessing company-level data in Paradox including conversations, groups, schools, areas, and AI assistant configuration.
    image: https://www.paradox.ai/images/paradox-logo.png
    humanURL: https://readme.paradox.ai/reference/get-company-conversations
    baseURL: https://api.paradox.ai/api/v1/public
    tags:
      - AI Assistant
      - Company
      - Conversations
      - Groups
    properties:
      - type: Documentation
        url: https://readme.paradox.ai/reference/get-company-conversations
      - type: API Reference
        url: https://readme.paradox.ai/reference/overview
      - type: OpenAPI
        url: openapi/paradox-api-openapi.yml
  - name: Paradox Candidates API
    description: API for managing candidates within the Paradox platform including creating, retrieving, updating, deleting, and unsubscribing candidates, as well as sending candidate messages and scheduling shortlist reviews.
    image: https://www.paradox.ai/images/paradox-logo.png
    humanURL: https://readme.paradox.ai/reference/get-candidates
    baseURL: https://api.paradox.ai/api/v1/public
    tags:
      - Candidates
      - Messaging
      - Recruiting
      - Screening
    properties:
      - type: Documentation
        url: https://readme.paradox.ai/reference/get-candidates
      - type: API Reference
        url: https://readme.paradox.ai/reference/create-candidate
      - type: OpenAPI
        url: openapi/paradox-api-openapi.yml
      - type: JSON Schema
        url: json-schema/paradox-candidate-schema.json
  - name: Paradox Users API
    description: API for managing users within the Paradox platform including creating, retrieving, updating, deleting, deactivating, and reactivating users, as well as managing user roles and looking up users by employee ID.
    image: https://www.paradox.ai/images/paradox-logo.png
    humanURL: https://readme.paradox.ai/reference/get-users
    baseURL: https://api.paradox.ai/api/v1/public
    tags:
      - Administration
      - Roles
      - Users
    properties:
      - type: Documentation
        url: https://readme.paradox.ai/reference/get-users
      - type: OpenAPI
        url: openapi/paradox-api-openapi.yml
  - name: Paradox Scheduling API
    description: API for managing interview scheduling within the Paradox platform including retrieving multiparty interviewers, interview settings, job location rooms, sending interview alerts, and accessing interview history.
    image: https://www.paradox.ai/images/paradox-logo.png
    humanURL: https://readme.paradox.ai/reference/send-interview-alerts
    baseURL: https://api.paradox.ai/api/v1/public
    tags:
      - Calendars
      - Interviews
      - Scheduling
    properties:
      - type: Documentation
        url: https://readme.paradox.ai/reference/send-interview-alerts
      - type: API Reference
        url: https://readme.paradox.ai/reference/get-job-location-rooms
      - type: OpenAPI
        url: openapi/paradox-api-openapi.yml
  - name: Paradox Locations API
    description: API for managing locations within the Paradox platform including creating, retrieving, updating, and deleting locations, as well as looking up locations by job location code and managing location rooms.
    image: https://www.paradox.ai/images/paradox-logo.png
    humanURL: https://readme.paradox.ai/reference/get-single-location-by-job_loc_code
    baseURL: https://api.paradox.ai/api/v1/public
    tags:
      - Job Sites
      - Locations
      - Rooms
    properties:
      - type: Documentation
        url: https://readme.paradox.ai/reference/get-single-location-by-job_loc_code
      - type: API Reference
        url: https://readme.paradox.ai/reference/update-a-location
      - type: OpenAPI
        url: openapi/paradox-api-openapi.yml
  - name: Paradox Reporting API
    description: API for accessing and generating reports within the Paradox platform including retrieving report lists, creating new reports, and accessing individual report details.
    image: https://www.paradox.ai/images/paradox-logo.png
    humanURL: https://readme.paradox.ai/reference/get-report-list
    baseURL: https://api.paradox.ai/api/v1/public
    tags:
      - Analytics
      - Data
      - Reporting
    properties:
      - type: Documentation
        url: https://readme.paradox.ai/reference/get-report-list
      - type: OpenAPI
        url: openapi/paradox-api-openapi.yml
  - name: Paradox Candidate Attributes API
    description: API for managing candidate attributes within the Paradox platform including retrieving, patching, and updating candidate attribute data.
    image: https://www.paradox.ai/images/paradox-logo.png
    humanURL: https://readme.paradox.ai/reference/get-candidate-attributes
    baseURL: https://api.paradox.ai/api/v1/public
    tags:
      - Attributes
      - Candidates
      - Custom Fields
    properties:
      - type: Documentation
        url: https://readme.paradox.ai/reference/get-candidate-attributes
      - type: OpenAPI
        url: openapi/paradox-api-openapi.yml
  - name: Paradox User Permissions API
    description: API for managing user location permissions within the Paradox platform including adding, retrieving, and deleting location-based access permissions for users.
    image: https://www.paradox.ai/images/paradox-logo.png
    humanURL: https://readme.paradox.ai/reference/authentication
    baseURL: https://api.paradox.ai/api/v1/public
    tags:
      - Access Control
      - Permissions
      - Users
    properties:
      - type: Documentation
        url: https://readme.paradox.ai/reference/authentication
      - type: OpenAPI
        url: openapi/paradox-api-openapi.yml
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
