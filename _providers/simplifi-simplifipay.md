---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.0
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Simplifi Simplifipay Agentic Access
  operation_count: 52
  slug: simplifi-simplifipay-agentic-access
  summary_line: 52 operations · 39 acting
api_count: 1
apis:
- baseURL: https://uat-lb.simplifipay.com
  baseurl_source: declared
  description: The Auth API from Simplifi/Simplifipay — 2 operation(s) for auth.
  name: Simplifi/Simplifipay Auth API
  slug: simplifi-simplifipay-auth-api
- baseURL: https://uat-lb.simplifipay.com
  baseurl_source: declared
  description: The Card API from Simplifi/Simplifipay — 12 operation(s) for card.
  name: Simplifi/Simplifipay Card API
  slug: simplifi-simplifipay-card-api
- baseURL: https://uat-lb.simplifipay.com
  baseurl_source: declared
  description: The Card Program API from Simplifi/Simplifipay — 9 operation(s) for card program.
  name: Simplifi/Simplifipay Card Program API
  slug: simplifi-simplifipay-card-program-api
- baseURL: https://uat-lb.simplifipay.com
  baseurl_source: declared
  description: The Fee API from Simplifi/Simplifipay — 5 operation(s) for fee.
  name: Simplifi/Simplifipay Fee API
  slug: simplifi-simplifipay-fee-api
- baseURL: https://uat-lb.simplifipay.com
  baseurl_source: declared
  description: The Funding Source API from Simplifi/Simplifipay — 6 operation(s) for funding source.
  name: Simplifi/Simplifipay Funding Source API
  slug: simplifi-simplifipay-funding-source-api
- baseURL: https://uat-lb.simplifipay.com
  baseurl_source: declared
  description: The Transaction API from Simplifi/Simplifipay — 3 operation(s) for transaction.
  name: Simplifi/Simplifipay Transaction API
  slug: simplifi-simplifipay-transaction-api
- baseURL: https://uat-lb.simplifipay.com
  baseurl_source: declared
  description: The User API from Simplifi/Simplifipay — 4 operation(s) for user.
  name: Simplifi/Simplifipay User API
  slug: simplifi-simplifipay-user-api
- baseURL: https://uat-lb.simplifipay.com
  baseurl_source: declared
  description: The Webhook API from Simplifi/Simplifipay — 4 operation(s) for webhook.
  name: Simplifi/Simplifipay Webhook API
  slug: simplifi-simplifipay-webhook-api
artifact_total: 22
asyncapis:
- description: 'Outbound webhook events SimpliFi delivers to a client-configured HTTPS endpoint. Async model: an API call returns 2xx/202 on receipt; the outcome arrives here. Each delivery carries X-SimpliFi-Webhook'
  name: SimpliFi Webhooks
  slug: simplifi-simplifipay-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SimpliFi Cards Auth API
  slug: open-simplifi-simplifipay-auth-api
- collection_type: open
  name: SimpliFi Cards Auth Card API
  slug: open-simplifi-simplifipay-card-api
- collection_type: open
  name: SimpliFi Cards Auth Card Program API
  slug: open-simplifi-simplifipay-card-program-api
- collection_type: open
  name: SimpliFi Cards Auth Document API
  slug: open-simplifi-simplifipay-document-api
- collection_type: open
  name: SimpliFi Cards Auth Fee API
  slug: open-simplifi-simplifipay-fee-api
- collection_type: open
  name: SimpliFi Cards Auth Funding Source API
  slug: open-simplifi-simplifipay-funding-source-api
- collection_type: open
  name: SimpliFi Cards Auth Transaction API
  slug: open-simplifi-simplifipay-transaction-api
- collection_type: open
  name: SimpliFi Cards Auth User API
  slug: open-simplifi-simplifipay-user-api
- collection_type: open
  name: SimpliFi Cards Auth Webhook API
  slug: open-simplifi-simplifipay-webhook-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/capabilities/simplifi-simplifipay-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/simplifi-simplifipay-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/overlays/simplifi-simplifipay-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/simplifi-simplifipay-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidoc.simplifipay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.simplifipay.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidoc.simplifipay.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://apidoc.simplifipay.com/introduction-1207172m0
- group: start
  title: ''
  type: SignUp
  url: https://simplifipay.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://prod-portal.simplifipay.com/simplifi-webapp/
- group: operate
  title: ''
  type: Support
  url: mailto:info@simplifipay.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://simplifipay.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://simplifipay.com/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/authentication/simplifi-simplifipay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/simplifi-simplifipay-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/agentic-access/simplifi-simplifipay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/simplifi-simplifipay-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/security/simplifi-simplifipay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/simplifi-simplifipay-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/llms/simplifi-simplifipay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/simplifi-simplifipay-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/errors/simplifi-simplifipay-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/simplifi-simplifipay-error-codes.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/asyncapi/simplifi-simplifipay-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/simplifi-simplifipay-webhooks-asyncapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/asyncapi/simplifi-simplifipay-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/simplifi-simplifipay-webhooks-asyncapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/conventions/simplifi-simplifipay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/simplifi-simplifipay-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/sandbox/simplifi-simplifipay-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/simplifi-simplifipay-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/components/simplifi-simplifipay-components.yml
  title: ''
  type: Components
  url: components/simplifi-simplifipay-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/mcp/simplifi-simplifipay-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/simplifi-simplifipay-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/data-model/simplifi-simplifipay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/simplifi-simplifipay-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/lifecycle/simplifi-simplifipay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/simplifi-simplifipay-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/conformance/simplifi-simplifipay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/simplifi-simplifipay-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/conformance/simplifi-simplifipay-conformance.yml
  title: ''
  type: Compliance
  url: conformance/simplifi-simplifipay-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://simplifipay.com
created: '2026-07-17'
description: SimpliFi (simplifipay.com) is a Cards-as-a-Service platform powering virtual and physical card programs for fintechs, startups, and enterprises across the GCC (UAE, Saudi Arabia, Kuwait, Bahrain, Oman, Qatar). Regulated by the Dubai Financial Services Authority (DFSA), SimpliFi offers off-the-shelf and fully customizable card programs with multi-currency support (50+ currencies), digital-wallet enablement (Apple/Google/Samsung Pay), programmable authorization, velocity, and merchant controls, and real-time transaction and fraud monitoring. Its developer platform exposes a JWT-authenticated REST API (card programs, funding sources, cards, users, transactions, fees, rule groups, and webhook management) on an asynchronous, webhook-driven architecture, plus a PCI-DSS-compliant Virtual Card SDK for securely displaying card data. Surfaced as a 500 Global portfolio company and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simplifi-simplifipay.png
layout: provider
modified: '2026-09-15'
name: Simplifipay
nav: Providers
network: true
overview: 'Simplifipay publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Simplifi/Simplifipay Auth API, Simplifi/Simplifipay Card API, Simplifi/Simplifipay Card Program API, and 5 more. Tagged areas include Company, Cards, Card Issuing, Virtual Cards, and Fintech.


  The Simplifipay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Simplifipay''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, sandbox, and 21 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 67.7
    developer_ergonomics: 63.7
    discoverability: 75.9
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 65.6
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/simplifi-simplifipay/refs/heads/main/screenshots/simplifi-simplifipay-2026-08-17T081912.png
security:
- kind: authentication
  name: Simplifi Simplifipay Authentication
  slug: simplifi-simplifipay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Simplifi Simplifipay Domain Security
  slug: simplifi-simplifipay-domain-security
  summary_line: TLSv1.3 · DMARC
slug: simplifi-simplifipay
tags:
- Company
- Cards
- Card Issuing
- Virtual Cards
- Fintech
- Payments
- Banking as a Service
- Embedded Finance
- GCC
- Webhook
website: https://simplifipay.com
---
