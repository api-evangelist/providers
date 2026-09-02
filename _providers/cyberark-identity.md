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
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Cyberark Identity Agentic Access
  operation_count: 22
  slug: cyberark-identity-agentic-access
  summary_line: 22 operations · 19 acting
api_count: 1
apis:
- description: REST API for CyberArk Identity covering authentication, authorization, OAuth 2.0 token endpoints, user and role management, directory services, application provisioning, and policy operations. Support
  name: CyberArk Identity API
  slug: identity-api
- description: The Authentication API from CyberArk Identity — 3 operation(s) for authentication.
  name: CyberArk Identity Authentication API
  slug: cyberark-identity-authentication-api
- description: The CDirectoryService API from CyberArk Identity — 3 operation(s) for cdirectoryservice.
  name: CyberArk Identity CDirectoryService API
  slug: cyberark-identity-cdirectoryservice-api
- description: The ExtData API from CyberArk Identity — 1 operation(s) for extdata.
  name: CyberArk Identity ExtData API
  slug: cyberark-identity-extdata-api
- description: The OAuth API from CyberArk Identity — 1 operation(s) for oauth.
  name: CyberArk Identity OAuth API
  slug: cyberark-identity-oauth-api
- description: The Org API from CyberArk Identity — 2 operation(s) for org.
  name: CyberArk Identity Org API
  slug: cyberark-identity-org-api
- description: The SCIM API from CyberArk Identity — 4 operation(s) for scim.
  name: CyberArk Identity SCIM API
  slug: cyberark-identity-scim-api
- description: The UserMgmt API from CyberArk Identity — 5 operation(s) for usermgmt.
  name: CyberArk Identity UserMgmt API
  slug: cyberark-identity-usermgmt-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CyberArk Identity REST Authentication API
  slug: open-cyberark-identity-authentication-api
- collection_type: open
  name: CyberArk Identity REST Authentication CDirectoryService API
  slug: open-cyberark-identity-cdirectoryservice-api
- collection_type: open
  name: CyberArk Identity REST Authentication ExtData API
  slug: open-cyberark-identity-extdata-api
- collection_type: open
  name: CyberArk Identity REST Authentication OAuth API
  slug: open-cyberark-identity-oauth-api
- collection_type: open
  name: CyberArk Identity REST Authentication Org API
  slug: open-cyberark-identity-org-api
- collection_type: open
  name: CyberArk Identity REST Authentication SCIM API
  slug: open-cyberark-identity-scim-api
- collection_type: open
  name: CyberArk Identity REST Authentication UserMgmt API
  slug: open-cyberark-identity-usermgmt-api
- collection_type: open
  name: CyberArk Identity REST API
  slug: open-cyberark-identity
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cyberark-identity-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cyberark-identity-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cyberark-identity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cyberark-identity-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cyberark.com/products/identity-management/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cyberark.com/identity/latest/en/
- group: docs
  title: ''
  type: API Docs
  url: https://api-docs-identity.cyberark.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cyberark.com/contact-us/
- group: start
  title: ''
  type: Signup
  url: https://www.cyberark.com/try-buy/
- group: company
  title: ''
  type: Blog
  url: https://www.cyberark.com/feed/
created: '2026-05-11'
description: CyberArk Identity is a SaaS identity and access management platform offering single sign-on (SSO), multi-factor authentication (MFA), adaptive access, lifecycle management, directory services, and privileged access controls for workforce and customer identities. The platform integrates with thousands of applications and supports enterprise zero-trust strategies. CyberArk Identity exposes REST APIs for authentication, authorization, user and role management, and policy operations, authenticated via OAuth 2.0 (including client_credentials) or session tokens obtained via /Security/StartAuthentication and /Security/AdvanceAuthentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cyberark-identity.png
layout: provider
modified: '2026-05-11'
name: CyberArk Identity
nav: Providers
network: true
overview: 'CyberArk Identity publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, CDirectoryService API, ExtData API, and 4 more. Tagged areas include Identity, Access Management, IAM, Single Sign-On, and SSO.


  CyberArk Identity''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 5 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 51.4
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 26.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cyberark-identity/refs/heads/main/screenshots/cyberark-identity-2026-06-20T175406.png
security:
- kind: authentication
  name: Cyberark Identity Authentication
  slug: cyberark-identity-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Cyberark Identity Domain Security
  slug: cyberark-identity-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Cyberark Identity Trust Center
  slug: cyberark-identity-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: cyberark-identity
tags:
- Identity
- Access Management
- IAM
- Single Sign-On
- SSO
- Multi-Factor Authentication
- Authentication
- Zero Trust
website: https://www.cyberark.com/products/identity-management/
---
