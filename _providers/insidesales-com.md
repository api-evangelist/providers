---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Access-key protected HTTP API that lets an organization or a third-party application download call recordings produced by Playbooks, and — with the second permission enabled — start and pause recordin
  name: Playbooks Call Recording API
  slug: playbooks-call-recording-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.insidesales.com/
- group: docs
  title: ''
  type: Documentation
  url: https://helpcenter.insidesales.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://helpcenter.insidesales.com/playbooks/getting-started/new-user/getting-started-with-playbooks/
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.insidesales.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.insidesales.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InsideSalesOfficial
- group: commercial
  title: ''
  type: Pricing
  url: https://resources.insidesales.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://resources.insidesales.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://resources.insidesales.com/platform-privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://resources.insidesales.com/commitment-to-gdpr-compliance/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.insidesales.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://helpcenter.insidesales.com/release-notes/
- group: build
  title: ''
  type: Packages
  url: packages/insidesales-com-packages.yml
- group: design
  title: ''
  type: Components
  url: components/insidesales-com-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/insidesales-com-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/insidesales-com-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/insidesales-com-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/insidesales-com-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/insidesales-com-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/insidesales-com-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/insidesales-com-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/insidesales-com-llms.txt
created: '2026-08-23'
description: 'InsideSales — branded XANT from 2019 until Aurea Software (ESW Capital) acquired the company in August 2021 and revived the original name — sells Playbooks, an AI-assisted sales engagement platform that layers cadence, automation, prioritization, scoring and call recording on top of a customer''s existing CRM (Salesforce, Microsoft Dynamics, SAP) rather than replacing it. Its only publicly documented programmable surface is the Playbooks Call Recording API, an access-key protected service for downloading call recordings by Call Detail Record (CDR) ID and for starting/pausing recording from third-party applications; the company also publishes a first-party React UI component library on npm and GitHub. The developer surface is materially decayed: the API reference host and the call-recording host named in the company''s own documentation no longer resolve in DNS, product release notes stop in July 2021, and the Atlassian status page is titled "Deprecated InsideSales".'
image: https://www.insidesales.com/wp-content/uploads/2020/03/InsideSales_Logo_Web.png
layout: provider
modified: '2026-08-23'
name: InsideSales (XANT / InsideSales.com)
nav: Providers
network: true
overview: 'InsideSales (XANT / InsideSales.com) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Sales Engagement, Sales Automation, and CRM.


  InsideSales (XANT / InsideSales.com)''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, changelog, authentication, and 15 more developer resources.'
plans:
- name: Insidesales Com Plans Pricing
  plan_count: 0
  slug: insidesales-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Insidesales Com Rate Limits
  slug: insidesales-com-rate-limits
score:
  band: thin
  composite: 30.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Insidesales Com Authentication
  slug: insidesales-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Insidesales Com Domain Security
  slug: insidesales-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: insidesales-com
tags:
- Company
- Sales
- Sales Engagement
- Sales Automation
- CRM
- Call Recording
- Artificial Intelligence
- Salesforce
- Microsoft Dynamics
- Enterprise Software
website: https://www.insidesales.com/
---
