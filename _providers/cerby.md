---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: The public Cerby REST API. Programmatic access to accounts, secrets, collections, users, teams, integrations, jobs, and vaults in a Cerby workspace. Requests are authenticated with a scoped API key se
  name: Cerby API
  slug: cerby-api
- description: Cerby's webhook notification service delivers real-time signed HTTPS events for account, credential, MFA, and automation lifecycle changes. Deliveries carry a fixed JSON envelope (envelope_version, ev
  name: Cerby Webhooks
  slug: cerby-webhooks
- description: Cerby exposes SCIM 2.0 endpoints so an identity provider can automatically provision and deprovision users and groups into a Cerby workspace. Documented for Okta, Microsoft Entra ID, and OneLogin, aut
  name: Cerby SCIM 2.0
  slug: cerby-scim
artifact_total: 9
asyncapis:
- description: ''
  name: Cerby Webhooks
  slug: cerby-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cerby-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cerby.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cerby.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.cerby.com/developer-tools/readme
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cerby.com/#api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.cerby.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.cerby.com/
- group: company
  title: ''
  type: Blog
  url: https://www.cerby.com/resources/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.cerby.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cerby.com/contact-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cerby.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cerby-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/cerby-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cerby-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cerby-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cerby-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/cerby-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cerby-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cerby-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cerby-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cerby-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cerby-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cerby-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cerby-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cerby-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cerby-data-model.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cerbyinc
created: '2026-08-09'
description: Cerby is an identity, access, and password management platform for nonfederated and disconnected applications — the enterprise software that does not support SAML, SCIM, or an integration API of its own. Cerby extends existing IAM, IGA, and PAM systems to those applications through browser and robotic automation, adding provisioning and deprovisioning, credential rotation, MFA enrollment, and access governance where no standards-based integration exists. Cerby publishes a public RESTful API (JSON:API-style envelope, X-API-Key authentication, scoped API keys) over eight resources — accounts, secrets, collections, users, teams, integrations, jobs, and vaults — plus a signed webhook notification service, a cross-platform CLI, and SCIM 2.0 endpoints for provisioning from Okta, Entra ID, and OneLogin.
image: https://www.cerby.com/hubfs/Logos/Cerby%20Favicon%20-%20Alternate.png
layout: provider
modified: '2026-08-09'
name: Cerby
nav: Providers
network: true
overview: 'Cerby publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Identity, Access Management, Security, Password Management, and Provisioning.


  The Cerby catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cerby''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 20 more developer resources.'
random_paper: 8
scopes:
- name: Cerby Scopes
  scope_count: 17
  slug: cerby-scopes
  summary_line: 17 scopes
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 60.7
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 44.7
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cerby/refs/heads/main/screenshots/cerby-2026-08-17T083439.png
security:
- kind: authentication
  name: Cerby Authentication
  slug: cerby-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Cerby Domain Security
  slug: cerby-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cerby Vulnerability Disclosure
  slug: cerby-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Cerby Trust Center
  slug: cerby-trust-center
  summary_line: trust center published
slug: cerby
tags:
- Identity
- Access Management
- Security
- Password Management
- Provisioning
- SCIM
- Identity Governance
- Nonfederated Applications
- Automation
- Webhook
website: https://www.cerby.com/
---
