---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/savana-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/savana-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/savana-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/savana-llms.txt
- group: company
  title: ''
  type: Website
  url: https://savanainc.com/
- group: other
  title: ''
  type: Platform
  url: https://savanainc.com/platform/
- group: operate
  title: ''
  type: Support
  url: https://savanainc.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://savanainc.happyfox.com/
- group: company
  title: ''
  type: Blog
  url: https://savanainc.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://savanainc.com/feed/
- group: company
  title: ''
  type: News
  url: https://savanainc.com/company/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/savanainc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://savanainc.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://savanainc.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://savanainc.com/company/
- group: company
  title: ''
  type: Careers
  url: https://savanainc.com/company/careers/
- group: operate
  title: ''
  type: ContactUs
  url: https://savanainc.com/contact/
- group: start
  title: ''
  type: Demo
  url: https://savanainc.com/request-a-demo/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/savana-inc./
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCR2YGJCa2VJGIO9QpnwRAAw
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/savana_stock/
coverage:
  checked: '2026-08-05'
  detail: Savana markets "Banking APIs" as the core of its platform but publishes no developer surface at all — the 13-page Yoast sitemap ends at "Request a Demo", the api./docs./developer. subdomains do not resolve, and the only documentation host that exists (savanainc.happyfox.com) is a customer login wall.
  evidence:
  - status: 200
    url: https://savanainc.com/request-a-demo/
  - status: 404
    url: https://savanainc.com/developers
  - status: 404
    url: https://savanainc.com/openapi.json
  - status: 200
    url: https://savanainc.happyfox.com/
  - status: 301
    url: http://status.savanainc.com/
  reason: sales-gate
  state: gated
created: '2026-08-05'
description: Savana is a Malvern, Pennsylvania based financial software company, founded in 2009, that sells a cloud-native, API-first Digital Delivery Platform to banks, credit unions and fintechs. The platform sits above the core banking system rather than replacing it, unifying banker-facing experiences (CRM, BPM, servicing, assisted account opening) and customer-facing experiences (online and mobile banking, digital account opening) across any core, and shipping 140+ pre-built configurable servicing workflows. Savana markets a set of "Banking APIs" that orchestrate whole servicing processes — not just data exchange — between assisted and self-service channels, but as of this profile the company publishes no public developer portal, API reference, or machine-readable specification; documentation and the status page are reachable only by authenticated customers. Savana raised a $45M Series A led by Georgian with participation from Fiserv in 2022.
image: https://savanainc.com/wp-content/uploads/2025/07/headerlogo.png
layout: provider
modified: '2026-08-05'
name: Savana
nav: Providers
network: true
overview: 'Savana is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Financial Services, Core Banking, and Digital Banking.


  Savana''s developer surface includes support, engineering blog, product news, YouTube channel, and 17 more developer resources.'
random_paper: 54
score:
  band: emerging
  composite: 18.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 18.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 30.4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: domain-security
  name: Savana Domain Security
  slug: savana-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: savana
tags:
- Company
- Banking
- Financial Services
- Core Banking
- Digital Banking
- Credit Unions
- Fintech
- Account Opening
- Workflow Automation
- CRM
- BPM
- Bank Servicing
website: https://savanainc.com/
---
