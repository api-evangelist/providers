---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Open Worldwide Application Security Project providing resources, tools, projects, and standards for application and web security.
  name: OWASP
  slug: owasp
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/owasp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/owasp-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://owasp.org/feed.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/owasp
- group: company
  title: ''
  type: Website
  url: https://owasp.org/
- group: docs
  title: ''
  type: Documentation
  url: https://owasp.org/projects/
- group: operate
  title: ''
  type: Community
  url: https://owasp.org/slack/invite
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OWASP
- group: operate
  title: ''
  type: Support
  url: https://owasp.org/contact/
- group: other
  title: ''
  type: Foundation
  url: https://owasp.org/www-policy/
created: '2026-03-16'
description: The Open Worldwide Application Security Project (OWASP) is a nonprofit foundation that works to improve the security of software through community-led open source projects, hundreds of chapters worldwide, and educational resources. OWASP does not provide a centralized public API, but maintains many open source projects, standards (such as the OWASP Top 10 and ASVS), and tools (such as ZAP) that include APIs.
finops:
- name: Owasp Finops
  service_category: API
  slug: owasp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/owasp.png
layout: provider
modified: '2026-04-28'
name: OWASP
nav: Providers
network: true
overview: 'OWASP publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Application Security, Open Source, Security, Web Security, and Standards.


  OWASP''s developer surface includes engineering blog, documentation, support, and 7 more developer resources.'
plans:
- name: Owasp Plans Pricing
  plan_count: 3
  slug: owasp-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Owasp Rate Limits
  slug: owasp-rate-limits
score:
  band: emerging
  composite: 23.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 23.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/owasp/refs/heads/main/screenshots/owasp-2026-06-20T191244.png
security:
- kind: domain-security
  name: Owasp Domain Security
  slug: owasp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Owasp Vulnerability Disclosure
  slug: owasp-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: owasp
tags:
- Application Security
- Open Source
- Security
- Web Security
- Standards
website: https://owasp.org/
---
