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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Paack Agentic Access
  operation_count: 10
  slug: paack-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 6
apis:
- description: 'REST API for creating and managing parcel delivery orders, generating shipping labels, checking delivery coverage, retrieving proof of delivery, and consuming real-time tracking events. Authenticated '
  name: Paack API
  slug: paack-api
- baseURL: https://api.paack.app
  baseurl_source: declared
  description: The Check coverage API from Paack — 1 operation(s) for check coverage.
  name: Paack Check coverage API
  slug: paack-check-coverage-api
- baseURL: https://api.paack.app
  baseurl_source: declared
  description: The Generate labels API from Paack — 1 operation(s) for generate labels.
  name: Paack Generate labels API
  slug: paack-generate-labels-api
- baseURL: https://api.paack.app
  baseurl_source: declared
  description: The Get access token API from Paack — 1 operation(s) for get access token.
  name: Paack Get access token API
  slug: paack-get-access-token-api
- baseURL: https://api.paack.app
  baseurl_source: declared
  description: The Manage orders API from Paack — 2 operation(s) for manage orders.
  name: Paack Manage orders API
  slug: paack-manage-orders-api
- baseURL: https://api.paack.app
  baseurl_source: declared
  description: The Retrieve delivery proof API from Paack — 1 operation(s) for retrieve delivery proof.
  name: Paack Retrieve delivery proof API
  slug: paack-retrieve-delivery-proof-api
- baseURL: https://api.paack.app
  baseurl_source: declared
  description: The Retrieve events history API from Paack — 1 operation(s) for retrieve events history.
  name: Paack Retrieve events history API
  slug: paack-retrieve-events-history-api
- baseURL: https://api.paack.app
  baseurl_source: declared
  description: The Retrieve last event API from Paack — 1 operation(s) for retrieve last event.
  name: Paack Retrieve last event API
  slug: paack-retrieve-last-event-api
artifact_total: 20
asyncapis:
- description: ''
  name: Paack Webhooks
  slug: paack-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/agentic-access/paack-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/paack-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/rules/paack-rules.yml
  title: ''
  type: Spectral
  url: rules/paack-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/json-ld/paack-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/paack-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/vocabulary/paack-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/paack-vocabulary.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/hosts/paack-hosts.yml
  title: ''
  type: Hosts
  url: hosts/paack-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/integrations/paack-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/paack-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/vendors/paack-vendors.yml
  title: ''
  type: Vendors
  url: vendors/paack-vendors.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://paack.co/feed/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/security/paack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paack-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/authentication/paack-authentication.yml
  title: ''
  type: Authentication
  url: authentication/paack-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/asyncapi/paack-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/paack-webhooks.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/packages/paack-packages.yml
  title: ''
  type: Packages
  url: packages/paack-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/packages/paack-packages.yml
  title: ''
  type: SDKs
  url: packages/paack-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/conventions/paack-conventions.yml
  title: ''
  type: Conventions
  url: conventions/paack-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/errors/paack-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/paack-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/lifecycle/paack-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/paack-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/changelog/paack-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/paack-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/conformance/paack-conformance.yml
  title: ''
  type: Conformance
  url: conformance/paack-conformance.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/sandbox/paack-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/paack-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/data-model/paack-data-model.yml
  title: ''
  type: DataModel
  url: data-model/paack-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/mcp/paack-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/paack-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/well-known/paack-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/paack-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://paack.co/
- group: start
  title: ''
  type: Portal
  url: https://paack.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://paack.readme.io/docs/start-intro
- group: docs
  title: ''
  type: APIReference
  url: https://paack.readme.io/reference/token
- group: start
  title: ''
  type: GettingStarted
  url: https://paack.readme.io/docs/start-integration
- group: operate
  title: ''
  type: Support
  url: https://help.paack.co/en/support/home
- group: company
  title: ''
  type: Blog
  url: https://paack.co/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://paack.readme.io/changelog/welcome-to-paack
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/paacklogistics/paack-apis/collection/p93tvmy/paack-api-systems
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paack.co/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paack.co/privacy-policy/
created: '2026-07-17'
description: Paack is a technology-driven last-mile parcel delivery company serving e-commerce retailers across Spain, Portugal, the United Kingdom, France and Italy. Founded in 2015 and headquartered in Barcelona, Paack provides scheduled, precise home delivery, returns and reverse logistics, real-time parcel tracking, and proof of delivery. Its developer platform exposes REST APIs for order creation and management, label generation, delivery coverage and postcode-zone lookup, and real-time tracking events, complemented by webhooks for event notifications and an sFTP batch integration. APIs are authenticated with Auth0 OAuth2 client-credentials JSON Web Tokens and documented on a ReadMe developer hub with staging and production environments.
image: https://files.readme.io/005f576-small-Logo_paack_negativo.png
json_schemas:
- name: AddOrderRequest
  property_count: 19
  slug: paack-add-order-request
- name: Covered
  property_count: 0
  slug: paack-check-coverage-response200
- name: Defines the request to generate labels.
  property_count: 12
  slug: paack-create-label-request-json
- name: statusGetResponse
  property_count: 2
  slug: paack-status-get-response
- name: statusListResponse
  property_count: 2
  slug: paack-status-list-response
- name: UpdateOrderRequest
  property_count: 6
  slug: paack-update-order-request
jsonld:
- class_count: 44
  name: Paack Context
  property_count: 70
  slug: paack-context
layout: provider
modified: '2026-10-06'
name: Paack
nav: Providers
network: true
overview: 'Paack publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Check coverage API, Generate labels API, and 6 more. Tagged areas include Company, Logistics, Last Mile Delivery, Parcel Delivery, and E-Commerce.


  The Paack catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Paack''s developer surface includes authentication, changelog, sandbox, developer portal, documentation, API reference, getting-started guide, and 26 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Paack API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: paack-rules
score:
  band: developing
  composite: 50.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 13.2
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 75.7
    developer_ergonomics: 53.6
    discoverability: 71.4
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/paack/refs/heads/main/screenshots/paack-2026-08-07T191232.png
security:
- kind: authentication
  name: Paack Authentication
  slug: paack-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Paack Domain Security
  slug: paack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: paack
tags:
- Company
- Logistics
- Last Mile Delivery
- Parcel Delivery
- E-Commerce
- Shipping
- Fulfillment
- Tracking
- Reverse Logistics
website: https://paack.co/
---
