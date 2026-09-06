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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: PlexTrac's JWT-authenticated REST API (v1 and v2) for managing clients, reports, findings, assets, and content-library writeups, along with tenant/RBAC administration and outbound webhooks. The base U
  name: PlexTrac API
  slug: plextrac-api
artifact_total: 6
asyncapis:
- description: ''
  name: Plextrac Llc Webhooks
  slug: plextrac-llc-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/plextrac-llc-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://app.drata.com/trust/9cbbf37d-0c38-11ee-865f-029d78a187d9
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/plextrac-llc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://plextrac.com/vulnerability-disclosure/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plextrac-llc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://plextrac.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.plextrac.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.plextrac.com/
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.plextrac.com/
- group: company
  title: ''
  type: Blog
  url: https://plextrac.com/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://plextrac.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plextrac.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plextrac.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plextrac-llc-llms.txt
created: '2026-07-17'
description: PlexTrac is a penetration test reporting and proactive exposure management platform that unifies offensive security data from pentests, vulnerability scanners, and bug bounty programs into a single system of record. It automates pentest report authoring (including AI-assisted findings), centralizes and prioritizes vulnerability data by business impact, and drives remediation through workflows integrated with tools such as Jira and ServiceNow. PlexTrac exposes a JWT-authenticated REST API (v1 and v2) for managing clients, reports, findings, assets, and content-library writeups, plus RBAC/tenant administration and outbound webhooks, letting security teams and MSSPs integrate reporting and remediation into their own pipelines.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plextrac-llc.png
layout: provider
modified: '2026-07-20'
name: PlexTrac, LLC
nav: Providers
network: true
overview: 'PlexTrac, LLC publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Penetration Testing, Vulnerability Management, and Security Reporting.


  The PlexTrac, LLC catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PlexTrac, LLC''s developer surface includes documentation, API reference, support, engineering blog, pricing, and 9 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 40.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plextrac-llc/refs/heads/main/screenshots/plextrac-llc-2026-09-02T151518.png
security:
- kind: authentication
  name: Plextrac Llc Authentication
  slug: plextrac-llc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Plextrac Llc Domain Security
  slug: plextrac-llc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Plextrac Llc Vulnerability Disclosure
  slug: plextrac-llc-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Plextrac Llc Trust Center
  slug: plextrac-llc-trust-center
  summary_line: SOC 2, ISO 27001
slug: plextrac-llc
tags:
- Company
- Cybersecurity
- Penetration Testing
- Vulnerability Management
- Security Reporting
- Exposure Management
- Offensive Security
- MSSP
- Remediation
website: https://plextrac.com/
---
