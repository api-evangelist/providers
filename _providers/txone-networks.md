---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/txone-networks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.txone.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.txone.com/
- group: operate
  title: ''
  type: Support
  url: https://www.txone.com/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.txone.com/
- group: company
  title: ''
  type: Blog
  url: https://www.txone.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TXOne-Networks
- group: start
  title: ''
  type: Login
  url: https://my.txone.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.txone.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.txone.com/legal/terms-of-use/
- group: auth
  title: ''
  type: Security
  url: https://www.txone.com/legal/disclosure-policy/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://www.txone.com/legal/security-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/txone-networks-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/txone-networks-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/txone-networks-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/txone-networks-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/txone-networks-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/txone-networks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/txone-networks-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/txone-networks-packages.yml
coverage:
  checked: '2026-09-01'
  detail: TXOne ships real REST APIs - its own SageOne 2.1 release note says "OpenAPI Support ... Refer to SageOne OpenAPI (1.0) for full details" - but every console that serves one (SageOne/Sennin, StellarOne, EdgeOne) is a customer-deployed on-premises appliance, so the spec, the base URL and the API reference exist only inside a licensed tenant; www.txone.com serves no /api, /developers or /pricing page and the 216-article public Help Center contains zero API articles.
  evidence:
  - status: 200
    url: https://help.txone.com/docs/txone-sageone-21-is-now-available
  - status: 404
    url: https://www.txone.com/developers
  - status: 404
    url: https://www.txone.com/api
  - status: 404
    url: https://www.txone.com/openapi.json
  - status: 404
    url: https://www.txone.com/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-09-01'
description: TXOne Networks is an operations-first OT (operational technology) cybersecurity company headquartered in Taipei, Taiwan, founded in 2019 as a joint venture between Trend Micro and Moxa and now operating independently. It protects industrial control systems, production floors and critical infrastructure with a prevention-first architecture designed to deploy without production downtime. The TXOne Complete portfolio unifies Edge (EdgeIPS Pro, EdgeFire, EdgeOne network security), Stellar (Stellar Protect, Stellar Discover, StellarOne endpoint protection), Element (Portable Inspector, Safe Port, ElementOne security inspection) and Sennin (SenninRecon, SenninOne, SageOne discovery, assessment and strategic governance), powered by CPSDR behavioral detection, TXODI deep packet inspection across 180+ industrial protocols, and VSAR operational-context vulnerability scoring. Products are delivered as customer-deployed appliances and on-premises management consoles rather than a public
  multi-tenant cloud service, so the REST/OpenAPI surfaces those consoles expose (SageOne OpenAPI 1.0 for asset management, health checks and vulnerability data; the StellarOne open API; EdgeOne API management) are reachable only inside a customer's own deployment. TXOne publishes no public developer portal, API reference or pricing page.
image: https://www.txone.com/icon.png
layout: provider
modified: '2026-09-01'
name: TXOne Networks
nav: Providers
network: true
overview: 'TXOne Networks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Operational Technology, and Industrial Control Systems.


  TXOne Networks'' developer surface includes documentation, support, engineering blog, changelog, and 16 more developer resources.'
plans:
- name: Txone Networks Plans Pricing
  plan_count: 0
  slug: txone-networks-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Txone Networks Rate Limits
  slug: txone-networks-rate-limits
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 23.1
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/txone-networks/refs/heads/main/screenshots/txone-networks-2026-09-02T164645.png
security:
- kind: domain-security
  name: Txone Networks Domain Security
  slug: txone-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Txone Networks Vulnerability Disclosure
  slug: txone-networks-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: txone-networks
tags:
- Company
- Security
- Cybersecurity
- Operational Technology
- Industrial Control Systems
- Critical Infrastructure
- Endpoint Protection
- Network Security
- Vulnerability Management
- Manufacturing
website: https://www.txone.com/
---
