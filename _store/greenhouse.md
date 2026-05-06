---
aid: greenhouse
name: Greenhouse
description: Greenhouse is an applicant tracking system (ATS) and recruiting software platform. It exposes a family of APIs and webhooks that let partners and customers manage candidates, jobs, applications, onboarding, audit logs, and assessment integrations.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - ATS
  - Recruiting
  - Candidates
  - Jobs
  - Onboarding
  - HR
created: '2025-01-07'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/greenhouse/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: greenhouse:harvest
    name: Greenhouse Harvest API
    description: The Harvest API provides programmatic access to Greenhouse Recruiting data, including candidates, applications, jobs, departments, offices, and users.
    humanURL: https://developers.greenhouse.io/harvest.html
    baseURL: https://harvest.greenhouse.io/v1
    tags:
      - Harvest
      - Candidates
      - Jobs
      - Applications
    properties:
      - type: Documentation
        url: https://developers.greenhouse.io/harvest.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/greenhouse/refs/heads/main/openapi/greenhouse-harvest-openapi.yml
  - aid: greenhouse:job-board
    name: Greenhouse Job Board API
    description: The Job Board API enables building careers pages with custom look and feel, retrieving jobs, offices, departments, sections, education reference data, and submitting applications.
    humanURL: https://developers.greenhouse.io/job-board.html
    baseURL: https://boards-api.greenhouse.io/v1/boards
    tags:
      - Job Board
      - Careers
      - Jobs
    properties:
      - type: Documentation
        url: https://developers.greenhouse.io/job-board.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/greenhouse/refs/heads/main/openapi/greenhouse-job-board-openapi.yml
  - aid: greenhouse:ingestion
    name: Greenhouse Candidate Ingestion API
    description: The Ingestion API enables sourcing partners to submit prospects and candidates to Greenhouse and to retrieve job and prospect pool information.
    humanURL: https://developers.greenhouse.io/candidate-ingestion.html
    baseURL: https://api.greenhouse.io/v1/partner
    tags:
      - Ingestion
      - Candidates
      - Sourcing
    properties:
      - type: Documentation
        url: https://developers.greenhouse.io/candidate-ingestion.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/greenhouse/refs/heads/main/openapi/greenhouse-ingestion-openapi.yml
  - aid: greenhouse:onboarding
    name: Greenhouse Onboarding API
    description: A GraphQL API for Greenhouse Onboarding. Provides queries and mutations for employees, departments, locations, custom fields, teams, and pending hires.
    humanURL: https://developers.greenhouse.io/gho.html
    baseURL: https://onboarding-api.greenhouse.io/graphql
    tags:
      - Onboarding
      - GraphQL
      - Employees
    properties:
      - type: Documentation
        url: https://developers.greenhouse.io/gho.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/greenhouse/refs/heads/main/openapi/greenhouse-onboarding-openapi.yml
  - aid: greenhouse:assessment
    name: Greenhouse Assessment API
    description: The Assessment Partner API enables assessment platforms (code testing, video interviewing, personality testing) to seamlessly integrate with the Greenhouse interview workflow.
    humanURL: https://developers.greenhouse.io/assessment.html
    tags:
      - Assessment
      - Testing
      - Candidates
    properties:
      - type: Documentation
        url: https://developers.greenhouse.io/assessment.html
  - aid: greenhouse:audit-log
    name: Greenhouse Audit Log API
    description: The Audit Log API offers a record of important events, providing insight into who accessed or edited information in Greenhouse.
    humanURL: https://developers.greenhouse.io/audit-log.html
    tags:
      - Audit
      - Compliance
      - Logging
    properties:
      - type: Documentation
        url: https://developers.greenhouse.io/audit-log.html
  - aid: greenhouse:recruiting-webhooks
    name: Greenhouse Recruiting Webhooks
    description: Recruiting Webhooks deliver event notifications for Greenhouse Recruiting activities such as candidate updates, application stage changes, and offers.
    humanURL: https://developers.greenhouse.io/webhooks.html
    tags:
      - Webhooks
      - Recruiting
      - Events
    properties:
      - type: Documentation
        url: https://developers.greenhouse.io/webhooks.html
  - aid: greenhouse:onboarding-webhooks
    name: Greenhouse Onboarding Webhooks
    description: Onboarding Webhooks deliver event notifications for Greenhouse Onboarding activities such as new hires and employee updates.
    humanURL: https://developers.greenhouse.io/onboarding_webhooks.html
    tags:
      - Webhooks
      - Onboarding
      - Events
    properties:
      - type: Documentation
        url: https://developers.greenhouse.io/onboarding_webhooks.html
common:
  - type: Documentation
    name: Greenhouse Developer Docs
    description: Top-level developer documentation hub for Greenhouse.
    url: https://developers.greenhouse.io
  - type: GitHubOrg
    name: Greenhouse GitHub
    description: Greenhouse open source repositories, including API docs.
    url: https://github.com/grnhse
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
