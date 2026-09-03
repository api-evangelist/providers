---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
  scored_at: '2026-09-03'
api_count: 6
apis:
- description: 'Single POST endpoint at lastpass.com/enterpriseapi.php that accepts a JSON payload selecting one of many command names (batchadd, batchchange, deluser, disableuser, getuserdata, getsfdata, getreport, '
  name: LastPass Enterprise API
  slug: enterprise-api
- description: Subset of the Enterprise API focused on the user-lifecycle commands - batchadd, batchchange, deluser, disableuser, and getuserdata - used by directory connectors (Active Directory, Entra ID, Okta, Goo
  name: LastPass Provisioning API
  slug: provisioning
- description: SCIM 2.0 endpoint that exposes Users and Groups for directory-based provisioning by Okta, Entra ID, OneLogin, JumpCloud, and Google Cloud Identity. Replaces ad-hoc provisioning calls with a standards-
  name: LastPass SCIM API
  slug: scim
- description: LastPass acts as either a SAML identity provider (IdP) for the cloud apps catalogued in the LastPass App Library or as a service provider (SP) when paired with an external IdP. Endpoints implement SAM
  name: LastPass SAML / SSO Endpoint
  slug: saml
- description: 'Server-side SDK for embedding LastPass MFA (push, biometric, TOTP) into custom cloud or on-prem applications. Wraps the underlying authentication endpoints so developers can add adaptive multi-factor '
  name: LastPass MFA SDK
  slug: mfa-sdk
- description: Reporting-oriented Enterprise API commands (getreport, getuserdata, getsfdata, getevents) that export login activity, shared-folder membership, and admin events for use in SIEMs and audit pipelines.
  name: LastPass Reporting Commands
  slug: reporting
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lastpass-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lastpass
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lastpass
- group: company
  title: ''
  type: Website
  url: https://www.lastpass.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.lastpass.com/help/use-the-lastpass-enterprise-api
- group: commercial
  title: ''
  type: Plans
  url: plans/lastpass-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lastpass-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lastpass-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.lastpass.com/
created: '2026-05-08'
description: LastPass is a password and identity-management platform offering personal and enterprise vaults, single sign-on, multi-factor authentication, and directory provisioning. The LastPass Enterprise API and Provisioning API let admins programmatically manage users, groups, shared folders, policies, and events. SCIM and SAML endpoints integrate with identity providers; an MFA SDK supports adaptive authentication for custom apps.
finops:
- name: Lastpass Finops
  service_category: Identity and Access Management
  slug: lastpass-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lastpass.png
layout: provider
modified: '2026-05-08'
name: LastPass
nav: Providers
network: true
overview: 'LastPass publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Password Manager, Vault, Identity, and Enterprise.


  LastPass'' developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Lastpass Plans Pricing
  plan_count: 7
  slug: lastpass-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Lastpass Rate Limits
  slug: lastpass-rate-limits
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lastpass/refs/heads/main/screenshots/lastpass-2026-06-20T184323.png
security:
- kind: domain-security
  name: Lastpass Domain Security
  slug: lastpass-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lastpass
tags:
- Security
- Password Manager
- Vault
- Identity
- Enterprise
- SSO
- MFA
website: https://www.lastpass.com/
---
