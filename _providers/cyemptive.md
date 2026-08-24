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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cyemptive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cyemptive.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/cyemptive_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cyemptive-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/cyemptive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cyemptive-rate-limits.yml
coverage:
  checked: '2026-08-11'
  detail: Cyemptive ships ZeroStrike as a delivered end-user security product sold direct and through partners — api.cyemptive.com and developer.cyemptive.com do not exist in DNS, no Cyemptive GitHub organization exists, no first-party package is published on any registry, and the only two reachable technical hosts are logins (an ASP.NET partner portal at partner.cyemptive.com and a Hudu IT-documentation tenant at docs.cyemptive.com), neither of which is an API reference.
  evidence:
  - status: 404
    url: https://partner.cyemptive.com/openapi.json
  - status: 404
    url: https://partner.cyemptive.com/.well-known/agent-card.json
  - status: 404
    url: https://docs.cyemptive.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/cyemptive
  - status: 404
    url: https://pypi.org/pypi/cyemptive/json
  - status: 0
    url: https://www.cyemptive.com/
  reason: no-developer-program
  state: none
created: '2026-08-11'
description: Cyemptive Technologies is a cybersecurity vendor founded in 2014 by Rob Pike, headquartered in Washington State with additional offices in North Carolina, the United Kingdom, France and India. It sells preemptive, detection-independent security to enterprise and government buyers under the Cyemptive ZeroStrike brand — built on its patented CyberSlice technology — alongside ZeroStrike Cloud Command, ZeroStrike Blueprint professional services, Compliancy Cloud and a cyber-insurance offering. Cyemptive is sold as a delivered end-user security product through a direct and partner motion; it publishes no public developer program, API reference or machine-readable contract of any kind.
layout: provider
modified: '2026-08-11'
name: Cyemptive
nav: Providers
network: true
overview: Cyemptive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security, Ransomware, and Endpoint Security.
plans:
- name: Cyemptive Plans Pricing
  plan_count: 0
  slug: cyemptive-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Cyemptive Rate Limits
  slug: cyemptive-rate-limits
score:
  band: minimal
  composite: 3.8
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Cyemptive Domain Security
  slug: cyemptive-domain-security
  summary_line: DMARC
slug: cyemptive
tags:
- Company
- Cybersecurity
- Security
- Ransomware
- Endpoint Security
- Cloud Security
- Threat Prevention
- Zero Trust
- Compliance
- Government
website: https://www.cyemptive.com/
---
