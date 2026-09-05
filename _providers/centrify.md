---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://www.centrify.com/'', ''status'': 301, ''note'': ''declared website redirects to https://delinea.com/centrify — a different registrable domain (centrify.com -> delinea.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST API for the Centrify Identity Platform / Cloud Suite (PAS). Programmatic access to authentication profiles, users, directories, roles, sets, resources, secrets, privileged access requests, connec
  name: Centrify Identity Services API
  slug: centrify-identity-services-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.centrify.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.delinea.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.delinea.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.delinea.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.delinea.com/docs/getting-access-to-the-api
- group: docs
  title: ''
  type: DocumentationLibrary
  url: https://docs.centrify.com/
- group: operate
  title: ''
  type: Support
  url: https://support.delinea.com/s/
- group: company
  title: ''
  type: Blog
  url: https://delinea.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://delinea.com/centrify
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DelineaXPM
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/centrify-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/centrify-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/centrify-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/centrify-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/centrify-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/centrify-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/centrify-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/centrify-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/centrify-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.delinea.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/centrify-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/centrify-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.delinea.com/
created: '2026-07-17'
description: Centrify is an identity and privileged access management (PAM) platform now delivered as part of Delinea (the company formed from the Centrify + Thycotic merger). The Centrify Identity Platform / Cloud Suite / Privileged Access Service secures access to applications, servers, network infrastructure, and privileged accounts with adaptive multi-factor authentication, single sign-on, least-privilege enforcement, session auditing, and analytics. The Centrify REST API exposes the full platform programmatically — authentication profiles, users and directories, roles and sets, resources and secrets, privileged access requests, connectors, webhooks, and audit/reporting — authenticated via OAuth2, bearer tokens, or MFA-aware session cookies. centrify.com now redirects to delinea.com and the developer documentation is served at developer.delinea.com.
image: https://delinea.com/hubfs/Delinea/images/logos/delinea-logo.svg
layout: provider
modified: '2026-07-18'
name: Centrify
nav: Providers
network: true
overview: 'Centrify publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Privileged Access Management, Access Management, and Authentication.


  Centrify''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 16 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 27.2
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/centrify/refs/heads/main/screenshots/centrify-2026-07-25T204934.png
security:
- kind: authentication
  name: Centrify Authentication
  slug: centrify-authentication
  summary_line: oauth2/http/apiKey · 4 schemes
- kind: domain-security
  name: Centrify Domain Security
  slug: centrify-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Centrify Vulnerability Disclosure
  slug: centrify-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Centrify Trust Center
  slug: centrify-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, ISO/IEC 27001:2022, PCI DSS v4.0.1, GDPR, EU-US Data Privacy Framework, CCPA, FedRAMP, DESC Cloud Service Provider
slug: centrify
tags:
- Company
- Identity
- Privileged Access Management
- Access Management
- Authentication
- Single Sign-On
- Multi-Factor Authentication
- Security
- Zero Trust
- IAM
website: https://www.centrify.com/
---
