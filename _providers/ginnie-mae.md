---
access_model:
  confidence: medium
  label: Free — U.S. government content API, no key, no account, no published plans
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  - plans
  trial: false
  try_now: true
api_count: 2
apis:
- description: Ginnie Mae's security- and loan-level disclosure for its mortgage-backed securities — daily, weekly, monthly and factor files covering single-family MBS, HMBS, Multifamily, REMIC and Platinum, plus th
  name: Ginnie Mae Disclosure Data
  slug: ginnie-mae
- baseURL: https://www.ginniemae.gov/api/v1
  baseurl_source: declared
  description: 'The public, unauthenticated JSON:API 1.0 surface that ginniemae.gov''s Angular single-page application is built on. A Drupal 10 back end exposes 120 resource types at https://www.ginniemae.gov/api/v1/ '
  name: Ginnie Mae Content API
  slug: ginnie-mae-content-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.ginniemae.gov/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ginnie-mae
- group: company
  title: ''
  type: Blog
  url: https://www.ginniemae.gov/newsroom/research-insights/haps-blog
- group: operate
  title: ''
  type: Support
  url: https://www.ginniemae.gov/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.ginniemae.gov/disclosure/create-account
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ginniemae.gov/site-policies/site-policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ginniemae.gov/site-policies/site-policies/disclaimer
- group: auth
  title: ''
  type: Security
  url: https://www.ginniemae.gov/site-policies/ginnie-mae-vulnerability-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ginnie-mae-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ginnie-mae-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ginnie-mae-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ginnie-mae-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ginnie-mae-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/ginnie-mae-packages.yml
created: '2024-12-03'
description: The Government National Mortgage Association (Ginnie Mae) is a government corporation within the U.S. Department of Housing and Urban Development (HUD), established in 1968 following the privatization of Fannie Mae. Its mission is to expand mortgage funding insured or guaranteed by federal agencies. By providing a full-faith-and-credit guarantee on securities backed by these mortgages, Ginnie Mae reduces investor risk and broadens the market for mortgage-backed securities. Ginnie Mae runs no developer program and publishes no API documentation, but ginniemae.gov is a decoupled Drupal 10 site whose public, unauthenticated JSON:API 1.0 surface at https://www.ginniemae.gov/api/v1/ is reachable by anyone — the FAQ, glossary, press releases, All Participant Memoranda, bulletins and document library the website is built from. MBS disclosure data is distributed separately as bulk files behind a free account, and issuer systems sit behind MyGinnieMae SSO.
finops:
- name: Ginnie Mae Finops
  service_category: API
  slug: ginnie-mae-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ginnie-mae.png
layout: provider
modified: '2026-09-12'
name: Ginnie Mae
nav: Providers
network: true
overview: 'Ginnie Mae publishes 1 API on the [APIs.io](https://apis.io/) network: Content API. Tagged areas include Federal-Government, Housing, Mortgages, Mortgage-Backed-Securities, and Open-Data.


  Ginnie Mae''s developer surface includes engineering blog, support, signup flow, and 12 more developer resources.'
plans:
- name: Ginnie Mae Plans Pricing
  plan_count: 0
  slug: ginnie-mae-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Ginnie Mae Rate Limits
  slug: ginnie-mae-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/ginnie-mae/refs/heads/main/screenshots/ginnie-mae-2026-06-20T181827.png
security:
- kind: authentication
  name: Ginnie Mae Authentication
  slug: ginnie-mae-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ginnie Mae Domain Security
  slug: ginnie-mae-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ginnie Mae Vulnerability Disclosure
  slug: ginnie-mae-vulnerability-disclosure
  summary_line: Hackerone
slug: ginnie-mae
tags:
- Federal-Government
- Housing
- Mortgages
- Mortgage-Backed-Securities
- Open-Data
- Content
- JSON-API
website: https://www.ginniemae.gov/
---
