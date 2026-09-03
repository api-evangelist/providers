---
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
- description: 'VIA''s OpenID Connect / OAuth 2.0 identity layer, operated on a VIA-run Keycloak server. It is the only machine-readable contract VIA publishes: each product realm serves an anonymous OIDC discovery do'
  name: VIA Zero Trust Fabric — OpenID Connect Identity
  slug: via-zero-trust-fabric-openid-connect-identity
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/via-science-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.solvewithvia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.ztf.solvewithvia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.ztf.solvewithvia.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.ztf.solvewithvia.com/via-ztf-components/
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.ztf.solvewithvia.com/integration/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/viascience
- group: operate
  title: ''
  type: Support
  url: https://github.com/viascience/ztf-tutorial/issues
- group: company
  title: ''
  type: Blog
  url: https://www.solvewithvia.com/latest/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.solvewithvia.com/feed/
- group: start
  title: ''
  type: SignUp
  url: https://www.solvewithvia.com/via-ztf/get-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.solvewithvia.com/qt-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solvewithvia.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/marketplace/pp/prodview-4occdwn5sc7w4
- group: start
  title: ''
  type: Sandbox
  url: sandbox/via-science-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/via-science-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/via-science-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/via-science-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/via-science-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/via-science-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/via-science-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/via-science-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/via-science-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/via-science-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/via-science-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/via-science-llms.txt
created: '2026-09-02'
description: Via Science, Inc. — trading as VIA — is a Somerville, Massachusetts security company founded in 2016 that builds decentralized, quantum-resistant data and identity protection for governments, defense agencies and large enterprises. Its products are VIA ZTF (Zero Trust Fabric), a passwordless authentication fabric built on verifiable credentials, a decentralized identity registry and a mobile holder wallet; VIA QT (Quantum Transfer), an end-to-end quantum-resistant large-file transfer service sold direct and as a metered AWS Marketplace AMI; SLAM AI, which lets organizations use generative AI models without exposing confidential data and keeps an immutable record of every prompt, response and data transformation; VIA Wallet; and VIA Secure Chain. VIA raised a $28M Series B led by Bosch Ventures with BMW i Ventures, MassMutual Ventures and Sentinel Global. Its developer surface is an OpenID Connect identity layer — a Keycloak server at auth.solvewithvia.com that serves anonymous
  OIDC, RFC 8414 and UMA 2.0 discovery documents per product realm — plus ZTF documentation and four runnable reference integrations on GitHub. VIA publishes no OpenAPI or other resource contract for any product.
image: https://www.solvewithvia.com/wp-content/uploads/2025/02/solve-with-VIA-home-page-preview-image.png
layout: provider
modified: '2026-09-02'
name: Via Science
nav: Providers
network: true
overview: 'Via Science publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Identity, Authentication, and Zero Trust.


  Via Science''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 19 more developer resources.'
plans:
- name: Via Science Plans Pricing
  plan_count: 3
  slug: via-science-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Via Science Rate Limits
  slug: via-science-rate-limits
scopes:
- name: Via Science Scopes
  scope_count: 0
  slug: via-science-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: authentication
  name: Via Science Authentication
  slug: via-science-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Via Science Domain Security
  slug: via-science-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: via-science
tags:
- Company
- Security
- Identity
- Authentication
- Zero Trust
- Decentralized Identity
- Verifiable Credentials
- Post-Quantum Cryptography
- Encryption
- File Transfer
- Defense
- Artificial Intelligence
- Blockchain
- OpenID Connect
website: https://www.solvewithvia.com/
---
