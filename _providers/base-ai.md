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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.base.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.base.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.base.ai/contact-us
- group: start
  title: ''
  type: Login
  url: https://go.base.ai/login/company
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.base.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.base.ai/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.base.ai/platform/security-and-privacy
- group: auth
  title: ''
  type: TrustCenter
  url: security/base-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/base-ai-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/base-ai-llms.txt
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.base.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.base.ai
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/base-ai-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/base-ai-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/base-ai-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/base-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/base-ai-rate-limits.yml
coverage:
  checked: '2026-08-13'
  detail: Base runs a real token-authenticated REST API — tokens are self-issued inside the logged-in app at Settings > Users & Team > Generate token — but every description of it lives behind that login; the public site has no developer portal, no API reference and no spec, and the app host go.base.ai answers unauthenticated requests for /openapi.json, /graphql and /.well-known/* with the same HTML SPA shell under HTTP 200.
  evidence:
  - status: 404
    url: https://www.base.ai/openapi.json
  - status: 404
    url: https://www.base.ai/api-docs
  - status: 200
    url: https://go.base.ai/openapi.json
  - status: 200
    url: https://www.unifyapps.com/docs/unify-integrations/base-ai
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Base is an AI Engagement OS for customer-led growth (CLG). The platform unifies advocacy, references, referrals, reviews, community, customer success, lifecycle engagement, and revenue attribution for B2B post-sale teams. Built for customer marketing, customer success, and RevOps teams, Base uses 100+ AI agents to automate onboarding, adoption, upsell/expansion, retention, and advocacy across the entire post-sale customer lifecycle, and to turn customer signals and feedback into references, testimonials, and expansion plays. Base integrates with Salesforce, HubSpot, Gainsight, Slack, Discord, Airtable, and Zendesk, and is backed by Wing Venture Capital. Base operates a token-authenticated REST API for its customers — tokens are generated inside the application under Settings > Users & Team — but publishes no public API reference, developer portal, OpenAPI definition, or SDKs, so the API surface is documented only by third-party integration platforms.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/base-ai.png
layout: provider
modified: '2026-08-13'
name: Base Ai
nav: Providers
network: true
overview: 'Base Ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Customer-Led Growth, Customer Success, and Customer Marketing.


  Base Ai''s developer surface includes engineering blog, support, changelog, authentication, and 13 more developer resources.'
plans:
- name: Base Ai Plans Pricing
  plan_count: 0
  slug: base-ai-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Base Ai Rate Limits
  slug: base-ai-rate-limits
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 22.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/base-ai/refs/heads/main/screenshots/base-ai-2026-07-25T202412.png
security:
- kind: authentication
  name: Base Ai Authentication
  slug: base-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Base Ai Domain Security
  slug: base-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Base Ai Trust Center
  slug: base-ai-trust-center
  summary_line: SOC 2 Type 2, ISO 27001:2013, ISO 27017, ISO 27018, CSA STAR Level 1, GDPR, CCPA
slug: base-ai
tags:
- Company
- Artificial Intelligence
- Customer-Led Growth
- Customer Success
- Customer Marketing
- Advocacy
- Revenue Operations
- Software-as-a-Service
website: https://www.base.ai/
---
