---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: REST API for the Cynet 360 SaaS platform (V3). Provides programmatic access to alerts, hosts and host groups, remediation actions, scans, and account/token operations. Authenticated with a tenant-scop
  name: Cynet 360 API (SaaS V3)
  slug: cynet-360-api-saas-v3
- description: REST API for the on-premises Cynet 360 deployment (V1). Documents authentication (get token), Cynet APIs for hosts, network, and client web API operations. Access-token based authentication using Cyne
  name: Cynet 360 API (On-Prem V1)
  slug: cynet-360-api-on-prem-v1
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://cynet.com
- group: start
  title: ''
  type: Portal
  url: https://portal.cynet.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.api.cynet.com/docs/API-V3/9g00cv3m8b10g-cynet-api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://help.api.cynet.com/docs/API-V3/9g00cv3m8b10g-cynet-api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://help.api.cynet.com/docs/cynet/iah0dsbmetd0e-welcome-to-cynet-api-reference
- group: operate
  title: ''
  type: Support
  url: https://help.cynet.com
- group: company
  title: ''
  type: Blog
  url: https://www.cynet.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cynet.com/packages/
- group: start
  title: ''
  type: SignUp
  url: https://www.cynet.com/request-a-demo/
- group: start
  title: ''
  type: Login
  url: https://portal.cynet.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cynet.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cynet.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://cynet.statuspage.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.cynet.com/whats-new/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.cynet.com/cynet-trust-center/
- group: auth
  title: ''
  type: Compliance
  url: https://www.cynet.com/cynet-trust-center/
- group: auth
  title: ''
  type: Authentication
  url: authentication/cynet-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cynet-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cynet-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cynet-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cynet-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cynet-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cynet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cynet.com/cynet-trust-center/
- group: auth
  title: ''
  type: TrustCenter
  url: security/cynet-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cynet-llms.txt
created: '2026-07-17'
description: Cynet is a unified, AI-powered cybersecurity platform built for MSPs and lean IT/security teams that consolidates endpoint (EDR/EPP), network, email, cloud/SaaS, mobile, and identity protection into a single agent and console. Its CyAI machine-learning engine automatically detects and remediates the majority of threats, CyOps delivers 24x7 managed detection and response, and built-in SOAR playbooks automate response across 80+ pre-built integrations. Cynet exposes a REST API (Cynet 360) for programmatic access to alerts, hosts, remediation, scanning, and account operations, offered as an On-Prem V1 API and a SaaS V3 API, authenticated with a tenant-scoped access token. This profile was surfaced as a portfolio company of Norwest Venture Partners and enriched by the API Evangelist pipeline.
image: https://www.cynet.com/wp-content/uploads/2025/06/cn-favicon-150x150.png
layout: provider
modified: '2026-07-18'
name: Cynet
nav: Providers
network: true
overview: 'Cynet publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security, XDR, and EDR.


  Cynet''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 19 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 37.8
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cynet/refs/heads/main/screenshots/cynet-2026-07-25T211051.png
security:
- kind: authentication
  name: Cynet Authentication
  slug: cynet-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cynet Domain Security
  slug: cynet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cynet Vulnerability Disclosure
  slug: cynet-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Cynet Trust Center
  slug: cynet-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR, HIPAA, PCI DSS, NIST CSF, NIST 800-171, DFARS 7012, CMMC, DORA, NIS2, TX-RAMP Level 2
slug: cynet
tags:
- Company
- Cybersecurity
- Security
- XDR
- EDR
- MDR
- SOAR
- Endpoint Security
- Threat Detection
- Incident Response
- MSP
website: https://cynet.com
---
