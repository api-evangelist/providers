---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Teamwork Agentic Access
  operation_count: 3
  slug: teamwork-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://{site}.teamwork.com/projects/api/v3
  baseurl_source: declared
  description: The Activity API from Teamwork.com — 1 operation(s) for activity.
  name: Teamwork.com Activity API
  slug: teamwork-activity-api
- baseURL: https://{site}.teamwork.com/projects/api/v3
  baseurl_source: declared
  description: The Projects API from Teamwork.com — 1 operation(s) for projects.
  name: Teamwork.com Projects API
  slug: teamwork-projects-api
- baseURL: https://{site}.teamwork.com/projects/api/v3
  baseurl_source: declared
  description: The Tasks API from Teamwork.com — 1 operation(s) for tasks.
  name: Teamwork.com Tasks API
  slug: teamwork-tasks-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Teamwork.com Projects API v3 Activity API
  slug: open-teamwork-activity-api
- collection_type: open
  name: Teamwork.com API v3 Activity Projects API
  slug: open-teamwork-projects-api
- collection_type: open
  name: Teamwork.com Projects API v3 Activity Tasks API
  slug: open-teamwork-tasks-api
- collection_type: open
  name: Teamwork.com Projects API v3
  slug: open-teamwork
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/teamwork-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/teamwork-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teamwork-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/teamwork-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teamwork
- group: company
  title: ''
  type: Website
  url: https://www.teamwork.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.teamwork.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.teamwork.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.teamwork.com/signup
- group: operate
  title: ''
  type: Support
  url: https://support.teamwork.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.teamwork.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teamwork-com
- group: company
  title: ''
  type: Blog
  url: https://www.teamwork.com/blog/
created: '2026-05-11'
description: Teamwork.com is a project management and client work platform built for client services, agencies, and professional services teams to manage projects, tasks, time tracking, billing, resource planning, and collaboration in one place. The platform provides product offerings including Projects, Desk, Chat, Spaces, and CRM with deep integrations across the client delivery lifecycle. Teamwork.com offers a comprehensive REST API (v3) for the Projects product allowing programmatic access to projects, tasks, time entries, milestones, people, and reporting, with Bearer Token (OAuth 2.0) and HTTP Basic authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-05-11'
name: Teamwork.com
nav: Providers
network: true
overview: 'Teamwork.com publishes 3 APIs on the [APIs.io](https://apis.io/) network: Activity API, Projects API, and Tasks API. Tagged areas include Project Management, Client Services, Task Management, Time Tracking, and Collaboration.


  Teamwork.com''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 7 more developer resources.'
random_paper: 13
screenshot: https://raw.githubusercontent.com/api-evangelist/teamwork/refs/heads/main/screenshots/teamwork-2026-06-20T195100.png
security:
- kind: authentication
  name: Teamwork Authentication
  slug: teamwork-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Teamwork Domain Security
  slug: teamwork-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: teamwork
tags:
- Project Management
- Client Services
- Task Management
- Time Tracking
- Collaboration
- Professional Services Automation
website: https://www.teamwork.com
---
