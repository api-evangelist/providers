---
aid: smartrecruiters
name: SmartRecruiters
description: SmartRecruiters is a talent acquisition platform that provides a comprehensive suite of APIs for recruiting, hiring, and workforce management. The platform enables organizations to manage job postings, candidate applications, assessments, interviews, and offers through a unified REST API ecosystem.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Human Resources
  - Recruiting
  - Talent Acquisition
  - Applicant Tracking
  - HR Technology
created: '2025-01-07'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/smartrecruiters/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: smartrecruiters:posting-api
    name: SmartRecruiters Posting API
    description: The Posting API enables customers to build fully customizable career sites by providing access to published job postings. It supports searching and filtering postings by keyword, location, department, and custom fields.
    humanURL: https://developers.smartrecruiters.com/docs/posting-api
    baseURL: https://api.smartrecruiters.com
    tags:
      - Jobs
      - Postings
      - Career Sites
    properties:
      - type: Documentation
        url: https://developers.smartrecruiters.com/docs/posting-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/smartrecruiters/refs/heads/main/openapi/smartrecruiters-posting-openapi.yml
  - aid: smartrecruiters:job-api
    name: SmartRecruiters Job API
    description: The Job API enables customers to extract and import jobs data, supporting full job lifecycle management including creation, updates, and status management.
    humanURL: https://developers.smartrecruiters.com/docs/api-reference
    baseURL: https://api.smartrecruiters.com
    tags:
      - Jobs
      - Hiring
    properties:
      - type: Documentation
        url: https://developers.smartrecruiters.com/docs/api-reference
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/smartrecruiters/refs/heads/main/openapi/smartrecruiters-jobs-openapi.yml
  - aid: smartrecruiters:candidate-api
    name: SmartRecruiters Candidate API
    description: The Candidate API enables customers to import, export, read, and update candidate data. Supports full candidate profile management, application tracking, and status updates.
    humanURL: https://developers.smartrecruiters.com/docs/api-reference
    baseURL: https://api.smartrecruiters.com
    tags:
      - Candidates
      - Applicants
      - Talent
    properties:
      - type: Documentation
        url: https://developers.smartrecruiters.com/docs/api-reference
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/smartrecruiters/refs/heads/main/openapi/smartrecruiters-candidates-openapi.yml
  - aid: smartrecruiters:application-api
    name: SmartRecruiters Application API
    description: The Application API enables integration of the full candidate application including screening questions, and allows new applications to be submitted through partner systems and career sites.
    humanURL: https://developers.smartrecruiters.com/docs/application-api-1
    baseURL: https://api.smartrecruiters.com
    tags:
      - Applications
      - Candidates
      - Screening
    properties:
      - type: Documentation
        url: https://developers.smartrecruiters.com/docs/application-api-1
  - aid: smartrecruiters:assessment-api
    name: SmartRecruiters Assessment API
    description: The Assessment API allows customers to order assessment services available through the SmartRecruiters Marketplace and allows partners to interface with the marketplace to provide and manage assessment services.
    humanURL: https://developers.smartrecruiters.com/docs/partners-assessment-api
    baseURL: https://api.smartrecruiters.com
    tags:
      - Assessments
      - Marketplace
      - Partners
    properties:
      - type: Documentation
        url: https://developers.smartrecruiters.com/docs/partners-assessment-api
  - aid: smartrecruiters:interview-api
    name: SmartRecruiters Interview API
    description: The Interview API provides self-scheduling capabilities and interview template management for streamlining the interview process between recruiters and candidates.
    humanURL: https://developers.smartrecruiters.com/docs/api-reference
    baseURL: https://api.smartrecruiters.com
    tags:
      - Interviews
      - Scheduling
    properties:
      - type: Documentation
        url: https://developers.smartrecruiters.com/docs/api-reference
  - aid: smartrecruiters:reporting-api
    name: SmartRecruiters Reporting API
    description: The Reporting API provides access to custom reports in CSV format, enabling analytics and data export capabilities for HR metrics and recruiting performance.
    humanURL: https://developers.smartrecruiters.com/docs/api-reference
    baseURL: https://api.smartrecruiters.com
    tags:
      - Reporting
      - Analytics
      - Data Export
    properties:
      - type: Documentation
        url: https://developers.smartrecruiters.com/docs/api-reference
  - aid: smartrecruiters:job-board-api
    name: SmartRecruiters Job Board API
    description: The Job Board API enables job board partners to integrate SmartRecruiters job postings directly into their platforms with real-time synchronization.
    humanURL: https://developers.smartrecruiters.com/docs/partners-job-board-api
    baseURL: https://api.smartrecruiters.com
    tags:
      - Job Boards
      - Partners
      - Jobs
    properties:
      - type: Documentation
        url: https://developers.smartrecruiters.com/docs/partners-job-board-api
common:
  - type: Website
    url: https://www.smartrecruiters.com/
  - type: Developer Portal
    url: https://developers.smartrecruiters.com/
  - type: Documentation
    url: https://developers.smartrecruiters.com/docs/the-smartrecruiters-platform
  - type: Authentication
    url: https://developers.smartrecruiters.com/docs/authentication
  - type: GitHub Organization
    url: https://github.com/smartrecruiters
  - type: Blog
    url: https://www.smartrecruiters.com/blog/
  - type: Marketplace
    url: https://www.smartrecruiters.com/marketplace/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
