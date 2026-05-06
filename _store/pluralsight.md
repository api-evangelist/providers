---
name: Pluralsight
description: APIs for the Pluralsight technology skills and engineering intelligence platform, providing access to courses, learning paths, assessments, user progress, channels, teams, and engineering metrics via GraphQL and REST APIs.
image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
url: https://raw.githubusercontent.com/api-evangelist/pluralsight/refs/heads/main/apis.yml
created: '2024'
modified: '2026-04-17'
tags:
  - Courses
  - Education
  - Engineering Metrics
  - Learning
  - Skills Assessment
  - Technology
  - Video Training
apis:
  - name: Pluralsight Course Catalog API
    description: GraphQL query for accessing course catalog information including titles, descriptions, authors, duration, release dates, and retirement status. Updated daily.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Catalog
      - Content
      - Courses
      - Graphql
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/course-catalog.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:course-catalog-api
  - name: Pluralsight Content Catalog API
    description: GraphQL query for accessing the general content catalog including videos, guides, interactive courses, and other content types beyond traditional courses.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Catalog
      - Content
      - Graphql
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/content-catalog.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:content-catalog-api
  - name: Pluralsight Learning Paths API
    description: GraphQL query for accessing learning path catalog data including structured sequences of courses and content organized around specific skills and roles.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Catalog
      - Content
      - Graphql
      - Learning Paths
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/learning-paths.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:learning-paths-api
  - name: Pluralsight Labs API
    description: GraphQL queries for accessing lab catalog and lab activity data for hands-on learning experiences and practical exercises.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Catalog
      - Graphql
      - Hands-On
      - Labs
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/labs.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:labs-api
  - name: Pluralsight Programs API
    description: GraphQL query for accessing the program catalog including structured learning programs and curriculum offerings.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Catalog
      - Curriculum
      - Graphql
      - Programs
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/programs.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:programs-api
  - name: Pluralsight Tags API
    description: GraphQL query for accessing content tags and taxonomy data used to categorize and organize learning content.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Content
      - Graphql
      - Taxonomy
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/tags.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:tags-api
  - name: Pluralsight Content Slug API
    description: GraphQL query for resolving content slugs to internal identifiers, enabling lookup of content by human-readable URL slugs.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Content
      - Graphql
      - Identifiers
      - Slugs
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/content-slug.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:content-slug-api
  - name: Pluralsight Channels API
    description: GraphQL queries and mutations for managing content channels including creating channels, managing members and groups, organizing content sections, and tracking channel progress.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Channels
      - Content Curation
      - Graphql
      - Members
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/channels.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:channels-api
  - name: Pluralsight Course Progress API
    description: GraphQL query for tracking user course progress including completion status and viewing history for video courses. Updated daily.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Completion
      - Courses
      - Graphql
      - Progress
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/course-progress.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:course-progress-api
  - name: Pluralsight Content Progress API
    description: GraphQL query for tracking user progress across all content types including videos, guides, paths, interactive courses, and projects. Currently in beta.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Analytics
      - Beta
      - Content
      - Graphql
      - Progress
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/content-progress.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:content-progress-api
  - name: Pluralsight Course Daily Usage API
    description: GraphQL query for retrieving daily course engagement metrics and usage statistics.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Analytics
      - Daily Metrics
      - Graphql
      - Usage
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/course-daily-usage.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:course-daily-usage-api
  - name: Pluralsight Practice Exams API
    description: GraphQL query for retrieving practice exam attempt data including scores and results.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Assessments
      - Certification Prep
      - Graphql
      - Practice Exams
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/practice-exams.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:practice-exams-api
  - name: Pluralsight Skills Assessment API
    description: GraphQL queries for accessing skill assessments, Skill IQ scores, assessment catalogs, and competency measurements.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Assessments
      - Graphql
      - Skill Iq
      - Skills
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/skills-assessment.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:skills-assessment-api
  - name: Pluralsight Role IQ API
    description: GraphQL queries and mutations for Role IQ assessments, role catalogs, skill assignments, and user/team role associations.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Assessments
      - Graphql
      - Role Iq
      - Roles
      - Skills
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/role-iq.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:role-iq-api
  - name: Pluralsight User Management API
    description: GraphQL queries and mutations for managing users including listing users, inviting members, editing user details, removing users, and canceling invitations.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Graphql
      - Invitations
      - Licensing
      - Users
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/user-management.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:user-management-api
  - name: Pluralsight Teams API
    description: GraphQL queries and mutations for managing teams including creating teams, managing membership, assigning managers, and configuring team permissions.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Graphql
      - Management
      - Permissions
      - Teams
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/teams.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:teams-api
  - name: Pluralsight Plan Info API
    description: GraphQL query for retrieving account and plan details including subscription tier and configuration.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://developer.pluralsight.com
    baseURL: https://paas-api.pluralsight.com/graphql
    tags:
      - Account
      - Graphql
      - Plan
      - Subscription
    properties:
      - type: Documentation
        url: https://developer.pluralsight.com
      - type: GraphQL
        url: https://paas-api.pluralsight.com/graphql
      - type: OpenAPI
        url: openapi/plan-info.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:plan-info-api
  - name: Pluralsight Flow DORA Metrics API
    description: REST API for accessing DORA engineering metrics including deployment frequency, lead time for changes, change failure rate, and time to restore service.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://help.pluralsight.com/hc/en-us/articles/27573677812884-DORA-metrics-API
    baseURL: https://flow-api.pluralsight.com/dora/build-release
    tags:
      - Change Failure Rate
      - Deployment Frequency
      - Dora
      - Engineering Metrics
      - Lead Time
    properties:
      - type: Documentation
        url: https://help.pluralsight.com/hc/en-us/articles/27573677812884-DORA-metrics-API
      - type: OpenAPI
        url: openapi/flow-dora-metrics.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:flow-dora-metrics-api
  - name: Pluralsight Flow Coding Metrics API
    description: REST API for accessing code-level engineering metrics and developer productivity data with date range filtering.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://help.pluralsight.com/hc/en-us/articles/31476876875028-Updated-Coding-metrics-API
    baseURL: https://flow-api.pluralsight.com/collaboration/code/metrics
    tags:
      - Coding Metrics
      - Engineering Metrics
      - Productivity
    properties:
      - type: Documentation
        url: https://help.pluralsight.com/hc/en-us/articles/31476876875028-Updated-Coding-metrics-API
      - type: OpenAPI
        url: openapi/flow-coding-metrics.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:flow-coding-metrics-api
  - name: Pluralsight Flow Collaboration Metrics API
    description: REST API for accessing pull request and collaboration metrics for engineering teams with date range filtering.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://help.pluralsight.com/hc/en-us/articles/24286030333332-Collaboration-metrics-API
    baseURL: https://api.appfireflow.com/collaboration/pullrequest/metrics
    tags:
      - Collaboration
      - Engineering Metrics
      - Pull Requests
    properties:
      - type: Documentation
        url: https://help.pluralsight.com/hc/en-us/articles/24286030333332-Collaboration-metrics-API
      - type: OpenAPI
        url: openapi/flow-collaboration-metrics.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:flow-collaboration-metrics-api
  - name: Pluralsight Flow Commits API
    description: REST API for accessing commit data and aggregated commit metrics across repositories.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
    baseURL: https://<workspace>.appfireflow.com/v3/customer/core
    tags:
      - Commits
      - Engineering Data
      - Source Control
    properties:
      - type: Documentation
        url: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
      - type: OpenAPI
        url: openapi/flow-commits.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:flow-commits-api
  - name: Pluralsight Flow Pull Requests API
    description: REST API for accessing pull request data, comments, and events across repositories.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
    baseURL: https://<workspace>.appfireflow.com/v3/customer/core
    tags:
      - Code Review
      - Engineering Data
      - Pull Requests
    properties:
      - type: Documentation
        url: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
      - type: OpenAPI
        url: openapi/flow-pull-requests.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:flow-pull-requests-api
  - name: Pluralsight Flow Repos API
    description: REST API for accessing repository data and metadata across connected source control systems.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
    baseURL: https://<workspace>.appfireflow.com/v3/customer/core
    tags:
      - Engineering Data
      - Repositories
      - Source Control
    properties:
      - type: Documentation
        url: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
      - type: OpenAPI
        url: openapi/flow-repos.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:flow-repos-api
  - name: Pluralsight Flow Users API
    description: REST API for managing Flow users including listing, updating, merging, hiding, and bulk operations on user accounts.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
    baseURL: https://<workspace>.appfireflow.com/v3/customer/core
    tags:
      - Engineering Data
      - Management
      - Users
    properties:
      - type: Documentation
        url: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
      - type: OpenAPI
        url: openapi/flow-users.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:flow-users-api
  - name: Pluralsight Flow Teams API
    description: REST API for managing Flow engineering teams and team membership data.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
    baseURL: https://<workspace>.appfireflow.com/v3/customer/core
    tags:
      - Engineering Data
      - Management
      - Teams
    properties:
      - type: Documentation
        url: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
      - type: OpenAPI
        url: openapi/flow-teams.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:flow-teams-api
  - name: Pluralsight Flow Integrations API
    description: REST API for managing Flow integrations and checking connection status with external tools and services.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://help.pluralsight.com/hc/en-us/articles/24285986280212-Integrations-API
    baseURL: https://<workspace>.appfireflow.com/v3/customer/core
    tags:
      - Connections
      - Engineering Data
      - Integrations
    properties:
      - type: Documentation
        url: https://help.pluralsight.com/hc/en-us/articles/24285986280212-Integrations-API
      - type: OpenAPI
        url: openapi/flow-integrations.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:flow-integrations-api
  - name: Pluralsight Flow Tickets API
    description: REST API for accessing ticket data including comments, events, and project associations from connected project management tools.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
    baseURL: https://<workspace>.appfireflow.com/v3/customer/core
    tags:
      - Engineering Data
      - Project Management
      - Tickets
    properties:
      - type: Documentation
        url: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
      - type: OpenAPI
        url: openapi/flow-tickets.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:flow-tickets-api
  - name: Pluralsight Reports REST API
    description: Legacy REST API for downloading user, course completion, and course usage reports as CSV files. Deprecated as of February 2025, removal scheduled for November 2025.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://help.pluralsight.com/hc/en-us/articles/24420566008084-Migrating-from-REST-to-GraphQL-APIs
    baseURL: https://app.pluralsight.com/plans/api/reports/v1
    tags:
      - Csv
      - Deprecated
      - Legacy
      - Reports
    properties:
      - type: Documentation
        url: https://help.pluralsight.com/hc/en-us/articles/24420566008084-Migrating-from-REST-to-GraphQL-APIs
      - type: OpenAPI
        url: openapi/reports-rest.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:reports-rest-api
  - name: Pluralsight Licensing REST API
    description: Legacy REST API for managing user invitations, users, and teams within a plan. Deprecated as of February 2025, removal scheduled for November 2025.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://help.pluralsight.com/hc/en-us/articles/24420566008084-Migrating-from-REST-to-GraphQL-APIs
    baseURL: https://app.pluralsight.com/plans/api/license/v1
    tags:
      - Deprecated
      - Invitations
      - Legacy
      - Licensing
      - Users
    properties:
      - type: Documentation
        url: https://help.pluralsight.com/hc/en-us/articles/24420566008084-Migrating-from-REST-to-GraphQL-APIs
      - type: OpenAPI
        url: openapi/licensing-rest.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:licensing-rest-api
  - name: Pluralsight Public Course Catalog REST API
    description: Legacy public REST API for accessing the full course catalog without authentication. Returns course IDs, titles, durations, release dates, and retirement status.
    image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
    humanURL: https://help.pluralsight.com/hc/en-us/articles/24420554286868-Skills-APIs-and-integrations
    baseURL: https://paas-rest-api.pluralsight.com
    tags:
      - Catalog
      - Courses
      - Legacy
      - Public
    properties:
      - type: Documentation
        url: https://help.pluralsight.com/hc/en-us/articles/24420554286868-Skills-APIs-and-integrations
      - type: OpenAPI
        url: openapi/public-course-catalog-rest.yml
    contact:
      - FN: Pluralsight API Support
        email: support@pluralsight.com
        url: https://help.pluralsight.com
    aid: pluralsight:public-course-catalog-rest-api
common:
  - type: Portal
    url: https://developer.pluralsight.com
  - type: GettingStarted
    url: https://developer.pluralsight.com/docs/getting-started
  - type: Authentication
    url: https://developer.pluralsight.com/docs/getting-started
  - type: FAQ
    url: https://developer.pluralsight.com/docs/getting-started/faqs
  - type: CodeExamples
    url: https://developer.pluralsight.com/docs/getting-started/examples
  - type: GraphQL
    url: https://developer.pluralsight.com/docs/getting-started/using-graphql
  - type: Documentation
    url: https://developer.pluralsight.com/docs/deprecations/2025-deprecation-guide
  - type: Documentation
    url: https://help.pluralsight.com/hc/en-us/articles/24420566008084-Migrating-from-REST-to-GraphQL-APIs
  - type: RateLimits
    url: https://developer.pluralsight.com/docs/rate-limits
  - type: TermsOfService
    url: https://www.pluralsight.com/terms
  - type: PrivacyPolicy
    url: https://www.pluralsight.com/privacy
  - type: Support
    url: https://help.pluralsight.com
  - type: StatusPage
    url: https://status.pluralsight.com
  - type: Blog
    url: https://www.pluralsight.com/blog
  - type: Features
    data:
      - name: Course Catalog API
        description: Access the full Pluralsight course catalog with titles, authors, duration, and release dates via GraphQL.
      - name: Skills Assessment
        description: Measure technology skills with Skill IQ assessments and track competency levels.
      - name: Role IQ
        description: Assess role readiness and track skill gaps for technology roles.
      - name: Learning Progress Tracking
        description: Track course completion, content progress, and daily usage across users and teams.
      - name: Channels
        description: Create and manage curated content channels with sections and member management.
      - name: User and Team Management
        description: Manage users, invitations, teams, and permissions via GraphQL mutations.
      - name: DORA Metrics
        description: Access DevOps Research and Assessment metrics for engineering team performance.
      - name: Coding Metrics
        description: Track code-level productivity metrics and developer activity.
      - name: Collaboration Metrics
        description: Monitor pull request and code review collaboration patterns.
      - name: Labs
        description: Access hands-on lab catalog and track lab activity for practical learning.
      - name: Practice Exams
        description: Retrieve practice exam attempts and scores for certification preparation.
      - name: Flow Engineering Intelligence
        description: Access commit, PR, ticket, and repository data for engineering analytics.
  - type: UseCases
    data:
      - name: LMS Integration
        description: Sync Pluralsight course catalog and completion data with enterprise learning management systems.
      - name: Skills Gap Analysis
        description: Assess team skill levels and identify training needs using Skill IQ and Role IQ data.
      - name: Engineering Performance
        description: Track DORA metrics, coding activity, and collaboration patterns for engineering teams.
      - name: Compliance Reporting
        description: Generate training completion reports for regulatory and compliance requirements.
      - name: Onboarding Automation
        description: Automate new hire provisioning, team assignment, and learning path enrollment.
      - name: Content Curation
        description: Build custom learning channels with curated content for specific teams and roles.
      - name: Developer Productivity
        description: Analyze commit, PR, and ticket data to measure and improve developer productivity.
      - name: Certification Tracking
        description: Track practice exam scores and assessment results for certification readiness.
  - type: Solutions
    data:
      - name: Pluralsight Skills
        description: Technology skills platform with courses, assessments, and learning paths for upskilling teams.
      - name: Pluralsight Flow
        description: Engineering intelligence platform with DORA metrics, coding analytics, and collaboration insights.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
aid: pluralsight
type: Index
specificationVersion: '0.19'
---
