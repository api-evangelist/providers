---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - https://blng.ai/pricing
  - https://billing.blng.ai/billing/products
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
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 49
  human_in_the_loop: 3
  name: Blng Agentic Access
  operation_count: 88
  slug: blng-agentic-access
  summary_line: 88 operations · 49 acting · 3 human-in-the-loop
api_count: 4
apis:
- description: REST API that manages BLNG users, roles and permissions, workspaces and workspace members, workspace and subscription invitations, organizations, SSO configuration, marketing consent, tooltips, and us
  name: BLNG User API
  slug: blng-user-api
- description: REST API that manages BLNG payment and billing — listing Stripe products and prices, creating Stripe checkout sessions and customer-portal sessions, confirming checkout, and submitting enterprise "con
  name: BLNG Billing API
  slug: blng-billing-api
- description: The Chat Prompts API from Blng — 2 operation(s) for chat prompts.
  name: Blng Chat Prompts API
  slug: blng-chat-prompts-api
- description: The Composite API from Blng — 2 operation(s) for composite.
  name: Blng Composite API
  slug: blng-composite-api
- description: The Design Journey API from Blng — 16 operation(s) for design journey.
  name: Blng Design Journey API
  slug: blng-design-journey-api
- description: The Invitation API from Blng — 5 operation(s) for invitation.
  name: Blng Invitation API
  slug: blng-invitation-api
- description: The Journeys API from Blng — 6 operation(s) for journeys.
  name: Blng Journeys API
  slug: blng-journeys-api
- description: The Organization API from Blng — 3 operation(s) for organization.
  name: Blng Organization API
  slug: blng-organization-api
- description: The Prompts API from Blng — 4 operation(s) for prompts.
  name: Blng Prompts API
  slug: blng-prompts-api
- description: The Subscription API from Blng — 4 operation(s) for subscription.
  name: Blng Subscription API
  slug: blng-subscription-api
- description: The User Subscription API from Blng — 3 operation(s) for user subscription.
  name: Blng User Subscription API
  slug: blng-user-subscription-api
- description: The User Tooltip API from Blng — 2 operation(s) for user tooltip.
  name: Blng User Tooltip API
  slug: blng-user-tooltip-api
- description: The Webhook API from Blng — 3 operation(s) for webhook.
  name: Blng Webhook API
  slug: blng-webhook-api
- description: The Workspace API from Blng — 15 operation(s) for workspace.
  name: Blng Workspace API
  slug: blng-workspace-api
artifact_total: 22
asyncapis:
- description: ''
  name: Blng Webhooks
  slug: blng-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/blng-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/blng-journey-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blng-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blng-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blng.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blng.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blng.ai/getting-started/
- group: operate
  title: ''
  type: HelpCenter
  url: https://portal.blng.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://blng.ai/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/blng-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://blng.ai/news
- group: operate
  title: ''
  type: Support
  url: mailto:support@blng.ai
- group: start
  title: ''
  type: SignUp
  url: https://app.blng.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blng.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blng.ai/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blng-ai/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/blng.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blng-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blng.ai/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blng-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.blng.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/blng-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blng-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/blng-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/blng-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/blng-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/blng-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blng-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/blng-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blng-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: BLNG is an AI-driven creative suite for the jewelry industry, giving jewelers, designers, brands, and retailers tools to explore, refine, and present designs fast and without compromise. Its Design product turns sketches, doodles, photos, illustrations, or text prompts into photorealistic renderings on web and iOS; Studio transforms CAD models into market-ready marketing photos and videos at scale; and Retail enables live, made-to-order design in-store. BLNG is a Speedinvest portfolio company. BLNG publishes no developer program, but the web application is backed by three first-party REST APIs whose OpenAPI definitions are served publicly and unauthenticated behind Swagger UI on its own hosts — a Journey API for design journeys, prompts, image assets and 3D model generation, a User API for users, workspaces, invitations, organizations and subscriptions, and a Billing API for Stripe-backed products, checkout and subscription webhooks. All three authenticate with AWS Cognito bearer
  tokens issued at auth.app.blng.ai.
image: https://cdn.sanity.io/images/4x3qe5zn/production/5354c7992cf9027bbe7400e2c4079f2c46e40cd8-4800x2520.png?w=1200&h=630
layout: provider
modified: '2026-08-13'
name: Blng
nav: Providers
network: true
overview: 'Blng publishes 14 APIs on the [APIs.io](https://apis.io/) network, including User API, Billing API, Chat Prompts API, and 11 more. Tagged areas include Company, Jewelry, Generative AI, Design, and Creative Tools.


  The Blng catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Blng''s developer surface includes documentation, getting-started guide, pricing, engineering blog, support, signup flow, authentication, and 24 more developer resources.'
plans:
- name: Blng Plans Pricing
  plan_count: 5
  slug: blng-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Blng Rate Limits
  slug: blng-rate-limits
scopes:
- name: Blng Scopes
  scope_count: 4
  slug: blng-scopes
  summary_line: 4 scopes · implicit
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 22
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 4.5
    contract_quality: 54.9
    developer_ergonomics: 49.4
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blng/refs/heads/main/screenshots/blng-2026-07-25T203330.png
security:
- kind: authentication
  name: Blng Authentication
  slug: blng-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Blng Domain Security
  slug: blng-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Blng Trust Center
  slug: blng-trust-center
  summary_line: trust center published
slug: blng
tags:
- Company
- Jewelry
- Generative AI
- Design
- Creative Tools
- Rendering
- Marketing
- Retail
- 3D Models
- Image-Generation
- Workspaces
- Billing
- OpenAPI
- AWS Cognito
website: https://blng.ai
---
