---
aid: indeed
name: Indeed
description: Indeed is the world's largest job site, connecting millions of job seekers with employers across industries and locations worldwide. Indeed offers a suite of APIs for applicant tracking systems, job boards, and hiring platforms to integrate with its employment ecosystem.
image: https://www.indeed.com/images/indeed-logo.png
url: https://raw.githubusercontent.com/api-evangelist/indeed/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
tags:
  - Careers
  - Employment
  - Hiring
  - Job Search
  - Jobs
  - Recruiting
apis:
  - aid: indeed:job-search
    name: Indeed Job Search API
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
    contact:
      - FN: Indeed API Support
        email: opensource@indeed.com
        url: https://opensource.indeedeng.io/
  - aid: indeed:publisher
    name: Indeed Publisher API
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
      - type: SignUp
        url: https://www.indeed.com/publisher/signup
  - aid: indeed:apply
    name: Indeed Apply API
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
      - type: GettingStarted
        url: https://docs.indeed.com/indeed-apply/add-indeed-apply
  - aid: indeed:job-sync
    name: Indeed Job Sync API
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
      - type: GettingStarted
        url: https://docs.indeed.com/job-sync-api/job-sync-api-guide
      - type: FAQ
        url: https://docs.indeed.com/job-sync-api/reference/faq
      - type: Sandbox
        url: https://docs.indeed.com/getstarted/simulated-graphql-environment
      - type: OpenAPI
        url: openapi/indeed-employer-api-openapi.yml
      - type: JSONLD
        url: json-ld/indeed-context.jsonld
  - aid: indeed:disposition-sync
    name: Indeed Disposition Sync API
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
      - type: GettingStarted
        url: https://docs.indeed.com/disposition-sync-api/disposition-sync-api-guide
  - aid: indeed:sponsored-jobs
    name: Indeed Sponsored Jobs API
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
      - type: GettingStarted
        url: https://docs.indeed.com/sponsored-jobs-api/sponsored-jobs-api-1-guides/get-started
      - type: APIReference
        url: https://docs.indeed.com/api/sponsored-jobs-api/sponsored-jobs-api-reference
  - aid: indeed:job-update
    name: Indeed Job Update API
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
  - aid: indeed:real-time
    name: Indeed Real-time API
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
      - type: GettingStarted
        url: https://docs.indeed.com/real-time-api/get-started
  - aid: indeed:interview
    name: Indeed Interview API
    description: A GraphQL API for scheduling, updating, retrieving information about, and canceling virtual interview events with job candidates. This API is deprecated.
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
      - type: GettingStarted
        url: https://docs.indeed.com/indeed-interview-api/indeed-interview-api-guide
      - type: APIReference
        url: https://docs.indeed.com/dev/reference/indeed-interview-api
  - aid: indeed:employer
    name: Indeed Employer API
    description: A RESTful abstraction of Indeed's employer-facing partner APIs, providing unified access to employer management, candidate retrieval, and job posting operations.
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
  - aid: indeed:employer-data
    name: Indeed Employer Data API
    description: A GraphQL API for creating and updating employer entities on Indeed and the Indeed PLUS platform.
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
      - type: APIReference
        url: https://docs.indeed.com/api/employers-api/create-using-post
      - type: Sandbox
        url: https://docs.indeed.com/getstarted/simulated-graphql-environment
  - aid: indeed:conversion-tracking
    name: Indeed Conversion Tracking API
    description: Tracks candidate events such as job application page visits and completed applications from Indeed to your site. Provides data for reporting, analytics dashboards, and apply-based bidding algorithms.
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
      - type: APIReference
        url: https://docs.indeed.com/api/conversion-tracking-api/conversion-tracking-api
  - aid: indeed:employer-registration
    name: Indeed Employer Registration API
    description: Part of the Candidate Sync APIs, this API allows ATS partners to register employers for Candidate Sync integration.
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
  - aid: indeed:retrieve-candidates
    name: Indeed Retrieve Candidates API
    description: Part of the Candidate Sync APIs, this API enables ATS partners to get candidate and application information from Indeed on behalf of employers.
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
      - type: JSONSchema
        url: json-schema/indeed-candidate-schema.json
      - type: JSONLD
        url: json-ld/indeed-context.jsonld
common:
  - type: DeveloperPortal
    url: https://opensource.indeedeng.io/
  - type: TermsOfService
    url: https://www.indeed.com/legal/terms-of-service
  - type: PrivacyPolicy
    url: https://www.indeed.com/legal/privacy
  - type: StatusPage
    url: https://status.indeed.com
  - type: Support
    url: https://support.indeed.com/hc/en-us
  - type: Blog
    url: https://engineering.indeedblog.com/
  - type: GitHubOrganization
    url: https://github.com/indeedeng
  - type: X
    url: https://twitter.com/indeedeng
  - type: RateLimits
    url: https://opensource.indeedeng.io/api-documentation/docs/rate-limits
  - type: Authentication
    url: https://docs.indeed.com/authorization/
  - type: GettingStarted
    url: https://docs.indeed.com/getstarted/
  - type: ReleaseNotes
    url: https://docs.indeed.com/release-notes/
  - type: Sandbox
    url: https://docs.indeed.com/getstarted/simulated-graphql-environment
  - type: LinkedIn
    url: https://www.linkedin.com/company/indeed-com/
  - type: NaftikoCapability
    url: capabilities/shared/employer-api.yaml
    title: Employer API Shared Definition
  - type: NaftikoCapability
    url: capabilities/talent-acquisition.yaml
    title: Talent Acquisition Workflow
  - type: Features
    data:
      - name: Job Search and Discovery
        description: Search millions of job listings by keyword, location, salary, and other criteria across industries worldwide.
      - name: Job Posting and Syndication
        description: Post and syndicate job listings from ATS platforms to Indeed's marketplace with automated synchronization.
      - name: Candidate Management
        description: Retrieve and manage candidate applications, track disposition status, and sync hiring data with ATS systems.
      - name: Sponsored Job Campaigns
        description: Create and manage pay-per-click sponsored job campaigns with budget controls and performance analytics.
      - name: Indeed Apply Integration
        description: Enable one-click job applications directly through Indeed with screener questions and EEO compliance.
      - name: Conversion Tracking
        description: Track candidate events from Indeed to employer sites for analytics, reporting, and bidding optimization.
      - name: Real-Time Event Streaming
        description: Stream server-sent events for instant application updates and job lifecycle notifications.
  - type: UseCases
    data:
      - name: ATS Job Distribution
        description: Automatically distribute job postings from applicant tracking systems to Indeed's marketplace with real-time synchronization.
      - name: Candidate Pipeline Management
        description: Retrieve and manage candidates through the hiring pipeline with disposition tracking and status updates.
      - name: Recruitment Marketing Analytics
        description: Track campaign performance, application conversions, and ROI across sponsored and organic job listings.
      - name: Employer Branding
        description: Create and manage employer profiles on Indeed to attract candidates with company information and branding.
      - name: High-Volume Hiring
        description: Scale recruitment operations with automated job posting, candidate retrieval, and application processing.
  - type: Integrations
    data:
      - name: Greenhouse
        description: Native ATS integration for job posting synchronization and candidate data exchange with Greenhouse.
      - name: Lever
        description: Pre-built integration for posting jobs and retrieving candidate applications through Lever ATS.
      - name: Workday
        description: Enterprise integration for syncing job postings and candidate data with Workday Recruiting.
      - name: iCIMS
        description: Integration for job distribution and candidate management through iCIMS talent acquisition platform.
      - name: SAP SuccessFactors
        description: Connector for job posting and candidate synchronization with SAP SuccessFactors Recruiting.
      - name: Oracle Taleo
        description: Integration for distributing jobs and managing candidates through Oracle Taleo ATS.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
