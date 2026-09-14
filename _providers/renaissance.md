---
api_count: 3
apis:
- baseURL: https://proficiency.renaissance.com
  baseurl_source: declared
  description: Renaissance-operated prediction service returning student proficiency on math skills and skill groups, the next recommended pathway activity for a student, a student's current reading level, and class
  name: Student Proficiency Service
  slug: student-proficiency-service
- baseURL: https://events.proficiency.renaissance.com
  baseurl_source: declared
  description: Event ingestion proxy that accepts Freckle practice events (assignment, activity and answer payloads) into the Renaissance student pathway pipeline. OpenAPI 3.1.0 published at the service root; the si
  name: Student Pathway Event Proxy
  slug: student-pathway-event-proxy
- baseURL: https://api.proxile.renaissance.com
  baseurl_source: declared
  description: Lexile measure lookup by ISBN-13, returning the stored Lexile book record. OpenAPI 3.0.1 published at the API host root; the API gateway validates a JWT issued by Renaissance auth (client credentials)
  name: Lexile API
  slug: lexile-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/renaissance-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.renaissance.com/
- group: operate
  title: ''
  type: Support
  url: https://support.renaissance.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.renaissance.com/resources/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.renaissance.com/resources/blog/feed/
- group: start
  title: ''
  type: Login
  url: https://login.renaissance.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.renaissance.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.renaissance.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RenaissancePlace
- group: operate
  title: ''
  type: StatusPage
  url: https://status.renaissance.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.renaissance.com/
- group: auth
  title: ''
  type: Compliance
  url: conformance/renaissance-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/renaissance-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/renaissance-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/renaissance-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/renaissance-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/renaissance-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.renaissance.com/.well-known/openid-configuration
- group: design
  title: ''
  type: Conventions
  url: conventions/renaissance-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/renaissance-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/renaissance-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/renaissance-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/renaissance-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/renaissance-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/renaissance-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.renaissance.com/product-updates/
- group: commercial
  title: ''
  type: Plans
  url: plans/renaissance-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/renaissance-rate-limits.yml
created: '2026-09-13'
description: 'Renaissance Learning, Inc. is a pre-K–12 education technology company whose assessment, practice and analytics products — Star Assessments, Accelerated Reader, Freckle, myON, Lalilo, Flocabulary, Nearpod, FastBridge, DnA, eduCLIMBER, eSchoolData, SchoolCity and the Renaissance Growth Platform — are used by schools in more than 100 countries. Its machine-readable surface is not a published developer program: district integration is delivered through 1EdTech OneRoster 1.1 rostering (certified across twelve products), LTI 1.3 / LTI Advantage launches (Nearpod, SchoolCity), an Ed-Fi Assessment Outcomes API certification for DnA, and a Renaissance-operated OAuth 2.0 / OpenID Connect authorization server at auth.renaissance.com. Three first-party OpenAPI contracts are served publicly but token-gated on Renaissance-controlled hosts: the Student Proficiency Service, the Student Pathway Event Proxy and the Lexile API.'
image: https://www.renaissance.com/wp-content/uploads/2023/04/renaissance-logo-facebook.png
layout: provider
modified: '2026-09-13'
name: Renaissance
nav: Providers
network: true
overview: 'Renaissance publishes 3 APIs on the [APIs.io](https://apis.io/) network: Student Proficiency Service, Student Pathway Event Proxy, and Lexile API. Tagged areas include Education, EdTech, K-12, Assessment, and Learning Analytics.


  Renaissance''s developer surface includes support, engineering blog, authentication, changelog, and 25 more developer resources.'
plans:
- name: Renaissance Plans Pricing
  plan_count: 0
  slug: renaissance-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Renaissance Rate Limits
  slug: renaissance-rate-limits
scopes:
- name: Renaissance Scopes
  scope_count: 0
  slug: renaissance-scopes
  summary_line: OAuth 2.0 · no documented scopes
security:
- kind: authentication
  name: Renaissance Authentication
  slug: renaissance-authentication
  summary_line: http/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Renaissance Domain Security
  slug: renaissance-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Renaissance Trust Center
  slug: renaissance-trust-center
  summary_line: SOC 2
slug: renaissance
tags:
- Education
- EdTech
- K-12
- Assessment
- Learning Analytics
- Student Data
- OneRoster
- LTI
- Ed-Fi
- Rostering
- Interoperability
- Machine Learning
website: https://www.renaissance.com/
---
