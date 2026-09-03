---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'The Silverfort REST API (internally the "Raven" service) exposes user and resource risk read and write, service-account inventory and insights, policy control, and enrollment. Access is controlled by '
  name: Silverfort REST API
  slug: silverfort-rest-api
artifact_total: 3
common:
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/silverfort-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.silverfort.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/silverfort-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/silverfort-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/silverfort-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silverfort-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.silverfort.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.silverfort.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.silverfort.com/product-documentation/docs/en/silverfort-rest-api-reference50-1
- group: operate
  title: ''
  type: Support
  url: https://support.silverfort.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.silverfort.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/silverfort-open-source
- group: commercial
  title: ''
  type: Pricing
  url: https://www.silverfort.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.silverfort.com/request-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.silverfort.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.silverfort.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/silverfort-llms.txt
coverage:
  checked: '2026-08-05'
  detail: The Silverfort REST API Reference at docs.silverfort.com 302s to a Document360 OIDC login at identity.document360.io, and that docs host then answers HTTP 200 with the identical ~10.7KB login shell for every path — /openapi.json, /swagger.json and /llms.txt included — while the live API host raven.silverfort.io serves "Silverfort Raven is UP :-)" and a real 404 for every spec location.
  evidence:
  - status: 302
    url: https://docs.silverfort.com/product-documentation/docs/en/silverfort-rest-api-reference50-1
  - status: 404
    url: https://raven.silverfort.io/openapi.json
  - status: 200
    url: https://raven.silverfort.io/
  reason: customer-only-docs
  state: gated
created: '2026-08-05'
description: Silverfort is an identity security platform that protects human and non-human identities across hybrid environments — on-premises, cloud, and legacy — without agents, proxies, or changes to existing infrastructure. Its Runtime Access Protection (RAP) technology integrates inline with existing IAM infrastructure (Active Directory, Entra ID, Okta, Ping, AWS) and evaluates every authentication attempt in real time before access is granted, extending MFA, identity threat detection and response (ITDR), identity security posture management (ISPM), privileged access security, service-account and non-human-identity governance, and AI agent security to resources that traditional identity tooling cannot reach. Founded in 2016 and headquartered in Dallas, Texas, Silverfort exposes a REST API (the "Raven" service at raven.silverfort.io, with EU and Singapore regional hosts) covering user and resource risk, service-account inventory and insights, policies and enrollment — but the REST API
  reference is published only inside a customer-authenticated knowledge base, so no public machine-readable contract is available.
image: https://www.silverfort.com/wp-content/uploads/2025/02/cropped-Silverfort-Symbol-Pos-RGB.png?w=192
layout: provider
modified: '2026-08-05'
name: Silverfort
nav: Providers
network: true
overview: 'Silverfort publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Security, Authentication, and Multi-Factor Authentication.


  Silverfort''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, and 11 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 24.7
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/silverfort/refs/heads/main/screenshots/silverfort-2026-09-02T155514.png
security:
- kind: domain-security
  name: Silverfort Domain Security
  slug: silverfort-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Silverfort Trust Center
  slug: silverfort-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: silverfort
tags:
- Company
- Identity
- Security
- Authentication
- Multi-Factor Authentication
- Identity Security
- Active Directory
- Zero Trust
- Non-Human Identity
- Cybersecurity
- ITDR
- Service Accounts
website: https://www.silverfort.com/
---
