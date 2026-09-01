---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 11.4
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: REST threat-intelligence API from the QAX Threat Intelligence Center. Provides IP reputation, domain and URL reputation, file/hash verdicts, compromise (失陷) detection intelligence and vulnerability in
  name: QAX Threat Intelligence API
  slug: qax-threat-intelligence-api
- description: Hosted Model Context Protocol server published by the QAX Threat Intelligence Center, announced on the QAX newsroom 2025-05-13. Exposes sixteen threat-intelligence query tools (vulnerability lookup, I
  name: QAX Threat Intelligence MCP Service
  slug: qax-threat-intelligence-mcp-service
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.qianxin.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qi-anxin-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://ti.qianxin.com/help
- group: docs
  title: ''
  type: APIReference
  url: https://ti.qianxin.com/help/?path=ip-illustration30
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ti.qianxin.com/
- group: start
  title: ''
  type: SignUp
  url: https://user.ti.qianxin.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.qianxin.com/support/index
- group: company
  title: ''
  type: Blog
  url: https://en.qianxin.com/news/list
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qi-anxin-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qi-anxin-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/qi-anxin-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qi-anxin-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qi-anxin-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/qi-anxin-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qi-anxin-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qi-anxin-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qi-anxin-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/qi-anxin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qi-anxin-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/qi-anxin-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qi-anxin-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qi-anxin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/qi-anxin-vulnerability-disclosure.yml
created: '2026-08-26'
description: 'Qi An Xin Technology Group (QAX, 奇安信) is a Beijing-headquartered cybersecurity vendor founded in 2014 and listed on the Shanghai Stock Exchange STAR Market (688561), with more than 10,000 employees across 65 branches. It builds enterprise- and national-scale security products spanning security operations and response (SIEM, NDR, vulnerability management), threat intelligence (TIP, TIOS, cyberspace mapping), network and perimeter security (NGFW, WAF, SD-WAN, secure web gateway), endpoint and identity security (EDR, zero-trust network access, privileged access management) and digital forensics. Its public developer surface is the QAX Threat Intelligence Center (ti.qianxin.com): an Api-Key authenticated REST reputation and intelligence API on webapi.ti.qianxin.com, and a hosted Model Context Protocol server at mcp.ti.qianxin.com that exposes sixteen threat-intelligence query tools to AI clients. QAX also operates the Butian (补天) vulnerability response platform and was the official
  cybersecurity services sponsor of the Beijing 2022 Olympic and Paralympic Winter Games.'
image: https://en.qianxin.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: QAX Threat Intelligence MCP Service
  slug: qax-threat-intelligence-mcp-service
modified: '2026-08-26'
name: Qi Anxin
nav: Providers
network: true
overview: 'Qi Anxin publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Threat Intelligence, and Endpoint Security.


  Qi Anxin''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, sandbox, and 16 more developer resources.'
plans:
- name: Qi Anxin Plans Pricing
  plan_count: 0
  slug: qi-anxin-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Qi Anxin Rate Limits
  slug: qi-anxin-rate-limits
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 18.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Qi Anxin Authentication
  slug: qi-anxin-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Qi Anxin Domain Security
  slug: qi-anxin-domain-security
  summary_line: TLSv1.2
- kind: vulnerability-disclosure
  name: Qi Anxin Vulnerability Disclosure
  slug: qi-anxin-vulnerability-disclosure
  summary_line: Hackerone
slug: qi-anxin
tags:
- Company
- Security
- Cybersecurity
- Threat Intelligence
- Endpoint Security
- Network Security
- Vulnerability Management
- MCP
- China
website: https://www.qianxin.com/
---
