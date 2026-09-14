---
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Acall Agentic Access
  operation_count: 13
  slug: acall-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.workstyleos.com/v1/
  baseurl_source: declared
  description: REST API (v1) for the Acall / WorkstyleOS workplace platform. Thirteen operations across six resource families — workers (users), facilities, events, gate access logs, spots, and spot reservations — w
  name: Acall Public API
  slug: acall-public-api
artifact_total: 8
asyncapis:
- description: ''
  name: Acall Webhooks
  slug: acall-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/acall-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acall-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acall-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.acall.inc/
- group: docs
  title: ''
  type: Documentation
  url: https://support.workstyleos.com/faq/show/598?site_domain=default
- group: docs
  title: ''
  type: APIReference
  url: https://www.workstyleos.com/publicapi/index.html
- group: operate
  title: ''
  type: Support
  url: https://support.workstyleos.com/?site_domain=default
- group: start
  title: ''
  type: Login
  url: https://portal.workstyleos.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.workstyleos.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workstyleos.com/terms_of_use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acall.inc/privacypolicy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.acall.inc/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.workstyleos.com/info/release/
- group: company
  title: ''
  type: Blog
  url: https://workstylelab.acall.inc/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acall-inc
- group: auth
  title: ''
  type: Compliance
  url: https://www.workstyleos.com/security/
- group: design
  title: ''
  type: Conventions
  url: conventions/acall-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/acall-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acall-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acall-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/acall-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/acall-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/acall-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acall-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/acall-public-api-overlay.yaml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acall-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acall-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/acall-changelog.yml
created: '2026-09-06'
description: 'Acall Inc. (アコール株式会社) is a Japanese workplace-experience software company, founded in 2010 and headquartered in Tokyo with a Kobe office, whose Acall / WorkstyleOS platform runs the physical side of hybrid work for more than 7,000 organizations. The product is a set of check-in surfaces — Acall Reception (iPad visitor reception and entry/exit records), Acall Meeting (meeting-room booking and utilization), Acall Desktop (free-address desk and workspace "spot" reservation / hoteling), Acall Gate (entry-gate integration), AI Meeting, Neat device integration and a multi-tenant building mode — stitched to Microsoft 365 and Google Calendar, Teams/Slack/Chatwork notifications, and SSO/SCIM-style provisioning. Acall publishes a REST "Acall Public API" (v1, bearer token) covering workers, facilities, events, gate access logs, spots and spot reservations, plus an outbound Webhook surface for appointment and internal-meeting events. API access is not self-serve: a token is issued only
  after a request through the contact form, and the API is unavailable on the multi-tenant plan.'
image: https://www.workstyleos.com/images/common/ogp/acall_ogp.png
layout: provider
modified: '2026-09-06'
name: Acall
nav: Providers
network: true
overview: 'Acall publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Workplace Management, Visitor Management, Meeting Room Booking, Desk Booking, and Hybrid Work.


  The Acall catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Acall''s developer surface includes authentication, documentation, API reference, support, pricing, changelog, engineering blog, and 22 more developer resources.'
plans:
- name: Acall Plans Pricing
  plan_count: 0
  slug: acall-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Acall Rate Limits
  slug: acall-rate-limits
security:
- kind: authentication
  name: Acall Authentication
  slug: acall-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Acall Domain Security
  slug: acall-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Acall Trust Center
  slug: acall-trust-center
  summary_line: ISO/IEC 27001 (ISMS)
slug: acall
tags:
- Workplace Management
- Visitor Management
- Meeting Room Booking
- Desk Booking
- Hybrid Work
- Access Control
- Facilities
- Smart Office
- Japan
- SaaS
website: https://www.acall.inc/
---
