---
aid: pluralsight
url: https://raw.githubusercontent.com/api-evangelist/pluralsight/refs/heads/main/apis.yml
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/course-catalog.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/content-catalog.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/learning-paths.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/labs.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/programs.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/tags.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/content-slug.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/channels.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/course-progress.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/content-progress.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/course-daily-usage.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/practice-exams.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/skills-assessment.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/role-iq.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/user-management.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/teams.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://developer.pluralsight.com
  - type: graphql
    url: https://paas-api.pluralsight.com/graphql
  - type: openapi
    url: openapi/plan-info.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://help.pluralsight.com/hc/en-us/articles/27573677812884-DORA-metrics-API
  - type: openapi
    url: openapi/flow-dora-metrics.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://help.pluralsight.com/hc/en-us/articles/31476876875028-Updated-Coding-metrics-API
  - type: openapi
    url: openapi/flow-coding-metrics.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://help.pluralsight.com/hc/en-us/articles/24286030333332-Collaboration-metrics-API
  - type: openapi
    url: openapi/flow-collaboration-metrics.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
  - type: openapi
    url: openapi/flow-commits.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
  - type: openapi
    url: openapi/flow-pull-requests.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
  - type: openapi
    url: openapi/flow-repos.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
  - type: openapi
    url: openapi/flow-users.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
  - type: openapi
    url: openapi/flow-teams.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://help.pluralsight.com/hc/en-us/articles/24285986280212-Integrations-API
  - type: openapi
    url: openapi/flow-integrations.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://help.pluralsight.com/hc/en-us/sections/24176771997588-Customer-API-references
  - type: openapi
    url: openapi/flow-tickets.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://help.pluralsight.com/hc/en-us/articles/24420566008084-Migrating-from-REST-to-GraphQL-APIs
  - type: openapi
    url: openapi/reports-rest.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://help.pluralsight.com/hc/en-us/articles/24420566008084-Migrating-from-REST-to-GraphQL-APIs
  - type: openapi
    url: openapi/licensing-rest.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
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
  - type: documentation
    url: https://help.pluralsight.com/hc/en-us/articles/24420554286868-Skills-APIs-and-integrations
  - type: openapi
    url: openapi/public-course-catalog-rest.yml
  contact:
  - FN: Pluralsight API Support
    email: support@pluralsight.com
    url: https://help.pluralsight.com
name: Pluralsight
tags:
- Courses
- Education
- Engineering Metrics
- Learning
- Skills Assessment
- Technology
- Video Training
type: Contract
image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for the Pluralsight technology skills and engineering intelligence platform, providing access to courses, learning paths, assessments, user progress, channels, teams, and engineering metrics via GraphQL and REST APIs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

