---
access_model:
  confidence: high
  label: Free public data — self-service API key
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - https://dataportal.dol.gov/registration
  trial: false
  try_now: false
api_count: 2
apis:
- description: ILAB's datasets are served through the U.S. Department of Labor Open Data Portal API (https://apiprod.dol.gov/v4) under the agency segment 'ilab'. The catalogue route /v4/datasets answers anonymously;
  name: DOL Open Data Portal API — ILAB datasets
  slug: dol-ilab-data-api
- description: 'The Sweat & Toil programme''s data now ships under the LaborShield, ImportWatch, SourcingStrong and SupplyChainTrace names. Seven tables are published through the DOL Open Data Portal API: Child_Labor_'
  name: ILAB Sweat & Toil / LaborShield dataset family
  slug: ilab-sweat-and-toil-data
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-international-labor-affairs-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/bureau-of-international-labor-affairs
- group: company
  title: ''
  type: Website
  url: https://www.dol.gov/agencies/ilab
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dol.gov/general/privacynotice
- group: start
  title: ''
  type: Data Portal
  url: https://catalog.data.gov/dataset?organization=dol-gov&q=ilab
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dataportal.dol.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://dataportal.dol.gov/user-guide
- group: docs
  title: ''
  type: APIReference
  url: https://dataportal.dol.gov/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://dataportal.dol.gov/getting-started
- group: operate
  title: ''
  type: Support
  url: https://dataportal.dol.gov/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://dataportal.dol.gov/registration
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dataportal.dol.gov/registration
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USDepartmentofLabor
- group: auth
  title: ''
  type: Authentication
  url: authentication/bureau-of-international-labor-affairs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bureau-of-international-labor-affairs-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bureau-of-international-labor-affairs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bureau-of-international-labor-affairs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bureau-of-international-labor-affairs-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bureau-of-international-labor-affairs-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/bureau-of-international-labor-affairs-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bureau-of-international-labor-affairs-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bureau-of-international-labor-affairs-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bureau-of-international-labor-affairs-plans-pricing.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bureau-of-international-labor-affairs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/bureau-of-international-labor-affairs-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bureau-of-international-labor-affairs-mcp.yml
created: '2024-11-25'
description: 'ILAB is the U.S. Department of Labor bureau that strengthens global labor standards, enforces labor commitments in trade agreements, promotes equity, and combats child labor, forced labor and human trafficking. ILAB operates no API of its own: its seven public datasets — the Child Labor Report and the ImportWatch and LaborShield families, all derived from ILAB''s three flagship reports — are served through the department-wide DOL Open Data Portal API at apiprod.dol.gov/v4, under the agency segment ''ilab'', with a free X-API-KEY credential.'
finops:
- name: Bureau Of International Labor Affairs Finops
  service_category: API
  slug: bureau-of-international-labor-affairs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-international-labor-affairs.png
layout: provider
modified: '2026-09-05'
name: Bureau of International Labor Affairs
nav: Providers
network: true
overview: 'Bureau of International Labor Affairs publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, International, Labor, Standards, and Child Labor.


  Bureau of International Labor Affairs'' developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, and 20 more developer resources.'
plans:
- name: Bureau Of International Labor Affairs Plans Pricing
  plan_count: 1
  slug: bureau-of-international-labor-affairs-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Bureau Of International Labor Affairs Rate Limits
  slug: bureau-of-international-labor-affairs-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-international-labor-affairs/refs/heads/main/screenshots/bureau-of-international-labor-affairs-2026-06-20T173810.png
security:
- kind: authentication
  name: Bureau Of International Labor Affairs Authentication
  slug: bureau-of-international-labor-affairs-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bureau Of International Labor Affairs Domain Security
  slug: bureau-of-international-labor-affairs-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bureau Of International Labor Affairs Vulnerability Disclosure
  slug: bureau-of-international-labor-affairs-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
slug: bureau-of-international-labor-affairs
tags:
- Federal-Government
- International
- Labor
- Standards
- Child Labor
- Forced Labor
- Human Trafficking
website: https://www.dol.gov/agencies/ilab
---
