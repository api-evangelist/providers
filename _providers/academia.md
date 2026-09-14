---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/academia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.academia.edu/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/academia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.academia.edu/
- group: operate
  title: ''
  type: Support
  url: https://support.academia.edu/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/academia-edu
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.academia.edu/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.academia.edu/privacy
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/academia-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/academia-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/academia-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Academia.edu is an end-user research-sharing product with no developer program of any kind - its own 2,624-line robots.txt enumerates the whole site with no /developers, /docs or API-reference section and Disallows the internal /v0/* JSON endpoints its web client calls to every named crawler, and the GitHub org's 81 public repositories are all internal Rails tooling and forks with no client SDK or specification.
  evidence:
  - status: 404
    url: https://www.academia.edu/llms.txt
  - status: 404
    url: https://www.academia.edu/.well-known/api-catalog
  - status: 404
    url: https://www.academia.edu/.well-known/agent-card.json
  - status: 200
    url: https://www.academia.edu/robots.txt
  - status: 200
    url: https://www.academia.edu/.well-known/security.txt
  - status: 403
    url: https://www.academia.edu/
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Academia (Academia.edu, Academia Inc.) is a San Francisco based platform for sharing and discovering academic research, founded in 2008 by Richard Price. Registered researchers upload papers, build public profiles, follow research interests and track readership analytics across a corpus of tens of millions of documents, and the company also runs the Academia journals program and sells Academia Premium subscriptions for advanced search, mentions, reader analytics and bulk PDF downloads. Academia publishes no public developer program, API reference or machine-readable specification; the /v0 JSON endpoints its own web client calls are explicitly disallowed to crawlers in robots.txt. It does publish an RFC 9116 security.txt with a named security contact and a disclosure posture, and a long per-crawler robots.txt that names AI and agent user-agents individually.
image: https://www.academia.edu/favicon.ico
layout: provider
modified: '2026-08-06'
name: Academia
nav: Providers
network: true
overview: 'Academia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Academic Research, research-papers, Scholarly Publishing, and Higher Education.


  Academia''s developer surface includes support and 10 more developer resources.'
random_paper: 7
screenshot: https://raw.githubusercontent.com/api-evangelist/academia/refs/heads/main/screenshots/academia-2026-08-07T160744.png
security:
- kind: domain-security
  name: Academia Domain Security
  slug: academia-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Academia Vulnerability Disclosure
  slug: academia-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: academia
tags:
- Company
- Academic Research
- research-papers
- Scholarly Publishing
- Higher Education
- Open Access
- academic-social-network
- Preprints
- research-discovery
website: https://www.academia.edu/
---
