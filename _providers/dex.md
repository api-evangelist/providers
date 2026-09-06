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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: gRPC management API for Dex covering OAuth2 client lifecycle (Create, Get, Update, Delete, List), password management (Create, Update, Delete, List, Verify), identity provider connector management (Cr
  name: Dex gRPC API
  slug: grpc-api
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/dexidp/dex/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/dexidp/dex/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/dexidp/dex/blob/master/.github/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/dexidp/dex/blob/master/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/dexidp/dex/blob/master/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dexidp.io/
- group: docs
  title: ''
  type: Documentation
  url: https://dexidp.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dexidp
- group: other
  title: ''
  type: Repository
  url: https://github.com/dexidp/dex
- group: commercial
  title: ''
  type: License
  url: https://github.com/dexidp/dex/blob/master/LICENSE
created: '2025-01-01'
description: A federated OpenID Connect provider that connects to other identity providers through connectors, enabling authentication for applications without handling passwords directly. Dex acts as a portal to other identity providers through connectors, making it easy to implement SSO across multiple providers. Dex is a single Go binary with pluggable storage and ships with a gRPC management API (api/v2/api.proto) for managing OAuth2 clients, passwords, connectors, and refresh tokens, alongside the standard set of OIDC endpoints.
finops:
- name: Dex Finops
  service_category: API
  slug: dex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dex.png
layout: provider
modified: '2026-04-28'
name: Dex
nav: Providers
network: true
overview: 'Dex publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Authentication, Connectors, Federation, gRPC, and Identity Provider.


  Dex''s developer surface includes documentation and 10 more developer resources.'
plans:
- name: Dex Plans Pricing
  plan_count: 3
  slug: dex-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Dex Rate Limits
  slug: dex-rate-limits
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 17.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dex/refs/heads/main/screenshots/dex-2026-06-20T175953.png
security:
- kind: domain-security
  name: Dex Domain Security
  slug: dex-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dex
tags:
- Authentication
- Connectors
- Federation
- gRPC
- Identity Provider
- LDAP
- OIDC
- OpenID Connect
- SAML
- Single Sign-On
- SSO
website: https://dexidp.io/
---
