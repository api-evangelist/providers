---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silent-eight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.silenteight.com/
- group: company
  title: ''
  type: Blog
  url: https://www.silenteight.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.silenteight.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.silenteight.com/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.silenteight.com/legal/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.silenteight.com/legal/cookie-policy
- group: auth
  title: ''
  type: Security
  url: https://www.silenteight.com/legal/security-vulnerability-disclosure
- group: other
  title: ''
  type: Awards
  url: https://www.silenteight.com/award-and-accreditations
- group: other
  title: ''
  type: WhitePapers
  url: https://www.silenteight.com/white-papers
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/silent-eight-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/silent-eight-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/silent-eight-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/silent-eight-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/silent-eight-rate-limits.yml
- group: company
  title: ''
  type: Careers
  url: https://silenteight.teamtailor.com/jobs
coverage:
  checked: '2026-08-27'
  detail: 'Silent Eight sells Iris 7 as an enterprise platform deployed inside each bank''s own tenant (managed service, customer cloud, hybrid or on-premise) and publishes no developer surface whatsoever: its own 161-URL sitemap and its own llms.txt contain no API, SDK, endpoint, integration-guide or developer-portal link, and none of docs/developer/api/portal/app/console.silenteight.com resolve in DNS.'
  evidence:
  - status: 200
    url: https://www.silenteight.com/llms.txt
  - status: 200
    url: https://www.silenteight.com/sitemap.xml
  - status: 404
    url: https://www.silenteight.com/openapi.json
  - status: 404
    url: https://www.silenteight.com/.well-known/agent-card.json
  - status: 404
    url: https://www.silenteight.com/.well-known/security.txt
  - status: 404
    url: https://api.github.com/orgs/silenteight
  reason: no-developer-program
  state: none
created: '2026-08-27'
description: 'Silent Eight is an AI-driven financial crime compliance (FCC) technology company founded in Singapore in 2015 and operating globally. Its flagship platform, Iris 7, delivers policy-bound agentic AI that replicates the investigative judgement of experienced compliance analysts, executing explainable, auditable decisions across sanctions screening, anti-money laundering, transaction monitoring, fraud, trade surveillance and complex customer due diligence. Iris 7 is composed of AI Agents by capability (Customer Screening, Payment Screening, Transaction Monitoring, Risk Data Manager, Adverse Media, Case Manager) plus pre-built and custom agents, and is deployed as a governed decision layer on top of existing screening and monitoring systems via managed service, customer cloud, hybrid or on-premise infrastructure. In production with Tier 1 institutions since 2018, including HSBC, Standard Chartered, Emirates NBD and First Abu Dhabi Bank. Silent Eight publishes no public developer
  program: the platform is delivered under enterprise contract and integrated into each institution''s tenant, so no machine-readable API contract is published to the open web.'
image: https://framerusercontent.com/assets/3oVvOPCtRMs62t6nHwQegaxRrk.jpg
layout: provider
modified: '2026-08-27'
name: Silent Eight
nav: Providers
network: true
overview: 'Silent Eight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Crime Compliance, Anti-Money Laundering, Sanctions Screening, and Transaction Monitoring.


  Silent Eight''s developer surface includes engineering blog, support, FAQ, and 13 more developer resources.'
plans:
- name: Silent Eight Plans Pricing
  plan_count: 0
  slug: silent-eight-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Silent Eight Rate Limits
  slug: silent-eight-rate-limits
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 10.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Silent Eight Domain Security
  slug: silent-eight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Silent Eight Vulnerability Disclosure
  slug: silent-eight-vulnerability-disclosure
  summary_line: Hackerone
slug: silent-eight
tags:
- Company
- Financial Crime Compliance
- Anti-Money Laundering
- Sanctions Screening
- Transaction Monitoring
- Know Your Customer
- Adverse Media
- RegTech
- Artificial Intelligence
- Agentic AI
- Financial-Services
- Compliance
website: https://www.silenteight.com/
---
