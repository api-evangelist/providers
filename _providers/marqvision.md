---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marqvision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.marqvision.com/
- group: company
  title: ''
  type: Blog
  url: https://www.marqvision.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://brand.marqvision.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/marqvision
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.marqvision.com/marqcommerce-tc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.marqvision.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.marqvision.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.vanta.com/marqvision/trust/epgpmrjuuy9q9tkqn5m8um
- group: auth
  title: ''
  type: Compliance
  url: https://www.marqvision.com/blog/marqvision-soc-2-type-ii
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/marqvision-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/marqvision-conformance.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/marqvision-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/marqvision-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/marqvision-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/marqvision-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/marqvision-llms.txt
coverage:
  checked: '2026-08-25'
  detail: 'MarqVision runs a real API — its own status page monitors a component named "MarqAI API" and its blog calls the Marq AI Slack app "the first product built on our Action-Enabled API" — but ships zero public developer surface: docs.marqvision.com and developer.marqvision.com do not resolve, api.marqvision.com 404s on every probed path, and access is routed through a customer success manager or the demo waitlist.'
  evidence:
  - status: 200
    url: https://status.marqvision.com/api/v2/components.json
  - status: 404
    url: https://api.marqvision.com/openapi.json
  - status: 404
    url: https://www.marqvision.com/llms.txt
  - status: 200
    url: https://brand.marqvision.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-08-25'
description: MarqVision is a brand-integrity and intellectual-property protection platform (Y Combinator S21) that uses AI-powered image recognition and semantic analysis to detect and remove counterfeits, unauthorized sellers, brand impersonation and pirated content across more than 1,500 online marketplaces, e-commerce sites, social platforms and app stores. The product line spans MarqCommerce (marketplace enforcement), MarqContents (content and piracy protection), MarqFolio (trademark portfolio management), MarqLaw (legal services) and a Brand Intelligence Agent for natural-language brand-threat analytics. MarqVision operates a customer-facing "MarqAI API" — named as a component on its own public status page and described in its engineering blog as the "Action-Enabled API" behind the Marq AI Slack app — but publishes no public developer portal, API reference or machine-readable contract; programmatic access is arranged through a customer success manager or the demo waitlist.
image: https://cdn.prod.website-files.com/5e51f2cd33d368869635e146/68c77f858e19fe35fee2eb73_favicon_gradient.png
layout: provider
modified: '2026-08-25'
name: MarqVision
nav: Providers
network: true
overview: 'MarqVision is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Brand Protection, Intellectual Property, Anti-Counterfeiting, Trademarks, and Content Protection.


  MarqVision''s developer surface includes engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Marqvision Plans Pricing
  plan_count: 0
  slug: marqvision-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Marqvision Rate Limits
  slug: marqvision-rate-limits
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 15.8
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marqvision/refs/heads/main/screenshots/marqvision-2026-09-02T150435.png
security:
- kind: domain-security
  name: Marqvision Domain Security
  slug: marqvision-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Marqvision Trust Center
  slug: marqvision-trust-center
  summary_line: SOC 2 Type II
slug: marqvision
tags:
- Brand Protection
- Intellectual Property
- Anti-Counterfeiting
- Trademarks
- Content Protection
- E-Commerce
- Artificial Intelligence
- Trust and Safety
- Enforcement
- Company
website: https://www.marqvision.com/
---
