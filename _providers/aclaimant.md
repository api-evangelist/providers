---
api_count: 1
apis:
- baseURL: https://api.aclaimant.com/api
  baseurl_source: declared
  description: The Aclaimant Platform API (x-id "platform-api") is the end-user integration surface for a company or collective on the Aclaimant platform. Swagger 2.0, base path /api, JSON in and JSON / transit+json
  name: Aclaimant Platform API
  slug: aclaimant-platform-api
- description: Callback API for TPAs, carriers, brokers and other Aclaimant partners working claims on behalf of an Aclaimant customer. Base URL https://api.aclaimant.com/partner, bearer-token authorization issued b
  name: Aclaimant Partner / Third-party API
  slug: aclaimant-partner-third-party-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/aclaimant-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.aclaimant.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.aclaimant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.aclaimant.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.aclaimant.com/api/index.html
- group: operate
  title: ''
  type: Support
  url: https://support.aclaimant.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.aclaimant.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.aclaimant.com/blog/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aclaimant.com/plans-and-pricing
- group: start
  title: ''
  type: Login
  url: https://dashboard.aclaimant.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aclaimant.com/service-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aclaimant.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aclaimant
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aclaimant.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.aclaimant.com/
- group: auth
  title: ''
  type: Security
  url: https://www.aclaimant.com/responsible-disclosure
- group: auth
  title: ''
  type: Compliance
  url: conformance/aclaimant-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aclaimant-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aclaimant-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/aclaimant-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aclaimant-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aclaimant-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aclaimant-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aclaimant-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.aclaimant.com/hc/en-us/sections/4406733144859-Product-Updates-Releases
- group: design
  title: ''
  type: DataModel
  url: data-model/aclaimant-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/aclaimant-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aclaimant-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aclaimant-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aclaimant-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aclaimant-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/aclaimant-platform-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aclaimant-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aclaimant-vulnerability-disclosure.yml
created: '2026-09-06'
description: Aclaimant is a Chicago-based risk management information system (RMIS) used by policyholders, insurance brokers, carriers and third-party administrators to run incident reporting and first notice of loss (FNOL), claims management and analytics, safety and loss control, OSHA logs, policy management, and assets and exposures from one workflow platform. Its machine-readable surface is the Aclaimant Platform API — a Swagger 2.0 contract published at api.aclaimant.com/api with a live Swagger UI console — which lets integrators create and upsert answer bundles, incidents, claims, claim reports, events, files, companies, policies, policy programs, exposures and exposure summations, including bulk jobs with a status endpoint. A separate Partner / Third-party API at api.aclaimant.com/partner lets carriers, TPAs and brokers acknowledge claim receipt and post loss-run claim financial updates back into Aclaimant.
image: https://www.aclaimant.com/hubfs/Aclaimant_February2020/Images/favicon.ico
layout: provider
modified: '2026-09-06'
name: Aclaimant
nav: Providers
network: true
overview: 'Aclaimant publishes 1 API on the [APIs.io](https://apis.io/) network: Platform API. Tagged areas include Risk Management, Insurance, Claims Management, Incident Management, and Safety.


  Aclaimant''s developer surface includes documentation, API reference, support, engineering blog, pricing, authentication, changelog, and 28 more developer resources.'
plans:
- name: Aclaimant Plans Pricing
  plan_count: 3
  slug: aclaimant-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Aclaimant Rate Limits
  slug: aclaimant-rate-limits
security:
- kind: authentication
  name: Aclaimant Authentication
  slug: aclaimant-authentication
  summary_line: apiKey/http-bearer · 2 schemes
- kind: domain-security
  name: Aclaimant Domain Security
  slug: aclaimant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aclaimant Vulnerability Disclosure
  slug: aclaimant-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Aclaimant Trust Center
  slug: aclaimant-trust-center
  summary_line: SOC 2, GDPR, Penetration test report
slug: aclaimant
tags:
- Risk Management
- Insurance
- Claims Management
- Incident Management
- Safety
- RMIS
- Workers Compensation
- OSHA
- Enterprise Risk Management
- Insurtech
website: https://www.aclaimant.com/
---
