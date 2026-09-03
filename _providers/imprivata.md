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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.imprivata.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.imprivata.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.imprivata.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.imprivata.com/onesign/content/topics/onesign/proveid/proveid_webapi.html
- group: company
  title: ''
  type: Blog
  url: https://www.imprivata.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/imprivata-idg
- group: operate
  title: ''
  type: Support
  url: https://www.imprivata.com/support
- group: auth
  title: ''
  type: Compliance
  url: https://www.imprivata.com/company/trust-and-security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.imprivata.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.imprivata.com/legal/imprivata-master-cloud-services-agreement
- group: auth
  title: ''
  type: Authentication
  url: authentication/imprivata-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/imprivata-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imprivata-domain-security.yml
created: '2026-07-17'
description: Imprivata is a digital identity and access management company built for healthcare and other mission-critical industries. Its platform delivers passwordless and multifactor authentication, single sign-on (Enterprise Access Management, formerly OneSign), privileged access management, mobile and shared device access (Mobile Access Management, formerly GroundControl), and drug enforcement e-prescribing (DEA-EPCS) workflows so that clinicians, partners, and increasingly AI agents can securely access systems and data without slowing down crucial work. Imprivata exposes integration surfaces for software and hardware vendors through the OneSign ProveID Web API and ProveID SDK and a Privileged Access Management REST API, governed through its Access Management Partner (developer) program. These APIs are deployed on customer/instance infrastructure rather than a single public cloud host, so Imprivata publishes integration documentation and a developer partner program rather than a hosted
  public API portal.
image: https://www.imprivata.com/themes/imprivata/images/logo_v2.svg
layout: provider
modified: '2026-07-19'
name: Imprivata
nav: Providers
network: true
overview: 'Imprivata is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Access Management, Authentication, and Single Sign-On.


  Imprivata''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 8 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 23.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imprivata/refs/heads/main/screenshots/imprivata-2026-07-25T222159.png
security:
- kind: authentication
  name: Imprivata Authentication
  slug: imprivata-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Imprivata Domain Security
  slug: imprivata-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Imprivata Trust Center
  slug: imprivata-trust-center
  summary_line: SOC 2, ISO 27001:2022, ISO 27701:2019, HIPAA, HITECH, NIST, Cyber Essentials, Cyber Essentials Plus, DEA-EPCS (21 CFR part 1311)
slug: imprivata
tags:
- Company
- Identity
- Access Management
- Authentication
- Single Sign-On
- Privileged Access Management
- Healthcare
- Security
- Passwordless
website: https://www.imprivata.com/
---
