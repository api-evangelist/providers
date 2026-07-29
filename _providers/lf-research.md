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
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Programmatic access to LF Research publications, open source trend data, and industry analysis resources.
  name: LF Research API
  slug: lf-research-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lf-research-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lf-research-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.linuxfoundation.org/research
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/LF-Engineering
- group: other
  title: ''
  type: Publications
  url: https://www.linuxfoundation.org/research
- group: operate
  title: ''
  type: Contact
  url: mailto:research@linuxfoundation.org
- group: company
  title: ''
  type: Blog
  url: https://www.linuxfoundation.org/blog/rss.xml
created: '2026-03-16'
description: LF Research is the Linux Foundation's research arm that publishes reports and studies on open source trends, OSPO practices, technology adoption, and industry analysis. It provides data-driven insights to help organizations understand and participate in open source ecosystems.
finops:
- name: Lf Research Finops
  service_category: API
  slug: lf-research-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lf-research.png
layout: provider
modified: '2026-04-28'
name: LF Research
nav: Providers
network: true
overview: 'LF Research publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Analysis, Linux Foundation, Open Source, and Research.


  LF Research''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Lf Research Plans Pricing
  plan_count: 3
  slug: lf-research-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 5
  name: Lf Research Rate Limits
  slug: lf-research-rate-limits
score:
  band: emerging
  composite: 19.9
  delta: -1.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lf-research/refs/heads/main/screenshots/lf-research-2026-06-20T184453.png
security:
- kind: domain-security
  name: Lf Research Domain Security
  slug: lf-research-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lf Research Vulnerability Disclosure
  slug: lf-research-vulnerability-disclosure
  summary_line: disclosure policy published
slug: lf-research
tags:
- Analysis
- Linux Foundation
- Open Source
- Research
---
