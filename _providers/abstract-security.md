---
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.abstract.security/
- group: company
  title: ''
  type: Blog
  url: https://www.abstract.security/abstract-canvas
- group: operate
  title: ''
  type: Support
  url: https://www.abstract.security/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.abstract.security/get-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abstract.security/policies/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abstract.security/policies/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AbstractSecurity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abstractsecurity
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abstract-security-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abstract-security-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/abstract-security-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/abstract-security-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/abstract-security-lifecycle.yml
coverage:
  checked: '2026-09-06'
  detail: Abstract Security serves no developer portal or API reference at all — /docs, /developers, /api, /api-docs and /openapi.json every one 404 on www.abstract.security, the 348-URL sitemap contains no developer page, and the site navigation has no Developers section — while the API host named in the company's own TLS certificate (api.abstract.security, seen in Certificate Transparency) publishes no public DNS record, so the only route to the platform is the demo request form at /get-a-demo that routes to sales.
  evidence:
  - status: 404
    url: https://www.abstract.security/developers
  - status: 404
    url: https://www.abstract.security/openapi.json
  - status: 200
    url: https://www.abstract.security/get-a-demo
  - status: 200
    url: https://www.abstract.security/llms.txt
  reason: sales-gate
  state: gated
created: '2026-09-06'
description: Abstract Security is a security data platform and AI-powered composable SIEM founded in 2023 by Colby DeRodeff and Aaron Shelmire. Its streaming-first architecture ingests security telemetry from cloud, SaaS, endpoint and on-prem sources, then filters, normalizes, enriches and routes it in real time to SIEMs, data lakes and low-cost archives. The platform separates high-value detection data from long-term compliance retention so teams can cut SIEM ingest cost without losing visibility. Named components include Collection (the security data control plane), Detection Fabric, AI-Enabled SecOps, Retention, and the Abstract Intel Gallery (AIG) for operationalizing threat intelligence. The company publishes a catalog of roughly 230 source, destination and action integrations covering AWS, Microsoft Sentinel, CrowdStrike, Splunk, Google SecOps, Palo Alto Cortex XSIAM, SentinelOne, Elastic and Netskope, and its threat research group (ASTRO) publishes open YARA rulesets on GitHub. Abstract
  Security has raised roughly $28.5M from Munich Re Ventures, Crosslink Capital, Rally Ventures and Liquid 2 Ventures. As of this profiling pass the company operates no public developer portal, publishes no API reference or machine-readable contract, and routes platform access through a sales/demo motion.
image: https://cdn.prod.website-files.com/69847dcdf15f603ba59220d8/6a28780d0e4dcdad57e2b620_abstract-logo.png
layout: provider
modified: '2026-09-06'
name: Abstract Security
nav: Providers
network: true
overview: 'Abstract Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Cybersecurity, SIEM, Security Data Pipeline, and Threat Detection.


  Abstract Security''s developer surface includes engineering blog, support, signup flow, and 10 more developer resources.'
plans:
- name: Abstract Security Plans Pricing
  plan_count: 0
  slug: abstract-security-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Abstract Security Rate Limits
  slug: abstract-security-rate-limits
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 14.3
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Abstract Security Domain Security
  slug: abstract-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: abstract-security
tags:
- Security
- Cybersecurity
- SIEM
- Security Data Pipeline
- Threat Detection
- Security Operations
- Log Management
- Data Streaming
- Observability
- Threat Intelligence
- Cloud Security
- AI Security
- Detection Engineering
- Data Routing
- Compliance Retention
website: https://www.abstract.security/
---
