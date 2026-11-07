---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
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
artifact_total: 11
asyncapis:
- description: ''
  name: Cerby Webhooks
  slug: cerby-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/cerby/plans/cerby-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cerby-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cerby.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cerby.com/blog/rss.xml
- group: auth
  href: https://artifacts.apis.io/cerby/security/cerby-domain-security.yml
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
  href: https://artifacts.apis.io/cerby/changelog/cerby-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cerby-changelog.yml
- group: build
  href: https://artifacts.apis.io/cerby/cli/cerby-cli.yml
  title: ''
  type: CLI
  url: cli/cerby-cli.yml
- group: agent
  href: https://artifacts.apis.io/cerby/llms/cerby-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cerby-llms.txt
- group: design
  href: https://artifacts.apis.io/cerby/lifecycle/cerby-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cerby-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cerby/conformance/cerby-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cerby-conformance.yml
- group: build
  href: https://artifacts.apis.io/cerby/packages/cerby-packages.yml
  title: ''
  type: Packages
  url: packages/cerby-packages.yml
- group: auth
  href: https://artifacts.apis.io/cerby/security/cerby-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cerby-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cerby/security/cerby-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cerby-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cerby/authentication/cerby-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cerby-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cerby/scopes/cerby-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cerby-scopes.yml
- group: design
  href: https://artifacts.apis.io/cerby/conventions/cerby-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cerby-conventions.yml
- group: design
  href: https://artifacts.apis.io/cerby/conventions/cerby-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cerby-conventions.yml
- group: design
  href: https://artifacts.apis.io/cerby/errors/cerby-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cerby-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cerby/asyncapi/cerby-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cerby-webhooks.yml
- group: design
  href: https://artifacts.apis.io/cerby/data-model/cerby-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cerby-data-model.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cerbyinc
created: '2026-08-09'
description: Cerby is an identity, access, and password management platform for nonfederated and disconnected applications — the enterprise software that does not support SAML, SCIM, or an integration API of its own. Cerby extends existing IAM, IGA, and PAM systems to those applications through browser and robotic automation, adding provisioning and deprovisioning, credential rotation, MFA enrollment, and access governance where no standards-based integration exists. Cerby publishes a public RESTful API (JSON:API-style envelope, X-API-Key authentication, scoped API keys) over eight resources — accounts, secrets, collections, users, teams, integrations, jobs, and vaults — plus a signed webhook notification service, a cross-platform CLI, and SCIM 2.0 endpoints for provisioning from Okta, Entra ID, and OneLogin.
finops:
- has_sources: true
  method: derived
  name: Cerby Finops
  primary_unit: ''
  service_category: ''
  slug: cerby-finops
  template: true
image: https://www.cerby.com/hubfs/Logos/Cerby%20Favicon%20-%20Alternate.png
layout: provider
modified: '2026-10-06'
name: Cerby
nav: Providers
network: true
overview: 'Cerby is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Identity, Identity and Access Management, Security, Password Management, and Provisioning.


  The Cerby catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cerby''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, signup flow, pricing, and 23 more developer resources.'
plans:
- name: Cerby Plans Pricing
  plan_count: 1
  slug: cerby-plans-pricing
random_paper: 5
scopes:
- name: Cerby Scopes
  scope_count: 17
  slug: cerby-scopes
  summary_line: 17 scopes
score:
  band: developing
  composite: 52.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 60.7
    discoverability: 78.6
    operational_transparency: 52.6
  previous_composite: 52.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cerby/cerby-2026-08-17T083439.png
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
- Identity and Access Management
- Security
- Password Management
- Provisioning
- SCIM
- Identity Governance
- Nonfederated Applications
- Automation
- Webhook
- Identity Federation
website: https://www.cerby.com/
---
