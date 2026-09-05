---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 71
  human_in_the_loop: 0
  name: Port Agentic Access
  operation_count: 110
  slug: port-agentic-access
  summary_line: 110 operations · 71 acting
api_count: 1
apis:
- baseURL: https://api.getport.io
  baseurl_source: declared
  description: The Action Runs API from Port — 6 operation(s) for action runs.
  name: Port Action Runs API
  slug: port-action-runs-api
- baseURL: https://api.getport.io
  baseurl_source: declared
  description: The Actions API from Port — 5 operation(s) for actions.
  name: Port Actions API
  slug: port-actions-api
- baseURL: https://api.getport.io
  baseurl_source: declared
  description: The Apps API from Port — 3 operation(s) for apps.
  name: Port Apps API
  slug: port-apps-api
- baseURL: https://api.getport.io
  baseurl_source: declared
  description: The Audit API from Port — 1 operation(s) for audit.
  name: Port Audit API
  slug: port-audit-api
- baseURL: https://api.getport.io
  baseurl_source: declared
  description: The Authentication / Authorization API from Port — 2 operation(s) for authentication / authorization.
  name: Port Authentication / Authorization API
  slug: port-authentication-authorization-api
- baseURL: https://api.getport.io
  baseurl_source: declared
  description: The Blueprints API from Port — 7 operation(s) for blueprints.
  name: Port Blueprints API
  slug: port-blueprints-api
- baseURL: https://api.getport.io
  baseurl_source: declared
  description: The Entities API from Port — 11 operation(s) for entities.
  name: Port Entities API
  slug: port-entities-api
- baseURL: https://api.getport.io
  baseurl_source: declared
  description: The Integrations API from Port — 5 operation(s) for integrations.
  name: Port Integrations API
  slug: port-integrations-api
- baseURL: https://api.getport.io
  baseurl_source: declared
  description: The Migrations API from Port — 3 operation(s) for migrations.
  name: Port Migrations API
  slug: port-migrations-api
- baseURL: https://api.getport.io
  baseurl_source: declared
  description: The Organization API from Port — 3 operation(s) for organization.
  name: Port Organization API
  slug: port-organization-api
- baseURL: https://api.getport.io
  baseurl_source: declared
  description: The Pages API from Port — 6 operation(s) for pages.
  name: Port Pages API
  slug: port-pages-api
- baseURL: https://api.getport.io
  baseurl_source: declared
  description: The Scorecards API from Port — 3 operation(s) for scorecards.
  name: Port Scorecards API
  slug: port-scorecards-api
- baseURL: https://api.getport.io
  baseurl_source: declared
  description: The Teams API from Port — 2 operation(s) for teams.
  name: Port Teams API
  slug: port-teams-api
- baseURL: https://api.getport.io
  baseurl_source: declared
  description: The Users API from Port — 3 operation(s) for users.
  name: Port Users API
  slug: port-users-api
- baseURL: https://api.getport.io
  baseurl_source: declared
  description: The Webhook API from Port — 3 operation(s) for webhook.
  name: Port Webhook API
  slug: port-webhook-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Port Action Runs API
  slug: open-port-action-runs-api
- collection_type: open
  name: Port Action Runs Actions API
  slug: open-port-actions-api
- collection_type: open
  name: Port Action Runs Apps API
  slug: open-port-apps-api
- collection_type: open
  name: Port Action Runs Audit API
  slug: open-port-audit-api
- collection_type: open
  name: Port Action Runs Authentication / Authorization API
  slug: open-port-authentication-authorization-api
- collection_type: open
  name: Port Action Runs Blueprints API
  slug: open-port-blueprints-api
- collection_type: open
  name: Port Action Runs Entities API
  slug: open-port-entities-api
- collection_type: open
  name: Port Action Runs Integrations API
  slug: open-port-integrations-api
- collection_type: open
  name: Port Action Runs Migrations API
  slug: open-port-migrations-api
- collection_type: open
  name: Port Action Runs Organization API
  slug: open-port-organization-api
- collection_type: open
  name: Port Action Runs Pages API
  slug: open-port-pages-api
- collection_type: open
  name: Port Action Runs Scorecards API
  slug: open-port-scorecards-api
- collection_type: open
  name: Port Action Runs Teams API
  slug: open-port-teams-api
- collection_type: open
  name: Port Action Runs Users API
  slug: open-port-users-api
- collection_type: open
  name: Port Action Runs Webhook API
  slug: open-port-webhook-api
- collection_type: open
  name: Port API
  slug: open-port
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/port-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/port-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/port-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/port-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/port-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.port.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.port.io/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.port.io/getting-started/overview/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.port.io/
- group: docs
  title: ''
  type: Guides
  url: https://docs.port.io/guides/
- group: company
  title: ''
  type: Blog
  url: https://www.port.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://roadmap.port.io/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.port.io
- group: auth
  title: ''
  type: Security
  url: https://www.port.io/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.port.io/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.port.io/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/port-labs
- group: company
  title: ''
  type: About
  url: https://www.port.io/company
- group: company
  title: ''
  type: Careers
  url: https://www.port.io/careers
- group: start
  title: ''
  type: Login
  url: https://app.getport.io
- group: start
  title: ''
  type: Signup
  url: https://app.getport.io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getport
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.port.io/llms.txt
created: '2025-01-08'
description: This API is documented in the OpenAPI format and provides programmatic access to Port and its components.
finops:
- name: Port Finops
  service_category: API
  slug: port-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/port.png
layout: provider
modified: '2026-05-19'
name: Port
nav: Providers
network: true
overview: 'Port publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Action Runs API, Actions API, Apps API, and 12 more. Tagged areas include Automations, Developer Portals, Internal Developer Portal, Platform Engineering, and Scorecards.


  Port''s developer surface includes authentication, developer portal, pricing, getting-started guide, documentation, engineering blog, changelog, and 16 more developer resources.'
plans:
- name: Port Plans Pricing
  plan_count: 3
  slug: port-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Port Rate Limits
  slug: port-rate-limits
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 33.3
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/port/refs/heads/main/screenshots/port-2026-06-20T191926.png
security:
- kind: authentication
  name: Port Authentication
  slug: port-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Port Domain Security
  slug: port-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Port Vulnerability Disclosure
  slug: port-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Port Trust Center
  slug: port-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: port
tags:
- Automations
- Developer Portals
- Internal Developer Portal
- Platform Engineering
- Scorecards
- Self-Service
- Software Catalog
website: https://www.port.io/
---
