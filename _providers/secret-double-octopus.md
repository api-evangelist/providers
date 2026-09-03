---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: REST API of the Octopus Authentication Server Management Console. SDO's own FAQ states "we provide comprehensive REST APIs that allow complete system control, including scripting, bulk updates, and in
  name: Octopus Management Console REST API
  slug: octopus-management-console-rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/secret-double-octopus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doubleoctopus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.doubleoctopus.com/support/solutions
- group: operate
  title: ''
  type: Support
  url: https://support.doubleoctopus.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://doubleoctopus.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.doubleoctopus.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doubleoctopus.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doubleoctopus.com/website-privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/secret-double-octopus-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/secret-double-octopus-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://support.doubleoctopus.com/support/solutions/articles/33000295981-octopus-authentication-end-of-life-end-of-support-plan
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/secret-double-octopus-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/secret-double-octopus-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/secret-double-octopus-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/secret-double-octopus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/secret-double-octopus-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/secret-double-octopus-packages.yml
created: '2026-08-26'
description: 'Secret Double Octopus (SDO) is an enterprise workforce authentication vendor whose Octopus Authentication Platform uses patented ZeroPassword technology to eliminate all user-managed passwords and deliver phishing-resistant, passwordless MFA across legacy, on-premises, cloud, and air-gapped systems. The platform covers SaaS and web apps, VPN, RDP, VDI/Citrix, Linux SSH, shared workstations, servers and domain-joined desktops, and integrates with existing identity infrastructure — Active Directory, Microsoft Entra ID and Okta — without redesign. Any authenticator is supported: mobile push, biometrics, FIDO2 security keys, X.509 smart cards, Windows Hello and OTP tokens. SDO ships an Octopus Management Console REST API for system control, scripting, bulk updates and IDM integration (SailPoint and similar), but that API is served from the customer''s own deployed Management Console and its reference is not published on a public developer portal.'
image: https://doubleoctopus.com/wp-content/uploads/2022/10/cropped-favicon_large-1-192x192.png
layout: provider
modified: '2026-08-26'
name: Secret Double Octopus
nav: Providers
network: true
overview: 'Secret Double Octopus publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Authentication, Identity and Access Management, Passwordless, and Multi-Factor Authentication.


  Secret Double Octopus'' developer surface includes documentation, support, engineering blog, changelog, and 13 more developer resources.'
plans:
- name: Secret Double Octopus Plans Pricing
  plan_count: 0
  slug: secret-double-octopus-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Secret Double Octopus Rate Limits
  slug: secret-double-octopus-rate-limits
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 26.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/secret-double-octopus/refs/heads/main/screenshots/secret-double-octopus-2026-09-02T154704.png
security:
- kind: authentication
  name: Secret Double Octopus Authentication
  slug: secret-double-octopus-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Secret Double Octopus Domain Security
  slug: secret-double-octopus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: secret-double-octopus
tags:
- Company
- Authentication
- Identity and Access Management
- Passwordless
- Multi-Factor Authentication
- Security
- FIDO2
- Zero Trust
- Enterprise
- Workforce Identity
website: https://doubleoctopus.com/
---
