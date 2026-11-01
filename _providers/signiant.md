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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-10-31'
api_count: 4
apis:
- description: Unified API to manage storage, endpoints, users, and roles across multiple Signiant products. Authenticates via OAuth 2.0 client_credentials, returning a one-hour JWT bearer token.
  name: Signiant Platform API
  slug: signiant-platform-api
- description: Automates system-to-system job creation, endpoint management, job notifications, and event webhooks for unattended, accelerated file transfers.
  name: Signiant Jet API
  slug: signiant-jet-api
- description: Automates Media Shuttle portal management and person-initiated transfers via the Platform API, Management API, and System-to-Person Automation API, with notification webhooks and a browser SDK for app
  name: Signiant Media Shuttle API
  slug: signiant-media-shuttle-api
- description: Schedules and runs jobs, manages users, and controls Signiant Manager software (Flight Deck) via a REST API.
  name: Signiant Flight Deck Manager REST API
  slug: signiant-flight-deck-manager-rest-api
artifact_total: 10
asyncapis:
- description: ''
  name: Signiant Webhooks
  slug: signiant-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/signiant/plans/signiant-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/signiant-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.signiant.com/feed/
- group: company
  title: ''
  type: Website
  url: https://www.signiant.com/
- group: auth
  href: https://artifacts.apis.io/signiant/security/signiant-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/signiant-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.signiant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.signiant.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.signiant.com/signiant-platform/api-documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.signiant.com/signiant-platform/getting-started/
- group: auth
  href: https://artifacts.apis.io/signiant/authentication/signiant-authentication.yml
  title: ''
  type: Authentication
  url: authentication/signiant-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://support.signiant.com/
- group: company
  title: ''
  type: Blog
  url: https://www.signiant.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Signiant
- group: commercial
  title: ''
  type: Pricing
  url: https://www.signiant.com/platform-pricing_page/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.signiant.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.signiant.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.signiant.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.signiant.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.signiant.com/technology/security/
- group: build
  title: ''
  type: CodeSamples
  url: https://code-samples.developer.signiant.com/
- group: build
  href: https://artifacts.apis.io/signiant/packages/signiant-packages.yml
  title: ''
  type: Packages
  url: packages/signiant-packages.yml
- group: build
  href: https://artifacts.apis.io/signiant/packages/signiant-packages.yml
  title: ''
  type: SDKs
  url: packages/signiant-packages.yml
- group: design
  href: https://artifacts.apis.io/signiant/asyncapi/signiant-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/signiant-webhooks.yml
- group: design
  href: https://artifacts.apis.io/signiant/lifecycle/signiant-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/signiant-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/signiant/changelog/signiant-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/signiant-changelog.yml
- group: design
  href: https://artifacts.apis.io/signiant/conventions/signiant-conventions.yml
  title: ''
  type: Conventions
  url: conventions/signiant-conventions.yml
- group: design
  href: https://artifacts.apis.io/signiant/conformance/signiant-conformance.yml
  title: ''
  type: Conformance
  url: conformance/signiant-conformance.yml
- group: agent
  href: https://artifacts.apis.io/signiant/well-known/signiant-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/signiant-well-known.yml
- group: agent
  href: https://artifacts.apis.io/signiant/mcp/signiant-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/signiant-mcp.yml
- group: agent
  href: https://artifacts.apis.io/signiant/llms/signiant-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/signiant-llms.txt
- group: design
  href: https://artifacts.apis.io/signiant/components/signiant-components.yml
  title: ''
  type: Components
  url: components/signiant-components.yml
created: '2026-07-17'
description: 'Signiant provides intelligent file-movement software that helps the world''s top content creators and distributors move large files fast and securely over public and private networks. The SaaS Signiant Platform unifies four products behind a common OAuth-secured REST API: the Signiant Platform API (storage, endpoints, users, and roles across products), Jet (automated system-to-system transfers with event webhooks), Media Shuttle (person-initiated transfers with Platform, Management, and System-to-Person APIs plus a browser SDK), and Flight Deck (the Manager REST API for scheduling and running jobs). All APIs authenticate with a client_id/client_secret pair exchanged for a one-hour OAuth 2.0 JWT bearer token at platform-api-service.services.cloud.signiant.com, and access is governed by product-scoped account roles.'
finops:
- has_sources: true
  method: derived
  name: Signiant Finops
  primary_unit: ''
  service_category: ''
  slug: signiant-finops
  template: true
image: https://www.signiant.com/wp-content/uploads/signiant-logo.png
layout: provider
modified: '2026-10-06'
name: Signiant
nav: Providers
network: true
overview: 'Signiant is listed with 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include File Transfer, Media Supply Chain, Managed File Transfer, Content Delivery, and Storage.


  The Signiant catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Signiant''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Signiant Plans Pricing
  plan_count: 1
  slug: signiant-plans-pricing
random_paper: 21
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.2
  facets:
    access_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 45.3
    developer_ergonomics: 64.3
    discoverability: 71.4
    operational_transparency: 44.7
  previous_composite: 50.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/signiant/signiant-2026-08-17T081855.png
security:
- kind: authentication
  name: Signiant Authentication
  slug: signiant-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Signiant Domain Security
  slug: signiant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Signiant Trust Center
  slug: signiant-trust-center
  summary_line: SOC 2, TPN (Trusted Partner Network), MPA (Motion Picture Association best practices)
slug: signiant
tags:
- File Transfer
- Media Supply Chain
- Managed File Transfer
- Content Delivery
- Storage
- Webhook
- Authentication
- Media and Entertainment
website: https://www.signiant.com/
---
