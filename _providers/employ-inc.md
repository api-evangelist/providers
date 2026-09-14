---
api_count: 4
apis:
- baseURL: https://www.employinc.com/wp-json/wp/v2
  baseurl_source: declared
  description: 'The WordPress REST API Employ, Inc. serves at www.employinc.com/wp-json/wp/v2. It exposes the Employ corporate site as JSON: blog posts, marketing and legal pages, media, the resource, case-study, new'
  name: Employ Inc Content API
  slug: employ-inc-content-api
- baseURL: https://www.employinc.com/wp-json/tribe/events/v1
  baseurl_source: declared
  description: The Events Calendar REST API (tribe/events/v1) for Employ, Inc. events and webinars, with a self-describing OpenAPI 3.0.0 contract the host publishes at its own /doc endpoint. Covers events, venues, o
  name: Employ Inc Events Calendar REST API
  slug: employ-inc-events-calendar-rest-api
- baseURL: https://www.employinc.com/wp-json/tec/v1
  baseurl_source: declared
  description: 'The newer tec/v1 generation of The Events Calendar REST API on www.employinc.com, published as a self-describing OpenAPI 3.0.4 contract at its own /docs endpoint. Covers events, organizers and venues '
  name: Employ Inc TEC Events REST API
  slug: employ-inc-tec-events-rest-api
- baseURL: https://status.employinc.com/api/v2
  baseurl_source: declared
  description: 'The public Atlassian Statuspage API on status.employinc.com. Eight anonymous endpoints report the rollup availability indicator, every monitored Employ platform component, the dated incident timeline '
  name: Employ Inc Status API
  slug: employ-inc-status-api
artifact_total: 16
asyncapis:
- description: ''
  name: Employ Inc Status Webhooks
  slug: employ-inc-status-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/employ-inc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/employ-inc-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.employinc.com/
- group: company
  title: ''
  type: Blog
  url: https://www.employinc.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.employinc.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.employinc.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.employinc.com/privacy-notice-general/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Employ-Inc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.employinc.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/82904967
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/employ-inc-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/employ-inc-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/employ-inc-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/employ-inc-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/employ-inc-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/employ-inc-conformance.yml
- group: auth
  title: ''
  type: Security
  url: security/employ-inc-security-policy.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/employ-inc-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/employ-inc-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/employ-inc-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/employ-inc-status-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/employ-inc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/employ-inc-rate-limits.yml
created: '2026-09-13'
description: 'Employ, Inc. is the Denver-based parent company of the JazzHR, Lever and Jobvite applicant tracking systems, and of the AI Interview, Screening and Sourcing Companions layered across them. Employ itself runs no developer program: the recruiting APIs its customers integrate against are published under each brand''s own domain and are profiled separately in this network. What Employ publishes on employinc.com is a corporate surface that is nonetheless machine-readable — the WordPress REST API behind its site, two self-describing Events Calendar REST contracts, and an anonymous Atlassian Statuspage API on status.employinc.com — plus the legal, security and responsible-AI documents (Security Exhibit, DPAs, SLAs, NYC Local Law 144 bias audit) that govern every brand underneath it.'
examples:
- key_count: 22
  name: Employ Inc Content Types
  slug: employ-inc-content-types
- key_count: 4
  name: Employ Inc Event Venues
  slug: employ-inc-event-venues
- key_count: 4
  name: Employ Inc Events
  slug: employ-inc-events
- key_count: 2
  name: Employ Inc Status Components
  slug: employ-inc-status-components
- key_count: 2
  name: Employ Inc Status Incidents
  slug: employ-inc-status-incidents
- key_count: 5
  name: Employ Inc Status Summary
  slug: employ-inc-status-summary
- key_count: 9
  name: Employ Inc Taxonomies
  slug: employ-inc-taxonomies
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/employ-inc.png
layout: provider
modified: '2026-09-13'
name: Employ Inc
nav: Providers
network: true
overview: 'Employ Inc publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Content API, Events Calendar REST API, TEC Events REST API, and 1 more. Tagged areas include Human Resources, Recruiting, Talent Acquisition, Applicant Tracking, and ATS.


  The Employ Inc catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Employ Inc''s developer surface includes authentication, engineering blog, support, and 21 more developer resources.'
plans:
- name: Employ Inc Plans Pricing
  plan_count: 0
  slug: employ-inc-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Employ Inc Rate Limits
  slug: employ-inc-rate-limits
security:
- kind: authentication
  name: Employ Inc Authentication
  slug: employ-inc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Employ Inc Domain Security
  slug: employ-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: employ-inc
tags:
- Human Resources
- Recruiting
- Talent Acquisition
- Applicant Tracking
- ATS
- Hiring
- HR Tech
- Content
- Events
- Status
website: https://www.employinc.com/
---
