---
aid: indeed
url: https://raw.githubusercontent.com/api-evangelist/indeed/refs/heads/main/apis.yml
apis:
- name: Indeed Job Search API
  description: Search for jobs by keyword, location, and other criteria. Returns job listings with details including title, company, location, and description. This API is deprecated and not available for new integrations.
  image: https://www.indeed.com/images/indeed-logo.png
  humanURL: https://developer.indeed.com/docs/publisher-jobs/job-search
  baseURL: https://api.indeed.com
  tags:
  - Deprecated
  - Jobs
  - Listings
  - Search
  properties:
  - type: Documentation
    url: https://opensource.indeedeng.io/api-documentation/docs/job-search/
  - type: OpenAPI
    url: https://api.indeed.com/openapi.json
  contact:
  - FN: Indeed API Support
    email: opensource@indeed.com
    url: https://opensource.indeedeng.io/
- name: Indeed Publisher API
  description: Monetize your website by displaying Indeed job listings. Earn revenue through cost-per-click advertising.
  image: https://www.indeed.com/images/indeed-logo.png
  humanURL: https://www.indeed.com/publisher
  baseURL: https://api.indeed.com/ads
  tags:
  - Advertising
  - Monetization
  - Publisher
  properties:
  - type: Documentation
    url: https://www.indeed.com/publisher/docs
  - type: Sign Up
    url: https://www.indeed.com/publisher/signup
- name: Indeed Apply API
  description: Allow job seekers to apply to your jobs directly through Indeed with a streamlined application process. Supports screener questions, EEO compliance for US employers, and disposition data integration.
  image: https://www.indeed.com/images/indeed-logo.png
  humanURL: https://docs.indeed.com/indeed-apply
  baseURL: https://api.indeed.com/apply
  tags:
  - Applications
  - Apply
  - Hiring
  properties:
  - type: Documentation
    url: https://docs.indeed.com/indeed-apply
  - type: Integration Guide
    url: https://www.indeed.com/hire/docs/apply-api
  - type: Screener Questions
    url: https://docs.indeed.com/indeed-apply/screener-questions
  - type: Application Data Reference
    url: https://docs.indeed.com/indeed-apply/application-data
  - type: ATS Integration
    url: https://docs.indeed.com/indeed-apply/ats
  - type: Direct Employer Integration
    url: https://docs.indeed.com/indeed-apply/direct-employer
  - type: Configuration Reference
    url: https://docs.indeed.com/indeed-apply/add-indeed-apply
- name: Indeed Job Sync API
  description: A GraphQL API that enables ATS partners to create, upsert, expire, and get status for job postings on Indeed. Supports qualifications, working hours, salary, benefits, and employer information.
  image: https://www.indeed.com/images/indeed-logo.png
  humanURL: https://docs.indeed.com/job-sync-api/
  baseURL: https://apis.indeed.com/graphql
  tags:
  - ATS
  - GraphQL
  - Jobs
  - Postings
  properties:
  - type: Documentation
    url: https://docs.indeed.com/job-sync-api/
  - type: Getting Started
    url: https://docs.indeed.com/job-sync-api/job-sync-api-guide
  - type: Integration Guide
    url: https://docs.indeed.com/job-sync-api/integrate-with-job-sync-api
  - type: FAQ
    url: https://docs.indeed.com/job-sync-api/reference/faq
  - type: Simulated Environment
    url: https://docs.indeed.com/getstarted/simulated-graphql-environment
  - type: OpenAPI
    url: openapi/indeed-employer-api-openapi.yml
  - type: JSONLD
    url: json-ld/indeed-context.jsonld
- name: Indeed Disposition Sync API
  description: A GraphQL API that enables ATS partners to send disposition data for Indeed Apply and non-Indeed Apply jobs to Indeed, tracking application status changes through various stages of the hiring process.
  image: https://www.indeed.com/images/indeed-logo.png
  humanURL: https://docs.indeed.com/disposition-sync-api/
  baseURL: https://apis.indeed.com/graphql
  tags:
  - Applications
  - ATS
  - Disposition
  - GraphQL
  - Tracking
  properties:
  - type: Documentation
    url: https://docs.indeed.com/disposition-sync-api/
  - type: Getting Started
    url: https://docs.indeed.com/disposition-sync-api/disposition-sync-api-guide
  - type: Integration Guide
    url: https://docs.indeed.com/disposition-sync-api/integrate-with-disposition-sync-api
- name: Indeed Sponsored Jobs API
  description: A GraphQL API used to get information about and manage an employer's sponsored job campaigns on Indeed, including campaign creation, budget management, and performance insights.
  image: https://www.indeed.com/images/indeed-logo.png
  humanURL: https://docs.indeed.com/sponsored-jobs-api/
  baseURL: https://apis.indeed.com/graphql
  tags:
  - Advertising
  - Campaigns
  - GraphQL
  - Sponsored
  properties:
  - type: Documentation
    url: https://docs.indeed.com/sponsored-jobs-api/
  - type: Getting Started
    url: https://docs.indeed.com/sponsored-jobs-api/sponsored-jobs-api-1-guides/get-started
  - type: Integration Guide
    url: https://docs.indeed.com/sponsored-jobs-api/sponsored-jobs-api-1-guides/integration-guide-for-ats-partners
  - type: API Reference
    url: https://docs.indeed.com/api/sponsored-jobs-api/sponsored-jobs-api-reference
- name: Indeed Job Update API
  description: Allows partners to list and update job postings on Indeed, including adding metadata to ATS-sourced jobs for improved quality and sponsorship grouping, and subscribing to jobs lifecycle events via webhooks.
  image: https://www.indeed.com/images/indeed-logo.png
  humanURL: https://docs.indeed.com/job-update-api/
  baseURL: https://apis.indeed.com/graphql
  tags:
  - GraphQL
  - Jobs
  - Updates
  - Webhooks
  properties:
  - type: Documentation
    url: https://docs.indeed.com/job-update-api/
- name: Indeed Real-time API
  description: Stream real-time server-sent events (SSE) to enable front-end applications to update instantly, supporting event filtering, deduplication, and latency tracking.
  image: https://www.indeed.com/images/indeed-logo.png
  humanURL: https://docs.indeed.com/real-time-api/get-started
  baseURL: https://apis.indeed.com
  tags:
  - Events
  - Real-Time
  - SSE
  - Streaming
  properties:
  - type: Documentation
    url: https://docs.indeed.com/api/real-time-api/indeed-real-time-api
  - type: Getting Started
    url: https://docs.indeed.com/real-time-api/get-started
- name: Indeed Interview API
  description: A GraphQL API for scheduling, updating, retrieving information about, and canceling virtual interview events with job candidates. Supports recording, interviewee and interviewer management, and calendar integration. This API is deprecated.
  image: https://www.indeed.com/images/indeed-logo.png
  humanURL: https://docs.indeed.com/indeed-interview-api
  baseURL: https://apis.indeed.com/graphql
  tags:
  - Deprecated
  - GraphQL
  - Interviews
  - Scheduling
  - Virtual
  properties:
  - type: Documentation
    url: https://docs.indeed.com/indeed-interview-api
  - type: Getting Started
    url: https://docs.indeed.com/indeed-interview-api/indeed-interview-api-guide
  - type: API Reference
    url: https://docs.indeed.com/dev/reference/indeed-interview-api
- name: Indeed Employer API
  description: A RESTful abstraction of Indeed's employer-facing partner APIs, providing unified access to employer management, candidate retrieval, and job posting operations. Covers the Employer Data API, Retrieve Candidates API, and Job Sync API in a single OpenAPI specification.
  image: https://www.indeed.com/images/indeed-logo.png
  humanURL: https://docs.indeed.com/employers/operations/create-employer
  baseURL: https://apis.indeed.com
  tags:
  - ATS
  - Candidates
  - Employers
  - Jobs
  properties:
  - type: Documentation
    url: https://docs.indeed.com/employers/operations/create-employer
  - type: OpenAPI
    url: openapi/indeed-employer-api-openapi.yml
  - type: JSONSchema
    url: json-schema/indeed-candidate-schema.json
  - type: JSONLD
    url: json-ld/indeed-context.jsonld
  - type: Candidates Overview
    url: https://docs.indeed.com/candidates/
  - type: Retrieve Candidates API
    url: https://docs.indeed.com/candidate-sync-apis/retrieve-candidates-api/
  - type: Job Sync API
    url: https://docs.indeed.com/job-sync-api/
  - type: Simulated Environment
    url: https://docs.indeed.com/getstarted/simulated-graphql-environment
- name: Indeed Employer Data API
  description: A GraphQL API for creating and updating employer entities on Indeed and the Indeed PLUS platform. Uses the patchEmployer mutation to submit employer data including name, location, and other attributes before creating associated job postings.
  image: https://www.indeed.com/images/indeed-logo.png
  humanURL: https://docs.indeed.com/employers/operations/create-employer
  baseURL: https://apis.indeed.com/graphql
  tags:
  - ATS
  - Employers
  - GraphQL
  properties:
  - type: Documentation
    url: https://docs.indeed.com/employers/operations/create-employer
  - type: Update Employer
    url: https://docs.indeed.com/employers/operations/update-employer
  - type: API Reference
    url: https://docs.indeed.com/api/employers-api/create-using-post
  - type: Simulated Environment
    url: https://docs.indeed.com/getstarted/simulated-graphql-environment
  - type: OpenAPI
    url: openapi/indeed-employer-api-openapi.yml
- name: Indeed Conversion Tracking API
  description: Tracks candidate events such as job application page visits and completed applications from Indeed to your site. Provides data for reporting, analytics dashboards, and apply-based bidding algorithms such as targetCPA.
  image: https://www.indeed.com/images/indeed-logo.png
  humanURL: https://docs.indeed.com/conversion-tracking-api/conversion-tracking-getting-started
  baseURL: https://apis.indeed.com
  tags:
  - Analytics
  - Conversion
  - Reporting
  - Tracking
  properties:
  - type: Documentation
    url: https://docs.indeed.com/conversion-tracking-api/conversion-tracking-getting-started
  - type: API Reference
    url: https://docs.indeed.com/api/conversion-tracking-api/conversion-tracking-api
  - type: HTML Tracker
    url: https://docs.indeed.com/conversion-tracking-api/conversion-tracker-html-code
  - type: OpenAPI
    url: https://developer.indeed.com/public/swagger/conversion-tracking.yaml
- name: Indeed Employer Registration API
  description: Part of the Candidate Sync APIs, this API allows ATS partners to register employers for Candidate Sync integration, manage feature settings, and synchronize candidate data between their ATS and Indeed.
  image: https://www.indeed.com/images/indeed-logo.png
  humanURL: https://docs.indeed.com/candidate-sync-apis/employer-registration-api/
  baseURL: https://apis.indeed.com/graphql
  tags:
  - ATS
  - Candidate Sync
  - Employers
  - Registration
  properties:
  - type: Documentation
    url: https://docs.indeed.com/candidate-sync-apis/employer-registration-api/
- name: Indeed Retrieve Candidates API
  description: Part of the Candidate Sync APIs, this API enables ATS partners to get candidate and application information from Indeed on behalf of employers, including fetching the most recent unacknowledged assets.
  image: https://www.indeed.com/images/indeed-logo.png
  humanURL: https://docs.indeed.com/candidate-sync-apis/retrieve-candidates-api/
  baseURL: https://apis.indeed.com/graphql
  tags:
  - Applications
  - ATS
  - Candidate Sync
  - Candidates
  properties:
  - type: Documentation
    url: https://docs.indeed.com/candidate-sync-apis/retrieve-candidates-api/
  - type: Candidates Overview
    url: https://docs.indeed.com/candidates/
  - type: JSONSchema
    url: json-schema/indeed-candidate-schema.json
  - type: JSONLD
    url: json-ld/indeed-context.jsonld
name: Indeed
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
type: Contract
image: https://www.indeed.com/images/indeed-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Indeed is the world's largest job site, connecting millions of job seekers with employers across industries and locations worldwide. Indeed offers a suite of APIs for applicant tracking systems, job boards, and hiring platforms to integrate with its employment ecosystem.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

