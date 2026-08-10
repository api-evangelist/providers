---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Aryaka Siem Log Streaming
  slug: aryaka-siem-log-streaming
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aryaka-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aryaka.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aryaka.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aryaka.com/space/KNOW/136773659/Getting+Started+with+Aryaka+Unified+SASE+as+a+Service
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.aryaka.com/space/KNOW/1606547/MyAryaka+Help+Home
- group: operate
  title: ''
  type: Support
  url: https://docs.aryaka.com/space/KNOW/1542320/Contact+Aryaka+Customer+Support
- group: start
  title: ''
  type: Login
  url: https://my.aryaka.com/
- group: company
  title: ''
  type: Partners
  url: https://aryaka.my.site.com/partnercommunity/CommunityLogin
- group: company
  title: ''
  type: Blog
  url: https://www.aryaka.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.aryaka.com/blog/feed/
- group: company
  title: ''
  type: Press
  url: https://www.aryaka.com/press/
- group: operate
  title: ''
  type: FAQ
  url: https://www.aryaka.com/faq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aryaka.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aryaka.com/privacy-policy/
- group: commercial
  title: ''
  type: Legal
  url: https://www.aryaka.com/services-terms/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.aryaka.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://www.aryaka.com/company/careers/
- group: auth
  title: ''
  type: Compliance
  url: https://www.aryaka.com/blog/aryaka-has-successfully-completed-soc-2-and-iso-27001-recertification-audits/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aryaka-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aryaka-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aryaka-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aryaka-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aryaka-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aryaka-changelog.yml
- group: company
  title: ''
  type: Investors
  url: https://forgeglobal.com/aryaka_stock/
created: '2026-08-02'
description: Aryaka Networks, Inc. is a San Mateo, California company that delivers Unified SASE as a Service — a converged, fully managed networking and security platform sold as a single service rather than as stitched-together appliances. The platform combines Aryaka's own private global Layer-2/Layer-3 core network and PoP footprint (Global Connectivity), a fully managed SD-WAN that replaces MPLS, WAN and application acceleration (TCP optimization, deduplication, compression, SMB and SSL acceleration), multi-cloud on-ramps to AWS, Azure, Google Cloud, Oracle and Alibaba, and a complete single-pass security stack — next-generation firewall, secure web gateway, CASB, DNS filtering, URL and domain reputation, anti-malware, IPS, tenant restriction and Universal ZTNA / secure remote access. Newer AI-oriented services, AI>Perform and AI>Secure, accelerate and inspect GenAI and LLM traffic. Customers operate the service through MyAryaka, a multi-tenant orchestration, monitoring and business-management
  portal (dashboards, site and policy configuration, alerting, log explorer, SLA and billing reports, order and contract management), with a companion MyAryaka Partner Portal for MSPs and telcos in the "Powered by Aryaka" program. Aryaka publishes a large public documentation portal at docs.aryaka.com and an llms.txt at the root of aryaka.com, and documents SIEM log-streaming integration with published log-attribute schemas, but as of this profiling round it publishes no public developer portal, no machine-readable API contract (OpenAPI/AsyncAPI/GraphQL), no client SDKs and no MCP or A2A agent surface — programmatic access is gated behind the MyAryaka portal.
image: https://www.aryaka.com/wp-content/uploads/2025/03/aryaka-logo-new.jpg
layout: provider
modified: '2026-08-02'
name: Aryaka
nav: Providers
network: true
overview: 'Aryaka is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networking, SASE, SD-WAN, and Network Security.


  The Aryaka catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aryaka''s developer surface includes documentation, getting-started guide, support, engineering blog, FAQ, legal docs, authentication, and 18 more developer resources.'
random_paper: 53
score:
  band: thin
  composite: 39.5
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 51.6
    developer_ergonomics: 37.0
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 39.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aryaka/refs/heads/main/screenshots/aryaka-2026-08-07T161748.png
security:
- kind: authentication
  name: Aryaka Authentication
  slug: aryaka-authentication
  summary_line: saml2/openid-connect/ldap/directory/password · 3 schemes
- kind: domain-security
  name: Aryaka Domain Security
  slug: aryaka-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aryaka
tags:
- Company
- Networking
- SASE
- SD-WAN
- Network Security
- Zero Trust
- ZTNA
- Cloud Connectivity
- Managed Services
- Firewall
- Secure Web Gateway
- WAN Optimization
- Multi-Cloud
- Telecommunications
website: https://www.aryaka.com/
---
