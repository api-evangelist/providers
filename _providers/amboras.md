---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 11.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The multi-tenant commerce backend Amboras operates at api.amboras.com. Every Amboras-built storefront calls it through the Medusa JS SDK, sending a publishable API key (x-publishable-api-key, pk_ pref
  name: Amboras Storefront Backend
  slug: amboras-storefront-backend
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/amboras-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amboras-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.amboras.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.amboras.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amboras-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amboras.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.amboras.com/what-is-amboras
- group: commercial
  title: ''
  type: Pricing
  url: https://www.amboras.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.amboras.com/register
- group: start
  title: ''
  type: Login
  url: https://admin.amboras.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amboras.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amboras.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.amboras.com/status
- group: operate
  title: ''
  type: Support
  url: https://www.amboras.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Amboras
- group: auth
  title: ''
  type: Authentication
  url: authentication/amboras-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amboras-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amboras-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amboras-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amboras-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/amboras-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/amboras-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/amboras-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/amboras-packages.yml
- group: design
  title: ''
  type: Components
  url: components/amboras-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amboras-llms.txt
created: '2026-07-17'
description: 'Amboras is an AI-native e-commerce platform - positioned as "the AI-native Shopify" - that puts an entire online store on autopilot. Merchants build or rebuild a storefront by talking to AI in natural language, and Amboras then autonomously generates design, copy, and product imagery, runs generative A/B tests, adjusts pricing and offers, and reads first-party analytics to continuously optimize conversion rate, retention, and average order value. It includes integrated checkout via Stripe and PayPal and first-party session, funnel, and revenue tracking with no third-party pixels. Founded in 2025 in San Francisco by Imad and Amin Mokadem, Amboras is a Y Combinator Spring 2026 (P26) company. Amboras publishes no developer portal, API reference, OpenAPI or GraphQL schema, but it does operate a real machine surface: a multi-tenant Medusa v2 backend at api.amboras.com that every storefront calls with a publishable key plus an X-Store-Environment-ID tenant header, a first-party npm
  scope of 33 TypeScript packages (@amboras-dev) implementing a 24-slot storefront plugin system, and a public GitHub organization of 458 provisioned Next.js storefront repositories that each ship Amboras-authored agent operating instructions.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amboras.png
layout: provider
modified: '2026-08-13'
name: Amboras
nav: Providers
network: true
overview: 'Amboras publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Artificial Intelligence, Generative AI, and Automation.


  Amboras'' developer surface includes documentation, pricing, signup flow, support, authentication, changelog, and 21 more developer resources.'
plans:
- name: Amboras Plans Pricing
  plan_count: 4
  slug: amboras-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Amboras Rate Limits
  slug: amboras-rate-limits
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 44.9
  provenance:
    conformance: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amboras/refs/heads/main/screenshots/amboras-2026-07-25T200029.png
security:
- kind: authentication
  name: Amboras Authentication
  slug: amboras-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Amboras Domain Security
  slug: amboras-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Amboras Vulnerability Disclosure
  slug: amboras-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Amboras Trust Center
  slug: amboras-trust-center
  summary_line: SOC 2 Type II, ISO 27001, PCI DSS, HIPAA Ready, GDPR, CCPA
slug: amboras
tags:
- Company
- E-Commerce
- Artificial Intelligence
- Generative AI
- Automation
- Conversion Rate Optimization
- Retail
- No-Code Store Builder
- Y Combinator
- Agentic Commerce
- Storefront
- Payments
- Checkout
- Analytics
- Headless Commerce
- Medusa
- Plugins
- Multi-Tenant
website: https://www.amboras.com/
---
