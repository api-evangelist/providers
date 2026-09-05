---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Platform-agnostic REST API for bi-directional task synchronization between Cynomi and any PSA or ticketing system — push remediation tasks from Cynomi and pull status updates back to keep both systems
  name: Cynomi Public API
  slug: cynomi-public-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://cynomi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cynomi.com/platform/integrations/public-api/
- group: docs
  title: ''
  type: Documentation
  url: https://cynomi.com/platform/integrations/
- group: company
  title: ''
  type: Blog
  url: https://cynomi.com/blog/
- group: start
  title: ''
  type: Login
  url: https://cynomi.com/product-login/
- group: commercial
  title: ''
  type: Pricing
  url: https://cynomi.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cynomi.com/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cynomi.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://cynomi.com/academy/
- group: company
  title: ''
  type: Partners
  url: https://partners.cynomi.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/cynomi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cynomi-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cynomi-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cynomi-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cynomi-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cynomi-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cynomi.com/security/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cynomi-llms.txt
created: '2026-07-17'
description: Cynomi is an AI-powered, automated virtual CISO (vCISO) platform built for MSPs, MSSPs, and cybersecurity consultancies to deliver scalable security and compliance services to their clients. The platform automates risk assessments, generates tailored security policies and prioritized remediation plans, and maps controls to leading frameworks including NIST CSF, ISO 27001, SOC 2, PCI DSS, GDPR, NIS2, and HIPAA, tracking security posture over time. Cynomi exposes a platform-agnostic Public API for bi-directional task synchronization with any PSA or ticketing system (ConnectWise, ServiceNow, Autotask, HaloPSA, Kaseya, NinjaOne, Atera), pushing remediation tasks out and pulling status updates back, alongside pre-built integrations with vulnerability scanners (Tenable, Qualys, Rapid7, CrowdStrike, SentinelOne) and cloud security tools. Authentication is handled through an Auth0 tenant using OAuth 2.0 / OpenID Connect. Cynomi is backed by Canaan Partners and Insight Partners.
image: https://cynomi.com/wp-content/uploads/2026/04/Share-image.png
layout: provider
modified: '2026-07-18'
name: Cynomi
nav: Providers
network: true
overview: 'Cynomi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security, Compliance, and vCISO.


  Cynomi''s developer surface includes documentation, engineering blog, pricing, support, authentication, and 13 more developer resources.'
random_paper: 4
scopes:
- name: Cynomi Scopes
  scope_count: 11
  slug: cynomi-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 26.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cynomi/refs/heads/main/screenshots/cynomi-2026-07-25T211052.png
security:
- kind: authentication
  name: Cynomi Authentication
  slug: cynomi-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Cynomi Domain Security
  slug: cynomi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cynomi Trust Center
  slug: cynomi-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR, HIPAA
slug: cynomi
tags:
- Company
- Cybersecurity
- Security
- Compliance
- vCISO
- Risk Management
- GRC
- MSP
- MSSP
- Vulnerability Management
website: https://cynomi.com/
---
